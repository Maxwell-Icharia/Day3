def find_missing(arr1, arr2):
    extra = 0
    if len(arr1) > len(arr2):
        list1 = arr1
        list2 = arr2
    else:
        list1 = arr2
        list2 = arr1
    for num in list1:
        if num not in list2:
            extra = num
    return extra
