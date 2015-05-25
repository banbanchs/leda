define('data', ['jquery'], function($) {

  return {
    getCity: function(cityName, handler) {
      var api = "/api/pm25/" + cityName + "/latest/";
      return $.getJSON(api, handler)
        .fail(function() {
          if (console && console.log) {
            console.log("$.getJSON failed.");
          }
        });
    }
  };
});
