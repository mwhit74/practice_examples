#Weight of the Atmosphere
import math
import sys
sys.path.append('F:\Programming\Python\Practice_Examples\linuxtopia_python\Class')
from loop_functions import cont

#define constants
Po = 1.01325E5 # newton/m^2; air pressure at sea level
g = 9.82 # meter/sec^2; mass of air per square meter
r = 6.37E6 # meter; radius of earth
m = 28.69E-3 # kg/mol; molecular weight of air
R = 8.134 # joule/deg*Kmol; gas constant


def mass_air(Po,g):
	mass_air = Po*g
	return mass_air
def area_sphere(r):
	a = 4*math.pi*pow(r,2)
	return a
def mass_atm(Po,g,a):
	mass_atmos = Po*g*a
	return mass_atmos
def elev_press(Po,m,g,R,T,z):
	elevation_pressure = Po*pow(math.e,(-(m*g/(R*T))*z))
	return elevation_pressure
def elev_mass(Po,g,A,P):
	elevation_mass = Po*g*A+P*g*A
	return elevation_mass

input("Calculate the mass of the atmosphere?")

m_air = mass_air(Po,g)
A_sphere = area_sphere(r)
m_atmos = mass_atm(Po,g,A_sphere)

answer = "The mass of the atmosphere is %d." % m_atmos
print(answer, "\n")

print("What is the mass of the atmosphere at your altitude?")
z = int(input("Elevation above sea level? (m): "))
C = int(input("Temperature at your eleveation in Celcius?: "))

T = 273 + C # deg Kelvin; convert deg Celcius to deg Kelvin

P1 = elev_press(Po,m,g,R,T,z)
M1 = elev_mass(Po,g,A_sphere,P1)

print(M1)



	