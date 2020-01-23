#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pennylane


# In[2]:


import pennylane as qml
from pennylane import numpy as np


# In[3]:


dev1 = qml.device("default.qubit", wires=1)


# In[4]:


def circuit(params):
    qml.RX(params[0], wires=0)
    qml.RY(params[1], wires=0)
    return qml.expval(qml.PauliZ(0))


# In[5]:


@qml.qnode(dev1)
def circuit(params):
    qml.RX(params[0], wires=0)
    qml.RY(params[1], wires=0)
    return qml.expval(qml.PauliZ(0))


# In[6]:


print(circuit([0.54, 0.12]))


# In[7]:


dcircuit = qml.grad(circuit, argnum=0)


# In[8]:


print(dcircuit([0.54, 0.12]))


# In[9]:


@qml.qnode(dev1)
def circuit2(phi1, phi2):
    qml.RX(phi1, wires=0)
    qml.RY(phi2, wires=0)
    return qml.expval(qml.PauliZ(0))


# In[10]:


dcircuit = qml.grad(circuit2, argnum=[0, 1])
print(dcircuit(0.54, 0.12))


# In[11]:


def cost(var):
    return circuit(var)


# In[12]:


init_params = np.array([0.011, 0.012])
print(cost(init_params))


# In[13]:


# initialise the optimizer
opt = qml.GradientDescentOptimizer(stepsize=0.4)

# set the number of steps
steps = 100
# set the initial parameter values
params = init_params

for i in range(steps):
    # update the circuit parameters
    params = opt.step(cost, params)

    if (i + 1) % 5 == 0:
        print("Cost after step {:5d}: {: .7f}".format(i + 1, cost(params)))

print("Optimized rotation angles: {}".format(params))


# In[ ]:




