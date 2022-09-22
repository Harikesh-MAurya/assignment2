# (question-1).........................................................
from keyword import kwlist

print("Learning Python")  # hatch it is used as a comment 


# (question-2)........................................................
""" harikesh"""  # """ name """ (triple enverted comma) this is use for multiline comment
# a,b,c,d=input("enter four variables : ").split(",")
# a=int(a)
# b=int(b)
# c=int(c)
# d=int(d)
# print("\n",a,"\n",b,"\n",c,"\n",d)


# (question-3)..........................................................
# a,b,c,d,e=35,True,"mysirji",5.46,3+4j
# print(type(a),type(b),type(c),type(d),type(e))


# (question-4).........................................................
x=5
y=5
print(id(x))
print(id(y))       # id will be same for both x and y


# (question-5).........................................................
a=float(10)
# b=bool("harikesh")
# c=int(10.63)
# d=str(19)
# print(type(a),id(a))
# print(type(b),id(b))
# print(type(c),id(c))
# print(type(d),id(d))


# (question-6).........................................................
print(kwlist)


# (question-8).........................................................
import assignments2
print(assignments2.x)
print(assignments2.y)


# (question-9)........................................................
x,y,z=22,9,2022
print(x,y,z,sep="-")

import datetime
current_time=datetime.datetime.now()
print(current_time)