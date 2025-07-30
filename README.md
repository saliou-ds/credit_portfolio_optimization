
# Credit Portfolio Risk & Capital Optimization

This repository contains a professional-grade simulation and optimization tool for credit portfolio analysis,
focusing on regulatory Risk-Weighted Asset (RWA) computation and capital optimization strategies in line with Basel II/III standards.

## 🔍 Project Overview

The project simulates a portfolio of 2,500 loans and applies regulatory formulas to compute credit risk metrics.
Optimization strategies such as Credit Default Swaps (CDS) and asset disposal are used to reduce the total capital requirement.

## 📁 Repository Structure

```
credit-portfolio-optimization/
├── data/
│   ├── simulated_portfolio.csv
│   ├── portfolio_with_rwa.csv
│   ├── portfolio_optimized.csv
│   └── powerbi_credit_portfolio.csv
├── app/
│   └── streamlit_app.py
├── reports/
│   └── Credit_Portfolio_Optimization_Report.pdf
├── notebooks/
│   └── (optional Jupyter notebooks)
├── utils/
│   └── (calculation modules if separated)
├── requirements.txt
└── README.md
```

## 🧮 Features

- Simulated loan portfolio with realistic PD, LGD, EAD, rating, and sector distributions
- Basel II/III RWA computation using IRB formulas
- Capital optimization via CDS and loan disposals
- Streamlit-based interactive dashboard
- Power BI-ready dataset
- Professional PDF summary report

## 📊 Optimization Results (Sample)

- **Original RWA:** €1.85B
- **Final RWA:** €1.41B
- **Capital Saved:** €445.5M
- **RWA Reduction:** 24.04%
- **CDS Applied to:** 250 loans
- **Loans Disposed:** 125

## 🚀 Getting Started

1. Clone this repository
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run app/streamlit_app.py
    ```

## 📦 Requirements

- Python 3.8+
- pandas, numpy, scipy, streamlit, fpdf

## 📝 License

This project is provided for academic and internal quantitative risk management use only.

---

*Developed by a Credit Risk Analyst for internal simulation and strategic capital planning.*
