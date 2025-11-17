# Managing Java OceanAtlas Features
The JOA application was written originally to be the application centerpiece of an electronic atlas of ocean profile data. The application has evolved and grown as users suggested new features and the authors conceived many of their own. Some specialty users needed features directed primarily at their interests. Also, while most JOA features are robust, some are still in development, or simply quirky. And the authors agree that a version of JOA with too many features up front would make JOA much less easy to use for first-time users.

Our solution has been to create a Feature Manager, accessible as one of the choices in the JOA Preferences dialog box, accessed from the "Java OceanAtlas" menu on Mac OS X and under the Edit menu on Windows and Linux. Through the Feature Manager, various JOA features can be turned on and off.

The default JOA enabled-feature set in the downloaded application is a balance between simplicity and power, chosen by Swift to match the needs of graduate student users of JOA, for example, students using the JOA DPO Examples. Educators who wish a simpler JOA for their students may want to turn off some of the default enabled features. Meanwhile, power users, or those curious to see what more lies within JOA, may want to experiment with enabling additional JOA features. Typically each feature adds one or more choices to the JOA menus.

Most JOA features are discussed in the JOA User Guide (available to the right).

We include, below, a list of the JOA features which can be turned on and off via the JOA Feature Manager. Note that "Objective Analysis" is still under development, "Gradient Contour Plots" permit plotting sections of geostrophic velocity, and "Station Calculation XY Plots" can be interesting and useful.

As we add new features to JOA, and complete implementation of some existing features, the choices in the JOA Feature Manager will change.

## List of Managed Features
### Filters
* Allow Observation Filtering
* Allow Station Filtering

### File Options
* Export EPIC Pointer file
* Allow File Merge
* Allow Exporting Station Calculations
* Access Dapper Servers
* Export WOCE Exchange Files
* Export netCDF Section
* Export Spreadsheet Files

### Calculations
* Allow Station Calculations
* Allow Custom Station Calculations
* Allow Parameter Calculations
* Allow Section Calculations
* Allow Modeling TS relationships
* Allow Custom Calculations
* Allow Value Recoding
* Allow Parameter Transformations

### NdEdit Options
* Allow NdEdit Browsing
* Allow Overlay Contours on Map Plots
* Overlay Contours Based on a Calculated Station Parameter
* Overlay Contours Based on an Isosurface

### Contour Plots
* Objective Analysis in Interpolation
* Overlay Contours

### Plots
* Allow Station Calculation Plots
* Allow Gradient Contour Plots
* Allow Profile Plots
* Allow Line Plots
* Allow Map Plots
* Allow Contour Plots
* Allow Station Calculation XY Plots
* Allow Property-Property Plots

### Station Calculations

* Allow Neutral Surface Calculations
* Allow Windspeed and Direction Calculations
* Allow Station Statistics Calculations
* Allow Interpolations Calculations
* Allow Integration Calculations
* Allow Mixed-layer Depth Calculations
* Allow Extrema Calculations

### Map Station Colors
* Station Coloring Based on Station Metadata
* Station Coloring Based on an Isosurface
* Station Coloring Based on a Calculated Station Parameter

### Resource Editors
* Allow Editing/Creating Interpolation Surfaces
* Allow Editing/Creating Color Bars
* Allow Editing/Creating Color Palettes

### Preferences
* Show General Preferences
* Show CTD Decimation Preferences
* Import World Ocean Data Select CSV Files
* Show Enhancement Preferences
* Show Parameter Substitutions Preferences
* Show Import Preferences
* Allow Users to Manage Features
* Show Font Preferences

### Section Calculations
* Allow Section Difference Calculations
* Allow Mean Cast Calculations

### Section Editors
* Show Section Manager
* Allow Editing Parameter properties
* Use NQuery Database Features
* Allow Station Data Editing
* Allow Editing File Properties
