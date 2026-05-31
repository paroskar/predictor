# FinShield AI

## Financial Wellness and Bankruptcy Early Warning System

## Team IntelliRate AI (Team 6, Group 15)

### Team Members
- Prasad Vishnu Aroskar
- Sai Sarath Chandra Ganti
- Gaganmeet Kapoor
- Samyuktha Siddam
- Yashaswini Nasa

---

## Project Overview

FinShield AI is a financial wellness assistant that predicts bankruptcy risk 6-12 months before traditional credit scores. The system uses **XGBoost** machine learning with **SHAP** explainability to provide transparent, actionable recommendations.

## Features

| Feature | Description |
|---------|-------------|
| Risk Score | 0-100 scale (0=low risk, 100=high risk) |
| Default Probability | Likelihood of missing payments in 6-12 months |
| Debt-to-Income Ratio | Calculated from your monthly payments |
| Wellness Commands | Specific actions to improve financial health |
| SHAP Analysis | Understand what factors affect your score |

## Dataset Information

- **Source:** UCI Machine Learning Repository - Default of Credit Card Clients Dataset
- **Size:** 30,000 records
- **Features:** Credit limit, payment history, bill amounts, demographics
- **Target:** Default payment next month (Yes/No)
- **Supplemental Data:** Federal Reserve Bank of NY Household Debt Report

## Technology Stack

| Component | Technology |
|-----------|------------|
| Backend | Django 6.0 |
| ML Model | XGBoost Classifier |
| Explainability | SHAP (SHapley Additive exPlanations) |
| Frontend | Bootstrap 5, HTML/CSS |
| Data Processing | Pandas, NumPy, Scikit-learn |

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/predictor.git
cd predictor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

## Usage

1. Open browser to `http://127.0.0.1:8000/`
2. Click "Start Your Analysis"
3. Enter your financial details:
   - Credit score (300-850)
   - Monthly income
   - Rent/mortgage payment
   - Car payment
   - Credit card payment
   - Student loan payment
   - Credit card balance and limit
   - Savings amount
4. Click "Analyze My Risk"
5. View your personalized risk report and recommendations

## References (APA 7th Edition)

Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 785–794.

Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. *Advances in Neural Information Processing Systems 30 (NIPS 2017)*, 4765–4774.

Altman, E. I. (1968). Financial ratios, discriminant analysis and the prediction of corporate bankruptcy. *The Journal of Finance*, *23*(4), 589–609.

Yeh, I. C., & Lien, C. H. (2009). The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. *Expert Systems with Applications*, *36*(2), 2473–2480.

Federal Reserve Bank of New York. (2025). *Household debt and credit report (Q4 2025)*. Center for Microeconomic Data.

## Data Sources

- [UCI Credit Default Dataset](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients)
- [FRBNY Household Debt Report](https://www.newyorkfed.org/microeconomics/databank.html)

## Contact

**Team IntelliRate AI**
New England College
Email: paroskar_gps@nec.edu

## License

This project is for academic purposes at New England College.

## Acknowledgments

- Dr. Nafees Qamar (Residency Lead)
- Dr. Joan Lawson (Program Director)
- New England College AI Program
