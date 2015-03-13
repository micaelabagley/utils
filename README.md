# utils README #

A package of modules common to and useful for all projects 

### Repo Contents ###

* ```match_cats.py``` - Match catalogs by RA and Dec.
>>Input: `RA`, `Dec` of catalog to be matched
>>> `refRA`, `refDec` of reference catalog
>>Returns:  
>>>(1) the indices of the reference catalog that match each source in the input catalog
>>>(2) the on-sky separation between each source's closest match in arcsec


=====

```match_cats.py``` - Match catalogs by RA and Dec.
                      Return 
                      1) the indices of the reference catalog that match 
                      each source in the input catalog, and 
                      2) the on-sky separation between each source's 
                      closest match in arcsec"""