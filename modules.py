#some functions from math module
import math
print(math.gcd(12,6))
print(math.factorial(5))
print(math.floor(12/2))
print(-math.inf)
print(math.pi)
#'sys' moudule provides access to variables and functions related to system 
#or python interpreter
import sys
def printData():
	print (sys.argv)
print(printData())
def printSum():
	print(int(sys.argv[1])+int(sys.argv[2]))
printSum()
print(sys.version)
#interpreter will search packages in their paths
print(sys.path)
print(sys.maxsize)
print(type(sys.stdin))
print(sys.stdout)
