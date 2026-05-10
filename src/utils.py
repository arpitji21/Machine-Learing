import os
import pickle
import sys

import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        logging.info("Error occured")
        raise CustomException(e,sys)
    

def evaluate_model(X_train, y_train, X_test, y_test, models,params):
   
    try:
        report = {}
        trained_models = {}

        for model_name, model in models.items():

            para = params[model_name]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            best_model = gs.best_estimator_

            best_model.fit(X_train, y_train)

            y_test_pred = best_model.predict(X_test)

            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

            trained_models[model_name] = best_model

        return report, trained_models

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
    
    
