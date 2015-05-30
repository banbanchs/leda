define('cookies', function() {
  function safeDecodeURIComponent(str) {
    try {
      return decodeURIComponent(str);
    } catch (e) {
      return str;
    }
  }

  return {

    /**
     * Get cookie value by key.
     * @param {String} key
     * @return {String} value
     *
     */
    get: function(key) {
      var i, len, cookie, value;
      var name = key + '=';
      var cookieArray = document.cookie.split('; ');

      for (i = 0, len = cookieArray.length; i < len; i++) {
        cookie = safeDecodeURIComponent(cookieArray[i]);
        if (cookie.indexOf(name) === 0) {
          value = cookie.slice(name.length);
        }
      }

      return value;
    },
    getObject: function(key) {
    },
    put: function(key, value, options) {
      options = options || {};
      if (options.expires === undefined) {
        options.expires = 7;
      }
      if (typeof options.expires === 'number') {
        var days = options.expires;
        var t = options.expires = new Date();
        t.setDate(t.getDate() + days);
      }

      return document.cookie = [
        encodeURIComponent(key) + '=',
        encodeURIComponent(value),
        options.expires ? '; expires=' + options.expires.toUTCString() : '',
        options.path ? '; path=' + options.path : '',
        options.domain ? '; domain=' + options.domain : '',
        options.secure ? '; secure' : ''
      ].join('');
    },
    putObject: function(key, value) {
      var result;

      if (value !== undefined && typeof value !== 'string') {
        result = JSON.stringify(value);
      }
      return this.put(key, value);
    },
    remove: function(key) {
      return this.put(key, '', { expires: -1 });
    }
  };
});
