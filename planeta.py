#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

G=1
M=1

class Planeta(object):
    '''
    Complete el docstring.
    '''

    def __init__(self, condicion_inicial, alpha=0):
        '''
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.

        Ej. de uso:
        >> mercurio = Planeta([x0, y0, vx0, vy0])
        >> print(mercurio.alpha)
        >> 0.
        '''
        self.y_actual = condicion_inicial
        self.t_actual = 0.
        self.alpha = alpha

    def ecuacion_de_movimiento(self):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        '''
        x, y, vx, vy = self.y_actual
        a = self.alpha
        r = np.sqrt(x**2 + y**2)
        f = G * M * (2. * a / r**4 - 1. / r**3 + )
        fx = f * x
        fy = f * y
        return [vx, vy, fx, fy]

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        y_anterior = self.y_actual
        self.y_actual = y_anterior + dt * ecuacion_de_movimiento()
        self.t_actual +=dt


    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        y_anterior = np.copy(self.y_actual)
        k1 = dt * ecuacion_de_movimiento()
        self.y_actual = y_anterior + k1 / 2.
        k2 = dt * ecuacion_de_movimiento()  
        self.y_actual = y_anterior + k2 / 2.
        k3 = dt * ecuacion_de_movimiento()
        self.y_actual = y_anterior + k3
        k4 = dt * ecuacion_de_movimiento()

        self.y_actual = y_anterior + (k1 + 2 * k2 + 2 * k3 + k4)/6.
        self.t_actual +=dt

    def avanza_verlet(self, dt):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        pass
