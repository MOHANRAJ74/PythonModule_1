# Python program to illustrate the use
# of 'is' identity operator
num1 = 5
num2 = 5

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = lst1

str1 = "hello world"
str2 = "hello world"

tup1=(1,2,3,4,5)
tup2=(1,2,3,4,5)
tup3=(2,3,5,8,9)

set1={1,2,3,4,5}
set2={1,2,3,4,5}
set3={3,4,5,6,8}

# using 'is' identity operator on different datatypes
print("Num1 is not Num2: ",num1 is not num2)
print("lst1 is not lst2: ",lst1 is not lst2)
print("str1 is not str2: ",str1 is not str2)
print("tup1 is not tup2: ",tup1 is not tup2)
print("tup1 is not tup3: ",tup1 is not tup3)
print("set1 is not set2: ",set1 is not set2)
print("set1 is not set3: ",set1 is not set3)


print("ID of num1: ",id(num1))
print("ID of num2: ",id(num2))
print("ID of lst1: ",id(lst1))
print("ID of lst2: ",id(lst2))
print("ID of str1: ",id(str1))
print("ID of str2: ",id(str2))
print("ID of tup1: ",id(tup1))
print("ID of tup2: ",id(tup2))
print("ID of tup3: ",id(tup3))
print("ID of set1: ",id(set1))
print("ID of set2: ",id(set2))
print("ID of set3: ",id(set3))







