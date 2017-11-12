    ## Comments ##
# This script requires the mpl_toolkits basemap package to run.
# This script uses shapefiles to show county lines but can be run without them and still functions.
# All the points are clickable and when clicked they give data about the point in the console/command line, if you cant click them do one of two things
# 1) Run the script from command prompt instead of spyder
# 2a) Put the following into the console: %matplotlib auto
# 2b) Go to Tools>Preferences>IPyton console>Graphics, change Backend to Automatic, restart Spyder which is the same as 2a but manually


#######################
### Import Packages ###
#######################

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
# Supress meaningless warning
import warnings
warnings.filterwarnings("ignore");


########################
### Define Functions ###
########################

# Function to allow data to be sorted as a list
def takePop(elem):
    return -int(elem[2]);

# Function to assign colours to each city based on the 2/3 power of their population relative to the population of Birmingham
def Colour(RootRelPop):
    RootRelPop = RootRelPop
    if RootRelPop > 1.2:    Hex = "#A0190E"
    elif RootRelPop > 0.9:  Hex = "#ED2F20"
    elif RootRelPop > 0.8:  Hex = "#E7571B"
    elif RootRelPop > 0.7:  Hex = "#E27F17"
    elif RootRelPop > 0.6:  Hex = "#DDA613"
    elif RootRelPop > 0.5:  Hex = "#D8CD10"
    elif RootRelPop > 0.4:  Hex = "#B2D30C"
    elif RootRelPop > 0.3:  Hex = "#83CE09"
    elif RootRelPop > 0.2:  Hex = "#54C906"
    elif RootRelPop > 0.1:  Hex = "#26C402"
    else:                   Hex = "#00BF07"
    return Hex

# Function to set positions and list of details as global variables so they can be used by PickCity 
def setGlobals(X,Y,List):
    global XGlobal
    XGlobal = X;
    global YGlobal
    YGlobal = Y;
    global ListGlobal
    ListGlobal = List;

# Function to allow user to click cities to print their details
def PickCity(event):
    # Find and store click location
    XPoint = event.artist.get_xdata();
    YPoint = event.artist.get_ydata();
    # Cross check click location with known city locations, then print details
    # List[i] has elements: Name, Type, Population, Latitude, Longtiude
    for i in range(len(XGlobal)):
        if (XPoint == XGlobal[i]) and (YPoint == YGlobal[i]):
            Rank = i+1;
            print(ListGlobal[i][0] + " is a " + ListGlobal[i][1].lower() + " with a population of " 
                  + ListGlobal[i][2] + " at (" + ListGlobal[i][3] + "," + ListGlobal[i][4] + ").");
            print("It is number " + str(Rank) + " in the list of most populous settlements in Great Britain.\n");



##########################
## Import and Sort List ##
##########################           
            
            
# Import List 
Filename = 'GBplaces.csv';

try:
    readFile = open(Filename,'r')
    FileOpen = 1;
except:
    print("Error:\n File: " + Filename + " does not exist.")
    FileOpen = 0;
    
    
# Create empty arrays for later use
Row = [];
List = [];
i = 0;

# Only run if the file exists and opens
if FileOpen:
    
    
    # Explanation given before map opens so user can read
    print("Click on points (while not in zoom mode [O]) to display information in the console\n" + 'Marker size and colour is dependent on the settlements population\n' + 'Markers go from small and green to large and red as population increases');

    
    for line in readFile:
        Split = line.split(',');
    
        # Take split line and create row array with integer population, then add to column array of row arrays
        if i:
            try:
                # Add +0.00001 to Westminster latitude to ensure no duplicate positions (breaks cursor), change is negligible
                if Split[0] == "Westminster":
                    Split[3] = str(float(Split[3])+0.00001);
                Row = (Split[0], Split[1], Split[2], Split[3], Split[4].rstrip());
                List.append(Row);  
            except:
                print("Error:\n " + Split[0] + "has a non integer population " + Split[2]);
        
        # Skip header
        else:
            i = i+1;
        
    readFile.close()

    # Sort "List" array by decreasing population (So when plotted the smallest points are on top of the larger ones and they do not get covered)
    List.sort(key=takePop)
    readFile.close()


###########################
## Create Base Map Of UK ##
###########################

    # Create Equidistant Conic map centred on lat_0, lon_0 with edges defined by Left Lower and Right Upper Corners
    fig, ax = plt.subplots(figsize=(10,20))
    m = Basemap(resolution='i', # c, l, i, h, f or None
                projection='eqdc',
                lat_0=54.22, lon_0=-3.13,
                llcrnrlon=-8.35, llcrnrlat= 49.53, urcrnrlon=3.57, urcrnrlat=58.91)
    
    # Colour the map
    m.drawmapboundary(fill_color='#7ac4e2')
    m.fillcontinents(color='#c1c1c1',lake_color='#7ac4e2')

    #m.drawcoastlines(color='#7ac4e2')
    # Add county borders (Will skip if shapefiles do not exist)
    try:
        m.readshapefile('Areas', 'areas', color='#DFDEDC')
    except:
        DoNothing = [];

##################
## Convert Data ##
##################
    
    # Create empty arrays for later use, X and Y are made to be the same legth as List so they can be overwriten
    Pop = [];
    Y = [0]*len(List);
    Lat = [];
    X = [0]*len(List);
    Long = [];
    
    for i in range(len(List)):
        # Convert Long and Lat in floating point numbers
        Lat.append(float(List[i][3]));
        Long.append(float(List[i][4]));
        # Convert long and lat to X and Y coordinates in the mercator projection
        X[i],Y[i] = m(Long[i], Lat[i]);
        # Create integer list of the populations
        Pop.append(int(List[i][2]));

    # Find the square root of the ratio of a cities population to londons population. (Used to define marker sizes)
    RootRelPop = [];
    ScndMaxPop = Pop[1];
    for i in range(len(Pop)):
        RootRelPop.append( (Pop[i]/ScndMaxPop)**(2/3) );
         
##############
## Plot Map ##
##############
        
    # Add latitude and longitude lines    
    LatLines = np.arange(-90., 90, 2.);
    m.drawparallels(LatLines, labels=[1, 0, 0, 0], fontsize=10, color='#605B5B',linewidth = 0.2);
    LongLines = np.arange(-360., 360., 2.);
    m.drawmeridians(LongLines, labels=[0, 0, 0, 1], fontsize=10, color='#605B5B',linewidth = 0.2);
   
        
        
        
        
    # Plot points on map with clickable regions of size 4, marker colour and size is dependant on the 2/3 power of the population comparison to Birmingham
    for i in range(len(X)):
        m.plot(X[i], Y[i], marker ='o', markersize = 3 + 3*RootRelPop[i], color = Colour(RootRelPop[i]), mec = "#605B5B",  picker=4)


    setGlobals(X,Y,List)
    ax.plot
    ax.set_title('Map of 100 most populous towns and cities in Great Britain')


    # On screen controls
    textstr = "Zoom mode on/off: O\nUndo zoom: Backspace"
    props = dict(boxstyle='round', facecolor="white", alpha=1)
    ax.text(550000, 1000000, textstr, fontsize=8, bbox=props)

    # When dot is clicked, console prints data
    fig.canvas.mpl_connect('pick_event', PickCity)

    plt.show();































