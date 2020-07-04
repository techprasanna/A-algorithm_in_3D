# A-algorithm_in_3D
This python application is an implementation of A* search algorithm on a map with terrain information and elevation contours

# Input Processing
..1. 1. For this assignment, we were given two separate inputs, both representing Mendon Ponds Park: a text representation of the elevations within an area (500 lines of 400 double values, each representing an elevation in meters) and a 395x500 simplified color-only terrain map (color legend below). To address the difference in width between the elevation and terrain files you should just ignore the last five values on each line of the elevation file.
a. I first converted the image into a list of RGB values, then assigned them the respective speeds ( Given in the code ) and converted the image into a list of speeds according to the color.
b. Then, I mapped the (x,y) co-ordinates with the speed and with the elevation file list which I made by eliminating the last 5 values from each line.
c. In this way, I created two major dictionaries, one with the x-y coordinates mapped with speed i.e pixel_speed and the other mapped with elevation of every pixel i.e pixel_elev. I used these two while computing the A* algorithm
2. Secondly, I assigned the speed of every RGB value mentioned in the table. Following is the table showing speed of every color.
