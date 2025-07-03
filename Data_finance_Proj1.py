import pandas as pd

# If the file is in the same directory:
df = pd.read_csv("nasdaq_screener.csv")

# If it's somewhere else, use the full path:
# df = pd.read_csv("C:/Users/YourUsername/Documents/nasdaq_tickers.csv")

# Preview the data
print(df.head(10))
