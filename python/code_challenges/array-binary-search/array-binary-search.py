# newarray = [1,2,3,4]
# value= input()

# def BinarySearch(array,key):
#      for i in range(len(newarray)):
#          if str(newarray[i]) == value:
#              return i
#              break
#      else:
#          return -1

# print(BinarySearch(newarray,value))


def  Binarysearch(arr,key):
    starting = 0
    ending= len(arr)-1
    middleval=0

    while ending >=  starting :
        middleval = (ending + starting) // 2
        if arr[middleval] == key:
            return middleval
        if arr[middleval] > key:
            ending=middleval-1
        else :
            starting=middleval+1

    return( -1)
print(Binarysearch([1,2,3,4,5,6,7],3))
