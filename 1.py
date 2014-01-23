import scipy as sp
import matplotlib.pyplot as plt
data=sp.genfromtxt("/home/maximus/web_traffic.tsv")
x=data[:,0]
y=data[:,1]
x=x[~sp.isnan(y)]
y=y[~sp.isnan(y)]
plt.scatter(x,y)
plt.title("web traffic over last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
fp1,residuals,rank,sv,rcond=sp.polyfit(x,y,3,full=True)
f1=sp.poly1d(fp1)
fx=sp.linspace(0,x[-1],1000)
plt.plot(fx,f1(fx),linewidth=4)
plt.autoscale(tight=True)
plt.grid
plt.show()
