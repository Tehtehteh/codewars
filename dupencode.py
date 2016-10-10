from collections import Counter
def duplicate_encode(word):
    g = Counter(word.lower())
    res = ''
    for x in word.lower():
        if g.get(x) > 1:
            res = res + ')'
        else:
            res = res + '('
    return res


print(duplicate_encode('Success'))




#
# Test.assert_equals(duplicate_encode("din"),"(((")
# Test.assert_equals(duplicate_encode("recede"),"()()()")
# Test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
# Test.assert_equals(duplicate_encode("(( @"),"))((")