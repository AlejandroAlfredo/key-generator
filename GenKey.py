# key generator

from random import *

count = 0
myList = []
myString = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
myInteger = "0,1,2,3,4,5,6,7,8,9"
myList = myString.split(",")
myList += myInteger.split(",")

for x in range(0, 500):
    print("{}-{}-{}-{}-{}".format("".join(choices(myList, k=5)), "".join(choices(myList, k=5)),
                                  "".join(choices(myList, k=5)), "".join(choices(myList, k=5)),
                                  "".join(choices(myList, k=5))))
