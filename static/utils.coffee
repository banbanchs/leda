define () ->
  setCookie = (name, value, days) ->
    if days
      date = new Date()
      date.setTime date.getTime() + (days * 24 * 60 * 60 * 1000)
      expires = "; expires=#{date.toGMTString}"
    else
      expires = ""
    # console.log "success#{value}"
    document.cookie = "#{name}=#{value} #{expires}; path=/"
    return

  getCookie = (name) ->
    nameEQ = "#{name}="
    cookies = document.cookie.split "; "
    for cookie in cookies
      if cookie.indexOf("#{name}=") is 0
        return cookie[name.length+1..]
    return

  return {
    setCookie: setCookie
    getCookie: getCookie
  }