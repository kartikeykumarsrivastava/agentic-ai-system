from fastapi import FastAPI
from pydantic  import BaseModel

app = FastAPI()

#------- ------------------------------------               
# Request Schema
#---------------------------------------

class EligibilityRequest(BaseModel):
    salary: int
    age: int
    existing_emi: int =0
    credit_score: int = 700
    employment_type: str = "salaried"  # salaried or self-employed

#---------------------------------------
# core logic
#---------------------------------------

def calculate_eligibility(data: EligibilityRequest):
    monthly_income = data.salary / 12
    max_emi_allowed = monthly_income * 0.4  

    if data.credit_score < 600: 
        return {"eligible": False, "reason": "Low credit score"}
    if data.age < 21 or data.age > 60:
        return {"eligible": False, "reason": "Age not in eligible range"}
    if data.existing_emi > max_emi_allowed:
        return {"eligible": False, "reason": "Existing EMIs exceed eligibility"}
    # Rule 4: Employment type risk
    risk_multiplier = 1.0
    if data.employment_type == "self-employed":
        risk_multiplier = 0.8

    # Loan estimation
    max_emi = max_emi_allowed - data.existing_emi
    tenure_years = 20

    loan_amount = max_emi * 12 * tenure_years * risk_multiplier


    return {
        "eligible": True,
        "max_loan_amount": round(loan_amount),
        "max_emi": round(max_emi),
        "tenure_years": tenure_years
    }

# -----------------------
# API Endpoint
# -----------------------
@app.post("/check")
def check_eligibility(req: EligibilityRequest):
    return calculate_eligibility(req)