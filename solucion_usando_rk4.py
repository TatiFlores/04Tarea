#!/usr/bin/env python
# -*- coding: utf-8 -*-

from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt


condicion_inicial = [10, 0, 0, 0.4]

p = Planeta(condicion_inicial)

dt = 0.1
iteraciones = 60000
x = np.zeros(iteraciones)
y = np.zeros(iteraciones)
energia = np.zeros(iteraciones)
tiempo = np.zeros(iteraciones)

for i in range(iteraciones):
    p.avanza_rk4(dt)
    x[i] = p.y_actual[0]
    y[i] = p.y_actual[1]
    energia[i] =p.energia_total()
    tiempo [i] = p.t_actual

plt.figure(1)
plt.clf()
plt.plot(x,y)
plt.xlabel('x[m]')
plt.ylabel('y[m]')
plt.grid(True)
plt.title(' 'u'Ó''rbita calculada con el m'u'é''todo de Rung Kutta 4 ')
plt.savefig('Orbita_rk4.eps')

plt.figure(2)
plt.clf()
plt.plot(tiempo,energia)
plt.xlabel('Tiempo [s]')
plt.ylabel('Energ'u'í''a')
plt.grid(True)
plt.title(' Energ'u'í''a en funci'u'ó''n del tiempo, m'u'é''todo de Runge Kutta 4 ')
plt.savefig('Energia_rk4.eps')

plt.show()
