if __name__ =="__main__":
	#what to do when the module is run directly
	print("M1 module is %s",(__name__))
else:
	#specify what to do when this module is imported
	print("I am in m1, imported in some other file")
