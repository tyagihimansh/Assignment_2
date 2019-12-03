from scipy.special import factorial
from time import time
def term(n):
    if (n==1):
        return 1
    fact=1
    fact=n*term(n-1)
    return fact
start=time()
print (term(20))
end=time()
print ("execu.time for python's user factorial\n",end-start)
start=time()
print (factorial(20))
end=time()
print ("execu.time for python's scipy factorial\n",end-start)
