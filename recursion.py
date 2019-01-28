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
    return fibonacci_memoized(n)
    # return fibonacci_dynamic(n)


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

  
    
    # Once implemented, change fibonacci (above) to call fibonacci_memoized
    # to verify that your memoized implementation passes all test cases

##################################################
##### Dynamic Programming
##### Meaning: is solving a problem by breaking it down into a subset of smaller problems,
#####          solving those subproblems once and storing their solution in a data structure.
def fibonacci_dynamic(n):
  # TODO: Implement the fibonacci function with dynamic programming here
  '''
    Approach 1: Using a dictionary
    (O)Notation, how could I implement this on this??
  '''
  #I need to solve this so that every time I get a solution I save it for the next time?
  #Some way to not save multiple times an element on the dictionary
  #Everytime a new value is added given the nature of  fibonacci you can recicle solutions

  fibonacci_values_dictionary = {}
  storage_number = 0
  # This helper function is meant to simplify adding values to the dictionary

  # Maybe t
  def _append_value_to_dictionary_(new_value):
    # this have to be sure that this is the first time you are adding this value
    # to this dictionary,
    if new_value is not in fibonacci_values_dictionary:
      fibonacci_values_dictionary[storage_number] = new_value
      storage_number += 1
   
    #

  return fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2)

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