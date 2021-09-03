# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 23:25:58 2021

@author: Usuario
"""

p= float(input('digite el valor de la presion:'))
v=float(input('digite el valor del volumen:'))
t=float(input('digite el valor de la temperatura:'))
m=(p*v)/(0.37*(t+460))
print(f"El valor de masa es: {m}")