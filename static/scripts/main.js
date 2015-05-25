require.config({
  baseUrl: '/static/scripts/',
  paths: {
    "jquery": "//dn-staticfile.qbox.me/jquery/2.1.0/jquery.min"
  }
});

// require(['script']);
require(['render'], function(render) {
  render.renderWidget();
});
