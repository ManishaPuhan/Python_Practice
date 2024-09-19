#1. wap to reverse a string

# def rev_string(input_string):
#     return input_string[::-1]
# input_string=input("enter a string  : ")
# rev_input=rev_string(input_string)
# print(rev_input)



# 2. to check if a string is palindrome or not

# def palin_string(input_string):
#     return input_string[::-1]
# input_string=input("enter a string : ")
# rev_input=palin_string(input_string)
# if(input_string==rev_input):
#     print("the string is palindrome")
# else:
#     print("not a palindrome string ")


# 3. to count the numbers of vowels in string

# def count_vowels(input_string):
#     vowels='aeiouAEIOU'
#     count=0
#     for i in input_string:
#         if i in vowels:
#             count+=1
#     return count
# input_str=input("enter a string : ")
# print(count_vowels(input_str))

# 4. find the most frequent character in a string


# from collections import Counter

# def most_frequent_char(input_string):
#     char_count=Counter(input_string)
#     most_common_char=char_count.most_common(1)[0][0]
#     return most_common_char
# input_str=input("enter a string : ")
# print(most_frequent_char(input_str))


# # 5. to remove all duplicates from a string and return the result

# def remove_duplicates(input_string):
#     # initialise an empty string to store unique character
#     result=""
#     for char in input_string:
#         # check if the character is already in the result string
#         if char not in result:
#             result+=char
#     return result
# input_str=input("enter a string : ")
# result=remove_duplicates(input_str)
# print(result)


# 6. check if a string contains only digits

# def check_if_all_digit(input_string):
#     # checks if the input string is not empty
#     if input_string:
#         # iterates through each character in the string
#         for char in input_string:
#              # check if the character is not a digit
#             if not char.isdigit():
#                 return False       # return false if no character is not a digit
#         return True # if all characters are digits
#     else:
#         return False # if the input string is empty
    
# test_string1="12456"
# test_string2="abv234"
# test_string3="9876543210"
# test_string4="abndcgf"
# print(check_if_all_digit(test_string1))
# print(check_if_all_digit(test_string2))
# print(check_if_all_digit(test_string3))
# print(check_if_all_digit(test_string4))


# 7. to count the occurances of each word in a sentences


# from collections import Counter
# def count_words(sentence):
#     words=sentence.lower().split()
#     word_count=Counter(words)
#     return word_count
# sentence="this is a test. this test is only a test."
# result=count_words(sentence)
# print(result)



# 8. to capitalize the first letter of each word in a sentence 

# def capitalize_first_letter(sentence):
#     words=sentence.split()
#     capitalize_words=[word.capitalize() for word in words]
#     capitalize_sentence=' '.join(capitalize_words)
#     return capitalize_sentence

# input_sentence=input("write a sentence : ")
# output_sentence=capitalize_first_letter(input_sentence)
# print(output_sentence)



# 9. convert lower letter to upper and upper letter to lower in a string 

# def swap_case(sentence):
#     swapped_sentence=sentence.swapcase()
#     return swapped_sentence
# sentence="Hello World. this Is a test"
# result=swap_case(sentence)
# print(result)


    
# 10. to search a specific word in a string


# def spec_word(sentence,word):
#     return word in sentence
# sentence="this book is mine"
# word_to_serach="book"
# found=spec_word(sentence,word_to_serach)
# print(found)



# 11. to sort letters of words by lower to upper case format

# def lower_to_upper_case(word):
#     sorted_word=' '.join(sorted(word,key=lambda c:(c.isupper(),c.islower())))
#     return sorted_word
# word="Python"
# sorted_word=lower_to_upper_case(word)
# print(sorted_word)



# 12. to count lower,upper,numeric and special characters in a string



# def count_character(input_string):
#     lower_count=0
#     upper_count=0
#     numeric_count=0
#     special_count=0

#     for char in input_string:
#         if char.islower():
#             lower_count+=1
#         elif char.isupper():
#             upper_count+=1
#         elif char.isdigit():
#             numeric_count+=1
#         else:
#             special_count+=1
#     return lower_count,upper_count,numeric_count,special_count
# input_string="thos89/%AB"
# print(count_character(input_string))



