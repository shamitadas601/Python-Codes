import time
def selection_sort(L):
    min_element=0
    min_index=0
    length=len(L)
    for i in range(length):
        #min_element=min(L)
        min_element=min(L[i:length])
        #print(min_element)
        min_index=L.index(min_element)
        #print(min_index)
        #for j in range(i,length):
        L[i],L[min_index]=L[min_index],L[i]
        #i-=1
    return L
t1=time.clock()
print(selection_sort([5,6,8,2,1]))
print(time.clock()-t1)