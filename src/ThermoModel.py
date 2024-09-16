class obj():
    sigma = 5.67 * 10**(-8) #Stefan-Boltzmann constant
    # sigma = 1.0#for test

    def __init__(self,specheat:float,mass:float,eps:float,kelv:float) -> None:
        self.__specheat = specheat
        self.__mass = mass
        self.__eps = eps    #emissivity
        self.__kelv = kelv  #(K) Kelvin
        self.__prekel = 0
        self.__hstlst = []   #history of tempreture of this object

    @property
    def specheat(self):
        return self.__specheat
    
    @property
    def mass(self):
        return self.__mass
    
    @property
    def eps(self):
        return self.__eps
    
    @property
    def kelv(self):
        return self.__kelv
    
    @kelv.setter
    def kelv(self, value):
        self.__kelv = value
    
    @property
    def hstlst(self):
        return self.__hstlst
    
    @property
    def prekel(self):
        return self.__prekel
    
    def heatup(self,Q:float,dt:float)->None:
        self.__prekel = self.__kelv
        self.__kelv += Q*dt/(self.__mass*self.__specheat)
        print(Q*dt/(self.__mass*self.__specheat))

    def radiate(self,dt,rate)->float:
        selfKelv = self.__kelv
        amtheat = -1*self.__eps*self.sigma*rate*selfKelv**4
        print(amtheat)
        self.heatup(amtheat,dt)
        return amtheat
    
    def save(self)->None:
        self.__hstlst.append(self.__kelv)
