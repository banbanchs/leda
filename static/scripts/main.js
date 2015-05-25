require.config({
  baseUrl: '/static/scripts/',
  paths: {
    "jquery": "//dn-staticfile.qbox.me/jquery/2.1.0/jquery.min"
  }
});

// require(['script']);
require(['data', 'dom'], function(data, dom) {
  data.getCity('Guangzhou', function(data) {
    dom.setWidgetValue('pm25', data[0].level, data[0].pm2_5);
    dom.setWidgetValue('aqi', data[0].level, data[0].aqi);
  });
});
