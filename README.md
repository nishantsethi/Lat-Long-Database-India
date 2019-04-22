# Lat-Long-Database-India
Provided with names of location, Getting the Latitude and Longitude, Creating a matrix having every city distance with every city

While creating a web platform, Sometimes we have to filter the results on the basis of location. With the help of Google Geocoding, I created this program in which the input I gave was the name of cities and the final output was a csv with Distance between every ciy. This can later be used for to filter to say states with difference under 100kms etc.

## WorkFlow

1. Provide a csv with all the names of location.
2. Use Geo-code.ipynb to get a csv with Latitude and Logitude.
3. Use dist.py to get the distance in kilometers between every location.
![Alt text](https://raw.githubusercontent.com/nishantsethi/Lat-long-Database-india/master/Screenshot%20at%20Mar%2015%2013-22-23.png?raw=true "CSV File")

4. The file load-matrix.py loads Matrix of distances between locations and gives the six most near ones.
![Alt text](https://raw.githubusercontent.com/nishantsethi/Lat-long-Database-india/master/Screenshot%20at%20Mar%2015%2013-26-34.png?raw=true "6 Nearest Cities")

For getting the final CSV shown in 3rd step. Kindly mail me at sethi.nishant43@gmail.com
This can work for any search option when trying to filter down with locations
