<p align="center">
  <img width="1000" height="300" src="https://github.com/breogann/Project-3.Finding-the-best-location-for-a-new-company/blob/master/Images/cover.png" alt="Where in the world?">
</p>

# Worldwide location pinning on given criteria 

Selection of a world-wide location for a gaming company given some criteria. Data used was a dataset with companies and FourSquare API to get locations for Starbucks. 

##  The problem ❗️ ## 
<p align="left">
  <img width="450" height="400" src="https://github.com/breogann/Project-3.Finding-the-best-location-for-a-new-company/blob/master/Images/problem.png" alt="problem">

## The solution 🟢 ##

### Data 📊 ###

First, we cleaned the dataset obtained from __crunchabse__ with the list of companies. Then, we added Starbucks locations using the __FourSquare API__.

### Data processing 🛠 ###
- Obtention of coordinates through MongoDB
- Formatting those coordinates
- Use the formatted data to iterate over through the API
- Place the coordinates in a map

<table border="0">
 <tr>
    <td><b style="font-size:15px">Used technologies 🔌</b></td>
    <td><b style="font-size:15px">Used libraries 📚</b></td>
 </tr>
 <tr>
    <td>
    <ul>
      <li>MongoDB</li>
      <li>Foursquare API</li>
      <li>Cartoframes</li>
      <li>Folium</li>
</ul>
</td>
<td>
<ul>
      <li>GeoPandas</li>
      <li>Pymongo</li>
      <li>Geopy</li>
      <li>Matoplotlib</li>
</ul>
</td>
 </tr>
</table>




##### To do #####
- Add more venue filters: vegan places, etc.
- Calculate minimun distance to rank possible places
