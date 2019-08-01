'''
This is function that takes in any string that represetns number , or if you 
want to say it is object with value number but type string and converts it to type intefer
without using built-in method int().
STEPS:
1) Create dictionary with corresponding values string - integer
2) Declare empty array where later I will store numbers
3) Declare main function that accepts one parametr
    a)Inside function iterate through string and then iterate through 
    dictionary and compare string characters with dictionarie's keys
    if they equal save the value of that key to array that we declared at step 2
    b) Declare variable coefficient which will be length of array minus one - we need
    it to use it in iteration throuh array
    c) Declare variable index which will be 0 at first
    d) Declare variable result which will be final result with converted integer


So far we have list with integers that we need , but we need one single integer.
In javascript it would be easy task we could just call function join, but in python 
as I know join function will convert it again to string but we don't need it.
So we will use math here. Let me explain principle that we will use.
For instance we have list such as [1,3,5] that contains integers and now we need 
to get single number 135. If we will look more close we will see that 135 is equal to
sum 100 + 30 + 5. And if we will even more close we can see that it is equal to 
1 * 10**2 + 3 * 10**1 + 5 * 10**0. One multiply to the 10 in power two plus 3 multiply
to the 10 in power one plus 5 multiply to 10 in power zero.
So as we can see we have 1,3,5 which is items in our list , we have 10 which is simple
number and now we need coefficient - power of 10. How we can get it? Okay the power of
the 10 is equal to the index of the item in reversed array such as [5,3,1] 
the index of 5 will be 0 ,the index of 3 will be one and the index of 1 will be two.
OR we  can get it from our initial list by just getting length of list minus one 
and then substract it from current index.
That what the while loop in the function does.
And that is it. We got our final result variable which we can print and return
'''


number_dictionary = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9
}
array_of_numbers = []
def convertion(numbers):
    for number in numbers:
        for item in number_dictionary:
            if item == number:
                array_of_numbers.append(number_dictionary[item])
    coefficient = len(array_of_numbers) -1
    index = 0
    result = 0
    while index <= coefficient:
        result +=array_of_numbers[index]*10**(coefficient-index)
        index+=1
    print(result,type(result))
    return result


convertion('453453453')