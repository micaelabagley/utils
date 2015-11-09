#! /usr/bin/env python
import numpy as np
from scipy import constants


def abmag_to_fnu(mag):
    """Convert an AB magnitude to flux in frequency units (fnu)"""
    return 10.**(-0.4 * (mag + 48.6))

def abmag_to_flambda(mag, wave):
    """Convert an AB magnitude to flux in Angstroms (flambda)"""
    fnu = abmag_to_fnu(mag)
    return fnu * (constants.c*1.e10) / wave**2


def main():
    pass


if __name__ == '__main__':
    main()
