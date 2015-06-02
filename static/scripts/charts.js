define(['jquery', 'data'], function($, data) {

  return {
    makeEchartOption: function(handledData) {
      return {
        title: {
          text: '最近12小时空气质量指数AQI的变化趋势'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: ['PM2.5', 'AQI']
        },
        toolbox: {
          show: true,
          feature: {
            mark: {
              show: true
            },
            dataView: {
              show: true,
              readOnly: false
            },
            magicType: {
              show: true,
              type: ['line', 'bar']
            },
            restore: {
              show: true
            },
            saveAsImage: {
              show: true
            }
          }
        },
        calculable: true,
        xAxis: [
        {
          type: 'category',
          data: handledData.x
        }
        ],
        yAxis: [
        {
          type: 'value'
        }
        ],
        series: [
        {
          name: 'PM2.5',
          type: 'bar',
          data: handledData.pm25,
          markLine: {
            data: [
            {
              type: 'average',
              name: '平均值'
            }
            ]
          }
        }, {
          name: 'AQI',
          type: 'bar',
          data: handledData.aqi,
          markPoint: {
            data: [
            {
              type: 'max',
              name: '最大值'
            }, {
              type: 'min',
              name: '最小值'
            }
            ]
          },
          markLine: {
            data: [
            {
              type: 'average',
              name: '平均值'
            }
            ]
          }
        }
        ]
      };
    }
  };
});
