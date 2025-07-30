
import pandas as pd
import numpy as np

np.random.seed(42)

n_loans = 2500
rating_pd_map = {'AAA': 0.0003, 'AA': 0.0006, 'A': 0.002, 'BBB': 0.005, 'BB': 0.018, 'B': 0.05, 'CCC': 0.2}
ratings = list(rating_pd_map.keys())
rating_weights = [0.05, 0.1, 0.2, 0.25, 0.2, 0.15, 0.05]
industries = ['Manufacturing', 'Retail', 'Energy', 'Real Estate', 'Transport', 'Finance', 'Healthcare']
countries = ['Germany', 'France', 'USA', 'UK', 'Italy', 'Brazil', 'China']

data = {
    "Loan ID": [f"L{str(i).zfill(5)}" for i in range(1, n_loans + 1)],
    "Rating": np.random.choice(ratings, size=n_loans, p=rating_weights),
    "EAD": np.random.lognormal(mean=13, sigma=0.5, size=n_loans),
    "Maturity": np.random.randint(1, 11, size=n_loans),
    "Sector": np.random.choice(industries, size=n_loans),
    "Country": np.random.choice(countries, size=n_loans),
    "Secured": np.random.choice(['Yes', 'No'], size=n_loans, p=[0.6, 0.4])
}

df = pd.DataFrame(data)
df["PD"] = df["Rating"].map(rating_pd_map)
df["LGD"] = df["Secured"].apply(lambda x: 0.45 if x == "Yes" else 0.75)
df["EAD"] = df["EAD"].round(2)
df.to_csv("data/simulated_portfolio.csv", index=False)
