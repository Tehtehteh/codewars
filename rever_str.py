def reverse(str):
    if not str:
        return ''
    else: return reverse(str[1:])+str[0:1]


