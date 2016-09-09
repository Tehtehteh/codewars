def iq_test(numbers):
    Odd = list(filter(lambda x: x%2==0, map(int, numbers.split())))
    Even = list(filter(lambda x: x%2==1, map(int, numbers.split())))
    if len(Odd)>len(Even):
        return list(map(int, numbers.split())).index(Even[0])+1
    else:
        return list(map(int, numbers.split())).index(Odd[0])+1

print(iq_test("1 2 2"))