# 13. to remove an empty character from a list of sequence

# def remove_empty_character(list):
#     cleaned_list=[]
#     for item in list:
#         if item !="":
#             cleaned_list.append(list)
#     return cleaned_list
# list=["hello","","world","","mani"]
# cleaned_list=remove_empty_character(list)
# print(list)
# print(cleaned_list)

        
# 14. to convert all the starting letter of a word in upper case format or in the title format


# def convert_uppercase_format(input_string):
#     return input_string.title()
# input_string="hello i am manisha puhan"
# print(convert_uppercase_format(input_string))



# 15. to calculate the length of a string

# def length_of_string(input_string):
#     length=0
#     for i in input_string:
#         length+=1
#     return length
# input_string="mamisha"
# print(length_of_string(input_string))



#  16. count the number of character in a string

# def count_number_of_character(input_string):
#     return len(input_string)
# input_string="manisha"
# total_character=count_number_of_character(input_string)
# print(total_character)



# 17. to get a string from a given string where all occurences of its first character have been cahnged to '@' , except the first character itself


# def replace_char(input_string):
#     if len(input_string)<=1:
#         return input_string
#     first_char=input_string[0]
#     result=first_char
#     for char in input_string[1:]:
#         if char==first_char:
#             result+='@'
#         else:
#             result+=char
#     return result
# input_string="manisham"
# print(replace_char(input_string))



#  18. to get a single string from two given strings,separated by a space and swap the first two character of each string


# def swap_and_combine(str1,str2):
#     if len(str1)<2 or len(str2)<2:
#         return"both strings must be atleast 2 characters long."
    
#     swap_str1=str2[:2]+ str1[2:]
#     swap_str2=str1[:2]+str2[2:]
#     combined_string=swap_str1+ '' +swap_str2

#     return combined_string
# str1="abc"
# str2="xyz"
# result=swap_and_combine(str1,str2)
# print(result)



# 19. remove the nth index character from a non-empty string

# def remove_nth_character(s,n):
#     if n<0 or n>=len(s):
#         return "index out of range"
#     return s[:n]+ s[n+1:]

# input_string=input("enter a string : ")
# index=int(input("enter the index of the character to remove: "))
# print(remove_nth_character(input_string,index))
       


# 20. To change a given string to a new string where the first AND last character have been exchanged


# def exchange_first_last(input_string):
#     if len(input_string)<2:
#         return input_string
    
#     # Directly swap the first and last characters
#     return input_string[-1] + input_string[1:-1]+ input_string[0]

# input_string="python"
# print(exchange_first_last(input_string))



# 21. to remove the characters which have odd index values of a given string


# def remove_odd_index_value(input_string):
#     result=' '
#     for i in range(len(input_string)):
#         if i%2==0:
#             result+=input_string[i]
#     return result
# input_string="python_language"
# print(remove_odd_index_value(input_string))



# 22.  write a python script that takes input from the user and displays that input back in upper and lower cases


# user_input=input("enter some text : ")
# uppercase_input=user_input.upper()
# lowercase_input=user_input.lower()

# print("uppercase : ",uppercase_input)
# print("lowercase: ",lowercase_input)




# 23. to reverse a string  if it's length is a multiple of 4

# def reverse_string(input_string):
#     if len(input_string)%4==0:
#         return input_string[::-1]
#     else:
#         return input_string

# input_string="manishapuhan"
# print(reverse_string(input_string))



# 24. to convert a given string to all uppercase if it contains at least 2 uppercase character in the first 4 characters

# def uppercase_char(text):
#     uppercase_count=0
#     for char in text[:4]:
#         if char.isupper():
#             uppercase_count+=1
    
#     if uppercase_count==2:
#         return text.upper()
#     else:
#         return text
    
# text="mAniSha"
# print(uppercase_char(text))



# 25. write a python progarm to sort a string lexilogically


