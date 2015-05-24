define(['jquery'], function($) {

  return {
    getCity: function(cityName, handler) {
      var api = "/api/pm25/" + cityName + "/latest/";
      return $.getJSON(api, handler);
    }
  };
});
