import yfinance as yf

def get_sector_performance():
    sectors = {
        'XLC': '$XLC Communication Services',
        'XLY': '$XLY Consumer Discretionary',
        'XLP': '$XLP Consumer Staples',
        'XLE': '$XLE Energy',
        'XLF': '$XLF Financials',
        'XLV': '$XLV Health Care',
        'XLI': '$XLI Industrials',
        'XLB': '$XLB Materials',
        'XLRE':'$XLRE Real Estate',
        'XLK': '$XLK Technology',
        'XLU': '$XLU Utilities'
    }
    
    data = yf.download(list(sectors.keys()),period="max")
    performances = {}
    
    for sector_ticker, sector_name in sectors.items():
        sector_data = data[('Close', sector_ticker)].pct_change()[-1] * 100
        performances[sector_name] = sector_data.item()
    
    return performances

sector_performance = get_sector_performance()
for sector, performance in sector_performance.items():
    print(f'{sector}: {performance:.2f}%')
