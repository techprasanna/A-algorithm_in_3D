# A-algorithm_in_3D
This python application is an implementation of A* search algorithm on a map with terrain information and elevation contours

# Input Processing
### 1. In this application, we are using two separate inputs, both representing Mendon Ponds Park: a text representation of the elevations within an area (500 lines of 400 double values, each representing an elevation in meters) and a 395x500 simplified color-only terrain map (color legend below). To address the difference in width between the elevation and terrain files you should just ignore the last five values on each line of the elevation file.
* a. I first converted the image into a list of RGB values, then assigned them the respective speeds ( Given in the code ) and converted the image into a list of speeds according to the color.
* b. Then, I mapped the (x,y) co-ordinates with the speed and with the elevation file list which I made by eliminating the last 5 values from each line.
* c. In this way, I created two major dictionaries, one with the x-y coordinates mapped with speed i.e pixel_speed and the other mapped with elevation of every pixel i.e         pixel_elev. I used these two while computing the A* algorithm
### 2. Secondly, I assigned the speed of every RGB value mentioned in the table. Following is the table showing speed of every color.
| Value(RGB)    | Speed Assigned (in m/s)
| ------------- |:-------------:
| Open land(248,148,18)      | 10 
| Rough meadow(255,192,0)      | 5      
| Easy movement forest(255,255,255)| 4
| Slow run forest(2,208,60)| 6
| Walk forest (2,136,40) | 4
| Impassible vegetation(5,73,24) | 3
| Lake/Swamp/Marsh(0,0,255) | 2
| Paved Road(71,51,3) | 12
| Footpath(0,0,0) | 9
| Out of bounds(205,0,101) | 0

# A* Algorithm
* 1. The A* algorithm makes use of two important functions to calculate the weightage of the pixel to decide which pixel to take next. They are the path cost between pixels and the heuristic function.
* 2. Path cost between pixels(g(n)): The path cost between pixels is calculated as a time function. The 3D distance between two pixels is taken along with the elevation as the third(Z) dimension. The distance is then used to calculate the time taken to go from one pixel to the neighbour’s pixel using the speed of the first pixel from the 2 pixels. Here, pixel_speed dictionary comes to use to calculate the time.
* 3. Along with the time, there is one more function called as Heuristic function (H(n)). In this, the time taken from the child pixel (neighbouring pixel) to the goal (here, goal is a control function which changes progressively) is calculated. Here, I am just considering the x-y co-ordinates of the pixels and the speed is taken as the maximum i.e 12m/s so as to ensure that there is no result better than the heuristic function because that’s the sole purpose of calculating the heuristic value.
* 4. The cost function (F(n)) is calculated as F(n) = G(n) + H(n), where G(n) is the path cost and H(n) is the heuristic cost. This value is calculated for every child pixel of the parent pixel and the child with the lowest value of F(n) is selected. In my code, f_n stores the pixel coordinates along with their cost functions. And key with the lowest value is selected which acts as a priority queue which is in O(1) time.

### Admissibility of the Heuristic:
In order to ensure the admissibility of the heuristic, I am using Euclidean distance to find the distance between two pixels and the highest speed in the table of speeds to ensure that there is not better value than the heuristic value. I have made sure that the heuristic never over-estimates the cost of reaching to the goal, i.e the cost it estimates is not higher than the lowest possible cost from the current point in the path.
