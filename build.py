def pairwise_swap(self, num):
    if num is None:
        raise TypeError('num cannot be None')
    if num == 0 or num == 1:
        return num
    odd = (num & int('101', base=2)) >> 1
    even = (num & int('010', base=2)) << 1
    return odd | even
