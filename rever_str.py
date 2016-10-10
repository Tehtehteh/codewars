def reverse(str):
    if not str:
        return ''
    else: return reverse(str[1:])+str[0:1]


print(reverse('qeqoos'))
print('sooqa'[1:] + 'sooqa'[0:1])