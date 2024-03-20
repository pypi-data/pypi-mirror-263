# dualPredictor/dual_model.py

from sklearn.base import BaseEstimator, RegressorMixin, clone
from sklearn.linear_model import LassoCV, RidgeCV, LinearRegression
from sklearn.metrics import confusion_matrix, balanced_accuracy_score,fbeta_score
import numpy as np

class DualModel(BaseEstimator, RegressorMixin):
    def __init__(self, model_type='lasso', default_cut_off=0.5):
        self.model_type = model_type
        self.default_cut_off = default_cut_off
        self.model = None
        self.optimal_cut_off = None
        self.y_label_true_=None

        if model_type == 'lasso':
            self.model = LassoCV(cv=5)
        elif model_type == 'ridge':
            self.model = RidgeCV(cv=5)
        elif model_type == 'ols':
            self.model = LinearRegression()
        else:
            raise ValueError("Unsupported model type. Choose 'lasso', 'ridge', or 'ols'.")

    def fit(self, X, y,metric='youden_index'):
        self.model.fit(X, y)

        # Create binary labels based on the default cut-off
        y_label_true = (y < self.default_cut_off).astype(int)
        self.y_label_true_=y_label_true

        # Tune the optimal cut-off
        cut_offs = np.linspace(self.default_cut_off, max(y) * 0.8, 20)
        metrics = []

        for cut_off in cut_offs:
            y_pred = (self.model.predict(X) < cut_off).astype(int)
            if metric == 'f1_score':
                metric_value = fbeta_score(y_label_true, y_pred,beta=1)
            elif metric == 'f2_score':
                metric_value = fbeta_score(y_label_true, y_pred,beta=2)
            elif metric == 'youden_index':
                metric_value = balanced_accuracy_score(y_label_true, y_pred, adjusted=True)
            else:
                raise ValueError("Unsupported metric. Choose 'f1_score', 'f2_score', or 'youden_index'.")

            metrics.append(metric_value)

        max_index = np.argmax(metrics)
        self.optimal_cut_off = cut_offs[max_index]

        return self

    def predict(self, X):
        grade_predictions = self.model.predict(X)
        class_predictions = (grade_predictions < self.optimal_cut_off).astype(int)
        return grade_predictions, class_predictions

    @property
    def alpha_(self):
        return self.model.alpha_

    @property
    def coef_(self):
        return self.model.coef_

    @property
    def intercept_(self):
        return self.model.intercept_

    @property
    def feature_names_in_(self):
        return getattr(self.model, 'feature_names_in_', None)
