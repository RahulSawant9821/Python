list = [10,20,30,40,50,60]
c = int(input('Enter the number to be searched:'))


def binarySearch(list,c):
    low = 0
    high =  len(list)-1
    while low <=high:
        mid = low + high // 2
        if list[mid] == c :
            print('Number found at ',mid)
            return mid
        elif list[mid] < c :
            low = mid + 1 
        else: 
            high = mid-1

    print('Not found')
    return -1


# O(log n) : This pattern aligns with the concept of logarithms. The logarithm of a number (base 2 in this case) represents how many times you can divide it by 2 before reaching 1.
#log₂(16) = 4, indicating that 4 iterations are needed to reduce the search space to 1 element. 

binarySearch(list,c)