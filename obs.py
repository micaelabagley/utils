#! /usr/bin/env python
import numpy as np

def sex_to_deg(RA, DEC):
    '''
    INPUT
    RA  = string of form: 'hh:mm:ss.ss'
    DEC = string of form: '[+/-]dd:mm:ss.ss'

    OUTPUT
    RA = right ascension, decimal degrees [float]
    DEC = declination, decimal degrees [float]
    '''
    # parse the strings
    h,rm,rs = [float(x) for x in RA.split(':')]
    d,dm,ds = [float(x) for x in DEC.split(':')]
    decimalRA = 15.*(h + rm/60. + rs/3600.)
    # Dec is tricky if < 0 degrees
    if d == 0.0:
        if DEC[0] == '-':
            decimalDEC = -1.0 * (np.abs(d) + dm/60. + ds/3600.)
        else: 
            decimalDEC = d + dm/60. + ds/3600.
    else:
        decimalDEC = np.sign(d) * (np.abs(d) + dm/60. + ds/3600.)

    return decimalRA, decimalDEC


def deg_to_sex(RA, Dec):
    '''
    INPUT
    RA = right ascension, decimal degrees [float]
    DEC = declimation, decimal degrees [float]

    OUTPUT
    RA = string of form: 'hh:mm:ss.ss'
    DEC = string of form: '[+/-]dd:mm:ss.ss'
    '''
    # RA
    rm,rs = divmod(RA/15.*3600., 60.)
    h,rm = divmod(rm, 60.)
    # Dec
    dm,ds = divmod(np.abs(Dec)*3600., 60.)
    d,dm = divmod(dm, 60.)
     
    # format strings
    strRA = '%02d:%02d:%2.2f' % (int(h), int(rm), rs)
    if np.sign(Dec) == -1.0:
        if d == 0.0:
            strDec = '-%02d:%02d:%2.2f' % (int(d), int(dm), ds)
        else:
            strDec = '%03d:%02d:%2.2f' % (int(np.sign(Dec)*d), int(dm), ds)
    else:
        strDec = '%02d:%02d:%2.2f' % (int(np.sign(Dec)*d), int(dm), ds)

    return strRA, strDec


def main():
    # convert to decimal
    degRA,degDec = sex_to_deg(RA, Dec)
    # convert to segessimal
    sRA,sDec = deg_to_sex(RA2000,Dec2000)


if __name__ == '__main__':
    main()
