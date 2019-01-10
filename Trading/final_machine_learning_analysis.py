'''
Machine Learning Buy & Sell signal 4
'''
from collections import Counter
import numpy as np 
import pandas as pd 
import pickle
from sklearn import svm, neighbors, model_selection as cross_validation
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

def process_data_for_labels(ticker):
    hm_days = 7 # Number of days taken under decision
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        print(i)
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker])/df[ticker]  #When you shift things negatively, future data goes up 
    
    df.fillna(0, inplace=True)
    return tickers, df

#Target Function
def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02 # If stock price changes 2%, we'll have a notification
    for col in cols:
        if col > 0.025:
            return 1
        if col < -0.025:
            return -1
    return 0

#Now need to map target function to process data function
def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)
    #lets define the new column where it'll be mapping the target function to process data
    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,
                                            df['{}_1d'.format(ticker)],
                                            df['{}_2d'.format(ticker)],
                                            df['{}_3d'.format(ticker)],
                                            df['{}_4d'.format(ticker)],
                                            df['{}_5d'.format(ticker)],
                                            df['{}_6d'.format(ticker)],
                                            df['{}_7d'.format(ticker)]
                                            ))

    vals = df['{}_target'.format(ticker)].values.tolist() # This will be 
    str_vals = [str(i) for i in vals]
    print('Data spread: ', Counter(str_vals))
    
    df.fillna(0, inplace=True)
    df=df.replace([np.inf, -np.inf], np.nan) # We replacing infinite bases to finite base.
    df.dropna(0, inplace=True) #So crazy values are out

    df_vals = df[[ticker for ticker in tickers]].pct_change() #Normalized by pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    X = df_vals.values
    y = df['{}_target'.format(ticker)].values

    return X, y, df

def do_ml(ticker):
    X, y, df = extract_featuresets(ticker)

    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.25)

    #clf = neighbors.KNeighborsClassifier()
    
    clf = VotingClassifier([('lsvc', svm.LinearSVC()),
                            ('knn', neighbors.KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())])
    
    clf.fit(X_train, y_train) #use a classifier that fit target data
    confidence = clf.score(X_test, y_test)
    print('Ticker: ', ticker)
    print('Accuracy ', confidence)
    predictions = clf.predict(X_test)
    print('Predicted spread: ', Counter(predictions))

    return confidence

do_ml('V')