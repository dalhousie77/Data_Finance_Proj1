import pandas as pd

# If the file is in the same directory:
df = pd.read_csv("nasdaq_screener.csv")



# Preview the data
print(df.head(10))
