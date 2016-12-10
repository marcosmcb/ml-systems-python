import scipy as sp
import matplotlib.pyplot as plt

data = sp.genfromtxt( "web_traffic.tsv", delimiter="\t" )

hours = data[:,0]
hits  = data[:,1]

print 'Invalid Values = ' + str( sp.sum(sp.isnan(hits)) )

hours = hours[~sp.isnan(hits)]
hits  = hits[~sp.isnan(hits) ]
'''
Plotting some data
'''
plt.scatter(hours,hits)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks( [w*7*24 for w in range(10)], ['week %i' % w for w in range(10)]  )
plt.autoscale(tight=True)
plt.grid()
#plt.show()

# Our error function is defined as the mean squared errors
def error( f, x, y ):
    return sp.sum( ( f(x)-y ) ** 2 )


# Starting with a simple line - Using linear regression in Scipy
fp1, residuals, rank, sv, rcond = sp.polyfit( hours, hits, 1, full=True )
print "Model parameters: %s " % fp1

print residuals

# We then use poly1d() to create a model function from the model parameters
f1 = sp.poly1d( fp1 )
print error( f1, hours, hits )

'''
Curve Fitting -  Trying to fit our 1st order model on the data
'''
fx = sp.linspace( 0, hours[-1], 1000 ) #generate X-values for plotting
plt.plot( fx, f1(fx), linewidth=4 )
plt.legend( ["d=%i" % f1.order ], loc = "upper left" )
#plt.show()

'''
Towards some advanced stuff - Fitting a more complex model, a polynomial of degree 2
'''
f2p = sp.polyfit( hours, hits, 2 )
print f2p

f2 = sp.poly1d( f2p )
print error( f2, hours, hits )

'''
Plotting the two models on the same graph
'''
fx = sp.linspace( 0, hours[-1], 1000 )
plt.plot( fx, f1(fx), linewidth=4 )
plt.plot( fx, f2(fx), linewidth=4 )
plt.legend( ["d=%i" % f1.order, "d=%i" % f2.order ], loc = "upper left" )
#plt.show()

