define ['jquery', 'semantic', 'utils', 'charts'], ($, semantic, utils, charts) ->

  city = utils.getCookie('city')
  availableCity = ['Guangzhou', 'Beijing', 'Shanghai', 'Chengdu', 'Shenyang']
  if city not in availableCity
    city = 'Guangzhou'
  charts.renderChart city

  # listen city click
  for city in availableCity
    $("##{city}").click () ->
      utils.setCookie 'city', city, 7
      return false
  $(".ui.dropdown").dropdown
    on: 'hover'
  return
