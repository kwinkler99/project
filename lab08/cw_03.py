def znaki(napis):
    if len(napis) == 0: return ''
    else: return znaki(napis[1:])+napis[0]


print(znaki('abc'))
