require.config({
  baseUrl: '/static/scripts/',
  paths: {
    "jquery": "//dn-staticfile.qbox.me/jquery/2.1.0/jquery.min"
  }
});

require(['render'], function(render) {
  render.renderWidget();
  render.renderChart('charts');
});

require(['dom'], function(dom) {
  dom.bindNav();
});

