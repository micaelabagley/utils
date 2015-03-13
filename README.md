# utils README #

A package of modules common to and useful for all projects 

### Repo Contents ###

* ```match_cats.py``` - Match a catalog of RA and Dec to a reference catalog

>Input: 

>> * `RA`, `Dec` of catalog to be matched

>> * `refRA`, `refDec` of reference catalog

>Returns:  

>> * the indices of the reference catalog that match each source in the input catalog

>> * the on-sky separation between each source's closest match in arcsec
