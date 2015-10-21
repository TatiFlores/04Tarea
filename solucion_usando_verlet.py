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
vx = np.zeros(iteraciones)
vy = np.zeros(iteraciones)
energia = np.zeros(iteraciones)
tiempo = np.zeros(iteraciones)

x[0] = p.y_actual[0]
y[0] = p.y_actual[1]
energia[0] = p.energia_total()
tiempo[0] = p.t_actual
vx[0] = p.y_actual[2]
vy[0] = p.y_actual[3]

#Verlet necesita una iteracion extra
p.avanza_rk4(dt)
x[1] = p.y_actual[0]
y[1] = p.y_actual[1]
energia[1] = p.energia_total()
tiempo[1] = p.t_actual
vx[1] = p.y_actual[2]
vy[1] = p.y_actual[3]

for i in range(2, iteraciones):
    y_anterior = np.array([x[i-2], y[i-2], vx[i-2], vy[i-2]])
    p.avanza_verlet(dt, y_anterior)
    x[i] = p.y_actual[0]
    y[i] = p.y_actual[1]
    vx[i] = p.y_actual[2]
    vy[i] = p.y_actual[3]
    energia[i] =p.energia_total()
    tiempo [i] = p.t_actual

plt.figure(1)
plt.clf()
plt.plot(x,y,color='green')
plt.xlabel('x[m]')
plt.ylabel('y[m]')
plt.grid(True)
plt.title(' 'u'Ó''rbita calculada con el m'u'é''todo de Verlet ')
plt.savefig('Orbita_verlet.eps')

plt.figure(2)
plt.clf()
plt.plot(tiempo,energia,'green')
plt.xlabel('Tiempo [s]')
plt.ylabel('Energ'u'í''a')
plt.grid(True)
plt.title(' Energ'u'í''a en funci'u'ó''n del tiempo, m'u'é''todo de Verlet ')
plt.savefig('Energia_verlet.eps')

plt.show()
