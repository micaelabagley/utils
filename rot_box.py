#! /usr/bin/env python
import pyfits
import os
import numpy as np
from matplotlib.path import Path


def get_theta(xx, yy):
    '''Determine the rotation angle of a rectangle'''
    # get difference between (x1,y1) and (x4,y4)
    deltax = xx[2] - xx[3]
    deltay = yy[2] - yy[3]
    # arctan2 should choose the quadrant correctly
    theta = np.arctan2(deltay, deltax)
    return theta


def get_region_box(xx, yy):
    '''Transform a box into a 'Path' '''
    # get rotation angle in radians
    theta = get_theta(xx, yy)
    
    box = np.array([[xx[0],yy[0]], [xx[1],yy[1]], [xx[2],yy[2]], 
                    [xx[3],yy[3]], [xx[0],yy[0]]])

    # rotation array
    rot = np.array([[np.cos(theta),np.sin(theta)],
                    [-np.sin(theta),np.cos(theta)]])
     
    tbox = [np.dot(x,rot) for x in box]
    tbox = np.array([[x,y] for x,y in tbox])

    path = Path(tbox, closed=True)
    return path


def get_region_box(xx, yy):
    '''Transform a box into a 'Path' '''
    # get rotation angle in radians
    theta = get_theta(xx, yy)

    box = np.array([[xx[0],yy[0]], [xx[1],yy[1]], [xx[2],yy[2]],
                    [xx[3],yy[3]], [xx[0],yy[0]]])

    path = Path(box, closed=True)
    return path


def make_masks():
    ''' '''
    paths = []
    for reg in r:
        paths.append(get_region_box())

    mask = np.array([True if path.contains_point([x,y]) else False for x,y in np.ndindex(shape)])

    im[np.where(mask)] = 0.0
