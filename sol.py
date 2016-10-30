"""
	solution('abc') # should return ['ab', 'c_']
	solution('abcdef') # should return ['ab', 'cd', 'ef']
"""
def ys(s):
	if len(s) == 0:
		return ''
	elif len(s) == 2 or len(s) == 1:
		yield s + '_'*(2-len(s))
		return
	yield s[:2]
	yield from ys(s[2:])

def solution(s):
	return list(ys(s))

print(solution('abcde'))