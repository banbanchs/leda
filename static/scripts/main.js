require.config({
  baseUrl: '/static/scripts/',
  paths: {
    "jquery": "//dn-staticfile.qbox.me/jquery/1.11.1/jquery.min"
  }
});

require(['render'], function(render) {
  render.renderWidget();
  render.renderOverview();
  render.renderChart('charts');
});

require(['dom'], function(dom) {
  dom.bindNav();
});

