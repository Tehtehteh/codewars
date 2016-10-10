from collections import Counter
def scramble(s1,s2):
    return set(Counter(s2)).issubset(set(Counter(s1)))



# Test.assert_equals(scramble('rkqodlw','world'),True)
# Test.assert_equals(scramble('cedewaraaossoqqyt','codewars'),True)
# Test.assert_equals(scramble('katas','steak'),False)
# Test.assert_equals(scramble('scriptjava','javascript'),True)
# Test.assert_equals(scramble('scriptingjava','javascript'),True)