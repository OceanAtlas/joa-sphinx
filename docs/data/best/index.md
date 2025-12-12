# Best CTD/Hydrographic Data

## About the 'Best CTD/Hydrographic Data' collection
The collection 'Best CTD/Hydrographic Data' contains the finest-quality vertical section data yet obtained from the World Ocean, sourced from WOCE, CLIVAR, GO-SHIP and other programs of similar focus and quality. We have curated and ‘cleaned’ the data (see below), adding value by organizing sections, combining and deleting casts, and correcting errors. No data values are changed.

Grooming (‘cleaning’) bottle data from the WOCE/CLIVAR/GO-SHIP transects makes them more readily used by students and others who prefer to not deal with quality codes, out-of-sequence data, and parameter/units differences between files. The cleaned vertical section data - data files with the word 'clean' in the file name - are ready for instant use in Ocean Data View (ODV), Java OceanAtlas (JOA), and other applications which read csv/ascii data (e.g., Matlab, spreadsheets). 

:::{important}
The cleaned data collection will soon move to the UCSD digital archive:

> Swift, James H. [additional authors to be determined]  (2026). Quality Edited Vertical Ocean Section and Gridded Hydrographic Data. UC San Diego Library Digital Collections. Dataset. https://doi.org/10.6075/J0K074P0
:::

## What do we mean by the term ‘cleaned data’?

Data files with ‘clean’ in the file name were downloaded from the CCHDO (https://cchdo.ucsd.edu) and then groomed as follows:

*	Bottle data parameters, columns and headers were rectified to a specified set and order.
*	Duplicate bottles and bottles with little/no data from oxygen or nutrient analyses were discarded.
*	Data which were quality coded bad or uncertain were eliminated.
*	Where there were multiple casts at a single station (or a single location with multiple stations), the ones which comprised the most nearly complete profile were combined into a single vertical profile.
*	Transects were sorted with south-to-north or west-to-east orientation.
*	Where it took several cruises to cover one transect, the data were combined.
*	Overlapping or off-transect data were eliminated; data relevant to the section were retained.

No measured data values were changed. In a few cases errors or omissions in station metadata such as position or depth to bottom were corrected.

The JOA Suite data library also includes exact-matched section segments – carefully curated data from the same sub-basin or path from different years.

```{toctree}
:maxdepth: 2

pacific
atlantic
indian
southern
arctic
```