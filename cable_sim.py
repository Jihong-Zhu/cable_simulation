# -*- coding: utf-8 -*-
"""
Bezier curve simulation of a flexible cable

UM-CNRS LIRMM
Jihong Zhu
2019.04.04

"""
import numpy as np
import bezier # for bezier curve
import matplotlib.pyplot as plt

def intermedPointCal(node_begin, node_end, theta_begin, theta_end):
    # Given begin and end point of the bezier curve, the tangent angle of each
    # point, calculate the intermediate point of the quadratic bezier curve
    # thete_begin and theta_end can not add up to pi (parallel)
    if (np.absolute(theta_begin - theta_end) < 10 ** -3):
        raise ValueError
    else:
        a = node_begin[0];
        b = node_begin[1];
        c = node_end[0];
        d = node_end[1];
        x = (a * np.tan(theta_begin) - c * np.tan(theta_end) + d - b) / \
        (np.tan(theta_begin) - np.tan(theta_end))
        if (x - c == 0):
            y = np.tan(theta_begin) * (x - a) + b
        else:
            y = np.tan(theta_end) * (x - c) + d
        intermediatePiont = np.array([x, y]).reshape(2,1)
    return intermediatePiont
# import seaborn
# Quadratic bezier curve
pose = np.genfromtxt('hand_pose.txt', delimiter = ' ')
node_begin = pose[0, 0 : 2].reshape(2,1)
node_end = pose[1, 0 : 2].reshape(2,1)
theta_begin = pose[0,2]
theta_end = pose[1,2]
node_intermediate =  intermedPointCal(node_begin, node_end, theta_begin, \
theta_end)
nodes = np.concatenate((node_begin, node_intermediate, node_end), axis = 1)
nodes_bezier = np.asfortranarray(nodes)
curve_current = bezier.Curve(nodes_bezier, degree = 2) 
'''
nodes = np.genfromtxt('data.txt', delimiter = ' ')
# for bezier curve
nodes = nodes.T  
nodes_bezier = np.asfortranarray(nodes)
bezier_current = nodes_bezier[:, 0:3]
bezier_target = nodes_bezier[:, 3:7]
curve_current = bezier.Curve(bezier_current, degree = 2) 
curve_target = bezier.Curve(bezier_target, degree = 2)
# instead of defining 3 points, we define 2 points and 2 angles
# This resembles real human manipulation

'''
# plot current and target shape
current = curve_current.plot(num_pts = 256)
# _ = curve_target.plot(num_pts = 256, ax = current) # use _ variable to hold
# _ = current.axis('scaled')
# _ = current.set_xlim(-0.125,1.5)
# _ = current.set_ylim(-0.125, 1)
# current.legend(['current shape','target shape'])