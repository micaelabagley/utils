# utils README #

A package of modules common to and useful for all projects 

### Repo Contents ###

* `match_cats.py` - Match a catalog of RA and Dec to a reference catalog
    * Input: 
        * `RA`, `Dec` of catalog to be matched
        * `refRA`, `refDec` of reference catalog
    * Returns:  
        * `idx` - the indices of the reference catalog that match each source in the input catalog
        * `sep2d` - the on-sky separation between each source's closest match (in arcsec)

* * *

* `opt_hist.py` - Calculate the optimal bin size for histogrammed data
    * Options:
        * `scotts_bins` -  Use Scott's rule to determine bin size. Best for random samples of normally distributed data
        * `freedman_diaconis_bins` - Use Freedman-Diaconis rule to determine bin size. The interquartile range (IQR) is less sensitive to outliers
    * Input:
        * `data` - array of values to be binned
    * Return:
        * `binsize` - the optimal bin size
        * `nbins` - the number of bins of this size spanning the range of `data`
        * `bins` - the array of bins

* * *

* `centroids.py` - `Centroids`, Class for different centroiding algorithms
    * Options:
        * `gauss_centroid()`
    * Input:
        * `im` - image, data array
        * `coords_init` - array of initial guesses for centroid positions, [x_init, y_init]
        * `size` - centroid is fit over a (2*size)^2 subsection of the image 
        * `sig_init` - array of initial guesses for sigma, [sig_x, sig_y]
    * Returns:
        * `cenx`, `ceny` - centroid x,y positions