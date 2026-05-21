from src.api_server.models.customer_data import CustomerData
from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/api",
    tags=["api"]
)

@router.post("/predict")
def predict(request: Request, customer_data: CustomerData):
    model = request.app.state.model
    api_model_services = request.app.state.api_model_services_obj
    # Dummy data for now
    # input_data = {'age': 57, 'dependents': 1, 'tenure_months': 6, 'monthly_charges': 102.4, 'total_charges': 614.4, 'avg_call_duration_mins': 180, 'monthly_data_usage_gb': 410, 'num_complaints_last_6_months': 5, 'network_outage_reports': 4, 'customer_support_calls': 7, 'last_login_days_ago': 28, 'mobile_app_usage_score': 35.8, 'late_payment_count': 6}
    # Perform inference using the model
    input_data = customer_data.model_dump()
    return api_model_services.predict(model, input_data=input_data)
    

