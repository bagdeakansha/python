# ---------------------integer value---------------
# x=10
# y=20
# z1=x+y
# print(z1)
# print(type(z1))
# z2=x-y
# print(z2)
# print(type(z2))
# z3=x/y
# print(z3)
# print(type(z3))
# print(id(z3))

# ------------------float value---------------------

# x=10.0
# y=20.0
# z1=x+y
# print(z1)
# print(type(z1))
# z2=x-y
# print(z2)
# print(type(z2))
# z3=x/y

# print(z3)
# print(type(z3))
# print(id(z3))

# -----------------complex value-----------------

# x=10+20j
# y=20+10j
# z1=x+y
# print(z1)
# print(type(z1))
# z2=x-y
# print(z2)
# print(type(z2))
# z3=x/y
# print(z3)
# print(type(z3))
# print(id(z3))
#----------------------------------
# === is used for compare value as well as check datatype
# a=(1,2,3,4,5,6)
# print(a[1])
# print(a[-1])

# my_name="Aakansha"
# print(my_name.index("a",(my_name.index("a")+1)))
# # print(my_name.index("A",2))
# # print(my_name.index("A",2,5))
# -----------------------------------------
# my_list=["Akansha",22,"Bhopal","Btech"]
# print(my_list[1])
# print(my_list.index("Bhopal"))

# a="AKANSHA"
# x=a[-1:4:-1]
# x=a[::-1] #reverse
# print(x)

# my_subj=["PYTHON","DJANGO","JS","REACT","C++"]
# x=my_subj[2:15:2]
# print(x)

#predefined function--------
# my_str="akansha"
# print(len(my_str))
# print(max(my_str))
# print(min(my_str))
# print(type(my_str))
# print(str(my_str))
# print(id(my_str))
# # print ord((my_str))
# # print(chr(my_str))

# inbuilt method---------------------
# a="i am Akansha...."
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.center(40,'-'))
# print(a.count('a'))
# str=['python','is','a','programming','language']
# print('-'.join(str))
#---------------------------------------

# a="abc"
# b="123"
# print(a.join(b))
# print('!'.join(b))
# str="My name is Akansha Bagde"
# print(str.split(" "))
# print(str.split(" ",1))

#list----------------------------------
# my_list=[10,20,'Akansha',10,'Cybrom','Bhopal']
# print(len(my_list))
# print(my_list[2])
# my_list[0]="Akku"
# print(my_list)
# print(my_list[2:4]) #slice
# print(my_list.index('Bhopal'))
# print(my_list[-1])

#----------------------------------------
#inbuild function---
# a=[12,58,63,23,45]
# print(sum(a))
# print(max(a))
# print(min(a))
# print(len(a))
#-----------------------------------------------
#inbuild method---
# a=[10,54,26,28,36,45]
# b=[20,59,56,25,78,20]
# a.append('50')#add values from last
# print(a)
# a.append("Akansha")
# print(a)
# a.extend(b) #merge two list
# print(a)
# a.pop() #remove value from last
# print(a)
# a.remove(28)#remove value
# print(a)
# a.insert(4,20) #insert value through index
# print(a)
# a.sort(reverse=True) #arrange value 
# print(a)
# a.reverse()
# print(a)  

#-------------------------------------------------

# a=[10,20,30,40,50]
# b=[1,5,4,6,8]
# tuple------
# a=(10,20,30,40,50)
# print(type(a))
# print(min(a))
# print(max(a))
# print(sum(a))
# print(len(a))
# print(a.count(10))
# print(a.index(10))

# b=(list(a))

# print(b)
# b.append("akansha")
# print(b)

# a.append(b)
# print(a)
# a.extend(b)
# print(a)
# print(c)

# dictionary-------


# my_dict=dict()
# print(my_dict)
# print(type(my_dict))
# print(id(my_dict))
# my_dict['Name']="Akansha"
# print(my_dict)
# my_dict['Age']="22"
# print(my_dict)
# my_dict['Name']="Akku"
# print(my_dict)
# my_dict['city']="Bhopal"
# print(my_dict)

# del my_dict['Name']
# print(my_dict)
# print(my_dict['Name'])
# print(my_dict.clear())
# print(len(my_dict))
# print(max(my_dict))
# print(min(my_dict))
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.get('educ','12th'))#it gives value of key
# print(my_dict.popitem())
# print(my_dict)
# my_dict.pop('Name')
# print(my_dict)
# del my_dict
# print(my_dict)



# my_list=list()
# print(my_list)

#set--------------------------------
# my_set={10,20,50,10,56}
# print(my_set)
# print(max(my_set))
# print(min(my_set))
# print(len(my_set))
# print(set(my_set))
#method----
# my_set.add(25)
# print(my_set)
# my_list=[12,52,32,85,96]
# my_set.update(my_list)
# print(my_set)
# print(len(my_set))
# my_set.remove(52)
# print(my_set)
# my_set.discard(5)
# print(my_set)
s1={10,20,30,40,50}
s2={10,20,32,40,55}
print(s1.union(s2))
print(s1.intersection(s2))





