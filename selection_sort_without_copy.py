import time# takes  less time and complexity is less as we are not making a copy
def selection_sort(L):
    min_element=0
    min_index=0
    length=len(L)
    i=0
    while i!=length:
        for j in range(i+1,length):
            if L[i]>L[j]:
                L[i], L[j] = L[j], L[i]
        i+=1
    return L
t1=time.clock()
print(selection_sort([5,6,8,2,1]))
print(time.clock()-t1)