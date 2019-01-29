#!python

############################################################
##### This is a recursion example using fibonacci sequence 
############################################################

def fibonacci(n):
    """fibonacci(n) returns the n-th number in the Fibonacci sequence,
    which is defined with the recurrence relation:
    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2), for n > 1"""
    # Check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('fibonacci is undefined for n = {!r}'.format(n))
    # Implement fibonacci_recursive, _memoized, and _dynamic below, then
    # change this to call your implementation to verify it passes all tests
    # return fibonacci_recursive(n)
    # return fibonacci_memoized(n)
    return fibonacci_dynamic(n)


def fibonacci_recursive(n):
    # Check if n is one of the base cases
    if n == 0 or n == 1:
        return n
    # Check if n is larger than the base cases
    elif n > 1:
        # Call function recursively and add the results together
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoized(n):
  # DONE: Memoize the fibonacci function's recursive implementation here
  # To improve speed you can use memoization where the most frequent calls are stored
  '''
  Approach 1: Using a dictionary
    (O)Notation, how could I implement this on this??
  '''
  if n > 9:
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
  else:
    #On space complixity what is the difference between making a smaller or bigger dictionary, 
    #is there much more cost in space for a few more variables
    frequent_calls_dict = {0:0, 1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34}
    return frequent_calls_dict[n]

##################################################
##### Dynamic Programming
##### Meaning: is solving a problem by breaking it down into a subset of smaller problems,
#####          solving those subproblems once and storing their solution in a data structure.
def fibonacci_dynamic(n):
  # TODO: Implement the fibonacci function with dynamic programming here

  ##################################################
  ### Current Status
  ### Approach 1
  ### Of all the tests only the first and fourth pass
  ### Breaks with big integers  
  ###             medium integers
  ###             floating point numbers
  ### Approach 2: NOT ANY WORK
  ### Approach 3: NOT ANY WORK
  
  ##################################################
  ### Scenario for this to exist, I constantly need to do fibonacci operations for 
  ### whatever reason, then it's likely that I already got the one I need

  ##################################################
  ### What is the process I'm setting up here, for every run you get a new fibonacci 
  ### value stored in the dictionary so that the next time if it's already there you
  ### don't need to do the whole operation
  #   1. Set up the variables
  #   2. Check if you have already have stored the value
  #   3. If you don't have it get it
  #   4. Add it to the dictionary
  #   5. return the value
  '''
    Approach 1: Using a dictionary
    (O)Notation, how could I implement this on this??
  '''
  #I need to solve this so that every time I get a solution I save it for the next time?
  #Some way to not save multiple times an element on the dictionary
  #Everytime a new value is added given the nature of  fibonacci you can recicle solutions

  # 1
  fibonacci_values_dictionary = {}

  # 2. Checking if I already got that key stored
  if n in fibonacci_values_dictionary.keys():
    # then return the value of the fibonacci sequence
    return fibonacci_values_dictionary.get(n)

  # 3. Stor
  f = fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2)

  # 4. 
  fibonacci_values_dictionary = fibonacci_values_dictionary.update({n:f})
   
  return f

  '''
    Approach 2: Using an array
    (O)Notation, how could I implement this on this??
  '''



  '''
    Approach 3: Using a set
    (O)Notation, how could I implement this on this??
  '''

    # Once implemented, change fibonacci (above) to call fibonacci_dynamic
    # to verify that your dynamic implementation passes all test cases
  pass

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = fibonacci(num)
        print('fibonacci({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()