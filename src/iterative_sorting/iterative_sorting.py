# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    smind = -1;
    for i in range(0, len(arr) - 1):
        smind = i;
        for j in range(i+1, len(arr)):
            if(arr[smind] > arr[j]):
                smind = j;
        if(smind != i):
            temp = arr[i];
            arr[i] = arr[smind];
            arr[smind] = temp;

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if(arr[j] > arr[j+1]):
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if(len(arr) < 2):
        return arr;
    vmax = max(arr);
    vmin = min(arr);
    if(vmin < 0):
        #raise Exception("Must not be Positive");
        return "Error, negative numbers not allowed in Count Sort";
    rng = vmax-vmin+1;
    count = [0 for i in range(rng)];
    output = [0 for i in range(len(arr))];
    for i in range(len(arr)):
        count[arr[i]-vmin] += 1;
    for i in range(1, len(count)):
        count[i] += count[i-1];
    for i in range(len(arr)-1, -1, -1):
        output[count[arr[i]-vmin]-1] = arr[i];
        count[arr[i]-vmin] -= 1;
    for i in range(len(arr)):
        arr[i] = output[i];
    return arr

def swapvalues(a, b):
    temp = a;
    a = b;
    b = temp;

if(__name__ == "__main__"):
    arr = [4,3,4,52,32,4,2,4,5,2,5,43,2,3,4,241,4,14,23,42,14,3,2,3,4,5,23];
    print(selection_sort(arr[:]));
    print(bubble_sort(arr[:]));
    print(count_sort(arr[:]));
