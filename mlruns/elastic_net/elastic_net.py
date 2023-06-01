import pandas as pd
import numpy as np
import mlflow as mf

import boto3 as aws

from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import os
import sys
mf.set_tracking_uri("http://localhost:5000")


def evaluate(actual: np.array, predictions: np.array):
    r_mse = np.sqrt(mean_squared_error(actual, predictions))
    mae = mean_absolute_error(actual, predictions)
    r2 = r2_score(actual, predictions)
    return r_mse, mae, r2


S3 = aws.client(
    "s3",
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', None),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', None),
    endpoint_url=os.getenv('MLFLOW_S3_ENDPOINT_URL', None)
)

S3.download_file(
    'csv-files',
    'diabetes_prediction_dataset.csv',
    'diabetes_prediction_dataset.csv'
)

alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

LE = LabelEncoder()
SS = StandardScaler()
M = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)

df = pd.read_csv("diabetes_prediction_dataset.csv")

df['gender'] = LE.fit_transform(df['gender'])
df['smoking_history'] = LE.fit_transform(df['smoking_history'])

df[['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']] = SS.fit_transform(df[['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']])

Y, X = df['diabetes'], df.drop('diabetes', axis=1)

x_train, x_test, y_train, y_test = tts(X, Y, test_size=.3, random_state=42)

M.fit(x_train, y_train)


y_predictions_train = M.predict(x_train)
y_predictions_test = M.predict(x_test)

r_mse, mae, r2 = evaluate(y_test, y_predictions_test)


with mf.start_run():
    mf.log_param("model", f"{M.__class__.__name__}")

    mf.log_param("alpha", alpha)
    mf.log_param("l1_ratio", l1_ratio)

    mf.log_metric("r_mse", r_mse)
    mf.log_metric("mae", mae)
    mf.log_metric("r2", r2)

    mf.sklearn.log_model(M, "model")
