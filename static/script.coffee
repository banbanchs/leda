setCookie = (name, value, days) ->
  if days
    date = new Date()
    date.setTime date.getTime() + (days * 24 * 60 * 60 * 1000)
    expires = "; expires=#{date.toGMTString}"
  else
    expires = ""
  console.log "success#{value}"
  document.cookie = "#{name}=#{value} #{expires}; path=/"

getCookie = (name) ->
  nameEQ = "#{name}="
  cookies = document.cookie.split "; "
  for cookie in cookies
    if cookie.indexOf("#{name}=") is 0
      return cookie[name.length+1..]
  null

renderChart = (city) ->
  xdata = []
  pm25_data = []
  aqi_data = []
  myChart = echarts.init(document.getElementById('charts'))
  myChart.showLoading
    text: '正在努力的读取数据中...'
  $.getJSON "/api/pm25/#{city}/lastest/", (data) ->
    for i in data
      xdata.unshift i.time[-9..-8] + '时'
      if i.pm2_5 != -1
        pm25_data.unshift i.pm2_5
        aqi_data.unshift i.aqi
      else
        pm25_data.unshift '-'
        aqi_data.unshift '-'
    myChart.hideLoading()
    option =
      title:
        text: '最近12小时空气质量的变化',
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
 

$ ->
  city = getCookie('city')
  availableCity = ['Guangzhou', 'Beijing', 'Shanghai', 'Chengdu', 'Shenyang']
  if city not in availableCity
    city = 'Guangzhou'
  # console.log city
  renderChart city

  # listen city click
  # FIXME: clean this quick and dirty code
  $('#Guangzhou').click () ->
    setCookie 'city', 'Guangzhou', 7
    renderChart 'Guangzhou'
    return false
  $('#Beijing').click () ->
    setCookie 'city', 'Beijing', 7
    renderChart 'Beijing'
    return false
  $('#Shanghai').click () ->
    setCookie 'city', 'Shanghai', 7
    renderChart 'Shanghai'
    return false
  $('#Shenyang').click () ->
    setCookie 'city', 'Shenyang', 7
    renderChart 'Shenyang'
    return false
  $('#Chengdu').click () ->
    setCookie 'city', 'Chengdu', 7
    renderChart 'Chengdu'
    return false