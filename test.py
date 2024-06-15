arr=[1,0,2,3,0,4,5,0]

def duplicateZeros(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        print(i)
        if i != 0 and arr[i] == 0 and arr[i-1] != 0:
            arr.insert(i,0)
        elif i == 0 and arr[i] == 0:
            arr.insert(i,0)
    print(f"PRE{arr}")      
    arr = arr[:len_arr]
    print(f"IN{arr}")

arr = duplicateZeros(arr)
print(arr)