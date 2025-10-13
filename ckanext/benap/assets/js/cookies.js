ckan.module('cookies', function (jQuery, _) {
  return {
    initialize: function () {
      function setCookie(name, value, days) {
        var expires = '';
        if (days) {
          var date = new Date();
          date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
          console.log = 'Aantal seconden:' + expires;
          expires = '; expires=' + date.toUTCString();
        }
        document.cookie = name + '=' + value + expires + '; path=/';
      }

      function getCookie(name) {
        var nameEQ = name + '=';
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
          var c = ca[i];
          while (c.charAt(0) == ' ') c = c.substring(1, c.length);
          if (c.indexOf(nameEQ) == 0)
            return c.substring(nameEQ.length, c.length);
        }
        return null;
      }

      function transportDataObjectLiteral(
        necessary,
        functional,
        analytical,
        marketing
      ) {
        return {
          necessary: necessary,
          functional: functional,
          analytical: analytical,
          marketing: marketing,
        };
      }

      function readTransportDataCookie(name) {
        var result = document.cookie.match(new RegExp(name + '=([^;]+)'));
        if (result) {
          const resultArray = result[1].split('|');
          result = transportDataObjectLiteral(...resultArray);
        }
        return result;
      }

      function setAllCookies(x) {
        const x_write =
          x.necessary +
          '|' +
          x.functional +
          '|' +
          x.analytical +
          '|' +
          x.marketing;
        if (x.functional) {
          setCookie('transportdata_cookies', x_write, 365);
        } else {
          setCookie('transportdata_cookies', x.necessary, false);
        }
        if (x.analytical) {
          window.dataLayer = window.dataLayer || [];
          function gtag() {
            dataLayer.push(arguments);
          }
          gtag('js', new Date());
          gtag('config', 'UA-153119613-1');
          window['ga-disable-UA-153119613-1'] = false;
        } else {
          let expires = '';
          let date = new Date();
          date.setTime(date.getTime() + -1 * 24 * 60 * 60 * 1000);
          expires = '; expires=' + date.toUTCString();
          document.cookie =
            '_ga' +
            '=' +
            '' +
            expires +
            '; path=/; domain=.ec2-63-33-90-161.eu-west-1.compute.amazonaws.com';
          document.cookie =
            '_gid' +
            '=' +
            '' +
            expires +
            '; path=/; domain=.ec2-63-33-90-161.eu-west-1.compute.amazonaws.com';
          document.cookie =
            '_gat_gtag_UA-153119613-1' +
            '=' +
            '' +
            expires +
            '; path=/; domain=.ec2-63-33-90-161.eu-west-1.compute.amazonaws.com';
          window['ga-disable-UA-153119613-1'] = true;
        }
        if (!x.marketing) {
          setCookie('r/collect', '', -1);
        }
      }

      let cookie = readTransportDataCookie('transportdata_cookies');
      if (cookie && cookie.analytical) {
        window.dataLayer = window.dataLayer || [];
        function gtag() {
          dataLayer.push(arguments);
        }
        gtag('js', new Date());
        gtag('config', 'UA-153119613-1');
        window['ga-disable-UA-153119613-1'] = false;
      } else {
        let expires = '';
        let date = new Date();
        date.setTime(date.getTime() + -1 * 24 * 60 * 60 * 1000);
        expires = '; expires=' + date.toUTCString();
        document.cookie =
          '_ga' +
          '=' +
          '' +
          expires +
          '; path=/; domain=.ec2-63-33-90-161.eu-west-1.compute.amazonaws.com';
        document.cookie =
          '_gid' +
          '=' +
          '' +
          expires +
          '; path=/; domain=.ec2-63-33-90-161.eu-west-1.compute.amazonaws.com';
        document.cookie =
          '_gat_gtag_UA-153119613-1' +
          '=' +
          '' +
          expires +
          '; path=/; domain=.ec2-63-33-90-161.eu-west-1.compute.amazonaws.com';
        window['ga-disable-UA-153119613-1'] = true;
      }
      if (cookie && !cookie.marketing) {
        setCookie('r/collect', '', -1);
      }

      function labelText(event) {
        let enabledText = 'Enabled';
        let disabledText = 'Disabled';
        let regexp = /^.*\/nl/;
        if (regexp.test(event.target.baseURI)) {
          enabledText = 'Ingeschakeld';
          disabledText = 'Uitgeschakeld';
        }

        if (event.target.checked == true) {
          event.target.previousElementSibling.innerText = enabledText;
        } else {
          event.target.previousElementSibling.innerText = disabledText;
        }
      }

      const checkboxF = document.getElementById('functional');
      if (checkboxF) {
        checkboxF.onclick = (event) => {
          labelText(event);
        };
      }
      const checkboxA = document.getElementById('analytical');
      if (checkboxA) {
        checkboxA.onclick = (event) => {
          labelText(event);
        };
      }
      const checkboxM = document.getElementById('marketing');
      if (checkboxM) {
        checkboxM.onclick = (event) => {
          labelText(event);
        };
      }

      if (!cookie || !cookie.necessary) {
        jQuery('#overlay-cookies').css('display', 'flex');
      }

      jQuery('#wrapper-cookies-2').hide();
      jQuery('#preferences').on('click', (event) => {
        jQuery('#wrapper-cookies-1').hide();
        jQuery('#wrapper-cookies-2').show();
      });

      jQuery('#overlay-cookies .accept-all').on('click', (event) => {
        const x = {
          necessary: true,
          functional: true,
          analytical: true,
          marketing: true,
          youtube: true,
        };
        setAllCookies(x);
        jQuery('#overlay-cookies').css('display', 'none');
      });

      jQuery('#accept-preferences').on('click', (event) => {
        const x = {
          necessary: jQuery('#necessary').is(':checked'),
          functional: jQuery('#functional').is(':checked'),
          analytical: jQuery('#analytical').is(':checked'),
          marketing: jQuery('#marketing').is(':checked'),
        };
        setAllCookies(x);
        jQuery('#overlay-cookies').css('display', 'none');
      });

      const acc = document.getElementsByClassName('category-item-nav');
      for (let i = 0; i < acc.length; i++) {
        acc[i].addEventListener('click', function () {
          this.classList.toggle('active');
          const panel = this.nextElementSibling;
          if (panel.style.display === 'block') {
            panel.style.display = 'none';
          } else {
            panel.style.display = 'block';
          }
        });
      }
    },
  };
});

// crude one-time script for this consent button
ckan.module('youtube-consent-button', function ($, _) {
  return {
    initialize: function () {
      const src = this.options.youtubeSrc;
      const button = this.el;
      const consentElement = $('[youtube-consent-button-iframe]');
      var iframe = $('[youtube-consent-button-iframe] iframe');

      button.on('click', function () {
        iframe.attr('src', src);
        consentElement.show();
        iframe.show();
        button.hide();
      });
    },
  };
});
