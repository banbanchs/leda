$ ->
  xdata = []
  pm25_data = []
  aqi_data = []
  myChart = echarts.init(document.getElementById('charts'))
  myChart.showLoading
    text: '正在努力的读取数据中...'
  $.getJSON '/api/pm25/', (data) ->
    for i in data
      xdata.unshift i.time[-8..-7] + '时'
      if i.pm2_5 != -1
        pm25_data.unshift i.pm2_5
      else
        pm25_data.unshift '-'
      if i.aqi != -1
        aqi_data.unshift i.aqi
      else
        aqi_data.unshift '-'
    myChart.hideLoading()
    option =
      title:
        text: '最近12小时pm2.5含量的变化',
        # subtext: '纯属虚构'
      tooltip:
        trigger: 'axis'
      legend:
        data:['PM2.5', 'AQI']
      toolbox:
        show: true,
        feature:
          mark: {show: true},
          dataView: {show: true, readOnly: false},
          magicType: {show: true, type: ['line', 'bar']},
          restore: {show: true},
          saveAsImage: {show: true}
      calculable: true,
      xAxis: [
          type: 'category',
          data: xdata
      ],
      yAxis: [
          type: 'value'
      ],
      series: [
        {
          name:'PM2.5'
          type:'bar'
          data: pm25_data
          markLine:
            data: [
              {type: 'average', name: '平均值'}
            ]
        }
        {
          name: 'AQI'
          type: 'bar'
          data: aqi_data
          markPoint:
            data: [
              {type: 'max', name: '最大值'}
              {type: 'min', name: '最小值'}
            ]
          markLine:
            data: [
              {type: 'average', name: '平均值'}
            ]
        }
      ]

    myChart.setOption option