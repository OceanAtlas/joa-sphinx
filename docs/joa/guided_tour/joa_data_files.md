# Java OceanAtlas Data Files

Java OceanAtlas reads oceanographic data in several common or useful formats. Each of these is indicated to Java OceanAtlas when it tries to open a data file by virtue of its file extension, i.e. a mandatory suffix at the end of a data file name. The requirement for file extensions is necessary because Java OceanAtlas must work on many different platforms, and with several different operating systems underpinning its Java code. The list of presently-accepted data format file extensions, each with a description of that file type follows:

```{list-table} Java OceanAtlas Data Files
:header-rows: 1

* - File extension (suffix)
  - Description of the file format represented by the extension
* - .joa
  - **Java OceanAtlas binary (read, write)**
    
    Good for storing custom sections as well as files that have been imported from other formats. Java OceanAtlas binary files will usually open significantly faster than importing files in plain text. Java OceanAtlas binaries store parameter units as well as bottle and observation quality codes.
* - .jos
  - **Spreadsheet (TSV) (read, write)**

    A tab-separated (TSV) format that is compatable with most spreadsheet applications.
* - .poa
  - **Power OceanAtlas binary (read, write)**

    These are files that were originally produced for Mac Power OceanAtlas. This format gives you access to large historical datasets created originally for OceanAtlas. These files do not store units or quality code information.
* - _hy1.csv
  - **WOCE Bottle section in WHP-Exchange format (read)**

    This is a comma separated value fle (CSV) produced by the WOCE Hydrographic Program. Files in this format include multiple stations and usually correspond to a complete section or cruise. Java OceanAtlas provides 'post processing' capabilities to filter observations by quality code information as well as perform units conversion.
* - _ct1.csv
  - **WOCE CTD profile in WHP-Exchange format (read)**
    
    This is a comma separated value file (CSV) produced by the WOCE Hydrographic Program. Files in this format include a single CTD cast. Java OceanAtlas preserves all units and quality codes. Java OceanAtlas provides significant 'post processing' to filter observations by quality information as well as units conversion. CTD files can be decimated to user-selected intervals or Java OceanAtlas standard levels.
* - _ct1.zip
  - **WOCE CTD section in WHP-Exchange format (read)**

    A zip file that contains multiple individual CTD profiles.
* - .nc
  - **netCDF Profile (read, write)**

    Individual CTD or bottle profiles that adhere to PMEL's EPIC standard. 
* - .sd2
  - **SD2 (read)**

    Text files that adhere to NODC's SD2 exchange format.
```

Note that Java OceanAtlas writes ('exports') data in four different formats (JOA Binary, POA Binary, JOA Spreadsheet, and netCDF Section). You can use Java OceanAtlas to read data in one of the other formats and translate into one of the four. Calculated parameters such as potential temperature and density can be added by Java OceanAtlas between reading and exporting the data, or data subsets or new sections can be made.

You may be interested in having Java OceanAtlas read your own data. Spreadsheet format data are the easiest for most users to generate if they are not already familiar with writing data in one of the other supported formats. Fortunately, Java OceanAtlas spreadsheet format is not too demanding. Java OceanAtlas 'understands' many data headers, and reads data in column (spreadsheet) format. For example, an Excel file saved as comma- or tab- delimited text, set up to meet minimal Java OceanAtlas requirements, will read straight into JOA.

Java OceanAtlas requires of each data set at least a **section name**, a **station number**, a **latitude**, a **longitude**, and **data at one level (one pressure)**. Columns must be labeled. Java OceanAtlas will try to recognize heading names from its internal lexicon. The words shown below are recognized.

**SECTION** names are short alphanumerics.

**STATION** numbers are typically 1-4 digit numbers but can be alphanumerics.

**LATITUDE**s are expressed in decimal degrees, positive in northern hemisphere and negative in the southern hemisphere.

**LONGITUDE**s are expressed in decimal degrees, positive in eastern hemisphere and negative in the western hemisphere.

Oceanographers use a left-handed coordinate system, meaning that while the X-axis and Y-axis point positive in the usual sense, the Z-axis is positive downward. Java OceanAtlas data are indexed by PRESsure, which is the parameter used most often for vertical orientation in physical oceanography. Because the pressure at 10 meters depth in the ocean is quite close to one bar, or one atmosphere, one decibar is nearly the same vertical extent as one meter. Decibars are the pressure unit used throughout oceanography and in Java OceanAtlas.

