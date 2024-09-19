# 1.  to print from 1 to n

# n=int(input("enter  number to print  : "))
# i=1
# while(i<=n):
#   print(i)
#   i=i+1


# 2. print from 1 to 10

# i=1
# while(i<=10):
#     print(i)
#     i=i+1



# 3. print n to 1

# n=int(input("enter number to print  :  "))
# i=1
# while(n>=i):
#     print(n)
#     n=n-i


#4. find sum from 1 to n 

# n=int(input("enter number for sum : "))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+i
#     i=i+1
#     print("sum= ",sum)



#5. print sum from n to 1


# n=int(input("enter number for sum : "))
# i=1
# sum=0
# while(n>=i):
#     sum=sum+n
#     n=n-i
#     print("sum= ",sum)
 


# 6. sum of square from 1 to n
 

# n=int(input("enter number which you want to sum : "))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+(i*i)
#     i=i+1
#     print("sum=  ",sum)



# 7.  sum of cube from 1 to n


# n=int(input("enter a number which you want to print : "))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+(i*i*i)
#     i=i+1
#     print("sum of cube is= ",sum)



# 8. wap to print even numbers between 1 to n

# n=int(input("enter number which you want to print : "))
# i=0
# while(i<=n):
#     print(i)
#     i=i+2



# 9.  wap to find sum of even numbers from 1 to n

# n=int(input("enter a number you want to print  : "))
# # i=0
# # sum=0
# # while(i<=n):
# #     sum=sum+i
# #     i=i+2

# print("sum of even number is : ",sum)



#
# 10.  find sum of first n even number

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




# 11. find sum of first n odd number

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



# 12. sum of digit of a given number 


# n=int(input("enter a number : "))
# sum=0
# while(n>0):
#     num=n%10
#     sum=sum+num
#     n=n//10
#     print("sum of a number : ",sum)


# 13. sum of cube of digits of a given number

# n=int(input("enter a number : "))
# sum=0
# while(n>0):
#     num=n%10
#     sum=sum+(num*num*num)
#     n=n//10
# print("cube of digit of a given number : ",sum)




# # 14. to check whether a given number is armstrong or not


# n=int(input("enter a number : "))
# sum=0
# num=n
# while(n>0):
#     i=n%10
#     sum=sum+(i*i*i)
#     n=n//10
# if(sum==num):
#     print("armstrong number ")
# else:
#     print("not armstrong")



# 15. to find a product of a given number


# n=int(input("enter a number : "))
# prod=1
# while(n>0):
#     prod=prod*(n%10)
#     n=n//10
# print("product of a given number is : ",prod)



# 16. sum of odd digit

# n=int(input("enter a number : "))
# sum=0
# while(n>0):
#     i=n%10
#     if(i%2!=0):
#         sum=sum+i
#     n=n//10
# print("sum of odd number is : ",sum)




# 17. product of odd digits

# n=int(input("enter a number you want to print  :"))
# prod=1
# while(n>0):
#      i=n%10
#      if(i%2!=0):
#         prod=prod*i
#      n=n//10
# print("product of odd digit of a given number is :",prod)



# 18. sum of square of digits of a given number



# n=int(input("enter a number : "))
# sum=0
# while(n>0):
#     i=n%10
#     sum=sum+(i*i) 
#     n=n//10
# print("sum of square of digit of a given number : ",sum)




# 19. palindrome number or not 



# n=int(input("enter a number : "))
# rev=0
# num=n
# while(n>0):
#     rev=(rev*10)+n%10
#     n=n//10
# if(num==rev):
#     print("palindrome number ")
# else:
#     print("not palindrome")



# 20. to check whether a given number is prime or not


# n=int(input('enter a number : '))
# i=1
# count=0
# while(i<=n):
#     if(n%i==0):
#         count=count+1
#     i=i+1
# if(count==2):
#     print("its a prime number")
# else:
#     print("non-prime number")


# 21. print factorial of a number


# n=int(input("enter a number : "))
# fac=1
# while(n>=1):
#     fac=fac*n
#     n=n-1
# print("factorial of a given number is : ",fac)


# 22. print fibonacci series

# n=int(input("enter a  number : "))
# count=0
# a=0
# b=1
# while(count<n):
#     print(a,end=' ')
#     a,b=b,a+b
#     count+=1




# 23.  product of even number

# n=int(input("enter a number  : "))
# prod=1
# while(n>0):
#     i=n%10
#     if(i%2==0):
#         prod=prod*i
#     n=n//10

# print("product of even digits of a given number is : ",prod)    



# 24.  write a program to find reverse of a given number.


# n=int(input("enter a number  : "))
# rev=0
# while(n>0):
#     rev=(rev*10)+n%10
#     n=n//10
#     print("reverse number is : ",rev)    



#25. 

# x=5
# while(x<15):
#     print(x**2)
#     x+=3

# 26.

# a=7
# b=5
# while(b<9):
#     print("H")
#     b+=1

# 27.
# b=15
# while(b>9):
#     print("hello")
#     b=b-2




# 28. wap that keep on accepting numbers from yhe user until user enters zero. display the sum and average of all the numbers


# num=1
# sum=0
# i=-1
# while(num!=0):
#     num=int(input("enter any number : "))
#     sum=sum+num
#     i=i+1
#  print("average of numbers : ",sum/i)










