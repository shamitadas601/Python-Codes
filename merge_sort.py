def merge(L1,L2):
    L = []
    #print(L1,L2)
    #print(type(L2))
    if not L1:
        return L1
    if not L2:
        return L2
    L=L1+L2
    print(L)
    #L=[]
    L.sort()
    return L
def merge_sort(Lis):

    if len(Lis)< 2:
        return Lis
    else:
        q = (len(Lis)) // 2
        left=merge_sort(Lis[:q])
        right=merge_sort(Lis[q:])
        return merge(left,right)
def modSwapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)
print(modSwapSort([8,6,5,2,1]))
print(merge_sort([5,6,8,2,1]))
