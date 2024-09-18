# 1. find the smallest and largest list elements on inputs provided by the user

# user_input=input("enter numbers separated by spaces: ")
# numbers=list(map(float,user_input.split()))
# smallest=min(numbers)
# largest=max(numbers)

# print("the smallest number is: ",smallest)
# print("largest number is : ",largest)


# 2. split a list in half and store the elements in two different lists


# def split_list(list):
#     mid=len(list) //2
#     list1=list[:mid]
#     list2=list[mid:]

#     return list1,list2

# original_list=[3,7,8,6,8,4,9]
# list1,list2=split_list(original_list)

# print("first half: ",list1)
# print("second half: ",list2)



# 3. remove multiple empty strings from a list of strings


# list_of_strings=["hello","","world","","","python"]
# cleaned_list=[s for s in list_of_strings if s]
# print(cleaned_list)


# 4. interchange first and last elements of in a list


# def interchange_first_last(list):
#     if len(list)<2:
#         return list
#     temp_var=list[0]
#     list[0]=list[-1]
#     list[-1]=temp_var
#     return list
    
# my_list=[2,3,7,8,9,1]
# result=interchange_first_last(my_list)
# print(result)


# 5. print elements with frequency greater than a value k



# from collections import Counter
# def print_element_with_frequency_greater_than_k(list,k):
#     frequency=Counter(list)
    
#     for element,count in frequency.items():
#         if count>k:
#             print(element)

# my_list=[1,2,2,3,3,3,4,4,4,4]
# k=3
# print(print_element_with_frequency_greater_than_k(my_list,k))



# 6. find all possible combination of a list with three combination

# from itertools import combinations

# def find_combination_of_three(list):
#     comb=combinations(list,3)

#     for c in comb:
#         print(c)

# my_list=[1,2,3,4,7,89]
# print(find_combination_of_three(my_list))
    


# 7. square each element of the list and print list in reverse order

# def square_and_reverse(list):
#     square_list=[x**2 for x in list]
#     square_list.reverse()

#     print(square_list)

# my_list=[1,3,4,5]
# print(square_and_reverse(my_list))



# 8. remove all occurances of an element from a given list


# def remove_all_occurances(list,element):
#     return[x for x in list if x!=element]

# my_list=[1,3,2,4,5,6,89]
# elements_to_remove=89
# print(remove_all_occurances(my_list,elements_to_remove))



# 9. remove empty list from a given list


# my_list=['mani'],[],['m']
# cleaned_list=[s for s in my_list if s]
# print(cleaned_list)



# 10. remove negative values from a list with filter()


# def remove_negative(list):
#     return [x for x in list if x>=0]

# my_list=[-1,2,3,-4,89,-56,345,-54]
# filter_list=remove_negative(my_list)
# print(filter_list)


# 11. create a flat list out of a given lists using built-in function


# list_of_lists=[[1,3,4],[2,6],[5,7,6]]
# flat_list=sum(list_of_lists,[])
# print(flat_list)



# 12. count and filter odd even numbers of given list using loops


# numbers=[2,7,89,67,54,90,34]
# even_count=0
# odd_count=0
# even_numbers=[]
# odd_numbers=[]
# for num in numbers:
#         if num%2==0:
#             even_count+=1
#             even_numbers.append(numbers)
#         else:
#             odd_count+=1
#             odd_numbers.append(numbers)

# print("even numbers : ",even_numbers)
# print("odd numbers : ",odd_numbers)
# print("count of even numbers : ",even_count)
# print("count of odd numbers : ",odd_count)

# 13. to swap two elements in a list


# def swap_two_elements(list,index1,index2):
#     list[index1],list[index2]=list[index2],list[index1]

# my_list=[10,34,23,67,89]
# print("original list :",my_list)

# swap_two_elements(my_list,1,3)
# print("list after swap : ",my_list)



# 14. swap elements in string list


# def swap_elemnts(string,index1,index2):
#     string[index1],string[index2]=string[index2],string[index1]

# my_string=['apple','ball','mango','kite']
# print("original string : ",my_string)

# swap_elemnts(my_string,1,3)
# print(my_string)



# 15. to find length of list


# def len_of_list(list):
#     length_count=0
#     for i in list:
#         if i in list:
#             length_count+=1
#     return length_count
# my_list=['apple','ball','rose','rpe']
# print(len_of_list(my_list))


# 16. maximum of numbers in python

# my_list=[12,43,67,90,24]
# b=max(my_list)
# print("maximum number : ",b)


# 17. minimum of two number in python


# num1=90
# num2=12
# minimum=min(num1,num2)
# print(minimum)

# 18. to check if elements exists in list

# elements=3
# my_list=[1,3,4,7,8,56]
# exists=elements in my_list
# print(exists)


# 19. clear a list in python


# my_list=[2,8,4,54,65,98]

# print('original list: ',my_list)
# b=my_list.clear()
# print("after clear list: ",b)



# 20. reversing a list


# def rev_list(list):
#     return list[::-1]
# my_list=[2,6,7,8,5,45]
# print(rev_list(my_list))


# 21. cloning or copying a list


# my_list=['ball','frog','tree','flower']
# b=my_list.copy()
# print(b) 

# 22. count occurance of an element in  a list

# my_list=[1,4,4,5,6,7]
# element=4
# count=my_list.count(element)
# print(count)

# 23. to find sum and average of list in python

