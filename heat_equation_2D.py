import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation


alpha = 1
delta_xy = 1

#Setter en stabil verdi for delta_t
delta_t = (delta_xy**2)/(4*alpha)

#gamma
gamma = (delta_t*alpha)/(delta_xy**2)

#antall punkter i lengde, bredd og tid
lengde_xy = 200
tidsiterasjoner = 400

#lager et plan for med foreløpige nullverdier
u =np.empty([tidsiterasjoner,lengde_xy,lengde_xy])
u.fill(0)

#fyller inn verdier i planet utifra startbetingelsene
#Velger å ha et kryss som starttilstand
u[:, (lengde_xy-112):(lengde_xy-88), :] = 100
u[:, :, (lengde_xy-112):(lengde_xy-88)] = 100


#grensebetingelser
u[:, :, :1] = 0
u[:, :, -1:] = 0
u[:, :1, :] = 0
u[:, -1:, :] = 0


def oppdater_plan(u):
    for k in range(1,tidsiterasjoner-1,1):
        for i in range(1,lengde_xy-1,delta_xy):
            for j in range(1,lengde_xy-1,delta_xy):

               u[k + 1, i, j] = gamma * (u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]

    return u

def plot(u_ved_gitt_tid, tidssteg):

    #fjerner forrige bilde ved forrige tidsiterasjon
    plt.clf()

    #kosmetikk for vinduet
    plt.title(f"Temperatur ved tidssteg {tidssteg}")
    plt.xlabel("x-retning")
    plt.ylabel("y-retning")

    #setter fargene i plottet og en bar som viser hvilken farge som tilsvarer hvilken temp
    plt.pcolormesh(u_ved_gitt_tid,cmap=plt.cm.jet,vmin=0,vmax=100)
    plt.colorbar


    return plt

u = oppdater_plan(u)

#animer lager et bilde for hver tidsiterasjon, hvor varmefordelingen har gått ett hakk videre
def animer(k):
    plot(u[k],k)

#kjører animer og lagrer som en gif
anim = animation.FuncAnimation(plt.figure(), animer, interval=10, frames = tidsiterasjoner)
anim.save("heat_equation_solution.gif")
  



