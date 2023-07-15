from numpy import cos, pi, arcsin, sin, tan, exp
from Layer import Layer


def beta(thickness, wave_length, N_j, theta_j):
        '''
        Returns beta of jth layer
        '''
        return ((2*pi*thickness)/wave_length) * N_j * cos(theta_j)

def complex_refractive_index(n, k):
    '''
    Returns complex refractive index based on n and k

    Note:
        in some cases + and - are changed due to differences in other formulas
    Default:
        -
    '''
    return n-1j*k

def theta_j(N_i, N_j, theta_i):
    '''
    Calculates theta angle of jth layer based on Schnells formula
    N0 sin(theta0) = N1 sin(theta1)
    '''
    
    return arcsin((N_i/N_j) * sin(theta_i))


def R_p(self, r_p):
    '''
    Returns p- reflectance but in a representative/comparative form rather than calculational
    '''
    return abs(r_p)**2
    
def R_s(self, r_s):
    '''
    Returns s- reflectance but in a representative/comparative form rather than calculational
    '''
    return abs(r_s)**2

def R_n(self, R_p, R_s):
    '''
    Returns mean value of p- and s- comparative reflectances
    
    Shown on refractiveindex.info so maybe somewhat useful
    '''
    return (R_p + R_s)/2

def rho(psi = None, delta = None, r_p = None, r_s = None):
        '''
        Probably the most important formula here calculating rho which is tan(psi) * exp(-1i*delta)
        '''
        if psi != None and delta != None:
            return tan(psi) * exp(-1j * delta)
        elif r_p != None and r_s != None:
            return r_p / r_s
        else: raise ValueError