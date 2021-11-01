
def insert_shift_array(array,value):
    count =0
    newarr =[]
    for i in array:
        count += 1
    if count %2 == 0:
        middle = count/2
    else:
        middle =count/2 + 0.5
    newarr = [0]*(count +1)
    j=0
    for i in array:
        if j<middle:
            newarr[j] = i
            j += 1
        elif j == middle:
            newarr[j]= value
            j += 1
        else:
            newarr[j] =i -1
            j +=1
        newarr[j] = i
    return newarr
print(insert_shift_array([1,2,3,4,5,6],100))
print(insert_shift_array([1,2,3,4,5,6,7],40))



