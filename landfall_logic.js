
var hurricanes = new L.layerGroup();

var overLayMap = {
    Hurricanes: hurricanes
}
// url set to the repo with the 
var url = 'https://raw.githubusercontent.com/spearjen/project2/main/Resources/landfall.js'

d3.json(url, function(data){
    // switch function for color of circle according too magnitude of quake
    function circleColor(Wind_mph){
        switch (true) {
            case Wind_mph < 95:
                return "green";
            case Wind_mph <111:
                return "lightgreen";
            case Wind_mph <130:
                return "yellow";
            case Wind_mph <157:
                return "orange";
            default:
                return "red";
        }    
    }
    L.geoJson(data, {
        pointToLayer: function(feature, latlng){
            return L.circleMarker(latlng);
        },
        style: function(feature) {
            return{
                color: "black",
                fillColor: circleColor(feature.properties.Wind_mph),
                fillOpacity: 0.65,
                weight: 0.5,
                radius: (feature.properties.Wind_mph) /5
            };
        },
        onEachFeature: function(feature, layer){
            layer.bindPopup(`<strong>Status:</strong> ${feature.properties.Status}<br><strong>Name:</strong> ${feature.properties.Name}<br><strong>Wind Speed:</strong> ${feature.properties.Wind_mph}`);
        }
    }).addTo(hurricanes);
    hurricanes.addTo(myMap);

    //set up legend for hurricane magnitude, using scale from above
    var legend = L.control({position: "bottomright"});
    legend.onAdd = function(){
        var div = L.DomUtil.create('div','info legend');
        var magnitudeLabels = [1,2,3,4,5];

        var legendInfo = "<strong><center>Storm<br>Magnitude</center></strong" + "<div class=\"labels\">" + "</div>";

        div.innerHTML = legendInfo;

        for( var i = 0; i<magnitudeLabels; i++) {
            div.innerHTML +=
            '<i style="background:'+ circleColor(magnitudeLabels[i]) + '"></i> ' +
            magnitudeLabels[i] + (magnitudeLabels[i + 1] ? ' &ndash; ' + magnitudeLabels[i + 1] + '<br>' : ' +');
        }
        return div;
    }
})