# Station Maps
Plots are the heart of the application. One of the first questions you might have would be ‘where are these data located?’ Java OceanAtlas includes station maps.

Select ‘Map...’ from the Plots menu. The will bring up the Configure Map Plot dialog box.

We have configured the dialog boxes for each JOA plot type so that a basic plot can be made with a minimum of user input.

For a JOA map plot, no further user inputs are required: the ‘Plot’ button is activated, meaning a basic map plot will be drawn by clicking on the ‘Plot’ button.

In this Guided Tour we show some basic plot customization features:

Select the ‘Miller’ projection from the scrollable list of projections.

Select the ‘Central Atlantic’ preset region. In the 'Latitude spacing (deg)’ and Longitude spacing (deg)’ boxes select the pre-set text and type in '10’ and '20’, respectively. Java OceanAtlas maps include default bathymetry based on the ETOPO60 one-degree coarse grid: click the 'bathymetry’ tab to see this (on a new copy of JOA it is set up this way by default). The dialog box should look like the examples in {numref}`configure_map_plot`.

```{figure} figures/fig2.webp
:name: configure_map_plot

Java OceanAtlas Map Options dialog box, set up for a Map plot of the A10_2011 data set.
```

Then click 'Plot'. You will see a map with the stations, shaded land masses, gray bathymetry, and a latitude/longitude grid, as shown in {numref}`station_position_map`.

```{figure} figures/fig3.webp
:name: station_position_map

Java OceanAtlas Map Options dialog box, set up for a Map plot of the A10_2011 data set.
```

Map plots show individual dots for each station, with a different station color for each section subset. (JOA determines this coloring for reasons mostly ignored here, for example when there is more than one section opened.) In {numref}`station_position_map` the apparent 'cruise line' is actually a series of 80 individual station dots. The map window is scrollable and resizable. (You may need to click on the 'Reset' button in the map plot window to force a redraw.) Selecting a subset of the plot by click-dragging the cursor will produce a subset of the map plot covering only the selected area. [Sometimes, due to a Java quirk, the new map subset plot is initially hidden under the original map plot window.]