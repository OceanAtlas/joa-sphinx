# Reid/Mantyla Section Data

## Data Downloads

* {download}`Reid/Mantyla Section Data in NOAA SD2 ASCII Format <nodc_sd2.7z>`
* {download}`Reid/Mantyla Section Data in JOA binary Format <joa.7z>`

## Description
Over nearly 30 years (roughly 1960-1990), Scripps Institution of Oceanography Professor Joseph L. Reid sifted data archives and contacted colleagues to assemble the best available data from each region of the World Ocean (except for the Arctic). These pre-WOCE (pre-1990s) data represent the state of knowledge of the characteristics of the waters of the deep ocean during that era.

His intended purpose was to make maps of water properties (which he used to great effect in his many publications), not vertical sections, and so he cut off stations from a cruise where a better (better for his purposes) cruise overlapped it. He also made corrections to many of the data for known offsets (mostly to salinity to correct for standard seawater batch offsets).

We have prepared ≈2200 mostly pre-WOCE (pre-1990’s) vertical sections assembled from the original data files contributing to the Reid collection. Here we went into the NOAA NODC (now NOAA NCEI) files and retrieved the entire cruise data set for each cruise used, assembled the stations into sensible vertical sections, applied the same corrections Joe used, and then we culled many bad data values. 

The data sets all include temperature and salinity, nearly all have dissolved oxygen data, and most have nutrient (NO3, PO4, and/or SiO3) data. The data are available in JOA binary and also in an NODC plain text data format called “SD2”. NODC no longer delivers data in SD2 format, but the JOA application will import/read any of these text data files if one changes the suffix from .txt to .sd2.

The data files all 2200+ sections are in zipped directories in both NODC SD2 ASCII and JOA binary. We list the individual file descriptions here, and suggest locating files of interest from searching the directories after downloading.

```{note} The oxygen and nutrient data in the Reid data collection are in volume units (numerically only ≈2.6% adjustment for nutrients but a factor of ≈45x for dissolved oxygen). To convert from O2 in ml/l to O2 in μmol/kg multiply by 44.660 and divide by density in CGS. [There is a small issue regarding what density to use, but it gets buried in the decimal place weeds. It is best to use sigma-0, i.e. (1000 + sigma0)/1000 in CGS.] To convert from nutrients in μmol/l to μmol/kg divide by density in CGS. Use sigma-0 for the nutrient conversion. See the document [O2 in volume units to O2 in mass units](../../outreach/projects/o2.md) in the JOA Suite (URL: https://joa.ucsd.edu; see Outreach --> Projects & Methods) for instructions on how to use JOA to convert oxygen and nutrient data from volume units to mass units, required for direct comparisons with data from cruises where those parameters are expressed in mass units (most cruises since 1990).
```

```{todo}
Link to O2 mass units page
```

```{toctree}
:maxdepth: 2

Atlantic/entire
Indian/entire
Pacific/entire
```