# Joseph Kirchhoff
# 11-21-2022
# Code built for through thickness heat transfer - upon cooling
# The heat transfer in the tape and substrate are accounted for

import math
import numpy as np
import plotly.express as px
import pandas as pd
import os

def ierfc(x):
    return (1/math.sqrt(math.pi))*math.exp(-x**2) - x*math.erfc(x)

# Initialize Variables
t_tape = 0.125 #just a single tape thickness
t_substrate = 10*t_tape #make it 10 layers thick
z_steps = np.linspace(0,t_substrate,100) #z interval

v_p = 50 #mm/s - Velocity 
x_l = 10 #mm - Heating length
t_l = x_l/v_p # s - Irradiation times
w_tape = 6.35 #mm - Tape Width
p_l = 100 #W - Laser Power
q0 =  p_l/(x_l*w_tape) #W/mm^2 - Heat Flux

alpha = 0.32 #mm^2/s
k_z = 0.66/1000 #W/mk

Tm = 343 #C
Tp = 370 #C
Td = 550 #C
T0 = 20 #C <- Set this equal to mold temperature


# Tool temperature heat penetration
tool_temp = np.linspace(20,200,20) #C
time = t_l + np.linspace(0.01,3,25) #seconds

T_list = []
for t in time:
    z = 0
    for z in z_steps:
        # c1 = c2 = 0
        # for i in range(100):
        #     c1 = c1 + ierfc((2*t_substrate*i+z)/(4*alpha*t)) + ierfc((2*t_substrate*(i+1)-z)/(4*alpha*t))
        # for i in range(100):
        #     c2 = c2 + ierfc((2*t_substrate*i+z)/(4*alpha*(t-t_l))) + ierfc((2*t_substrate*(i+1)-z)/(4*alpha*(t-t_l)))
        # calc = T0 + ((2*q0)/k_z)*math.sqrt(alpha)*(math.sqrt(t)*c1 - math.sqrt(t-t_l)*c2)
        calc = T0 + ((2*q0)/k_z)*math.sqrt(alpha)*(ierfc(z/(2*math.sqrt(alpha*t)))*math.sqrt(t) - ierfc(z/(2*math.sqrt(alpha*(t-t_l))))*math.sqrt(t-t_l))
        T_list.append([z,t-t_l,calc])

df = pd.DataFrame(T_list,columns=['z (mm)','cooling time (seconds)','temp (C)']) #heat penetration
fig = px.scatter(df, x="z (mm)",y="temp (C)",color="cooling time (seconds)",title="upon cooling 50mm/s 100 W T0=20",color_continuous_scale='Inferno') #heat penetration
fig.update_layout(legend=dict(title_font_family="Times New Roman",
                              font=dict(size= 10)))
#if not os.path.exists("/images"):
 #   os.mkdir("/images")

#fig.show()
fig.write_image("res_stress/images/uponCooling.eps")