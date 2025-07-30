
import pandas as pd
import numpy as np
from scipy.stats import norm

def calculate_rwa(pd, lgd, ead, maturity):
    R = 0.12 * (1 - np.exp(-50 * pd)) / (1 - np.exp(-50)) + 0.24 * (1 - (1 - np.exp(-50 * pd)) / (1 - np.exp(-50)))
    b = (0.11852 - 0.05478 * np.log(pd)) ** 2
    maturity_adj = (1 + (maturity - 2.5) * b) / (1 - 1.5 * b)
    d = norm.ppf(pd)
    k = lgd * (norm.cdf((d + np.sqrt(R) * norm.ppf(0.999)) / np.sqrt(1 - R)) - pd)
    rwa = 12.5 * k * maturity_adj * ead
    return rwa

df = pd.read_csv("data/simulated_portfolio.csv")
df["RWA"] = df.apply(lambda row: calculate_rwa(row["PD"], row["LGD"], row["EAD"], row["Maturity"]), axis=1)
df["RWA"] = df["RWA"].round(2)
df.to_csv("data/portfolio_with_rwa.csv", index=False)
