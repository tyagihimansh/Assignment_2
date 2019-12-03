from ctypes import*
fun=CDLL("./fact.so")
print(fun.term(20))
