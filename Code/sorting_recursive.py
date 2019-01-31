#!python


def merge(list1, list2):
  """Merge given lists of items, each assumed to already be in sorted order,
  and return a new list containing all items in sorted order.
  TODO: Running time: ??? Why and under what conditions?
  TODO: Memory usage: ??? Why and under what conditions?"""
  # TODO: Repeat until one list is empty
  # TODO: Find minimum item in both lists and append it to new list
  # TODO: Append remaining items in non-empty list to new list
  ###############################################################
  ### Logic: You already have lists that are already sorted, you want to 
  ###        mix them and keep them in order 

  '''
   Approach1: Given that you don't need to organize the given lists, step
              ignored. You compare each list first item with the other list
              first item and append the lower value to the new list until 
              there is none
  '''
  ### Process: 1. Create new list that will hold the merged values
  ###          2. Make position variables for each list
  ###          3. If list1 has a lower value add it to the new_list
  ###             increase corresponding position variable
  ###          4. if not then it means that list2 has a lower value
  ###             so add that instead to the new_list and increase 
  ###             corresponding position variable
  ###          5. If neither is lower than the other then they must
  ###             be equal, so append both.

  new_list = list()

  list1_current_position = 0
  list2_current_position = 0

  if list1[list1_current_position] < list2[list2_current_position]:
    new_list.append(list1[list1_current_position])
    list1_current_position += 1
  elif list2[list2_current_position] < list1[list1_current_position]:
    new_list.append(list2[list2_current_position])
    list2_current_position += 1
  else:
    new_list.append(list1[list1_current_position])
    list1_current_position += 1
    new_list.append(list2[list2_current_position])
    list2_current_position += 1
  
  return new_list

  '''
   Approach2: This time forget positional values and to save space delete 
  '''
  ### Process: 1. Make a new list
  ###          2. if the first item (python lists start at index 0) of list 1
  ###             at the first index is lower than the first index of list 2.
  ###             Append the item been taken out of the list 1 to the new list
  ###          3. if the first item of list 2 at the first index is lower than
  ###             the first index of list 1.
  ###             Append the item been taken out of the list 1 to the new list.
  ###          4. if anything in list1.
  ###             if something still in list2 
  ###             Append the item at index 0 been taken out of the list 2 to the 
  ###             new list.
  ###             elif anything in list2 too
  ###             return the new list
  ###          5. if anything in list2.
  ###             if something still in list1
  ###             Append the item at index 0 been taken out of the list 1 to the 
  ###             new list.
  ###             elif anything in list1 too
  ###             return the new list
  ###          6. else this means both items are the same append to the new list.
  ###             Append the first item from list1 and list2 to the new list, after
  ###             getting them out
  
  new_list = list()

  if list1[0] < list2[0]:
    new_list.append(list1.pop(0))

  elif list2[list2_current_position] < list1[list1_current_position]:
    new_list.append(list2.pop(0))

  elif not list1:
    if list2:
      new_list.append(list2.pop(0))
    elif not list2:
      return new_list
  
  elif not list2:
    if list1:
      new_list.append(list1.pop(0))
    elif not list1:
      return new_list
  else:
    new_list.append(list1.pop(0))
    new_list.append(list2.pop(0))
  
  # If I don't return the list does the if loop keeps on going until it return 
  # the new list given that both lists are empty
  # return new_list

def split_sort_merge(unsplit_list):
  """Sort given items by splitting list into two approximately equal halves,
  sorting each with an iterative sorting algorithm, and merging results into
  a list in sorted order.
  TODO: Running time: ??? Why and under what conditions?
  TODO: Memory usage: ??? Why and under what conditions?"""
  # TODO: Split items list into approximately equal halves
  # TODO: Sort each half using any other sorting algorithm
  # TODO: Merge sorted halves into one list in sorted order
  ###############################################################
  ### Logic: I have items in a unarranged list, I want to divide and conquer  
  ###        or better said divide and merge, I will be separating the 
  ###        totality of the list into smaller fragments that are easier to sort
  '''
   Approach1: Get the totality of items and divide the list in two new lists, 
              then sort those sublists and merge those lists

  '''
  ### Process: 1. Get the lenght of the list
  ###          2. Create the new lists
  ###          3. Set a position holder
  ###          4. While index is lower or equal to half the lenght of the given list.
  ###             Add the corresponding index value to the splitted list 1.
  ###             Increase by one the value of the position holder so by the end you 
  ###             get the splitted list 1 with half the value of the original list.
  ###          5. Given that index kept on increasing until half the list, now it goes
  ###             while it is one value lower than the lenght of the unsplit list.
  ###             Add the value on position of the current index to splitted list 2.
  ###             Increase the value plus 1 in the index

  
  splitted_list1 = list()
  splitted_list2 = list()
  lenght_unsplit_list = len(unsplit_list)
  index = 0

  while index <= int(lenght_unsplit_list/2):
    splitted_list1.append(unsplit_list[index])
    index =+ 1
  print(index)
  while index < lenght_unsplit_list:
    splitted_list2.append(unsplit_list[index])
    index =+ 1
  
  # Sort each list
  # Sum them up


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
  ###############################################################
  ### Logic: 
  '''
   Approach1:

  '''
  ### Process: 1. 

    lenght_unsplit_list = len(unsplit_list)
  splitted_list1 = list()
  splitted_list2 = list()
  index = 0

  while index <= int(lenght_unsplit_list/2):
    splitted_list1.append(unsplit_list[index])
    index =+ 1
  print(index)
  while index < lenght_unsplit_list:
    splitted_list2.append(unsplit_list[index])
    index =+ 1


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
  ###############################################################
  ### Logic: 
  '''
   Approach1:

  '''
  ### Process: 1. 


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
  ###############################################################
  ### Logic: 
  '''
   Approach1:

  '''
  ### Process: 1. 
