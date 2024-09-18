# 1. print 1st 10 natural number

# for i in range(1,11):
#     print(i)


# 2. to print all the even numbers within the given range

# for i in range(0,55,2):
#     print(i)

# 3. to calculate the sum of all numbers from 1 to a given number

# n=int(input("enter a number : "))
# sum=0
# for i in range(1,n+1):
#         sum=sum+i
#         print("sum=",sum)


# 4. to calculate the sum of all odd numbers within the given range

# n=int(input("enter a number : "))
# sum=0
# for i in range(1,n+1,2):
#     sum=sum+i
#     print("sum of odd number= ",sum)


#  5. to print a multiplication table of a given number by user

# n=int(input("enter a number : "))
# for i in range(1,11):
#     product=n*i
#     print("multiplication table is :",product)



# 6.  to display numbers from a list using a for loop

# list=[23,67,908,345]
# for u in list:
#     print(u)


# 7. to count the total number of digits in a number

# n=input("enter a number : ")
# count=0
# for i in n:
#     count=count+1
#     print(count)



# 8. to check if the given string is palindrome or not


# a=input("enter a string : ")
# b=a[(len(a)-1)::-1]
# if(a==b):
#     print(a,"is a palindrome number.")
# else:
#     print(a,"is not a palindrome number.")
       

#  9.  PROGRAM TO FIND REVERSE OF A STRING
# a="nitu"
# for i in range((len(a)-1),-1,-1):
#     print(a[i],end="")



# 10. to count vowel and consonant in a string 


# n=input("enter your name  : ")
# cons=0
# vowel=0
# for i in range(0,len(n)):
#     if(n[i]!=''):
#         if(n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u'):
#             vowel=vowel+1
#         else:
#            cons=cons+1
# print("total no of vowel is : ",vowel)
# print("total no of consonant is : ",cons)


#  11. to check if a given number is Armstrong or not



# number=int(input("enter a number : "))
# num_str=str(number)
# num_digits=len(num_str)
# sum=0
# for i in num_str:
#     digit=int(i)
#     sum+=digit**num_digits
# if(sum==number):
#     print("it is an armstrong number")
# else:
#     ("it is not an armstrong number")


# 12. count the number of even and odd numbers from a series of numbers

# numbers=[8,56,34,23,56,78,90,2,7]
# even_count=0
# odd_count=0
# for i in numbers:
#     if i%2==0:
#         even_count+=1
#     else:
#         odd_count+=1

# print("numbers of even numbers : ",even_count)
# print("number of odd numbers:",odd_count)


# 13. to display all numbers within a range except the prime number


# start=int(input("enter starting number : "))
# end=int(input("enter a number : "))
# for i in range(start,end+1):
#     if i>1:
#         for j in range(2,i):
#             if(i%j)==0:
#              break
#         else:
#            print(i)
       


 #  14. to get fibonacci series between 0 to 50

# sum=0
# for i in range(0,51):
#     sum=sum+i
# print("fibonacci series is :",sum)


# 15. to find the factorial of a given number

# n=int(input("enter a number : "))
# factorial=1
# for i in range(1,n+1):
#     factorial=factorial*i
# print("factorial of a given number is ",factorial)

# 16. accepts a string and calculates the number of digits and letters

# n=input("enter a string :")
# digits=0
# letters=0
# for i in n:
#     if i.isdigit():
#         digits+=1
#     elif i.isalpha():
#         letters+=1
# print("the input string",n,"has",letters,"letters and",digits,"digits")


# 17. iterates  the integers from 1 to 25

# for i in range(1,26):
#     print(i)

# 18. to check the validity of password input by users


# password=input("enter a password  : ")
# valid=True
# for char in password:
#     if not char.isalnum():
#         valid=False
#         break
# if valid and len(password)>=8:
#     print("password is valid!")
# else:
#     print("password is invalid.")




# 19. to convert the month name to a number of days

# month=["january","february","march","april","may","june","july","august","september","october","november","december"]
# for i in month:
#     if i=="february":
#         print(i,"the month  has 28/29 days")
#     elif i in("april","june","september","november"):
#          print("the month of",i,"has 30 days.")
#     else:
#          print(" month of",i,"has 31 days.") 


# 20. accept 10 number from user and display their average


# n=int(input("enter a number : "))
# sum=0
# for i in range(10):
#     sum=sum+n
#     avg=sum/10
# print(avg)


# 21. display sum of odd numbers and even numbers that fall in between 12 and 37
    

# even_num=0
# odd_num=0
# for i in range(12,37):
#     if(i%2==0):
#         even_num+=1
#     else:
#         odd_num+=1
# print(even_num)
# print(odd_num)


# 22. display all the number which are divisible by 11 but not by 2 between 100 and 500


# for i in range(100,500):
#     if i%11==0 and i%2!=0:
#         print(i)


# 23. accept 10 numberss from the user and display their average

# sum=0
# for i in range(10):
#     n=int(input("enter number : "))
#     sum=sum+n
#     avg=sum/10
# print("average of 10 numbers is : ",avg)


# # 24. print all prime numbers that fall between two numbers including both(accepts two  numbers from the user)



# start=int(input("enter starting number : "))
# end=int(input("enter a number : "))
# for i in range(start,end+1):
#     if i>1:
#         for j in range(2,i):
#             if(i%j)==0:
#              break
#         else:
#            print(i)



# 25. to print numbers from 1 to 20 except multiple of 2 and 3


# for i in range(1,21):
#     if i%2!=0 and i%3!=0:
#         print(i)
            

# 26. table of a number (accepted from user) 


# n=int(input("enter a  number : "))
# for i in range(1,11):
#     table=n*i
#     print(n,"*",i,"=",table)


# 27. wap to accept a number and check whether it is a perfect number or not ( perfect means a positive integer which is equal to the sum of divisors )


# num=int(input("enter a number : "))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i
# if num==sum:
#     print("number is perfect")
# else:
#     print("number is not perfect")


# 28. find the largest number in a list 


# numbers=[23,87,90,1,45,890]
# max_num=numbers[0]
# for num in numbers:
#     if num>max_num:
#         max_num=num

# print(f"the largest number in a list is : ",max_num)  


# 29. find the average of numbers in a list

# numbers=[23,6,7,8,9]
# sum=0
# for i in numbers:
#     sum=sum+i
#     avg=sum/5

# print("average of numbers in a list : ",avg)



# # 30. print all uppercase letter in a list



# letter="AeNopuJ"
# for i in letter:
#     if (i.isupper()):
#         print(i)


# 31. use a loop to display elements from a given list present at odd index position


# elements=[12,76,9,2,3,90]
# for i in range(1,len(elements),2):
#     print(elements[i])
      

# 32. find  the series upto n terms

# n=5
# series=[]
# for i in range(1,n+1):
#     series.append(i**2)
# print(series)

# 33. find the sum of series upto n term

# n=5
# sum_series=0
# for i in range(1,n+1):
#     sum_series+=i

# print("the sum of the series upto n terms is : ",sum_series)