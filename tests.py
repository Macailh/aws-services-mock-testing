import boto3
import os
from fastapi.testclient import TestClient
from moto import mock_aws
from main import app

client = TestClient(app)
SOURCE = os.getenv("SOURCE", "")
DESTINATION = os.getenv("DESTINATION", "")

@mock_aws
def test_ses_endpoint():
    ses_client = boto3.client('ses')
    ses_client.verify_email_identity(EmailAddress=SOURCE)
    ses_client.verify_email_identity(EmailAddress=DESTINATION)

    response = client.get("/ses")

    print(response)
    assert response.status_code == 200