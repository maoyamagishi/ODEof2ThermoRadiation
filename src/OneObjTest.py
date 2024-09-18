from ThermoModel import obj
import matplotlib.pyplot as plt
#initial condition
pilot =   obj(1,5.0,1.0,360.0)
fairing = obj(1,1.0,1.0,300.0)
dt = 0.001  #Global time interval
heatgen = 400  #(W) generating heat from pilot

for ii in range(200):
    pilot.save()
    fairing.save()
    #pilot.heatup(heatgen,dt)
    #print("pilot heat up!")
    pilotrad = pilot.radiate(dt,1)
    fairing.heatup(-1*pilotrad,dt)
    fairingrad = fairing.radiate(dt,1)
    pilot.heatup(-1*fairingrad,dt)

plt.plot(pilot.hstlst,label = "pilot")
plt.plot(fairing.hstlst,label = "fairing")

pilot2 = obj(1,5.0,1.0,360.0)
fairing2 = obj(1,1.0,1.0,300.0)

for ii in range(200):
    pilot2.save()
    fairing2.save()
    #pilot2.heatup(heatgen,dt)
    #print("pilot heat up!")
    pilotrad2 = pilot2.radiate(dt,1)
    fairing2.heatup(-1*pilotrad2,dt)
    fairingrad2 = fairing2.radiate(dt,0.5)
    pilot2.heatup(-1*fairingrad2,dt)

plt.plot(pilot2.hstlst,label = "pilot2")
plt.plot(fairing2.hstlst,label = "fairing2")
plt.legend()
plt.show()
for ii in range(len(fairing.hstlst)):
    print(f"{fairing.hstlst[ii]}")