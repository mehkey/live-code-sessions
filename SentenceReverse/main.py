
def reverse_words(arr):
    arr.reverse()

    i = 0
    total = len(arr)

    while i < total:

        j = i
        
        while j < total and arr[j] != ' ' :
            j += 1
        
        start = i
        end = j-1
        while start <= end :
            arr[start] , arr[end] = arr[end] , arr[start]
            start += 1
            end -= 1

        i = j +1

    return arr


