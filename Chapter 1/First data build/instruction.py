#assume data file is web_traffic.tsv
import numpy as np
#first let data is that file
data = np.genfromtxt("web_traffic.tsv", delimiter = "\t")
#generate data from file, using "\t" (tab) as delimiter
#let x is the first column values
x=data[:,0]
#let y is the second column values
y=data[:,0]
#sanity check, sum all not a number value
np.sum(np.isnan(y)
#if there is exist nan values, clean data set
#set x, or y is x, or y without nan values
x = x[~np.isnan(y)]
y=y[~np.isnan(y)]

#following function will generate graphical representation of data set from x and yield
import matplotlib.pyplot as plt

def plot_web_traffic(x,y,models = None)
	#python consider indentation as bracket in java, becareful when placing indentation
	#anything indent from def is belong to def fuction
	plt.figure(figsize=(12,6)) # set width and high of the plot in inches
	plt.scatter(x, y, s=10)#s: scalar or array_like, shape (n, ), optional. s=10 we are setting the line width.
	#plt.scatter(x, y, s=10), which plots the web traffic in y over the individual days in
	plt.title("Web traffic over the last month")#set title
	plt.xlabel("Time")#x label
	plt.ylabel("Hits/hour")#y label
	plt.xticks([w*7*24 for w in range(5)],
				['week %i' %(w+1) for w in range(5)])
				#ticks: array_like. A list of positions at which ticks should be placed. You can pass an empty list to disable xticks.
				#[labels] array_like, optional, A list of explicit labels to place at the given locs.
	if models:
		colors = ['g', 'k', 'b', 'm', 'r']
		linestyles = ['-', '-.', '--', ':', '-']
		mx = sp.linspace(0, x[-1], 1000)
		for model, style, color in zip(models, linestyles, colors):
			plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)
		plt.legend(["d=%i" % m.order for m in models], loc="upper left")
	plt.autoscale(tight=True)
	plt.grid()
#end of funtion

#we can than call the function:
plot_web_traffic(x, y)
#for a cmd, we need to save the plot into file
plt.savefig("web_traffic.png"))
