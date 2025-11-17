# Mac Installation Instructions

* You do not have to install a separate Java environment for JOA 5.5
* The installation process depends on what operating system you are using. To check what version of macOS is installed on your computer, go to the apple menu in the top left corner of your screen and select About This Mac. JOA 5.5 has been tested on versions 10.12-10.15, 11, 12, and 13 of macOS.
* The only difference in the "pro" version of JOA is that it requires a computer with at least 16 GB of RAM. This permits JOA to open full resolution versions of the largest global gridded data sets (reduced resolution versions are available, however).
* Due to Apple security protocols, JOA for MacOS 13 and above cannot be installed by direct download of the application. JOA can sometimes be installed via copying from a flash drive (both regular and pro versions). A more reliable installation method is via using the MacOS Terminal app to unpack the "tar" file available via download from this site (regular version only). [Either method should also work for Mac OSs 10.12 through 13, too.]
* The JOA folder (containing the JOA app and its support files) must be on your hard drive for JOA to run.

## Installation on macOS Catalina (10.15), Big Sur (11), and Monterey (12) 
1. You must download JOA 5.5 from Safari. Open Safari and go to Preferences. In the General tab, turn on Open “safe” files after downloading. This is necessary for JOA to install correctly.

   ![Safari Safe Downloads](figures/mac1.webp)
2. Download the Zip file.
3. When the download is finished, there will be a folder called Java OceanAtlas in your Downloads folder that contains these files:

   ![JOA Directory Contents](figures/mac2.webp)
4. Move or copy the Java OceanAtlas folder to the desired location on your computer. We recommend putting it in Applications.

## Installation on macOS Sierra (10.12), High Sierra (10.13), Mojave (10.14), Catalina (10.15), and Big Sur (11). Provisionally on macOS 12 (Monterey).
1. Download the DMG file 
2. Double click Java OceanAtlas.dmg to open it. You will see this window:

   ![JOA DMG File Contents](figures/mac3.webp)
3. Drag the folder called Java OceanAtlas to the provided link to your Applications folder, or to the desired location on your computer. Do not run JOA directly from the DMG.
4. You will see these files in the Java OceanAtlas folder. You can now eject the DMG from finder or unmount it using the Disk Utility application. The DMG can be kept as a backup or discarded entirely.

   ![JOA Directory Contents](figures/mac2.webp)

## Installation on MacOS 13 and higher (and should also work for previous MacOS versions).
### Method A
JOA can sometimes be transferred via a flash drive from any MacOS computer where JOA is working OK.

To install Java OceanAtlas (JOA) for MacOS from a flash drive, copy the entire folder (for example, "Java OceanAtlas 5.5" or "Java OceanAtlas 5.5 pro") onto an appropriate location on your MacOS computer, such as the Applications folder or the Desktop. Copy the entire folder - not just the contents, but folder and all. Notes: (1) Keep the JOA contents together in the folder and (2) JOA will not work directly from the flash drive.

:::{note}
1. Keep the JOA contents together in the folder and
2. JOA will not work directly from the flash drive. 
:::

:::{note}
Method A worked reliably until 2023, but there have now been verified reports of JOA failing to properly open after using this method.
:::

### Method B
Download the file [OceanAtlas5.tar.gz](https://cchdo.ucsd.edu/data/41044/OceanAtlas5.tar.gz)

On your Mac, open/start the Terminal app (usually found in the Utilities folder of the Applications folder).

Using Terminal, use the command "cd" to change directories to whatever directory the file "OceanAtlas5.tar.gz" is in. Once there, use this command: 

```console
tar -xzvf OceanAtlas5.tar.gz
```

Below are the contents of the Terminal window on J. Swift's computer, when the tar.gz file was on the desktop: 
```console
Last login: Thu Sep 28 15:07:48 on ttys000
[jhswift:~] jamesswift% cd desktop
[jhswift:~/desktop] jamesswift% tar -xzvf OceanAtlas5.tar.gz
```

After executing this command, a long list of files appears in the Terminal window. Look for the folder OceanAtlas5 on your Mac. That is your Java OceanAtlas folder. You can move it anywhere you wish but keep the contents together (in the folder). 

:::{note}
At the time this was prepared, the tar.gz of the "Pro" version of JOA was not successfully working with this method. If the tar.gz of the Pro version does appear on this site, that means we have fixed that problem.
:::

## Fixing Blurry Fonts in JOA
If you are using Mojave or Catalina, you may notice certain text to be poorly rendered and difficult to read, such as colorbar labels:

![Blurry colorbar labels](figures/mac4.webp)

1. Quit JOA. Open Terminal (Terminal can be found in your /Applications/Utilities/ folder). You will see some text in your Terminal window. The gray box is your cursor.
2. Copy and paste the following text into Terminal and press return: 
   ```console
   defaults write -g CGFontRenderingFontSmoothingDisabled -bool NO
   ```
    ![terminal window with above command](figures/mac5.webp)
3. After you press return, a new line of text with your computer and account name will appear. There will be nothing to indicate that a change has taken effect. Quit terminal and restart JOA. If text still appears fuzzy, try logging out of your account and logging back on.

## System Requirements:
* JOA 5.5: macOS 10.12 or higher (may work under previous versions of macOS but has not been tested)
* JOA 5.3: Mac OS X 10.10 or higher
* 4 GB of RAM (standard version) or 16 GB of RAM (pro version)