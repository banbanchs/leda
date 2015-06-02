define('render', ['cookies', 'data', 'dom', 'charts'], function(cookies, data, dom, charts) {
  function getCityName() {
    var defaultCity = 'Guangzhou';
    var city = cookies.get('city');
    var availableCity = ['Guangzhou', 'Beijing', 'Shanghai', 'Chengdu', 'Shenyang'];
    if (availableCity.indexOf(city) < 0) {
      city = defaultCity;
      cookies.put('city', city);
    }
    return city;
  }
  var currentCity = getCityName();
  var promiseData = $.when(data.getCity(currentCity));

  var renderWidget = function() {
    promiseData.then(function(airData) {
      dom.setWidgetValue('pm25', airData[0].level, airData[0].pm2_5);
      dom.setWidgetValue('aqi', airData[0].level, airData[0].aqi);
    });
  };
  var renderChart = function(chartId) {
    if (typeof chartId !== 'string') {
      chartId = 'charts';
    }
    var ex = echarts;
    myChart = echarts.init(document.getElementById(chartId));
    myChart.showLoading({
      text: '正在努力的读取数据中...'
    });
    promiseData.then(function(airData) {
      var handledData = data.handleAirData(airData);
      var option = charts.makeEchartOption(handledData);
      myChart.hideLoading();
      return myChart.setOption(option);
    });
  };
  var renderOverview = function() {
    promiseData.then(function(airData) {
      dom.setAirOverview(currentCity, airData[0].level, airData[0].time);
    });
  };
  var reRenderAll = function() {
    currentCity = getCityName();
    promiseData = $.when(data.getCity(currentCity));
    renderWidget();
    renderOverview();
    renderChart();
  };

  return {
    renderWidget: renderWidget,
    renderOverview: renderOverview,
    renderChart: renderChart,
    reRenderAll: reRenderAll
  };
});
