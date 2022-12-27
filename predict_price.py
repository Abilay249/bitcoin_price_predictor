import pandas as pd

def get_trading_signals(data):
  # Calculate the moving average for the data
  data['ma'] = data['price'].rolling(window=10).mean()
  
  # Create a column for signals
  data['signal'] = 0
  
  # Set the signal to 1 if the price is above the moving average
  data.loc[data['price'] > data['ma'], 'signal'] = 1
  
  # Set the signal to -1 if the price is below the moving average
  data.loc[data['price'] < data['ma'], 'signal'] = -1
  
  return data

# Load the data
df = pd.read_csv('bitcoin_data.csv')

# Get the trading signals
signals = get_trading_signals(df)

# Print the signals
print(signals)