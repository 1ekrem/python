import datetime

list1 = ['Jack', 'BTC', 'KTC']
list2 = ['35.0', '25.5', '324.5']

d = {}


for i, j in zip(list1, list2):
  d[i] = d.get(i, {})
  d[i]['%s' % j] = j= j

print(d)

