"""
list  is a collections of hetrogenous items it could be a string , integer or boolean or etc that means there can be a
dictionary inside the list , list ,
(1) A list can be shown by []
(2) A list maintains the order
(3) Duplicate can be created
(4) list is mutable
  - list can be read create update delete

"""
example1=[]
print(type(example1))
example2=[1,2,3,"devansh",True,False,2+3j,[1,2,"mohan"],{"singh":19}]
print(type(example2))

"""
how to convert a string to list
"""

#name="devansh singh"
#print(list(name))

#print(list("name")==["n","a","m","e"])

#name=[1,2,"a","b","c","parveen pathania"]
#print(name[1:3:1])

"""
nest=[1,2,3,[3,4,5,[6,7,8,["a","b","c"]]]]
print(nest[3][2])
nest[2:]="devansh"
print(nest)
"""
list=[1,2,34.3,23]
print(len(list))
print(max(list))
print(min(list))
list.append("devansh")
print(list)