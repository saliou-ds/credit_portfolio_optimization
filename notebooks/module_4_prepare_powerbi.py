
import pandas as pd

df = pd.read_csv("data/portfolio_optimized.csv")
df_powerbi = df[[
    "Loan ID", "Rating", "PD", "EAD", "LGD", "Maturity",
    "Sector", "Country", "Secured",
    "RWA", "RWA_after_CDS", "RWA_final"
]]
df_powerbi = df_powerbi.round(2)
df_powerbi.to_csv("data/powerbi_credit_portfolio.csv", index=False)
