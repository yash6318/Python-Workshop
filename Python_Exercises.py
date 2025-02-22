
# ## Exercises

# Answer the questions or complete the tasks outlined in bold below.


from sys import flags


def power(a,b):
    
    # ** What is 7 to the power of 4?**
    p=1
    for i in range(b):
      p= p*a

    
    return p



def split_str(s):
    
    # ** Split this string:**
 
    s = "Hi there Sam!"
    lst=list(s.split())
    return lst  
     
# **into a list. **
    


def format(planet, diameter):
    # ** Given the variables:**
    #
    #     planet = "Earth"
    #     diameter = 12742
    #
    # ** Use .format() to print the following string: **
    #
    #     The diameter of Earth is 12742 kilometers.
    x = "The diameter of {} is {} kilometers.".format(planet, diameter)
    return x


def indexing(lst):
    
# ** Given this nested list, use indexing to grab the word "hello" **

  lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
  tmp= lst[3][1][2][0]

  return tmp


def dictionary(d):
    
# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

  d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
  tmp2= d['k1'][3]['tricky'][3]['target'][3]

  return tmp2


def subjective():
    
# ** What is the main difference between a tuple and a list? **
# Tuple is _______ 

    return "immutable"




def domainGet(email):
    
    # ** Create a function that grabs the email website domain from a string in the form: **
# 
    sourceemail="user@domain.com"
    lst=list(sourceemail.split('@'))
    domain=lst[1]

#     
# **So for example, passing "user@domain.com" would return: domain.com**

    return domain


def findDog(st):
    
# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **
    
    flag=False
    if(st.find('dog') != -1):
      flag=True

    return flag


def countDog(st):

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **
    ct=st.count('dog')

    return ct



def lambdafunc(seq):
    
    # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
    seq = ['soup','dog','salad','cat','great']
    lst=list(filter(lambda str:str.startswith('s'),seq))
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

    return lst


def caught_speeding(speed, is_birthday):
    
    
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

  if(not is_birthday):
    if(speed<=60): 
      message="No ticket"
    elif(speed>60 and speed<=80):
      message="Small Ticket"
    else:
      message="Big Ticket"
  else:
    if(speed<=65): 
      message="No ticket"
    elif(speed>65 and speed<=85):
      message="Small Ticket"
    else:
      message="Big Ticket"

  return message


## Numpy Exercises

import numpy as np


def create_arr_of_fives():
    
  #### Create an array of 10 fives
  #### Convert your output into list 
  #### e.g return list(arr)
  arr=np.ones(10)*5

  return list(arr)



def even_num():
    
  ### Create an array of all the even integers from 10 to 50
  ### Convert your output into list 
  ### e.g return list(arr)
  res=list(np.arange(10,51,2))

  return res



def create_matrix():
    
  ### Create a 3x3 matrix with values ranging from 0 to 8
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  matrixx=np.arange(9)
  arr2d=matrixx.reshape(3,3).tolist()

  return arr2d



def linear_space():
    
  ### Create an array of 20 linearly spaced points between 0 and 1
  ### Convert your output into list 
  ### e.g return list(arr)
  res=list(np.linspace(0,1,20))

  return res



def decimal_mat():
    
  ### Create an array of size 10*10 consisting of numbers from 0.01 to 1
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  arr=np.around(np.linspace(0.01,1,10*10),decimals=2)
  res=arr.reshape(10,10).tolist()
  

  return res



def slices_1():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])
  
  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[12, 13, 14, 15],
  #      [17, 18, 19, 20],
  #      [22, 23, 24, 25]])
  arrslice=arr[2:,1:]

  return (arrslice).tolist()



def slices_2():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[ 2],
  #      [ 7],
  #      [12]])
  arrslice=arr[:3,1:2].reshape(3,1)

  return arrslice.tolist() 



def slices_3():
    
  # This is a given array
  arr = np.arange(1,26).reshape(5,5)
  # array([[ 1,  2,  3,  4,  5],
  #      [ 6,  7,  8,  9, 10],
  #      [11, 12, 13, 14, 15],
  #      [16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])

  # Write a code to slice this given array
  ### Convert your output into list 
  ### e.g return (arr).tolist()
  # array([[16, 17, 18, 19, 20],
  #      [21, 22, 23, 24, 25]])
  arrslice=arr[3:].reshape(2,5)
    
  return arrslice.tolist()


# Great job!
