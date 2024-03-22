from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from pathlib import Path
import joblib
import os
# from sklearn.inspection import permutation_importance
import pandas as pd
from dazer import utils


class Classifier:
    
    def __init__(self, X_train, y_train, X_test, y_test):
       
        self.label_encodings = {}
        
        X_test = X_test.copy()
        X_train = X_train.copy()
        
        # encode categorical columns
        categorical_columns = X_train.columns[~X_test.columns.isin(X_test._get_numeric_data().columns)]
        for col in categorical_columns:
            self.label_encodings[col] = {x: i for i, x in enumerate(X_test[col].unique())}
            X_test[col] = X_test[col].map(self.label_encodings[col])
            X_train[col] = X_train[col].map(self.label_encodings[col])
            
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        
        
    @staticmethod
    def get_model_from_string(model_string: str):
        if model_string == 'rf':
            return RandomForestClassifier()
        elif model_string == 'xgb':
            from xgboost import XGBClassifier
            return XGBClassifier(objective='binary:logistic')
        elif model_string == 'mlp':
            from sklearn.neural_network import MLPClassifier
            return MLPClassifier()
        elif model_string == 'gnb':
            from sklearn.naive_bayes import GaussianNB
            return GaussianNB()
        elif model_string == 'svc':
            from sklearn.svm import SVC
            return SVC()
            
    
    def train_test(self, model_string: str, param_grid={}, cv=10, n_jobs=-1, model_path='', verbose=1, scoring='f1'):
        classifier = self.get_model_from_string(model_string)
        model = self.train(classifier, param_grid=param_grid, cv=cv,
                           n_jobs=n_jobs, verbose=verbose, scoring=scoring)
        
        y_pred = self.test(model)
        evals = self.eval_pred(y_pred)
        
        if model_path:
            Path(os.sep.join(model_path.split(os.sep)[:-1])).mkdir(parents=True, exist_ok=True)
            joblib.dump(model, model_path)

        return model, evals
    
    
    def train(self, model, param_grid={}, cv=10, n_jobs=-1, verbose = 1, scoring='f1'):
        model = GridSearchCV(estimator = model, param_grid = param_grid, cv = cv, n_jobs = n_jobs, verbose = verbose, scoring=scoring)
        model.fit(self.X_train, self.y_train)
        return model
    
    
    def test(self, model):
        return model.predict(self.X_test)
    
    
    def eval_pred(self, y_pred):
        clrep = classification_report(self.y_test, y_pred, target_names=None, output_dict=True)
       
        if '1' not in clrep:
           print('Warning: No positive class in test set')
        if '0' not in clrep:
            print('Warning: No negative class in test set')
       
        return {'n_samples_train': len(self.X_train), 
                'n_samples_test': len(self.X_test), 
                'accuracy': clrep['accuracy'],
                'f1': clrep['1']['f1-score'] if '1' in clrep else None,
                'precision': clrep['1']['precision' if '1' in clrep else None],
                'recall': clrep['1']['recall'] if '1' in clrep else None,
                'TNR': clrep['0']['recall' if '0' in clrep else None],
                }
        
        
    def get_feature_weights_random_forests(self, model_paths=[]):
        weights = []
        columns = self.X_train.columns
        for rf_path in  model_paths:
            clf = joblib.load(rf_path)
            data = list(clf.best_estimator_.feature_importances_)
            data.append(rf_path)
            weights.append(data)
            
        columns.append('model_path')
        df = pd.DataFrame(data=weights)

        df['model'] = df['model_path'].map(lambda x: x.split('/')[-1])
        return df
    

    def classifier_prediction_evaluation(self, models):
        prediction_evaluation_list = []
        for model in models:
            y_pred = model.predict(self.X_test)
            evaluation = utils.evaluate_prediction(self.y_test, y_pred)
            prediction_evaluation_list.append(evaluation)
        return prediction_evaluation_list
    
    
    def simulate_random_classifier_prediction_evaluation(self, n_models, random_state=101):
        
        random_evaluation_list = utils.random_classifier_prediction_evaluation(n_models, self.y_test, len(self.X_test), random_state)
        
        return random_evaluation_list
        
    
    
    # def permutation_test_random_forest(self, model_path, ratio, random_state=101):
    #     # random forest
    #     model = joblib.load(model_path)
        
    #     permutation_result = permutation_importance(
    #         model, self.X_train, self.y_train, n_repeats=10, random_state=random_state, n_jobs=5
    #     )
        
    #     return {
    #         'ratio': ratio,
    #         'dataset': self.dataset_name,
    #         'permutation_importances_mean': permutation_result.importances_mean,
    #         'permutation_importances_std': permutation_result.importances_std
    #     }