<template>
  <div id="he-plugin-simple"></div>
</template>

<script>
export default {
  created() {
    //和风天气插件调用
    window.WIDGET = {
      CONFIG: {
        modules: "02",
        background: "5",
        tmpColor: "#FFFFFF",
        tmpSize: "22",
        aqiColor: "#FFFFFF",
        aqiSize: "30",
        weatherIconSize: "90",
        alertIconSize: "18",
        padding: "10px 10px 10px 10px",
        shadow: "0",
        language: "auto",
        fixed: "false",
        vertical: "center",
        horizontal: "center",
        key: "bb0bd610ef8e4dd0b28f6920d11d41a8",
      },
    };
    (function (d) {
      var c = d.createElement("link");
      c.rel = "stylesheet";
      //   c.href = "";
      c.href =
        "https://widget.heweather.net/simple/static/css/he-simple.css?v=1.4.0";
      var s = d.createElement("script");
      //   s.src = "../static/js/he-simple.js";
      s.src =
        "https://widget.heweather.net/simple/static/js/he-simple.js?v=1.4.0";
      var sn = d.getElementsByTagName("script")[0];
      sn.parentNode.insertBefore(c, sn);
      sn.parentNode.insertBefore(s, sn);
    })(document);
  },
};
</script>
