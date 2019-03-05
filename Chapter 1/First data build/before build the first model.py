#approximation error: guide us in choosing the right model among the many choices we have
def error(f,x,y):
	return np.sum((f(x)-y)**2)
#put the line among ploted points so that we have a line with smallest approximation error
#Scipy's polyfit() will help, this will minimize the error of function
fp1 = np.polyfit(x, y, 1)
#we now have the line y = ax + b with a, b are getting from:
print("Model parameters: %s" % fp1)
#the result is a and b values in this order