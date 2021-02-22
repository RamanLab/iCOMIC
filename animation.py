import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib import animation

fig,ax = plt.subplots()
ax.set_aspect('equal','box')
circle = Circle((0,0), 1.0)
ax.add_artist(circle)
ax.set_xlim([0,10])
ax.set_ylim([-2,2])

def animate(i):
    circle.center=(i,0)
    return circle, 

anim = animation.FuncAnimation(fig,animate,frames=10,interval=100,repeat=False,blit=True)

plt.show()