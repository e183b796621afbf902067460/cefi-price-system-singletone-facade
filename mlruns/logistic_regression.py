import pandas as pd
import mlflow as mf

import boto3 as aws

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score, precision_score, recall_score

import os
mf.set_tracking_uri("http://localhost:5000")


s3 = aws.client(
    "s3",
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', None),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', None),
    endpoint_url=os.getenv('MLFLOW_S3_ENDPOINT_URL', None)
)

s3.download_file(
    'csv-files',
    'diabetes_prediction_dataset.csv',
    'diabetes_prediction_dataset.csv'
)

LE = LabelEncoder()
SS = StandardScaler()
M = LogisticRegression()

df = pd.read_csv("diabetes_prediction_dataset.csv")

df['gender'] = LE.fit_transform(df['gender'])
df['smoking_history'] = LE.fit_transform(df['smoking_history'])

df[['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']] = SS.fit_transform(df[['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']])

Y, X = df['diabetes'], df.drop('diabetes', axis=1)

x_train, x_test, y_train, y_test = tts(X, Y, test_size=.3, random_state=42)

M.fit(x_train, y_train)


y_predictions_train = M.predict(x_train)
y_predictions_test = M.predict(x_test)

train_accuracy_score = accuracy_score(y_train, y_predictions_train)
test_accuracy_score = accuracy_score(y_test, y_predictions_test)

train_precision_score = precision_score(y_train, y_predictions_train)
test_precision_score = precision_score(y_test, y_predictions_test)

train_recall_score = recall_score(y_train, y_predictions_train)
test_recall_score = recall_score(y_test, y_predictions_test)


with mf.start_run():
    mf.log_param("model", f"{M.__class__.__name__}")

    mf.log_metric("train_accuracy_score", train_accuracy_score)
    mf.log_metric("test_accuracy_score", test_accuracy_score)

    mf.log_metric("train_precision_score", train_precision_score)
    mf.log_metric("test_precision_score", test_precision_score)

    mf.log_metric("train_recall_score", train_recall_score)
    mf.log_metric("test_recall_score", test_recall_score)

    mf.sklearn.log_model(M, "model")
