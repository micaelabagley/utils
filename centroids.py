#! /usr/bin/env python
import numpy as np
try:
    from astropy.modeling import models,fitting
except:
    print 'astropy.modeling module not installed'
    exit()

class Centroids():

    def __init__(self, im, coords_init, size, sig_init):
        self.im = im
        self.x_init = coords_init[0]
        self.y_init = coords_init[1]
        self.size = size
        self.sig_x = sig_init[0]
        self.sig_y = sig_init[1]


    def gauss_centroid(self):
        '''Find centroid of psf by fitting a 2D Gaussian'''
        fitter = fitting.LevMarLSQFitter()

        # get initial guesses for the parameters
        sz = self.size
        amplitude = np.max(self.im[self.y_init-sz:self.y_init+sz, 
                                   self.x_init-sz:self.x_init+sz])

        g_init = models.Gaussian2D(amplitude, self.x_init, self.y_init, 
                                   self.sig_x, self.sig_y)

        # get indices of subsection of image
        x,y = np.mgrid[self.x_init-sz:self.x_init+sz, 
                       self.y_init-sz:self.y_init+sz]

        p = fitter(g_init, x, y, self.im[self.x_init-sz:self.x_init+sz, 
                                         self.y_init-sz:self.y_init+sz])

        cenx = p.x_mean.value
        ceny = p.y_mean.value

        return cenx,ceny
