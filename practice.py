
# 1. wap to check whether a person eligible for voting or not

# age=int(input("enter your age"))
# if age>=18:
#     print("eligible for voting")
# else:
#     print("not eligible for voting")


#  2. WAP TO CHECK WHETHER A NUMBER ENTERED BY USER IS EVEN OR ODD

# num=int(input("enter a number"))
# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd")


#     3. WAP TO CHECK WHETHER A NUMBER IS DIVISIBLE BY 7 OR NOT

# num=int(input("enter a number"))
# if num%7==0:
#     print("it is divisible by 7")
# else:
#     print("not divisible by 7")

# 4. WAP TO DISPLAY "HELLO" IF A NUMBER ENETERED BY USER IS A MULTIPLE OF 5

# num=int(input("enter a number"))
# if num%5==0:
#     print("hello")
# else:
#     print("bye")

# 5. WAP TO CALCULATE THE ELECTRICITY BILL

# amt=0
# unit=int(input("number of unit"))
# if unit<=100:
#     amt=0
# if unit>100 and unit<=200:
#     amt=(unit-100)*5
# if unit>200:
#     amt=500+((unit-200)*10)
#     print("electricity bill:",amt)

# 6.WAP TO DISPLAY THE LAST DIGIT NUMBR

# num=int(input("enter a number"))
# print("last digit number:",num%10)

#7. WAP TO CHECK WHETHER THE LAST DIGIT OF A NUMBER IS DIVISIBLE BY 3 OR NOT

# num=int(input("enter a number"))
# print("last digit number:",num%10)
# lastdigit=num%10
# if lastdigit%3==0:
#     print("divisible by 3")
# else:
#     print("not divisible")

#8.WAP TO ACCEPT ANY CITY FROM THE USER AND DISPLAY MONUMENT OF THAT CITY
# city=(input("enter the city name :"))
# if city.lower()=="delhi":
#     print("red fort")
# elif city.lower()=="agra":
#         print("taj mahal")

# 9. TO ACCEPT PERCENTAGE FROM THE USER

# marks=int(input("enter marks  :"))
# if marks>90:
#     print("grade A")
# elif marks>80 and marks<=90:
#     print("grade B")

# 10. A PERSON IS SENIOR CITIZEN OR NOT 

# age=int(input("enter age of a citizen"))
# if age>=60:
#     print("a person is senior citizen")
# else:
#   print("a person is not a senior citizen")

# 11.  A NUMBER IS POSITIVE OR NEGATIVE

# num1=float(input("enter a number"))
# if num1>0:
#     print("the number is positive")
# else:
#     print("number is negative")

# 12. NUMBER IS DIVISIBLE BY 2 & 3 BOTH

# num=int(input("enter a number  :"))
# if num%2==0 and num%3==0:
#     print("number is divisible by 2 and 3 both")
# else:
#     print("not divisible")

# 13. FIND THE LARGEST NUMBER OUT OF THREE NUMBER EXPECTED FROM User

# num1=int(input("enter a number  : "))
# num2=int(input("enter a number  : "))
# num3=int(input("enter a number  : "))
# if num1>num2 and num1>num3:
#     print("largest number is  : ",num1)
# elif num2>num1 and num2>num3:
#     print("largest number is  : ",num2)
# elif num3>num1 and num3>num2:
#     print("largest number is  : ",num3)

# 14. accept the age of 4 people and display youngest one

# age1=int(input("enetr age  : "))
# age2=int(input("enetr age  : "))
# age3=int(input("enetr age  : "))
# if age1<age2 and age1<age3:
#     print("youngest among 3 people is: ",age1)
# elif age2<age1 and age2<age3:
#     print("youngest among 3 people is: ",age2)
# elif age3<age1 and age3<age2:
#     print("youngest among 3 people is: ",age3)

# 15. TO CHECK A CHARACTER IS VOWEL OR NOT

# ch=str(input("enter a character"))
# vow="aeiouAEIOU"
# if ch in vow:
#   print("it is a vowel ")
# else:
#   print("not a vowel")

