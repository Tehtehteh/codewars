def solution(digits):
    nums = list(map(int, NumR(digits)))
    print(max(nums))
    return 0

def NumR(digits):
    if len(digits)==5:
        yield digits
        return
    yield digits[:5]
    yield from NumR(digits[1:])

solution('176531330624919225119674426574742355349194934969835')