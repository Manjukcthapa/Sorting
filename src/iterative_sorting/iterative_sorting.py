# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for number in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[number]:
                smallest_index = number


        # TO-DO: swap
          # Swap the two values so the larger value is on the right
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr
   
print(selection_sort ([5,9,1,2,7,0]))
# 5 is the minimum
# 5<9: nothing happens
# 5>1: 1 is new minimum
# 1<2: nothing happens
# 1<7: nothing happens
# 1>0: 0 is the new minimum
# Swap 0 and 5
# alist =  [0,9,1,2,7,5]

print(selection_sort ([35, 3, 34, 65, 2, 5]))





# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    while True:
        swaps = 0
        for i in range(len(arr) - 1):
            value_1 = arr[i]
            value_2 = arr[i+1]
            if arr[i+1] < arr[i]:
                arr[i] = value_2
                arr[i+1] = value_1
                swaps += 1
        if swaps == 0:
            break

  
    return arr
# print(bubble_sort([6,8,1,3,0,5]))
# 0 - 6<8 (no swap) - [6,8,1,3,0,5]
# 1 - 8>1 (swap) - [6,1,8,3,0,5]
# 2 - 8>3 (swap) - [6,1,3,8,0,5]
# 3 - 8>0 (swap) - [6,1,3,0,8,5]
# 4 - 8>5 (swap) - [6,1,3,0,5,8]
# 8 is in its correct place
   

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr