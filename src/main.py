from ThermoModel import obj
import matplotlib.pyplot as plt
#initial condition
pilot = obj(1,1.0,1.0,360.0)
fairing = obj(1,1.0,1.0,300.0)
dt = 0.001  #Global time interval
heatgen = 400  #(W) generating heat from pilot

for ii in range(400):
    pilot.save()
    fairing.save()
    #pilot.heatup(heatgen,dt)
    #print("pilot heat up!")
    pilotrad = pilot.radiate(dt,1)
    fairing.heatup(pilotrad,dt)
    print("pilot radiate!")
    fairingrad = fairing.radiate(dt,0.1)
    pilot.heatup(fairingrad,dt)
    print("fairing radiate!")
    # if fairing.kelv > 306.0:
    #     fairing.kelv = 306.0

plt.plot(pilot.hstlst,label = "pilot")
plt.plot(fairing.hstlst,label = "fairing")

pilot2 = obj(5,1.0,0.8,303.0)
fairing2 = obj(5,1.0,0.8,303.0)

# pilot2 = obj(1,70.0,1.0,363.0)
# fairing2 = obj(1,1.0,1.0,303.0)
# for ii in range(40):
#     pilot2.save()
#     fairing2.save()
#     #pilot2.heatup(heatgen,dt)
#     #print("pilot heat up!")
#     pilot2.radiate(fairing2.kelv,dt,1)
#     #print("pilot radiate!")
#     # fairing.heatup(-1*pilotrad,dt)
#     fairing2.radiate(pilot2.prekel,dt,0.1)
#     # if fairing.kelv > 306.0:
#     #     fairing.kelv = 306.0

# for ii in range(40):
#     pilot2.save()
#     fairing2.save()
#     pilot2.heatup(heatgen,dt)
#     #print("pilot heat up!")
#     pilotrad = pilot2.radiate(fairing2.kelv,dt,1)
#     print("pilot radiate!")
#     fairingrad = fairing2.radiate(pilot2.prekel,dt,0.1)
#     print("fairing radiate!")
#     fairing2.heatup(-1*pilotrad,dt)
#     pilot2.heatup(-1*fairingrad,dt)

# plt.plot(pilot2.hstlst,label = "pilot2")
# plt.plot(fairing2.hstlst,label = "fairing2")
plt.legend()
plt.show()
# for ii in range(len(fairing.hstlst)):
#     print(f"{fairing.hstlst[ii]}")