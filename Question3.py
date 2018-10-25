def merge(list1, list2):
    total=(list1+list2)
    mergeSort(total)
    return total

def mergeSort(total):
    if len(total)>1:
        mid = len(total)//2
        left = total[:mid]
        right = total[mid:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                total[k]=left[i]
                i=i+1
            else:
                total[k]=right[j]
                j=j+1
            k=k+1
        while i < len(left):
            total[k]=left[i]
            i=i+1
            k=k+1
        while j < len(right):
            total[k]=right[j]
            j=j+1
            k=k+1
    


print(merge([1,3,5,7],[2,4,6,8]))