# 16. 

# nd=int(input("no of working days : "))
# na=int(input("number of days for absent : "))
# per=(nd-na)/nd*100
# if per<75:
#     print("student will not able to sit in exam")
# else:
#     print("able to present")

# 17.

# per=float(input("enter your percentage :  "))
# if per>80:
#     print("your grade is A+")
# elif per>60 and per<80:
#     print("your grade is A")
# elif per>50 and per<60:
#     print("your grade is B+")

#18

# ser=int(input("enter years of service  : "))
# sal=float(input("enter your salary  : "))
# if ser>10:
#     a=10/100*sal
# if ser>=6 and ser<=10:
#     a=8/100*sal
# if ser<6:
#     a=5/100*sal
# print("net bonous amount  : ",a)

#20. 

# num1=int(input("enter a number  : "))
# num2=int(input("enter a number  :"))
# opt=input("enter a opertaor  : ")
# if opt=="+":
#     print("answer is : ",num1+num2)
# if opt=="-":
#     print("answer is : ",num1-num2)


# 21. CREATE A PYTHON LIST

# mylist=[12,34,23,78,90,87,56]
# print(mylist)

# mylist1=["nitu","jitu","guddu"]
# print(mylist1)

# 22. CRETAE LIST WITH DIFFERENT DATATYPES

# my=["jitu",10,9.5]
# print(my)

# 23. ACCESS VALUES FROM A LIST

# my=["jitu",10,9.5]
# print(my[1])

#  24. update list values

# my=["jitu",10,9.5]
# my[1]="manisha"
# print("update list=\n",my)

#  25. REMOVE ELEMENTS FROM A LIST

# my=["jitu",10,9.5]
# print(my)
# del my[1]
# print(my)

# 26.  REMOVE A SPECIFIC ELEMENT FROM A PYTHON LIST

# my=["jitu",10,9.5]
# print(my)
# my.remove("jitu")
# print(my)

# 27. wap to perform addition,subtraction,multiplication,division

# a=int(input("enter 1st number  :  "))
# b=int(input("enter 2 nd number  : "))
# add=a+b
# sub=a-b
# mul=a*b
# div=a/b
# print("addition of two number :",add )

# 28. area of rectangle

# length=float(input("enter length of rectangle in meter:  "))
# width=float(input("enter width of  rectangle in meter:  "))
# area=length*width
# print("area of rectangle=  ",area)


# 29. perimeter of rectangle

# length=float(input("enter length of rectangle in meter :  "))
# width=float(input("enter width of  rectangle meter :  "))
# perimeter=2*(length+width)
# print("perimeter of rectangle = ",perimeter)


#30. area of square

# s=float(input("enter side length in centimeter  : "))
# s1=float(input("enter side length in centimeter  : "))
# side=s*s1
# print("area of square= ",side)

# 31. perimeter of square

# s=float(input("enter side length of square in cm :  "))
# per=4*s
# print("perimeter of side =  ",per)

# 32. area of circle

# a=float(input("enter radius of circle  : "))
# area=22/7*a
# print("area of circlr is : ",area)

# 33. circumference of circle

# a=float(input("enter radius of circle in cm : "))
# cir=2*22/7*a
# print("circumference of circle : ",cir)

# 34. wap to accept electicity unit consumption and calculate total price at the rate of 5 rs unit. give a discount on 10% on all over bill

# unit=int(input("enter your electricity unit :  "))
# total=unit*5
# print("total unit before discounting : ",total)
# dis=unit*10/100
# print("total amount to pay = ",dis)

# 35. wap to accept marks of 5 subjects and find total marks and percentage assuming full marks as 100 in each subject

# a=int(input("enter marks of english :  "))
# b=int(input("enter marks of math : "))
# c=int(input("enter marks of odia : "))
# d=int(input("enter marks of history : "))
# e=int(input("enter marks of sanskrit : "))
# total=a+b+c+d+e
# print("total marks : ",total)
# per=(total/500)*100
# print("total percentage = ",per)

