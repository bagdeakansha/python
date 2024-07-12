#map()-----
#WAP to print the square  of values---
# my_list=[1,2,3,4,5]
# def sq(n):
#     return n**2
# new_list=tuple(map(sq,my_list))
# print(new_list)

#WAP to find addition of two list on the basis of indexing--
# my_list1=[1,2,3,4,5]
# my_list2=[5,4,3,2,1]
# def add(x,y):
#     return x+y
# new_list=list(map(add,my_list1,my_list2))
# print(new_list)

#-----------------------------

# def add(x,y):
#     return x+y
# new_list=list(map(add,[2,4,6,8],[1,2,3,4]))
# print(new_list)

#lambda function---
x=lambda a,b:a+b
y = list(map(x,[1,2,3,4,5],[1,2,3,4,5]))
print(y)