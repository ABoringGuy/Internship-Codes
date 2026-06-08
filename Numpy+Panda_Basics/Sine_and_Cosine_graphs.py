import numpy as np
import matplotlib.pyplot as plt

"""Below x=np.linspace(start, end, points)
start=0
end= 2*pi
num= 100,for smooth curve

np.linspace() is used to create evenly spaced values for plot"""
x= np.linspace(0,2*np.pi,100)

choice=input("""[1] Sine
[2] Cosine""")

if choice=="1":
    sine_graph=np.sin(x)
    plt.plot(x, sine_graph, label="sin(x)")
    title="Sine graph"
    plt.title(title)
else:
    cosine_graph=np.cos(x)
    plt.plot(x,cosine_graph, label="cos(x)")
    title="Cosine graph"
    plt.title(title)

plt.legend()
plt.show()