from numpy import deg2rad
from Methods import *

class Layer:
    def __init__(self, complex_refractive_indexes: list[tuple], incidence_angle: float) -> None:
        self.complex_refractive_indexes = [(1,0)]
        self.complex_refractive_indexes.extend(complex_refractive_indexes)

        self.incidence_angles = [deg2rad(incidence_angle),
                                 theta_j(N_i=self.complex_refractive_indexes[0],
                                         N_j=self.complex_refractive_indexes[1],
                                         theta_i=self.incidence_angles[-1])]

    
    def r_p(self):
        '''
        Returns p- reflectance of layer
        Fresnells formula
        '''

        nominator = (self.complex_refractive_indexes[1] * cos(self.incidence_angles[0]) - self.complex_refractive_indexes[0] * cos(self.incidence_angles[1]))
        denominator = (self.complex_refractive_indexes[1] * cos(self.incidence_angles[0]) + self.complex_refractive_indexes[0] * cos(self.incidence_angles[1]))

        return nominator / denominator

    def r_s(self):
        '''
        Returns s- reflectance of layer
        Fresnells formula
        '''

        nominator = (self.complex_refractive_indexes[0] * cos(self.incidence_angles[0]) - self.complex_refractive_indexes[1] * cos(self.incidence_angles[1]))
        denominator = (self.complex_refractive_indexes[0] * cos(self.incidence_angles[0]) + self.complex_refractive_indexes[1] * cos(self.incidence_angles[1]))

        return nominator / denominator