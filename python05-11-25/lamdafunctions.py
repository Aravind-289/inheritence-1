#1
add_num=lambda a,b:a+b
print(add_num(5,6))
#2
add_num=lambda a,b:a**b
print(add_num(5,2))
#3 to convert celsius in to farenheit
celTofar=lambda c:(9/5)*c+32
print(celTofar(37))
# write a lambda functions even or odd
evenodd=lambda num: 'even' if num%2==0 else 'odd'
print(evenodd(8))
# greterthen 2 numbers
gretar=lambda num1,num2: 'big' if num1>num2 else 'num2 is big'
print(gretar(4,6))   
# lambda functions with sort
names=['aravind','nikhil','ajay','raju','lavanya']
names.sort(key=lambda name:len(name))
print(names)
#lambda functions with sort numbers
num=[89,75,68,25,34,75,12]
num.sort(key=lambda numbers:numbers)
print(num)
#lambda functions with map() function
list1=[1,2,3,4,5]
sqrlist=list(map(lambda num:num**2,list1) )
print(sqrlist)
#lambd with filter() functions
list2=[1,2,3,4,5,6,7,8,9,10]
filterFunc=list(filter(lambda   num:num%2==0 , list2))
print(filterFunc)
# lambda with reduce() function
from functools import reduce
list3=[1,2,3,4,5]
reduceFunc=reduce(lambda num1,num2: num1*num2,list3)
print(reduceFunc)

list=['aravind kukatla','velpula rachana','dandiga soumya','ankem mahesh']
print(list[1][8])