spoken = lambda greeting: greeting[0].upper() + greeting[1:] + '.'#?
shouted = lambda greeting: greeting.upper() + '!'#?
whispered = lambda greeting: greeting.lower() + '.'#?
#
greet = lambda style, msg: style(msg) #?

print(greet(spoken,'Hello'))


class mylist(list):
    def __init__(self, *args):
        super().__init__(*args)
    def __call__(self, *args, **kwargs):
        return 'qeq'

f = mylist([1,2,3])
print(help(super))