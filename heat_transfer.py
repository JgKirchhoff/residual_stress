# Joseph Kirchhoff
# 11-21-2022
# Code built for through thickness heat transfer
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

v_p = 400 #mm/s - Velocity 
x_l = 10 #mm - Heating length
t_l = x_l/v_p # s - Irradiation times
t_l = 1.5 # seconds
w_tape = 6.35 #mm - Tape Width
p_l = 100 #W - Laser Power
q0 =  p_l/(x_l*w_tape) #W/mm^2 - Heat Flux

alpha = 0.32 #mm^2/s
k_z = 0.66/1000 #W/mk

Tm = 343 #C
Tp = 370 #C
Td = 550 #C
T0 = 20 #C <- Set this equal to mold temperature

# Plotting heat penetration depth for irradiation
# time = np.linspace(0.01,1,20) #seconds
# T_list = []
# for t in time:
#     z = 0
#     for z in z_steps:
#         calc = T0 + ((2*q0)/k_z)*math.sqrt(alpha)*math.sqrt(t)*ierfc(z/math.sqrt(4*alpha*t)) #heat penetration
#         velocity = x_l/t
#         T_list.append([z,t,calc])

# df = pd.DataFrame(T_list,columns=['z (mm)','irradiation time (seconds)','temp (C)']) #heat penetration
# fig = px.scatter(df, x="z (mm)",y="temp (C)",color="irradiation time (seconds)",title="heat penetration per irradiation time",color_continuous_scale='Inferno') #heat penetration
# fig.update_layout(legend=dict(title_font_family="Times New Roman",
#                               font=dict(size= 10)))
# #if not os.path.exists("/images"):
#  #   os.mkdir("/images")

# #fig.show()
# fig.write_image("res_stress/images/heatpenetration_vs_irradiation.eps")


# # Plotting velocity with heat penetration
# time = np.linspace(0.01,1,20) #seconds
# T_list = []
# for t in time:
#     z = 0
#     for z in z_steps:
#         calc = T0 + ((2*q0)/k_z)*math.sqrt(alpha)*math.sqrt(t)*ierfc(z/math.sqrt(4*alpha*t)) #heat penetration
#         velocity = x_l/t
#         T_list.append([z,str(round(velocity,4)),calc])

# df = pd.DataFrame(T_list,columns=['z (mm)','velocity (mm/seconds)','temp (C)']) #heat penetration
# fig = px.scatter(df, x="z (mm)",y="temp (C)",color="velocity (mm/seconds)",title="heat penetration per velocity",color_continuous_scale='Inferno') #heat penetration
# fig.update_layout(legend=dict(title_font_family="Times New Roman",
#                               font=dict(size= 10)))
# #if not os.path.exists("/images"):
#  #   os.mkdir("/images")

# fig.show()
# fig.write_image("res_stress/images/heatpenetration_vs_velocity.eps")

# Heat Penetration, Constant Velocity, Changing Power
time = np.linspace(0.01,1,20) #seconds
T_list = []
for t in time:
    z = 0
    for z in z_steps:
        calc = T0 + ((2*q0)/k_z)*math.sqrt(alpha)*math.sqrt(t)*ierfc(z/math.sqrt(4*alpha*t)) #heat penetration
        velocity = x_l/t
        T_list.append([z,t,calc])

df = pd.DataFrame(T_list,columns=['z (mm)','irradiation time (seconds)','temp (C)']) #heat penetration
fig = px.scatter(df, x="z (mm)",y="temp (C)",color="irradiation time (seconds)",title="heat penetration per irradiation time",color_continuous_scale='Inferno') #heat penetration
fig.update_layout(legend=dict(title_font_family="Times New Roman",
                              font=dict(size= 10)))
#if not os.path.exists("/images"):
 #   os.mkdir("/images")

#fig.show()
fig.write_image("res_stress/images/heatpenetration_vs_irradiation.eps")