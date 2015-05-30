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
    },
    /**
     * Handle air data and separate it to three array.
     *
     * @param {Array} airData
     * @return {Ojbect} The echarts data
     * @return {Array} return.x X axis
     * @return {Array} return.pm25 The pm25 data array
     * @return {Array} return.aqi The aqi data array
     *
     */
    handleAirData: function(airData) {
      var i, len, single;
      var xAxis = [];
      var pm25Data = [];
      var aqiData = [];
      for (i = 0, len = airData.length; i < len; i++) {
        single = airData[i];
        xAxis.unshift(single.time.slice(-9, -7) + '时');
        if (single.pm2_5 !== -1) {
          pm25Data.unshift(single.pm2_5);
          aqiData.unshift(single.aqi);
        } else {
          pm25Data.unshift('-');
          aqiData.unshift('-');
        }
      }
      return {
        x: xAxis,
        pm25: pm25Data,
        aqi: aqiData
      }
    }
  };
});
