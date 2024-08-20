# A Quick Review of JOA Tools Useful for Data Examination

James H. Swift, UCSD Scripps Institution of Oceanography, September 2021

This document was written to provide an overview of Java OceanAtlas (JOA) functions and capabilities useful to examine and explore data and data products available through the Java OceanAtlas Suite web site, [data homepage](../../data/index.md).

```{note}
There is a learning curve associated with use of any computer application.
It is very strongly recommended that those intending to use JOA, for example on student projects, first familiarize themselves with JOA by downloading and installing the application [](../../joa/index.md), and then working through its Guided Tour starting at [](../../joa/guided_tour/basic_features.md).
JOA users who wish to compare data files should also examine the document [](./comparing.md).
```

```{note}
This document refers to JOA features which may or may not be enabled in a given installation of JOA.
To enable a missing feature, go to Preferences, under the JOA menu, then horizontal-select-scroll right to "Feature Management" in the Configure Preferences dialog box and vertical-scroll through the list of selectable JOA features to enable a desired feature which does not show up in your present installation of JOA.
```

```{note}
Complete guides to each JOA feature are found in the JOA User Guide (https://joa.ucsd.edu/assets/documents/JOA5_userguide.pdf). (An updated User Guide is in preparation.)
```

```{todo}
Fix above user guide link
```

## JOA Preferences
If you are importing your own ascii bottle data (as opposed to data download from the JOA Suite site), be sure to examine the "Import" tab on the JOA Configure Preferences dialog box and set the choices to your liking before you import the data set.
Also, it is very strongly recommended that you refer to the JOA Guided Tour page about JOA data (https://joa.ucsd.edu/16.html) and try importing the sample file it suggests.
If a sample file imports correctly, you can compare it to your data file to look for discrepancies if your intended file fails to import correctly.

```{todo}
Fix link to guide 16 above
```

If you are importing data you downloaded from a search of NODC's World Ocean Database (WOD; see <https://www.ncei.noaa.gov/access/world-ocean-database-select/dbsearch.html>), please examine the "WOD Select Import Options" tab on the JOA Configure Preferences dialog box and set the choices to your liking before you import the data set. WOD import can take time, but when successful it provides access to unique JOA data exploration functions for any WOD data.

If you are importing your own CTD data, be sure to examine the "CTD Decimation" tab on the JOA Configure Preferences dialog box and set the choices to your liking before you import the data set. The less decimation you carry out, the finer the vertical resolution of the data once into JOA (and the larger the data file; very large data files can burden JOA).

## JOA File menu
You can open additional data files (each in their own data windows) or add more data to the already-open data file(s) (all in one data window).

You can export any or all of the data as an ascii spreadsheet data file, a binary netCDF section, or an ascii WHP-Exchange comma-separated-value data file. (Exporting as an ascii file may make it easier to use the data in another application.)

## JOA Edit menu
With the File Manager you can reverse the order of stations, merge multiple casts at the same station, merge all stations into one new section (can be useful when making new sections from individual stations or pieces of sections), re-order/sort/delete stations (a powerful way to choose stations and place them in the order you wish), and filter parameters by a missing parameter (for example if you wanted only data from bottles where CFC-12 was measured).

## JOA Calculations menu
Parameters calculations enable a wide range of oceanographically-useful calculations such as potential temperature, various density parameters, O2 % saturation, various stability- related parameters, etc. These yield one value per observation, which then become new parameters in the data list.

Custom Parameter calculations can be used to make new parameters from existing parameters, including any calculated parameter. These yield one value per observation, which then become new parameters in the data list. This is an easy tool to generate nutrient ratios, for example. These calculations can be stacked, enabling simple algebraic expressions.

Station Parameter calculations yield one value per station, and include possibilities such as mixed layer depth, interpolation onto any defined single surface, integration (weighted mean value) between two surfaces, calculation of temperature or salinity on a neutral surface, the value of the extrema of a parameter over the profile or over a range within the profile, and several station statistics.

Custom station parameter calculations can be used to make new station parameters from existing parameters, including any calculated station parameter.

Section calculations can be used to subtract one section from another (see the document [](./comparing.md)) or to prepare an all-section "mean cast" (useful to use to look at differences from the mean along a section).

## JOA Plots menu
JOA plots are the core of the application. JOA was made to provide usable plots with minimal user input, yet also to provide a wide range of optional customization and special features. Here are the minimum inputs required for each JOA plot type (a data file must be opened to see and use the plot types):

* Property-Property (x-y plots, a major JOA plot type[^footnote]):
  The user must select one Y- axis parameter and at least one X-axis parameter (up to seven can be selected via command-clicking) from the scrolling lists before clicking "Plot" (or "OK").
* Line Plot (x-y plots with one colored line per station connecting the observations at each station):
  The user must select one X-axis parameter and one Y-axis parameter from the scrolling lists before clicking "Plot" (or "OK").
* Profile (waterfall x-y plots):
  The user must select one X-axis parameter and one Y- axis parameter from the scrolling lists before clicking "Plot" (or "OK").
* Map (maps showing the station locations, a major JOA plot type[^footnote]):
  No selections are required before clicking "Plot" (or "OK").
  ```{note}
  Special note about JOA Map plots: JOA map plots contain tools which allow (1) direct/graphical selection of a regional subset of the data or (2) selection of a section- oriented subset of data.
  For the latter, when a gridded data set is opened, one can generate a section following an arbitrary path.
  This can be an easy, powerful method to generate a new section along a path of interest.
  ```
* Contour (contoured vertical section plots, a major JOA plot type[^footnote]):
  The user must select one "parameter" from the scrolling list, one "interpolation surface" from the scrolling list (a good choice for deep-ocean data is "PRES-0-6000_srf.xml"), and either one colorbar (almost always one for the parameter being plotted) from the scrolling list or create an autoscale colorbar using one of the color schemes (e.g., "Rainbow(inv)-32" and one of the four autoscale shape buttons) before clicking "Plot" (or "OK").

[^footnote]: Many JOA users will use only the Property-Property, Map, and Contour plot types.

In each of the above providing the minimum input and clicking "Plot" (or "OK") will generate a JOA plot of that type. Most aspects can be customized after drawing the default/minimum plot. Just double-click on whatever aspect of the plot needs attention or use the Edit: (plotname) from the JOA Edit menu or command-R.

## JOA Filters menu
Station Filters permit exclusion or inclusion of selected data sets or of selected sections within a multiple-section data file. This can be a helpful tool to narrow the focus onto the data of greatest interest or to eliminate data which are not pertinent to the analysis at hand.

Missing Parameter Filters can be useful the exclude stations missing one or more selected parameters. For example, one could use this to eliminate any stations that had no CFC-12 data.

## JOA Resources menu
The JOA Contour Manager provides the means to generate and save color bars tuned to the needs of the analysis. This is a powerful JOA extra that is often worth exploiting. All of the color/contour bars included with JOA were made with the Contour Manager.

The JOA Surface Manager is useful to define custom surfaces for interpolation of data. An interpolation surface can be defined for any parameter. For example, using the Custom Parameters calculator to generate nitrate/phosphate ratios, one could use the Surface Manager to create standard surfaces of silicate, and then plot the nitrate/phosphate ratio on standard silicate surfaces.