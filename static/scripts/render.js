define('render', ['cookies', 'data', 'dom'], function(cookies, data, dom) {
  var defaultCity = 'Guangzhou';
  var currentCity = cookies.get('city');
  var availableCity = ['Guangzhou', 'Beijing', 'Shanghai', 'Chengdu', 'Shenyang'];
  if (availableCity.indexOf(currentCity) < 0) {
    currentCity = defaultCity;
    cookies.put('city', currentCity);
  }

  return {
    renderWidget: function() {
      data.getCity(currentCity, function(airData) {
        dom.setWidgetValue('pm25', airData[0].level, airData[0].pm2_5);
        dom.setWidgetValue('aqi', airData[0].level, airData[0].aqi);
      });
    }
  };
});
