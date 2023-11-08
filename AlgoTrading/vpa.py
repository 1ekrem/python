import yfinance as yf
import pandas as pd

def analyze_stock_data(stock_symbol, start_date, end_date):
    # Download stock data
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    
    # Volume Analysis
    max_volume = stock_data['Volume'].max()
    min_volume = stock_data['Volume'].min()

    
    # Define the rules for analysis
    def rule_1(candle):
        # Large Body + No Wicks
        if (candle['Volume']/max_volume) >= high_volume_threshold and (((candle['Close'] - candle['Open']) / (candle['High'] - candle['Low'])) >= 0.15):
            if candle['Close'] > candle['Open']:
                return "Strong Bullish move"
            else:
                return "Strong Bearish move"
        else:
            if (candle['Close'] > candle['Open']) and ((candle['Volume']/max_volume) >= 0.6):
                return "Weak Bullish Move"
            elif (candle['Close'] < candle['Open']) and ((abs(candle['Close'] - candle['Open']) /candle['Open'] ) >= 0.03) and (0.3 <= (candle['Volume']/max_volume) <= 0.4):
                return "Weak Bearish Move"
            else:
                return
    
    def rule_2(candle):
        # Small Body + Large Wick
        body_size = abs(candle['Close'] - candle['Open'])
        lower_wick = candle['Low'] - min(candle['Open'], candle['Close'])
        upper_wick = max(candle['Open'], candle['Close']) - candle['High']
        if candle['Volume'] >= high_volume_threshold:
            if lower_wick > body_size:
                return "Buyers stepping in"
            elif upper_wick > body_size:
                return "Sellers stepping in"
        else:
            if lower_wick > body_size:
                return "No significant buyers"
            elif upper_wick > body_size:
                return "No significant sellers"
    
    def rule_3(candle):
        #Small Body + 2 Wicks (doji candle)
        body_size = abs(candle['Close'] - candle['Open'])
        if body_size < small_body_threshold:
            return "Doji Candle"
    
    def rule_4(candle):
        #Validating Price Action With Volume
        body_size = abs(candle['Close'] - candle['Open'])
        if body_size < small_body_threshold and len(candle) == 4:
            return "Doji Candle"
    
    def rule_5(candle):
        body_size = abs(candle['Close'] - candle['Open'])
        if candle['Volume'] >= high_volume_threshold and body_size < small_body_threshold:
            return "Trend is weak"
    
    def rule_6(candle):
        body_size = abs(candle['Close'] - candle['Open'])
        if body_size >= small_body_threshold:
            if candle['Volume'] >= high_volume_threshold:
                return "Strong Move"
            else:
                return "Weak Move"
    
    def rule_7(candle):
        if candle['Volume'] >= high_volume_threshold:
            return "Reversal"
        else:
            return "REAL PULLBACK"
    
    # Set your threshold values here
    high_volume_threshold = 0.75  # Set your threshold for high volume
    small_body_threshold = 0.01  # Set your threshold for a small body
    
    # Apply the rules to each candle
    stock_data['Rule1'] = stock_data.apply(rule_1, axis=1)
    # stock_data['Rule2'] = stock_data.apply(rule_2, axis=1)
    # stock_data['Rule3'] = stock_data.apply(rule_3, axis=1)
    # stock_data['Rule4'] = stock_data.apply(rule_4, axis=1)
    # stock_data['Rule5'] = stock_data.apply(rule_5, axis=1)
    # stock_data['Rule6'] = stock_data.apply(rule_6, axis=1)
    # stock_data['Rule7'] = stock_data.apply(rule_7, axis=1)
    stock_data.insert(0, 'Date',stock_data.index.date)
   
    return stock_data

# Example usage
stock_symbol = "AMD"
start_date = "2023-01-01"
end_date = "2023-12-31"
result = analyze_stock_data(stock_symbol, start_date, end_date)

# Save the results to an Excel file
output_filename = "stock_analysis_results.xlsx"
result.to_excel(output_filename, index=False)
print(f"Data exported to {output_filename}")
