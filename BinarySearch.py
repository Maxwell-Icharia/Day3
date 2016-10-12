class BinarySearch(list):
    def __init__(self, a, b):
        length = len(list)
        self.a = len
        self.b = l
    def bin_search(arr, tar):
        lower = 0
        upper = len(arr)
        while lower < upper:
            x = lower + (upper - lower) // 2
            val = arr[x]
            if tar == val:
                return x
            elif tar > val:
                if lower == x:
                    break
                lower = x
            elif tar < val:
                upper = x
