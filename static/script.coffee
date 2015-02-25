define ['jquery', 'semantic', 'utils', 'charts'], ($, semantic, utils, charts) ->

  currentCity = utils.getCookie('city')
  availableCity = ['Guangzhou', 'Beijing', 'Shanghai', 'Chengdu', 'Shenyang']
  currentCity = 'Guangzhou' if currentCity not in availableCity
  charts.renderChart currentCity

  # listen city click
  for city in availableCity
    $("##{city}").click () ->
      utils.setCookie 'city', city, 7
      return false
  $(".ui.dropdown").dropdown
    on: 'hover'
  return