#  36. swap values of two numbers

# a=int(input("enter 1st number : "))
# b=int(input("enter 2 nd number : "))
# print("before swap : ",a)
# print("before swap : ",b)

# c=a
# a=b
# b=c
# print("after swap : ",a)
# print("before swap : ",b)

# 37. find the middle number in a group of 3 number

# a=int(input("enter 1st number  :  "))
# b=int(input("enter 2nd number  : "))
# c=int(input("enter 3rd number  :  "))

# if (a>b and a<c) or (a<b and a>c):
#     print("middle number is :  ",a)
# elif(b>a and b<c) or (b<a and b>c):
#     print("middle number is : ",b)
# else:
#     print("middle number is : ",c)





# 38. to print from 1 to n

# n=int(input("enter  number to print  : "))
# i=1
# while(i<=n):
#   print(i)
#   i=i+1
# 39. print from 1 to 10

# i=1
# while(i<=10):
#     print(i)
#     i=i+1

# 40. print n to 1

# n=int(input("enter number to print  :  "))
# i=1
# while(n>=i):
#     print(n)
#     n=n-i

#  41. find sum from 1 to n 

# n=int(input("enter number for sum : "))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+i
#     i=i+1
#     print("sum= ",sum)

#  42. print sum from n to 1

# n=int(input("enter number for sum : "))
# i=1
# sum=0
# while(n>=i):
#     sum=sum+n
#     n=n-i
#     print("sum= ",sum)
 
#  43.  wap to find sum of square from 1 to n
 

# n=int(input("enter number which you want to sum : "))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+(i*i)
#     i=i+1
#     print("sum=  ",sum)


# 44. wap to print sum of cube from 1 to n


# n=int(input("enter a number which you want to print : "))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+(i*i*i)
#     i=i+1
#     print("sum of cube is= ",sum)

# 45. wap to print even numbers between 1 to n

# n=int(input("enter number which you want to print : "))
# i=2
# while(i<=n):
#     print(i)
#     i=i+2



# 46. wap to find sum of even numbers from 1 to n

# n=int(input("enter a number you want to print  : "))
# # i=0
# # sum=0
# # while(i<=n):
# #     sum=sum+i
# #     i=i+2

# print("sum of even number is : ",sum)



# 47. find sum of first n even number

# n=int(input("enter a number which you want to print  : "))
# i=1
# sum=0
# count=0
# while(count<n):
#     if(i%2==0):
#         sum=sum+i
#         count=count+1
#     i=i+1

# print("sum of first n even number is : ",sum)




# 48. find sum of first n odd number

# n=int(input("enter a number which you want to print  : "))
# i=1
# sum=0
# count=0
# while(count<n):
#     if(i%2!=0):
#         sum=sum+i
#         count=count+1
#     i+=1

# print("sum of first n odd number is :",sum)


# #  49. product of odd digits

# n=int(input("enter a number you want to print  :"))
# prod=1
# while(n>0):
#      i=n%10
#      if(i%2!=0):
#         prod=prod*i
#      n=n//10
# print("product of odd digit of a given number is :",prod)


# #  50. product of even number

# n=int(input("enter a number  : "))
# prod=1
# while(n>0):
#     i=n%10
#     if(i%2==0):
#         prod=prod*i
#     n=n//10

# print("product of even digits of a given number is : ",prod)    



# 51. write a program to find reverse of a given number.


# n=int(input("enter a number  : "))
# rev=0
# while(n>0):
#     rev=(rev*10)+n%10
#     n=n//10
#     print("reverse number is : ",rev)    



#  52. wap whether a number is  palindrome number or not

# n=int(input("enter a number  : "))
# rev=0
# x=n
# while(n>0):
#     rev=(rev*n)+n%10
#     n=n//10
# if (x==rev):
#         print("its a palindrome number ")
# else:
#         print("its not a palindrome number")

