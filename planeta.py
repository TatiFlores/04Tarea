#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

G = 1
M = 1
m = 1


class Planeta(object):
    '''
    Contiene las posiciones y velocidades de un Planeta, la ecuacion de
    movimiento de este, y los metodos de rnge Kutta 4, Euler y Verlet que
    avanzan 1 paso. Tambien s calcula la energia del planeta dada sus
    condiciones actuales
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
        f = G * M * (2. * a / r**4 - 1. / r**3)
        fx = f * x
        fy = f * y
        return np.array([vx, vy, fx, fy])

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        y_anterior = np.copy(self.y_actual)
        self.y_actual = y_anterior + dt * self.ecuacion_de_movimiento()
        self.t_actual += dt
        pass

    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        y_anterior = np.copy(self.y_actual)
        k1 = dt * self.ecuacion_de_movimiento()

        self.y_actual = y_anterior + k1 / 2.
        k2 = dt * self.ecuacion_de_movimiento()

        self.y_actual = y_anterior + k2 / 2.
        k3 = dt * self.ecuacion_de_movimiento()

        self.y_actual = y_anterior + k3
        k4 = dt * self.ecuacion_de_movimiento()

        self.y_actual = y_anterior + (k1 + 2 * k2 + 2 * k3 + k4)/6.
        self.t_actual += dt
        pass

    def avanza_verlet(self, dt, y_anterior):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        x_ant, y_ant, vx_ant, vy_ant = y_anterior
        x, y, vx, vy = self.y_actual
        vx, vy, fx, fy = self.ecuacion_de_movimiento()

        x_desp = 2 * x - x_ant + dt**2 * fx
        y_desp = 2 * y - y_ant + dt**2 * fy
        vx_desp = (x_desp - x_ant) / (2. * dt)
        vy_desp = (y_desp - y_ant) / (2. * dt)

        self.y_actual = np.array([x_desp, y_desp, vx_desp, vy_desp])
        self.t_actual += dt

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        x, y, vx, vy = self.y_actual
        r = np.sqrt(x**2 + y**2)
        k = m * (vx**2 + vy**2)/2.
        u = - G * M * m / r + self.alpha * G * M * m / r**2
        energia_actual = k + u
        return energia_actual
