from django import forms

class FinancialForm(forms.Form):
    credit_score = forms.IntegerField(label="Credit Score", min_value=300, max_value=850, initial=680)
    age = forms.IntegerField(label="Age", min_value=18, max_value=100, initial=35)
    monthly_income = forms.IntegerField(label="Monthly Income", initial=5000)
    rent = forms.IntegerField(label="Rent or Mortgage", initial=1500)
    car_payment = forms.IntegerField(label="Car Payment", required=False, initial=400)
    credit_card_payment = forms.IntegerField(label="Credit Card Payment", initial=300)
    student_loan = forms.IntegerField(label="Student Loan", required=False, initial=200)
    late_payments = forms.IntegerField(label="Late Payments", initial=0)
    credit_balance = forms.IntegerField(label="Credit Card Balance", initial=3000)
    credit_limit = forms.IntegerField(label="Credit Card Limit", initial=10000)
    savings = forms.IntegerField(label="Savings", initial=10000)