# def sort_string_lexilogically(input_string):
#     sorted_chars=sorted(input_string)
#     sorted_sorting=''.join(sorted_chars)
#     return sorted_sorting
# input_string="hello"
# sorted_string=sort_string_lexilogically(input_string)

# print("original string : ",input_string)
# print("after sorting : ",sorted_string)



# 26. wap to remove newline in python


# def remove_newline(input_string):
#     no_newline_string=input_string.replace('\n','  ')
#     return no_newline_string
# input_string="hello\nworld\nthis\nis\na\ntest"
# no_newline_string=remove_newline(input_string)

# print("original string : ",input_string)
# print("string without newline : ",no_newline_string)



# 27. wap to check whether a string starts with special characters


# input_string="hello,world!"
# specified_character="book"

# if input_string.startswith(specified_character):
#     print("true")
          
# else:
#     print("false")




# 28.  to remove existing indentation from all of the lines in a given text.


# import textwrap

# def remove_indentation(text):
#     dedented_text=textwrap.dedent(text)
#     return dedented_text

# input_text="""
#             this is some example text
#             with indentation.
             
#                more lines with deeper
#                indentation.
#             back to less indentation.

# """
# processed_text=remove_indentation(input_text)

# print("original text : ")
# print(input_text)
# print("\ntext with removed indntation: ")
# print(processed_text)


# 29. to add a prefix text to all of the lines in a string



# def add_prefix_to_lines(text,prefix):
    
#     result_text=prefix + text.replace('\n','\n' + prefix)
#     return result_text

# input_text="""hello
# world
# python
# programming
# """

# prefix="* "
# result=add_prefix_to_lines(input_text,prefix)
# print(result)



# 30. to print the following floating numbers upto 2 decimal places

# def format_to_two_decimal_places(number):
#     return f"{number:.2f}"

# numbers=[5.6754098,8.98076]
# for num in numbers:
#     print(format_to_two_decimal_places(num))


   
# 31.  to print the following floating numbers upto 2 decimal places with a sign


# numbers=[3.8796,-2.87654]
# print("using format function:")

# for num in numbers:
#     formatted_number="{:+.2f}".format(num)
#     print(formatted_number)



# 32.  to print the following floating numbers with no decimal places


# numbers=[45.780965,78,908.65]
# print("using int() function: ")
# for num in numbers:
#     print(int(num))


# 33. to strip a set of characters from a string


# str="she is very beautiful"
# ch="aeiouAEIOU"
# print("original string :",str)
# print("afterr stripping :"," ".join(c for c in str if c not in ch))



# 34. to convert a given string into a list of words


# def convert_string_into_list(input_string):
#     word_list=input_string.split()
#     return word_list
# input_list="hello , how are you?"
# print(convert_string_into_list(input_list))




# 35. wap to swap comma and dot in a string

# def swap_comma_dot(input_string):
#     swapped_string=" "

#     for char in input_string:
#         if char==' ,':
#             swapped_string+='.'
#         elif char=='.':
#             swapped_string+=','
#         else:
#             swapped_string+=char
#     return swapped_string

# input_string="this is a beautiful monument.i like to visit .konark is a beautiful place in odisha,"
# print(swap_comma_dot(input_string))




# 36. to split a string on the last occurance of the delimeter


# def split_on_last_occurance(input_string,delimeter):
#     parts=input_string.rsplit(delimeter,1)

#     if len(parts)==1:
#         return parts[0]
#     return parts[0],parts[1]

# input_string="hello, world, how are you, world?"
# delimeter=","
# first_part, last_part=split_on_last_occurance(input_string,delimeter)
# print("first part: ",first_part)
# print("last_part:",last_part)




# 37. wap to find the non_repeating character in given string


# def first_non_repeating_char(s):
#     freq={}
# #  count the frequency of each character in the string
#     for char in s:
#         if char in freq:
#             freq[char]+=1
#         else:
#             freq[char]=1

#     # find the first character with frequency 1
#     for char in s:
#         if freq[char]==1:
#             return char
#     return None

