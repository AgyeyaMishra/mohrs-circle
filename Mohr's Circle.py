# Author: Agyeya Mishra
# Institute: Delhi Technological University (formerly, Delhi College of Engineering)
# Language: Python
# Version: 3.x


#This script plots Mohr's Circle when given the two-dimensional state of stress. 


#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import math

#Function for Mohr's Circle
def mohrcircle():
    #Taking user input for normal stress in x-direction
    σx = float(input('Enter the value of σx = '))
    #Taking user input for normal stress in y-direction
    σy = float(input('Enter the value of σy = '))
    #Taking user input for tangetial stress in xy plane
    τxy = float(input('Enter the value of τxy = '))
    #Taking user input for stress unit
    u = input('Enter the stress unit = ')
    #Taking user input for angle (in degrees) of plane's axis from x-axis
    #Here, positive angles are considered counter clockwise
    w = float(input("Enter the angle (in degrees) of plane's axis from x axis (here, +ve angles are counter clockwise), θ = "))
    θ = math.radians(w)
    R = np.sqrt(0.25 * (σx - σy) ** 2 + (τxy) ** 2)
    σavg = (σx + σy) / 2
    ψ = np.linspace(0, 2 * np.pi, 360)
    x = σavg + R * np.cos(ψ)
    y = R * (np.sin(ψ))
    φ1 = math.degrees(0.5 * math.atan(2 * τxy / (σx - σy)))
    φ2 = φ1 + 90
    σθ1 = σavg + R * np.cos(2 * np.radians(φ1) + 2 * θ)
    σθ2 = σavg + R * np.cos(2 * np.radians(φ1) + 2 * θ + np.pi)
    τθ = R * np.sin(2 * np.radians(φ1) + 2 * θ)
    
    print(f'''
       Radius, R = √(0.25*(σx-σy)^2 + τxy^2) 
               = √(0.25*({σx}-{σy})^2 + {τxy}^2)  = {R} {u}
       Average Stress, (which acts at the Center of Mohr's Circle) 
               = σavg = (σx + σy)/2 = ({σx} + {σy})/2 = {σavg} {u}
               
       Principal Stresses:
       σ1 = σavg + R = {σavg} + {R} = {σavg + R} {u}
       σ2 = σavg - R = {σavg} - {R} = {σavg - R} {u}
       
       Angle which σ1 makes with the x-axis, 
       φ1 = 0.5(atan(2*τxy/(σx - σy)) = 0.5 * atan(2*{τxy}/({σx} - {σy})) = {φ1} degrees
       Angle which σ2 makes with the x-axis,
       φ2 = φ1 + 90 = {φ2} degrees
       
       Maximum Shear Stress = τmax = R = {R} {u}
       It occurs at, α = φ1 + 45 = {φ1 + 45} degrees
       
       Stresses at a plane with axis at θ anticlockwise from x axis, 
        σθ1 = σavg + R* Cos(2φ1 + 2θ) = {σavg} + {R}* Cos({2 * φ1 + 2 * θ})
           = {σθ1}, {u}
        σθ2 = σavg + R* Cos(2φ1 + 2θ + pi) = 
            {σθ2} {u}
        τθ = R*Sin(2*φ1 + 2*θ)  = {R * np.sin(2 * np.radians(φ1) + 2 * θ)} {u}
       ''')
   
#Plotting Mohr's Circle
    plt.plot(x, y)
    plt.plot([σavg - R - 10, σavg + R + 10], [0, 0], linestyle='--', color='black')
    plt.plot([σavg, σavg], [-R - 10, R + 10], linestyle='--', color='black')
    plt.plot([σx, σy], [-τxy, τxy], [σx, σx], [-τxy, 0], [σy, σy], [τxy, 0], linestyle='-', color='green')
    plt.xlabel('σ')
    plt.ylabel('τ')
    plt.title("Mohr's Circle")
    plt.show()

#Function Call
mohrcircle()
