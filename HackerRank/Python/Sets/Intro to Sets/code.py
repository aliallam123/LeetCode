def average(array):
    # your code goes here
    unique = set(array)
    average = sum(unique) / len(unique)
    return average
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
