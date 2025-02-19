# filter
from functools import reduce
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print("filter data over 75 : ",over_75)


#map
a = ['Tina', 'Raj', 'Tom']
print("list : ",a)
print ("length of above list : ",list(map(len, a)))  
# prints [4, 3, 3]


#Reduce
print('printing final itrative result : ',reduce(lambda x, y : x + y,[1,2,3]))


# prints 6