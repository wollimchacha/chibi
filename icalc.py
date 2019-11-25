import pegpy
peg = pegpy.grammar('chibi.tpeg')
parser = pegpy.generate(peg)

class Expr(object):
    @classmethod
    def new(cls, v):
        if isinstance(v, Expr):
            return v
        return Val(v)

class Val(Expr):
    __slot__=['value']

    def__init__(self,value):
        self.value=value

    def__repr__(self):
        return f'Val({self.value})'

    def eval(self, env: dict):
        return self.value


#t = parser('1+2*3')
#print(repr(t))

def calc(t):
    if t == 'Int':
        return int(str(t))
    if t == 'Add':
        return calc(t[0]) + calc(t[1])
    if t == 'Mul':
        return calc(t[0]) * calc(t[1])
    print(f'TODO{t.tag}')
    return 0

#t = parser('1+2*3+4*5')
#print(repr(t))
#print(calc(t))


def main():
    s = input('$')
    t = parser(s)
    print(calc(t))

if __name__ == '__main__':
    main()
