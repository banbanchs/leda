define ['jquery', 'semantic', 'utils', 'charts'], ($, semantic, utils, charts) ->

  city = utils.getCookie('city')
  availableCity = ['Guangzhou', 'Beijing', 'Shanghai', 'Chengdu', 'Shenyang']
  if city not in availableCity
    city = 'Guangzhou'
  charts.renderChart city

  # listen city click
  # FIXME: clean this quick and dirty code
  $('#Guangzhou').click () ->
    utils.setCookie 'city', 'Guangzhou', 7
    charts.renderChart 'Guangzhou'
    return false
  $('#Beijing').click () ->
    utils.setCookie 'city', 'Beijing', 7
    charts.renderChart 'Beijing'
    return false
  $('#Shanghai').click () ->
    utils.setCookie 'city', 'Shanghai', 7
    charts.renderChart 'Shanghai'
    return false
  $('#Shenyang').click () ->
    utils.setCookie 'city', 'Shenyang', 7
    charts.renderChart 'Shenyang'
    return false
  $('#Chengdu').click () ->
    utils.setCookie 'city', 'Chengdu', 7
    charts.renderChart 'Chengdu'
    return false
  $(".ui.dropdown").dropdown
    on: 'hover'
  return