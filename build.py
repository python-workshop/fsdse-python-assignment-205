def build(num):
    if num is None:
      return False
    if num == 0 or num == 1:
        return num
    else:
        odd = (num & int('1010101010101010',2))
        odd = odd >> 1
        even = (num & int('0101010101010101',2))
        even = even << 1
        return odd | even
