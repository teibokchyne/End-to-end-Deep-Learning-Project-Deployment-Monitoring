from fastapi.testclient import TestClient
from src.api_server import create_app
from src.api_server.models.customer_data import CustomerData

app = create_app()
client = TestClient(app)
input_data = {'age': 1, 'dependents': 2, 'tenure_months': 60, 'monthly_charges': 102.4, 'total_charges': 614.4, 'avg_call_duration_mins': 180, 'monthly_data_usage_gb': 410, 'num_complaints_last_6_months': 5, 'network_outage_reports': 4, 'customer_support_calls': 7, 'last_login_days_ago': 28, 'mobile_app_usage_score': 35.8, 'late_payment_count': 1}

with TestClient(app) as client:

    response = client.post(
        "/api/predict",
        json=input_data
    )

    print(response.json())