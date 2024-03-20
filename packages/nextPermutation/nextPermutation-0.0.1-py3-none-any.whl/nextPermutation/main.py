def reverse(index,arr):

    i=index
    j=len(arr)-1
    while i<j:

        arr[i],arr[j]=arr[j],arr[i]
        i=i+1
        j=j-1

    return arr

def nextGreaterPermutation(a):

    n=len(a)
    index=-1

    for i in range(n-2,-1,-1):

        if a[i]<a[i+1]:
            index=i
            break

    if index==-1:
        a.reverse()
        return a

    for i in range(n-1,index,-1):

        if a[i]>a[index]:
            a[i],a[index]=a[index],a[i]
            break

    arr=reverse(index+1,a)
    return arr

