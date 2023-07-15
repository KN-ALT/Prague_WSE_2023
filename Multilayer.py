from Layer import Layer
from Methods import *

class Multilayer:
    def __init__(self, layers: list[Layer]) -> None:
        self.layers = layers

        self.complex_refractive_indexes = [(1,0)]

        for layer in self.layers:
            self.complex_refractive_indexes.append(layer.complex_refractive_indexes[1])
        
        self.incidence_angles = [layers[0].incidence_angles[0]]

        for i in range(len(self.complex_refractive_indexes)-1):
            self.incidence_angles.append(theta_j(N_i=self.complex_refractive_indexes[i],
                                                 N_j=self.complex_refractive_indexes[i+1],
                                                 theta_i=self.incidence_angles[-1]))
            
    def reflectance(self):
        