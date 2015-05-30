define('dom', ['jquery', 'cookies', 'map'], function($, cookies, map) {
  return {
    setWidgetValue: function(type, level, value) {
      var $widget = $('#widget-' + type);
      var degree, degreeText;
      switch (level) {
        case -1:
          degree = 'nodata';
          degreeText = '无数据';
          break;
        case 1:
          degree = 'good';
          degreeText = '优';
          break;
        case 2:
          degree = 'moderate';
          degreeText = '良';
          break;
        case 3:
        case 4:
          degree = 'middle';
          degreeText = '中轻度污染';
          break;
        case 5:
        case 6:
        default:
          degree = 'bad';
          degreeText = '中重度污染';
          break;
      }
      $widget.addClass('widget-' + degree)
        .find('.widget-value').text(value).end()
        .find('.widget-value-description').text(degreeText);
    },
    bindNav: function() {
      $('#cities').delegate('a', 'click', function(event) {
        event.preventDefault();
        var cityName = this.id;
        cookies.put('city', cityName);
        console.log(cityName);
        return false;
      });
    },
    }
  };
});
