import time

cusip = input("Enter CUSIP: ")
messagetype = input("Enter message type: ")
side = input("Enter side: 1-BUY or 2-SELL: ")
qty = input("Enter quantity in numbers. Ex: 100. : ")
ordertype = input("Enter order type: ")
price = input("Enter desired price level: ")
scenario = input("Behavior of the dealer? : ")

def outgoing():
    if messagetype == '35=R' and scenario == 'accept':
        print('Order is accepted by the dealer! Please check your execution report')
        time.sleep(3)
        print(('8=FIX4.4^9=261^35=AJ^34=997^49=ProxyVBond^52=20140225-16:27:35.546^56=ProxyWFS^57=executions^11=10530867^22=1^38={}^44={}^48=025815AA9^54={}').format(qty, price, side)+
                ('^55=025815AA9^64=6^64=20140303^117=RFQ:4312342:2014022500209764:WELLSFD2^236=0.654^423=1^693=10530867^694=1^6370=WELLSFD2^6371=N/A^10=181'))
    if scenario == 'reject':
        print("Dealer has rejected the trade! Please submit a new RFQ!")
    

# outgoing('tsla', '35=R', 2, 200, 'LMT', 100.375)

outgoing()
