import pandas as pd
#fb = pd.read_csv('../data/facebook.csv', index_col = 0)

data = {'A': [1, 2, 3, 4, 5,6]}
df = pd.DataFrame(data)

df_shifted = df.shift(1)
print(df_shifted)
rolling_mean = df.rolling(1).mean()
print(rolling_mean)