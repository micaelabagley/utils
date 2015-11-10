#! /usr/bin/env python
import argparse
import numpy as np


class Thing():
    def __init__(self, n, happy, prime, verbose):
        self.status = ''

        if (not happy) & (not prime):
            happy = True
            prime = True

        try: 
            int(n)
        except ValueError:
            print '\nNumber must be an integer. Flooring %s' % n
            n = str(int(float(n)))

        if int(n) < 1:
            print '\nNumber must be positive'
            exit()

        print '\n%s:' % n
        if (happy & prime):
            self.is_happy(n, verbose=verbose)
            self.status += ' '
            self.is_prime(n)
        elif (happy) & (not prime):
            self.is_happy(n, verbose=verbose)
        elif (prime) & (not happy):
            self.is_prime(n)


    def is_happy(self, n, verbose=False):
        """ """
        if int(n) <= 0:
            print 'Gots to be positive, fucker'
            exit()

        if verbose:
            print '  %s' % n

        if n == '1':
            self.status += 'happy'
        elif n == '4':
            self.status += 'sad'
        else:
            tot = 0
            for dig in n:
                tot += int(dig)**2
            self.is_happy(str(tot), verbose)


    def is_prime(self, n):
        """ """
        n = int(n)
        if n == 1:
            self.status += 'one'
        elif n <= 3:
            self.status += 'prime'
        elif (n % 2 == 0) | (n % 3 == 0):
            self.status += 'composite'
        else:
            k = 5
            while k*k <= n:
                if n % k == 0:
                    self.status += 'composite'
                    return
                k += 1
            self.status += 'prime'


    def __str__(self):
        return self.status

    def __repr__(self):
        return str(self)


def main():
    parser = argparse.ArgumentParser(description=
        '')
    parser.add_argument('number', type=str, help='')
    parser.add_argument('--prime', '-p', action='store_true',
        help='')
    parser.add_argument('--happy', '-f', action='store_true',
        help='')
    parser.add_argument('--verbose', '-v', action='store_true',
        help='')
    args = parser.parse_args()

    T = Thing(args.number, args.happy, args.prime, args.verbose)
    print T


if __name__ == '__main__':
    main()

