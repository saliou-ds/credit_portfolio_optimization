
import pandas as pd
from module_2_rwa_calculation import calculate_rwa

df = pd.read_csv("data/portfolio_with_rwa.csv")
original_total_rwa = df["RWA"].sum()
threshold_rwa = df["RWA"].quantile(0.90)
cds_coverage = df["RWA"] >= threshold_rwa
df.loc[cds_coverage & (df["LGD"] > 0.45), "LGD"] = 0.45
df["RWA_after_CDS"] = df.apply(lambda row: calculate_rwa(row["PD"], row["LGD"], row["EAD"], row["Maturity"]), axis=1)

disposal_threshold = df["RWA_after_CDS"].quantile(0.95)
df["RWA_final"] = df["RWA_after_CDS"]
df.loc[df["RWA_after_CDS"] >= disposal_threshold, "RWA_final"] = 0.0

df.to_csv("data/portfolio_optimized.csv", index=False)
