def prawdo(n, k):
   if n == 1: return 1/2
   else: return prawdo(n-1, k)*1/2

print(prawdo(3,2))