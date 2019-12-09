def moneta(n,k):
   if n == 0:
      if k ==0: return 1
      else: return 0
   else: return(
      1/2*moneta(n-1,k)+ 1/2*moneta(n-1, k-1))



print(moneta(3,2))
