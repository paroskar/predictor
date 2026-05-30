from django.shortcuts import render
from .forms import FinancialForm

def home(request):
    return render(request, "predictor_app/home.html")

def analyze(request):
    result = None
    form = FinancialForm()
    if request.method == "POST":
        form = FinancialForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            total_debt = data["rent"] + data.get("car_payment", 0) + data["credit_card_payment"] + data.get("student_loan", 0)
            dti = total_debt / data["monthly_income"] if data["monthly_income"] > 0 else 1
            risk_score = min(100, int(dti * 100 + data["late_payments"] * 5))
            if risk_score >= 70:
                status = "HIGH RISK"
            elif risk_score >= 30:
                status = "MEDIUM RISK"
            else:
                status = "LOW RISK"
            result = {"risk_score": risk_score, "status": status, "default_prob": risk_score}
    return render(request, "predictor_app/analyze.html", {"form": form, "result": result})
