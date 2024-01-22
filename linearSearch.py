numbers = [10,20,30,40,50,60]
choice =  int(input('Enter the number you want to search '))


def linear_Search(numbers,c):
    for i in range(len(numbers)):
        if numbers[i] == c:
            print('Number found at index: ',i)
            return i
        
    print('Number not found')
    return -1


#Time Complexity : O(n)

index =  linear_Search(numbers,choice)
