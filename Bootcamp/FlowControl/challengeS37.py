

ipAddress = input("Please enter a IP address: \n")

segment = 1
segment_length = 0
char=""

for char in ipAddress:
    if char ==".":
        print("Segment {} contains {} characters".format(segment,segment_length))
        segment+=1
        segment_length=0
    else:
        segment_length+=1
if char != ".":
    print("Segment {} contains {} characters".format(segment,segment_length))
