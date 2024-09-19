# 1. Print pattern

# row=5
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print("")

# 2. pyramid pattern of number

# row=5
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")

# 3. inverted pyramid pattern of numbers

# row=5
# b=0
# for i in range(row,0,-1):
#     b+=1
#     for j in range(1,i+1):
#         print(b,end=" ")
#     print(" ")

# 4. inverted pyramid pattern with the same digit

# row=5
# for i in range(row,0,-1):
#     b=5
#     for j in range(1,i+1):
#         print(b,end=" ")
#     print(" ")

# 5. another inverted half pyramid pattern with a number

# row=5
# for i in range(row,0,-1):
#     for j in range(0,i+1):
#         print(j,end=" ")
#     print(" ")

# 6. alternate numbers pattern using a while loop

# row=5
# i=1
# while i<=row:
#     j=1
#     while j<=i:
#         print((i*2-1),end=" ")
#         j=j+1
#     i=i+1
#     print(" ")

# 7. reverse number pattern

# row=5
# for i in range(row,0,-1):
#     for j in range(i,0,-1):
#         print(i,end=" ")
#     print(" ")

# 8. reverse pyramid of numbers

# row=5
# for i in range(1,row+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print(" ")

# 9. number triangle pattern

# row=6
# for i in range(1,row):
#     num=1
#     for j in range(row,0,-1):
#         if j>i:
#             print(" ",end=" ")
#         else:
#             print(num,end=" ")
#             num+=1
#     print(" ")


# 10. pascals triangle pattern using numbers

def print_pascal_triangle(size):
    for i in range(0,size):
        for j in range(0,i+1):
            print(decide_number(i,j),end=" "):
        print()