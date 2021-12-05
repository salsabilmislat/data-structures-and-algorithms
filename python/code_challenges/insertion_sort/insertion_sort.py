# def insertion_sort(arr=[]):
#     arr_len=len(arr)
#     for i in range(arr_len):
#         min_index=i
#         for j in range(i+1,arr_len):
#             if (arr[j]< arr[min_index]):
#                 min_index=j
#         temp=arr[min_index]
#         arr[min_index]=arr[i]
#         arr[i]=temp

#     return(arr)


def insertion_sort(arr=[]):

    if len(arr)==0:
        return 'this array is empty'

    arr_len=len(arr)
    for i in range(1,arr_len):
        j=i-1
        temp=arr[i]
        # print(i)
        # print(j)
        # print(temp)
        while j>=0 and temp < arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
        # print(arr)

    return(arr)

print(insertion_sort([8, 4, 23, 42, 16, 15]))



