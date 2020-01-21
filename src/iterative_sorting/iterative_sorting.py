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
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr
print(selection_sort ([11, 33, 2, 45, 6, 5]))





# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
        # n = length of the array
    n = len(arr)

    # For every item in the array
    for i in range(n):
        # last item in range
        for j in range(0, n-i-1):
            # traverse the array from begging to end
            # and swap out if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubble_sort([5,2,1,9,0,4,6]))
   

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr