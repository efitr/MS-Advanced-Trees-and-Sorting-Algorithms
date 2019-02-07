#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(1) Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
  #####################
  ### Logic: This has to make sure that all the items in the array are in
  ###        sorted order and return true or false
  
  
  #####################
  ### Approach: Make it go from the start to the end, while it does that
  ###           it has to compare the previous with the next value and keep
  ###           going until it's false or everything is sorted
  #####################
  ### Process1: 1. Compare that if the list has 0 or 1, return True
  ###          2. If the items are not sorted, return False
  ###          3. Then it's asume that it must be sorted
  # if len(items) == 0 or len(items) == 1:
  #   return True
  # elif items != sort(items)
  #   return False
  # else:
  #   return True  
  

  #####################
  ### Process2: 1. If the items are not sorted, return False
  ###          2. If the items are not sorted then they must be sorted, return True
  if items != sort(items):
    return False
  else:
    return True

def bubble_sort(items):
  """Sort given items by swapping adjacent items that are out of order, and
  repeating until all items are in sorted order.
  TODO: Running time: ??? Why and under what conditions?
  TODO: Memory usage: ??? Why and under what conditions?"""
  # TODO: Repeat until all items are in sorted order
  # TODO: Swap adjacent items that are out of order
  ###############################################################
  ### Logic: I want to get my items sorted and I don't care how long it takes.
  ###        So I will check continous elements and if the one in a higher 
  ###        position is lower than the one in the next position change them, 
  ###        until order reigns.
  '''
   Approach1: Here 

  '''
  ### Process: 1. 
    


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
