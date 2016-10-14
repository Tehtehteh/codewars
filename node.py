class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def push(self, data):
        self.next = Node(data)


def build_one_two_three():
    f = Node(None)
    f.push(1)
    f.push(2)
    f.push(3)
    return f


print(build_one_two_three().next)
