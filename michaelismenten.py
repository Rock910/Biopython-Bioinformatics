#Python differential equation solving to solve the nonlinear differential equations-michaelis-menten equations
#Rough draft, needs some adjustment by user to operate(like including correct rate coefficients)

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#function 
def rxn(x, t):
    #reaction function: takes in species and differential equations, returns differential equation results
    
  
    E= x[0]
    S= x[1]
    ES = x[2]
    P= x[3]
    
    #set up constants, K_f(reaction forwardrate), K_r(backwards rate), K_cat(K_c)
    K_f= 3
    K_r= 2
    K_c= 1
   
    #set up differential equations - uses the pre-factors above
    dEdt= -K_f * E * S + K_r * ES + K_c * ES
    dSdt= -K_f * E * S + K_r * ES 
    dESdt= K_f * E * S - K_r * ES -K_c * ES
    dPdt= K_c * ES

    print ("t = " + str(t))
    #print "dnedt = " + str(dnedt)
    #print "dTedt = " + str(dTedt)


    return [dEdt, dSdt, dESdt, dPdt]




#Constants



#Initial conditions
x0= [1, 1, 1, 1]


#Defining the time vector
t0 = 0.0
tend = 10000
nt = 100000

T = np.linspace(t0, tend, nt)



#Integrating the governing equation provided by the function
X = odeint(rxn, x0, T)


print (("Final value of E = %e \n") % X[-1,0])
print (("Final value of S = %f ") % X[-1,1])






#Plotting
label_size = 16

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,6))

ax1.plot(T, X[:, 0], 'b', linewidth=2)
ax1.set_title(r'Evolution of E')
ax1.set_xlabel(r'$t$ $(s)$', fontsize=label_size)
ax1.set_ylabel(r'Concentration', fontsize=label_size)


ax2.plot(T, X[:, 1], 'r', linewidth=2)
ax2.set_title(r'Evolution of S')
ax2.set_xlabel(r'$t$ $(s)$', fontsize=label_size)
ax2.set_ylabel(r'$Concentration$', fontsize=label_size)
#plt.legend()
plt.show()



















