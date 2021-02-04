import numpy as np
import matplotlib.pyplot as plt
x= np.array([1,2,3])
y=np.array([1.2,1.9,3.2])

def values(x,y):
	g=x.sum()
	h=y.sum()
	m=(x*x).sum()
	n=(y*y).sum()
	l=len(x)
	w0=(m*h-g*n)/(m*l-g*g)
	w1=(h-(l*w0))/g
	return w1,w0
slope,intercept=values(x,y)
final_values=[slope*i+ intercept for i in x]

plt.title("Maximum Likelihood Linear Line")
plt.xlabel("Data Points")
plt.ylabel("Fitted Points")
plt.scatter(x,y)
plt.plot(x,y,'co')
plt.plot(x,final_values,'k')
plt.show()