/* CKAN module: initializes a Leaflet map for display snippets.
 * Usage in template:
 *   <div data-module="map-display" 
 *      data-module-geojson="{{ data[field.field_name]|safe }}"
 *      style="height: 180px; "></div>
 * {% asset 'benap/leaflet-maps-js' %}
 * {% asset 'benap/leaflet-maps-css' %}
 */
ckan.module('map-display', function ($) {
  return {
    options: {
      geojson: "",
    },
      initialize: function () {
        var el = this.el[0];
        var mymap = L.map(el).setView([50.859933, 4.351969], 7);
        L.tileLayer('https://{s}.tile.osm.org/{z}/{x}/{y}.png', {
             attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
         }).addTo(mymap);
    
        var geojsonFeature = this.options.geojson ;
    
        var geoJSONLayer = L.geoJSON(geojsonFeature);
        geoJSONLayer.addTo(mymap);
        mymap.fitBounds(geoJSONLayer.getBounds());
    
      }
    }
});



