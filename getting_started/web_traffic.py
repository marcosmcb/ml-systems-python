import scipy as sp
import matplotlib.pyplot as plt

data = sp.genfromtxt( "web_traffic.tsv", delimiter="\t" )

hours = data[:,0]
hits  = data[:,1]

print 'Invalid Values = ' + str( sp.sum(sp.isnan(hits)) )

hours = hours[~sp.isnan(hits)]
hits  = hits[~sp.isnan(hits) ]

plt.scatter(hours,hits)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hours")
plt.xticks( [w*7*24 for w in range(10)], ['week %i' % w for w in range(10)]  )
plt.autoscale(tight=True)

plt.grid()
plt.show()