* To make a simple data spreadsheet set, look up the latitude and longitude of your city, convert to decimal degrees, and substitute the name and position for 'YOURCITY', '35.00', and '-120.00' in the example:

  SECTION<tab>STATION<tab>LATITUDE<tab>LONGITUDE<tab>PRES<cr> TEST<tab>YOURCITY<tab>35.00<tab>-120.00<tab>1.0<cr>

  The use of '<tab>' in the above denotes a tab character, and '<cr>' denotes a carriage return.

This two-line file, if saved as plain text and with a file name given a '.jos' suffix, can be opened by Java OceanAtlas. If you then do a map plot, you will find a station dot at the position you provided.

It is only a small extension from this minimum example to see the makings of a small Java OceanAtlas spreadsheet data file holding oceanographic profile data, shown below as a table:

| STATION | LATITUDE | LONGITUDE | PRES | TEMP   | SALT    | O2   |
|---------|----------|-----------|------|--------|---------|------|
| 312     | 64.002   | -27.833   | 16   | 8.0754 | 35.0699 | 7.25 |
| 312     | 64.002   | -27.833   | 49   | 7.6206 | 35.0744 | 6.89 |
| 312     | 64.002   | -27.833   | 99   | 7.4723 | 35.0872 | 6.79 |
| 312     | 64.002   | -27.833   | 199  | 6.8717 | 35.0855 | 6.43 |
| 312     | 64.002   | -27.833   | 254  | 6.6958 | 35.0683 | 6.42 |
| 312     | 64.002   | -27.833   | 354  | 6.3275 | 35.031  | 6.34 |
| 312     | 64.002   | -27.833   | 454  | 5.9039 | 34.9862 | 6.44 |
| 312     | 64.002   | -27.833   | 554  | 5.7533 | 34.987  | 6.38 |
| 312     | 64.002   | -27.833   | 844  | 5.0649 | 34.9598 | 6.13 |
| 314     | 64.110   | -29.000   | 51   | 7.7994 | 35.0822 | 6.91 |
| 314     | 64.110   | -29.000   | 403  | 6.6015 | 35.0678 | 6.46 |
| 314     | 64.110   | -29.000   | 707  | 5.5014 | 34.976  | 6.31 |
| 314     | 64.110   | -29.000   | 960  | 4.633  | 34.9474 | 6.1  |
| 314     | 64.110   | -29.000   | 1109 | 4.1972 | 34.9435 | 6.19 |
| 314     | 64.110   | -29.000   | 1417 | 3.7364 | 34.9235 | 6.38 |
| 314     | 64.110   | -29.000   | 1598 | 3.3992 | 34.9006 | 6.51 |
| 315     | 64.132   | -29.533   | 17   | 8.6936 | 35.0759 | 7.12 |
| 315     | 64.132   | -29.533   | 41   | 7.8779 | 35.0814 | 6.44 |
| 315     | 64.132   | -29.533   | 111  | 7.0148 | 35.0911 | 6.51 |
| 315     | 64.132   | -29.533   | 313  | 6.5638 | 35.0706 | 6.34 |
| 315     | 64.132   | -29.533   | 609  | 5.5097 | 34.9747 | 6.14 |
| 315     | 64.132   | -29.533   | 1011 | 4.4229 | 34.9566 | 6.27 |
| 315     | 64.132   | -29.533   | 1215 | 3.9963 | 34.9411 | 6.3  |
| 315     | 64.132   | -29.533   | 1517 | 3.4827 | 34.908  | 6.49 |
| 315     | 64.132   | -29.533   | 1619 | 3.4704 | 34.9063 | 6.5  |

Other header columns that Java OceanAtlas 'understands' (but does not require) include CAST, BOTTOM (depth to bottom in meters), DATE (yyyymmdd format), and TIME (hhmm format).

Java OceanAtlas will read any column of profile parameter data. For many common parameters, its internal lexicon helps Java OceanAtlas to interpret which of its standard parameters, for example those for which there are predefined color bars, is meant. But Java OceanAtlas will read any parameter, and even assign a name if the column heading (name) is more than four characters, though it is best for new parameters (e.g., concentration of a phytoplankton pigment) for users to supply a four character name in the column heading. Java OceanAtlas has many tools for making new and customized color bars, and for autoscaling contour plots, and so nearly any data will work. A small caveat is that it is best to avoid representing data values as very small (close to zero) numbers, e.g., 0.0003456. Such data often are best shown in columns pre-multiplied by a power of ten to bring their apparent numerical value - to Java OceanAtlas - away from zero. (This has to do with how computers handle arithmetic for very small numbers.)