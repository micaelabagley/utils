#! /usr/bin/env python
import numpy as np

def scotts_bins(data):
    '''Use Scott's rule to determine bin size.
       Best for random samples of normally distributed data
    '''
    Nsrc = data.shape[0]
    sig = np.std(data)
    binsize = 3.5*sig / Nsrc**(1./3.)
    bins = np.arange(np.min(data), np.max(data), binsize)
    nbins = bins.shape[0]
    return binsize, nbins, bins


def freedman_diaconis_bins(data):
    '''Use Freedman-Diaconis rule to determine bin size.
       The interquartile range (IQR) is less sensitive to outliers
    '''
    Nsrc = data.shape[0]
    q75,q25 = np.percentile(data, [75,25])
    iqr = q75 - q25
    binsize = 2. * iqr / Nsrc**(1/3.)
    bins = np.arange(np.min(data), np.max(data), binsize)
    nbins = bins.shape[0]
    return binsize, nbins, bins
