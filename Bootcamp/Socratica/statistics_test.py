import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg) 

print(list(filter(lambda x: x > avg, data)))

above_average = []
for i in data:
    if avg < i:
        above_average.append(i)
print(above_average)

print(list(filter(lambda x: x < avg, data)))
