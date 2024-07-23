# Reid/Mantyla Section Data

## Data Downloads

* {download}`Reid/Mantyla Section Data in NOAA SD2 Format <reid_data/nodc_sd2.7z>`
* {download}`Reid/Mantyla Section Data in JOA <reid_data/joa.7z>`

## Description

We have prepared ≈2200 mostly pre-WOCE (pre-1990's) vertical sections assembled from the original NODC data files contributing to SIO Professor Joseph L. Reid's World Ocean data collection.
From cruises in NODC archives, and some newer cruises originally from colleagues, over more than two decades Joe sifted for the best available data from each region of the World Ocean (except for the Arctic).
His intended purpose was to make maps of water properties (which he used to great effect in his many publications), not vertical sections, and so he cut off stations from a cruise where a better (better for his purposes) cruise overlapped it.
He made corrections to many of the data for known offsets (mostly standard seawater batch offsets).
Here we went into the NODC files and retrieved the entire cruise data set for each cruise Joe used, assembled the stations into sensible vertical sections, applied the same corrections Joe used, and then we culled many bad data values.
The resulting 2200 sections represent the basic data knowledge of the deep ocean basins prior to the 1990s.
The data sets all include temperature and salinity, nearly all have dissolved oxygen data, and most have nutrient (NO3, PO4, and/or SiO3) data.
The data are available in JOA binary and also in an NODC text data format called "SD2".
NODC no longer delivers data in SD2 format, but the JOA application will import/read any of these text data files if one changes the suffix from .txt to .sd2.

```{note} The oxygen and nutrient data in the Reid data collection are in volume units (numerically only ≈2.6% adjustment for nutrients but a factor of ≈45x for dissolved oxygen).
To go from O2 in ml/l to O2 in μmol/kg multiply by 44.660 and divide by density in CGS.
[There is a small issue regarding what density to use, but it gets buried in the decimal place weeds.
It is best to use sigma-0, i.e. (1000 + sigma0)/1000 in CGS.]
To go from nutrients in μmol/l to μmol/kg divide by density in CGS.
Use sigma-0 for the nutrient conversion.
See the document "O2 in volume units to O2 in mass units.pdf" for instructions on how to use JOA to convert oxygen and nutrient data from volume units to mass units, required for direct comparisons with data from cruises where those parameters are expressed in mass units.
```

## Atlantic Ocean Data File Descriptions
```{include} reid_data/_reid_atlantic.md
```
## Indian Ocean Data File Descriptions
```{include} reid_data/_reid_indian.md
```
## Pacific Ocean Data File Descriptions
```{include} reid_data/_reid_pacific.md
```

