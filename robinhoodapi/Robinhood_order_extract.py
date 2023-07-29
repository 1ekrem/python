import robin_stocks as rs
import datetime

today_date = datetime.datetime.now().strftime("%m-%d-%Y")

secToExp = 86400
password_val = '2058007Ee@'

rs.login(username="ersekrem@gmail.com", password=password_val, expiresIn=86400, by_sms=True )


'''OPTION TRANSACTIONS EXTRACT'''
rs.export_completed_option_orders("C:\\PythonClass\\robinhoodapi\\order_history", "option_history_{}".format(today_date))

'''STOCK TRANSACTIONS EXTRACT'''
#rs.export_completed_stock_orders("C:\\PythonClass\\robinhoodapi\\order_history", "stock_history_{}".format(today_date))