# input_string='hello'
# result=first_non_repeating_char(input_string)

# if result:
#     print(f"the first non_repeating character in '{input_string}' is '{result}'")
# else:
#     print(f"there is no non-repeating character in '{input_string}'")




# 38. to find the first repeated word in a given string



# def find_first_repeated_word(sentence):
#     words=sentence.split()
#     words_count={}

#     for word in words:
#         word=word.strip(",.?;:")
#         word_lower=word.lower()

#         if word_lower in words_count:
#             return word
#         words_count[word_lower]=1
#     return None
# sentence="he had had quite enough of this nonsense."
# result=find_first_repeated_word(sentence)

# if result:
#     print(f"the first repeated word is'{result}'.")
# else:
#     print("there are no repeated words in the sentence.")




#  39. wap to remove speces from a given string


# def remove_spaces(input_string):
#     return ''.join(input_string.split())

# input_string="hello, how are you doing today?"
# result=remove_spaces(input_string)
# print("original string:",input_string)
# print("string without spaces:",result) 
 


# 40. to compute sum of digits of a given string

# def sum_of_digit(input_string):
#      total=0
#      for char in input_string:
#           if char.isdigit():
#                total+=int(char)
#      return total
# input_string="ma12bi35"
# result=sum_of_digit(input_string)
# print("the sum of digits in the string is: ",result)




# 41. to create a string from two given strings concatenating uncommon characters of the said strings



# def uncommon_characters(str1, str2):
#     set1=set(str1)
#     set2=set(str2)

#     uncommon_in_str1=set1 - set2
#     uncommon_in_str2=set2 - set1
#     result=''.join(uncommon_in_str1) + ''.join(uncommon_in_str2)
#     return result

# string1="abcdef"
# string2="cdefgh"
# result=uncommon_characters(string1,string2)
# print("the concatinated string of uncommon characters is:",result)




# 42. to count number of non-empty substrings of a given string


# def count_non_empty_substrings(input_string):
#     n=len(input_string)
#     return n*(n+1)//2

# input_string="abd"
# result=count_non_empty_substrings(input_string)
# print("the number of non_empty substrings is: ",result)




# 43. find the smallest and largest word in a given string


# def find_smallest_and_largest_words(input_string):
#     words=input_string.split()

#     if not words:
#         return "the input string is empty"
    
#     smallest_word=largest_word=words[0]

#     for word in words:
#         if len(word)< len(smallest_word):
#             smallest_word=word
#         if len(word)> len(largest_word):
#             largest_word=word
#     return smallest_word, largest_word

# input_string="myself manisha puhan. i have completed master of computer application"
# smallest, largest=find_smallest_and_largest_words(input_string)
# print("smallest word: ",smallest)
# print("largest word: ", largest)





#  44. wap to count number of substrings with same first and last characters of a given string

# def count_substrings_with_same_ends(input_string):
#     count=0
#     n=len(input_string)

#     for start in range(n):
#         for end in range(start,n):
#             substring=input_string[start:end+1]
#             if substring[0]==substring[-1]:
#                 count+=1
#     return count
# input_string="ababa"
# result=count_substrings_with_same_ends(input_string)
# print("the number of substring with the same first and last character is:",result)


# 45. wap to wrap a given string into a paragraph of given width


# import textwrap

# def wrap_text(text,width):
#     wrapper=textwrap.TextWrapper(width=width)
#     wrapped_text=wrapper.wrap(text)
#     return '\n'.join(wrapped_text)

# input_text="this is an example of a long string that need to be wrapped into multiple lines based on a specified width"
# wrap_width=18
# wrapped_paragraph=wrap_text(input_text,wrap_width)
# print(wrapped_paragraph)


# 46. to split a given multiline string into a list of lines

# def split_into_lines(multline_string):
#     return multline_string.splitlines()

# input_string=""" this is a beautiful monument
# this is konark
# this book is mine.
# """
# lines=split_into_lines(input_string)
# for i,line in enumerate(lines,start=1):
#     print(f"line{i}: {line}")


