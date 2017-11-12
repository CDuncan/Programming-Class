# Function to return third element of input array
def takePop(elem):
    return elem[2];

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

if FileOpen:
    for line in readFile:
        Split = line.split(',');
    
        # Take split line and create row array with integer population, then add to column array of row arrays
        if i:
            try:
                Row = (Split[0],Split[1],int(Split[2]),Split[3],Split[4]);
                List.append(Row);  
            except:
                print("Error:\n " + Split[0] + "has a non integer population " + Split[2]);
        
        # Retain header
        else:
            Header = line;
            i = i+1;
        
    readFile.close()

    # Sort "List" array by increasing population
    List.sort(key=takePop)

    # More empty arrays for later use
    Names = [];
    Type = [];
    Pops = [];
    Lat = [];
    Long = [];

    # Create column arrays of variables sorted by population
    for line in List:
        Names.append(line[0]);
        Type.append(line[1]);
        Pops.append(str(line[2]));
        Lat.append(line[3]);
        Long.append(line[4]);

    
    # Write new file "GBplaces_PopSort.csv" with header
    writeFile = open('GBplaces_PopSort.csv','w');
    writeFile.write(Header);
    for i in range(len(Pops)):
        writeFile.write(Names[i] + "," + Type[i] + "," + Pops[i] + "," + Lat[i] + "," + Long[i]);
    writeFile.close();
