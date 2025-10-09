/*
 * use: <div style="height: 280px; " data-module="map-form" 
 *          data-module-input-id="field-{{field.field_name}}" 
 *          ></div>
 * {% asset 'benap/leaflet-maps-js' %}
 * {% asset 'benap/leaflet-maps-css' %}
 */
ckan.module("map-form", function ($) {
  return {
    options: {
      inputId: "",
    },
    initialize: function () {
      var el = this.el[0];

      var map = L.map(el).setView([50.859933, 4.351969], 7);
      L.tileLayer('https://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution:
          '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(map);

      var drawnItems = new L.FeatureGroup();
      map.addLayer(drawnItems, { crs: L.CRS.EPSG4326 });
      map.pm.addControls({
        position: "topleft",
        drawMarker: false,
        drawCircleMarker: false,
        drawPolyline: false,
        drawRectangle: true,
        drawPolygon: false,
        drawCircle: false,
        editMode: false,
        dragMode: false,
        cutPolygon: false,
        removalMode: true,
      });

      var input_field = document.getElementById(this.options.inputId);
      if (input_field.value) {
        var layer = L.geoJSON(JSON.parse(input_field.value));
        drawnItems.addLayer(layer);
      }

      map.on("pm:create", (e) => {
        var layer = e.layer;
        var layerGeoJSON = layer.toGeoJSON().geometry;
        drawnItems.clearLayers();
        drawnItems.addLayer(layer);
        input_field.value = JSON.stringify(layerGeoJSON);
      });

      map.on("pm:remove", (e) => {
        layer = e.layer;
        input_field.value = null;
      });
    },
  };
});
