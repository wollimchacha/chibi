
def calc(s):
    nums = map(int,s.split('+'))
    print('nums=',nums)
    return sum(nums)
    nums = map(int,s.split('*'))
    print('nums=',nums)
    return numpy.prod(nums)
    
print(calc("1"))
print(calc("1+2"))
print(calc("1+2+3"))
print(calc("1*2+3"))