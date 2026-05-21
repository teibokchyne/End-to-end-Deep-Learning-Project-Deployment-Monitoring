import pandas as pd
from src.utils.logger import Logger

class DummyData:
    dummy_X_test = pd.DataFrame(
        {'age': 57, 'dependents': 1, 'tenure_months': 6, 'monthly_charges': 102.4, 'total_charges': 614.4, 'avg_call_duration_mins': 180, 'monthly_data_usage_gb': 410, 'num_complaints_last_6_months': 5, 'network_outage_reports': 4, 'customer_support_calls': 7, 'last_login_days_ago': 28, 'mobile_app_usage_score': 35.8, 'late_payment_count': 6}
    )
    
    def __init__(self):
        self.logger = Logger.get_logger(self.__class__.__name__)

    def generate_dummy_original_dataframe(self):
        # Implementation for generating dummy data
        data = [
            {
                "customer_id": "CUST_100245",
                "gender": "Female",
                "age": 42,
                "marital_status": "Married",
                "dependents": 2,
                "city": "Bangalore",
                "tenure_months": 18,

                # Subscription Information
                "phone_service": True,
                "multiple_lines": False,
                "internet_service": "Fiber Optic",
                "online_security": False,
                "online_backup": True,
                "device_protection": True,
                "tech_support": False,
                "streaming_tv": True,
                "streaming_movies": True,

                # Contract & Billing
                "contract_type": "Month-to-Month",
                "paperless_billing": True,
                "payment_method": "Electronic Check",
                "monthly_charges": 89.75,
                "total_charges": 1615.50,

                # Usage Metrics
                "avg_call_duration_mins": 240,
                "monthly_data_usage_gb": 320,
                "num_complaints_last_6_months": 3,
                "network_outage_reports": 2,
                "customer_support_calls": 5,

                # Engagement Metrics
                "last_login_days_ago": 12,
                "mobile_app_usage_score": 58.3,
                "promo_offer_used": False,
                "autopay_enabled": False,

                # Derived Behavioral Features
                "late_payment_count": 4,
                "plan_downgrade_last_year": True,
                "international_roaming": False,

                # Target Variable
                "churn": 1
            },

            {
                "customer_id": "CUST_100246",
                "gender": "Male",
                "age": 31,
                "marital_status": "Single",
                "dependents": 0,
                "city": "Mumbai",
                "tenure_months": 48,

                # Subscription Information
                "phone_service": True,
                "multiple_lines": True,
                "internet_service": "DSL",
                "online_security": True,
                "online_backup": True,
                "device_protection": False,
                "tech_support": True,
                "streaming_tv": False,
                "streaming_movies": False,

                # Contract & Billing
                "contract_type": "Two Year",
                "paperless_billing": False,
                "payment_method": "Credit Card",
                "monthly_charges": 54.20,
                "total_charges": 2601.60,

                # Usage Metrics
                "avg_call_duration_mins": 410,
                "monthly_data_usage_gb": 120,
                "num_complaints_last_6_months": 0,
                "network_outage_reports": 0,
                "customer_support_calls": 1,

                # Engagement Metrics
                "last_login_days_ago": 2,
                "mobile_app_usage_score": 89.5,
                "promo_offer_used": True,
                "autopay_enabled": True,

                # Derived Behavioral Features
                "late_payment_count": 0,
                "plan_downgrade_last_year": False,
                "international_roaming": True,

                # Target Variable
                "churn": 0
            },

            {
                "customer_id": "CUST_100247",
                "gender": "Female",
                "age": 57,
                "marital_status": "Widowed",
                "dependents": 1,
                "city": "Chennai",
                "tenure_months": 6,

                # Subscription Information
                "phone_service": True,
                "multiple_lines": False,
                "internet_service": "Fiber Optic",
                "online_security": False,
                "online_backup": False,
                "device_protection": False,
                "tech_support": False,
                "streaming_tv": True,
                "streaming_movies": True,

                # Contract & Billing
                "contract_type": "Month-to-Month",
                "paperless_billing": True,
                "payment_method": "Mailed Check",
                "monthly_charges": 102.40,
                "total_charges": 614.40,

                # Usage Metrics
                "avg_call_duration_mins": 180,
                "monthly_data_usage_gb": 410,
                "num_complaints_last_6_months": 5,
                "network_outage_reports": 4,
                "customer_support_calls": 7,

                # Engagement Metrics
                "last_login_days_ago": 28,
                "mobile_app_usage_score": 35.8,
                "promo_offer_used": False,
                "autopay_enabled": False,

                # Derived Behavioral Features
                "late_payment_count": 6,
                "plan_downgrade_last_year": True,
                "international_roaming": False,

                # Target Variable
                "churn": 1
            }
        ]
        return pd.DataFrame(data)