import time
def bubble_sort(L):
    i=len(L)
    swap=True
    while(i>0 and swap==True):
        swap = False
        for j in range(0,i-1):
            if L[j]>L[j+1]:
                swap=True
                temp=L[j]
                L[j]=L[j+1]
                L[j+1]=temp
        i-=1
    return L
t1=time.clock()
print(bubble_sort([5,6,8,2,1]))
print(time.clock()-t1)

#if the swap flag not used time complexity will be more