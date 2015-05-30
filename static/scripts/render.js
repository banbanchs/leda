define('render', ['cookies', 'data', 'dom', 'charts'], function(cookies, data, dom, charts) {
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
        dom.setAirOverview(currentCity, airData[0].level);
      });
    },
    renderChart: function(chartId) {
      if (typeof chartId !== 'string') {
        chartId = 'charts';
      }
      var ex = echarts;
      myChart = echarts.init(document.getElementById(chartId));
      myChart.showLoading({
        text: '正在努力的读取数据中...'
      });
      data.getCity(currentCity, function(airData) {
        var handledData = data.handleAirData(airData);
        var option = charts.makeEchartOption(handledData);
        myChart.hideLoading();
        return myChart.setOption(option);
      });
    }
  };
});
