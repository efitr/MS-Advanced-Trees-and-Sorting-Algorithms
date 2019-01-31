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
  ###          3. 
  ###
  ###
  ###
  new_list = list()

  if list1[0] < list2[0]:
    new_list.append(list1.pop(0))

  elif list2[list2_current_position] < list1[list1_current_position]:
    new_list.append(list2.pop(0))

  elif not list1:
    if list2:
      new_list.append(list2.pop(0))
    else not list2:
      return new_list
  
  elif not list2:
    if list1:
      new_list.append(list1.pop(0))
    else not list1:
      return new_list
  else:
    new_list.append(list1.pop(0))
    new_list.append(list2.pop(0))
  
  return new_list

def split_sort_merge(items):
  """Sort given items by splitting list into two approximately equal halves,
  sorting each with an iterative sorting algorithm, and merging results into
  a list in sorted order.
  TODO: Running time: ??? Why and under what conditions?
  TODO: Memory usage: ??? Why and under what conditions?"""
  # TODO: Split items list into approximately equal halves
  # TODO: Sort each half using any other sorting algorithm
  # TODO: Merge sorted halves into one list in sorted order
  ###############################################################
  ### Logic: 
  '''
   Approach1:

  '''
  ### Process: 1. Create new list that will hold the merged values



def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


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