# my_list=[10,30,56,9]
# total_sum=sum(my_list)
# average=total_sum/len(my_list)

# print("sum= ",total_sum)
# print("average= ",average)


# 24. sum of number digits in list

# my_list=[1,3,5,4,9]
# b=sum(my_list)
# print(b)

# 25. multiply all numbers in the list

# my_list=[8,5,6,2]
# product=1
# for num in my_list:
#     product=product*num

# print("product = ",product)


# 26. to find the second largest number in a list


# def second_largest(numbers):
#     unique_numbers=list(set(numbers))
#     if len(unique_numbers)<2:
#         raise ValueError
#     unique_numbers.sort()
#     return unique_numbers[-2]

# numbers=[2,4,5,7,8,9]
# print("second largest element is: ",second_largest(numbers))



# 27. to print even numbers in a list


# list=[2,54,3,8]
# for i in list:
#     if i%2==0:
#         print(i,"it is an even number")
#     else:
#         print(i,"not an even number")

# 28. to print odd numbers in a list

# list=[12,3,4,5,67]
# for i in list:
#     if i%2!=0:
#         print(i,"is an odd number")
#     else:
#         print(i,"is not an odd number")


# 29. to count even and odd numbers in a list

# my_list=[12,89,67,70,56]
# even_count=0
# odd_count=0
# for i in my_list:
#     if i%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
    
# print("even numbers =",even_count)
# print("odd numbers= ",odd_count)


# 30. to print positive numbers


# list=[12,-34,90]
# for i in list:
#     if i>0:
#         print(i,"positive numbers are : ")



# 31. to print negative numbers in a list


# my_list=[21,-23,-67]
# for i in my_list:
#     if i<0:
#         print(i,"is a negaive number")



# 32. to count positive and negative number in a list


# my_list=[19,-90,-56,-23,76,87]
# positive_count=0
# negative_count=0

# for i in my_list:
#     if i>0:
#         positive_count+=1
#     else:
#         negative_count+=1

# print("positive numbers : ",positive_count)
# print("negative numbers : ",negative_count)


# 33. remove multiple elements from a list 


# def remove_multiple_elements(list,element):
#     return[x for x in list if x not in element]

# my_list=[90,87,45,34,2]
# elements_to_remove=[45,2,34]
# print(remove_multiple_elements(my_list,elements_to_remove))


# 34. remove empty tuples in a list


# def remove_empty_tuples(list):
#     return [t for t in list if t]

# original_list=[(1,8),(),(2,4,3),(),()]
# updated_list=remove_empty_tuples(original_list)
# print(updated_list)

# 35. to print duplicates from a list of integers


# def print_duplicates(list):
#     seen=set()
#     duplicates=set()

#     for number in list:
#         if number in seen:
#             duplicates.add(number)
#         else:
#             seen.add(number)

#     print("duplicates: ",duplicates)

# numbers=[1,4,3,5,2,4,6,6,7,7]
# print_duplicates(numbers)


# # 36. remove empty list from list 

# my_list=[[1,2,3],[],[2,5,4],[]]
# update_list=[x for x in my_list if x]
# print(update_list)


# 37. convert list to list of dictionnaries

# values=[2,6,5]
# dict_list=[{'value': val} for val in values]
# print(dict_list)


# 38. convert lists of list to dictionary

# list_of_lists=[['a',1],['b',2],['c',4]]
# dict_from_list=dict(list_of_lists)
# print(dict_from_list)


# 39. uncommon elements in lists of list



# 40. to select random value from list of lists


# import random

# def select_random_value(lists):
#     flat_list=[item for sublist in lists for item in sublist]

#     if not flat_list:
#         raise ValueError("the list of lists is empty")
    
#     random_value=random.choice(flat_list)
#     return random_value

# lists_of_list=[[1,2,3],[4,5],[6,7,8]]
# print(select_random_value(lists_of_list))



# 41. reverse row sort in lists of list


# def reverse_sort_rows(lists):
#     sorted_lists=[sorted(row,reverse=True) for row in lists]
#     return sorted_lists
# lists_of_list=[[1,2,3],[1,5,6],[9,8,7]]
# result=reverse_sort_rows(lists_of_list)
# print(result)

# 42.  find the strongest neighbour

# def find_the_strongest_neighbour(list):
#     n=len(list)
#     strongest_neighbour=[]

#     for i in range(n):
#         left_neighbour=list[i-1] if i>0 else float('-inf')
#         right_neighbour=list[i+1] if i<n-1 else float('-inf')

#         strongest=max(left_neighbour,right_neighbour)
#         strongest_neighbour.append(strongest)
#     return strongest_neighbour
# list=[10,3,5,8,12]
# print(find_the_strongest_neighbour(list))

# 43. count strings with substrings  string list


# def count_strings_with_substrings(string_list,sub_string):
#     count=0
#     for s in string_list:
#         if sub_string in s:
#             count+=1
#     return count
# strings=['apple','ball','banana','cherry split','apple crips','cherry crips']
# substrings='apple'
# print(count_strings_with_substrings(strings,substrings))


# 44. replace substrings from string list

# def replace_substrings_in_list(string_list,old_substring,new_substring):
#     return[s.replace(old_substring,new_substring) for s in string_list]

# strings=['apple','orange','banana','mango']
# old_substring='apple'
# new_substring='cherry'
# print(replace_substrings_in_list(strings,old_substring,new_substring))

