Input : {4,4,3,1,2}
Lambda:

fn(x):
	x!=maxv
arr={4,4,3,1,2}
l = list(filter(fn(arr),arr))

Filter + Lambda
lambda returns false when max value is filtered complet and filter will remove all the Max values and return the array say {3,1,2}
Now max(array) will return the 3 