import pandas as pd
from bsm_functions import bsm_call_imp_vol, bsm_call_value, bsm_vega

h5 = pd.HDFStore("FinancialCrashCourse\\Chapter3\\vstoxx_data_31032014.h5", "r")

#h5 = pd.HDFStore('./source/vstoxx_data_31032014.h5', 'r')
futures_data = h5['futures_data'] # VSTOXX futures data
options_data = h5['options_data'] # VSTOXX call option data
h5.close()

options_data = options_data[['DATE', 'MATURITY', 'TTM', 'STRIKE', 'PRICE']]

options_data['IMP_VOL'] = 0.0

print(options_data.head())

tol = 0.5
for option in options_data.index:
    #iterating over all option quotes
    forward = futures_data[futures_data['MATURITY'] == \
        options_data.loc[option]['MATURITY']]['PRICE'].value[0]
    # picking the right futures value
    if (forward * (1 - tol) < options_data.loc[option]['STRIKE']
        < forward * (1 + tol)):
    # only for options with moneyness within tolerance
        imp_vol = bsm_call_imp_vol(
            #V0, # VSTOXX value
            options_data.loc[option]['STRIKE'],
            options_data.loc[option]['TTM'],
            #r, # short rate
            options_data.loc[option]['PRICE'],
            sigma_est=2., # estimate for implied volatility
            it=100)
        options_data['IMP_VOL'].loc[option] = imp_vol