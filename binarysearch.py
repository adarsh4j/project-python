def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

arr=list(map(int,input("Enter the elements separated by space : ").split()))
target=int(input("Enter the target element to be searched :"))
result=binary_search(arr,target)
if result!=0:
    print(f"Elements to be found in index {result} ")
else:
    print("Elements not be found")
