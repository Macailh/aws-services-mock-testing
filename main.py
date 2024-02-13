import boto3
import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
ses_client = boto3.client("ses")
SOURCE = os.getenv("SOURCE", "")
DESTINATION = os.getenv("DESTINATION", "")

@app.get("/")
def root():
    return {"message": "Hello from root"}


@app.get("/ses")
def ses():
    response = ses_client.send_email(
        Source=SOURCE,
        Destination={
            'ToAddresses': [DESTINATION]
        },
        Message={
            'Subject': {
                'Data': 'Subject'
            },
            'Body': {
                'Text': {
                    'Data': 'Content'
                }
            }
        }
    )
    print(response)
    return response