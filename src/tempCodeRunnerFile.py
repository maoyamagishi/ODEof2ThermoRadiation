
# for ii in range(60000):
#     pilot.save()
#     fairing.save()
#     #pilot.heatup(heatgen,dt)
#     #print("pilot heat up!")
#     pilotrad = pilot.radiate(dt,1)
#     fairing.heatup(-1*pilotrad,dt)
#     #print("pilot radiate!")
#     fairingrad = fairing.radiate(dt,1)
#     pilot.heatup(-1*fairingrad,dt)
#     #print("fairing radiate!")
#     # if fairing.kelv > 306.0:
#     #     fairing.kelv = 306.0

# plt.plot(pilot.hstlst,label = "pilot")
# plt.plot(fairing.hstlst,label = "fairing")