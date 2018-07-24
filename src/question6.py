import math

#formula: sqrt((2 * C * D)/H)
#ex: str[(100 * D)/30]


my_input = input("Enter stuff: ")
data=my_input.split(",")

for temp in data:
    q = math.sqrt(2 * 50 * float(temp)/30)
    print("q is : " + str(q))
    




