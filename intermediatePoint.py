"""
Use begin and end node with 2 angles, to calculate the intermediate point
for the Quadratic bezier curve

UM-CNRS LIRMM
Jihong Zhu
2019.04.04

"""
# initialize 4 parameters 
import numpy as np
node_begin = np.array([0.0, 0.0]).reshape(2,1)
node_end = np.array([1.0, 0.0]).reshape(2,1)
theta_begin = np.pi / 2; 
theta_end = np.pi * 5 / 6;

# caculate intermediate point
def intermedPointCal(node_begin, node_end, theta_begin, theta_end):
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
        '''
        # test the calculation (it is correct if y2 = y)
        y2 = np.tan(theta_begin) * (x - a) + b
        print y, y2
        '''
        intermediatePiont = np.array([x, y]).reshape(2,1)
    return intermediatePiont

node = intermedPointCal(node_begin, node_end, theta_begin, theta_end)
print node

