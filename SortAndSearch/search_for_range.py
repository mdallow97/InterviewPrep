# search_for_range.py

def searchRange(arr, target):
    try:
        begin = arr.index(target)
    except:
        return [-1,-1]

    end = begin
    while end < len(arr)-1 and arr[end+1] == target:
        end += 1

    return [begin,end]


print(searchRange([8], 10))
