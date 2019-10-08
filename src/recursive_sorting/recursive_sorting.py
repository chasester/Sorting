import random;

def split(input_list):
    #splits the arra into parts and merges the parts
    mid = len(input_list)//2; #// is even divide
    #divide this into everything before the midpoint and everthing after the mid point
    #return this as a tuple return variable
    return input_list[:mid], input_list[mid:]

def merge_sorted_lists(right, left):
    ileft = iright = 0;
    merged = [];
    
    while True:
        if(left[ileft] <= right[iright]):
            merged.append(left[ileft]);
            ileft += 1;
        else:#we have the oppisite
            merged.append(right[iright]);
            iright += 1;

        if(iright == len(right)): #check if we are done with either array
            merged += left[ileft:]
            break;
        elif(ileft == len(left)):
             merged += right[iright:];
             break;
    return merged;

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if(len(arr)) <= 1: #cuz they normally make you check this
        return arr;
    #do the first split into to parts and then call the sort to start the process
    left,right = split(arr);
    
    return merge_sorted_lists(merge_sort(left), merge_sort(right))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

if(__name__ == "__main__"):
    li = []
    for i in range(0, random.randint(100000,200000)):
        li.append(random.randint(-999,999));
    print(merge_sort(li));
