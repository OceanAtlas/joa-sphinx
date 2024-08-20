# How to Filter Your Data

Java OceanAtlas provides extensive capabilities for filtering data. Filtering allows one to focus on specific data of interest. Two types of data filters are available under the Filters menu. (A third type of filtering called 'enhancement' is described in the User Guide.)

Station Filters (illustrated in {numref}`filter_station_dialog`) select (or de-select) stations:

* The 'Station Selection Filter' allows one to choose stations to exclude or include by clicking on the header to choose one station, by shift-clicking to choose a contiguous list of stations, or by control-clicking on multiple headers to choose a discontiguous list of stations.
* The 'Missing Parameter Filter' permits the user to exclude stations which do not have at least one reported value for a specified parameter. Why do this? Some oceanographic sections contain only occasional stations for a more exotic parameter (admittedly use of the word 'exotic' lies in the eyes of the beholder) such as radiocarbon, helium, or tritium. Where data are missing for a given parameter when it is used to color plots, Java OceanAtlas colors the missing values by a pre-set color (a gray color in a 'factory fresh' copy of Java OceanAtlas). In contour plots, which are interpolated, a lot of missing data can make for a poor-looking plot. So by selecting name of the sparsely-sampled parameter, and excluding all stations without at least one value for that parameter, the user can make plots of that parameter look better.
* The 'Location Filter' offers the capability to filter out all data outside a selected region. The region can be chosen via a selection rectangle or by typing in latitude and longitude limits.

Clicking the 'OK' closes the dialog and applies the selected conditions to the data, 'Remove' cancels the current station filter, 'Apply' applies the selected conditions to the data but does not close the dialog, and 'Close' closes the dialog box without performing any actions.

```{figure} figures/fig20.webp
:name: filter_station_dialog

Java OceanAtias Station Filters dialog box for the A10_2011 section.
```

The 'Observation Filter' permits the user to, on all plots, exclude data outside of up to two nested 'and/or' parameter range conditions each containing a nested 'and/or' choice, or to highlight the matching observations indicated by those same choices. It also works fine with a single parameter choice and range.

With the Atlantic A10_2011 data set open in the Data Window, open the 'Observation Filter' dialog box from the Filters menu. In the first (top) condition, select 'SILCAT' to filter by, and type in '50' and '150' for the lower and upper limits, respectively. Now click on 'OK'. {numref}`filtered_sections` shows the Observation Filter dialog box with these entries and the resulting effect of this filter on the contour plot of SALNTY on PRES from the Atlantic A10_2011 data set.

```{figure} figures/fig21.webp
:name: filtered_sections

Using Java OceanAtlas Observation Filters to limit the salinity data plotted on the A10_2011 section (top section) to only those data points i.e., bottle samples) with silicate values between 50 and 150 µMol/kg (bottom section).
```

The filtered salinity section plot now shows only those data where silicate is between 50-150 μmol/kg.

```{admonition} Oceanographic Note

This rather neatly pared out the low-silicate upper layer and North Atlantic-origin layers. The remaining colored portions of the section plot now show the salinity structure within the nominal southern-origin waters in the section.
```