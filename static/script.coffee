define ['jquery', 'semantic', 'utils', 'charts'], ($, semantic, utils, charts) ->

  currentCity = utils.getCookie('city')
  availableCity = ['Guangzhou', 'Beijing', 'Shanghai', 'Chengdu', 'Shenyang']
  currentCity = 'Guangzhou' if currentCity not in availableCity
  charts.renderChart currentCity

  # listen city click event
  $("div.city-list").delegate "a", "click", () ->
    city = @.id
    utils.setCookie 'city', city, 7
    charts.renderChart city
    return false

  $(".ui.dropdown").dropdown
    on: 'hover'
  return
