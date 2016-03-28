function htmlEscape(str) {
    return String(str)
            .replace(/&/g, '&amp;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
}

function htmlDscape(str) {
    return String(str)
            .replace(/&amp;/g, "&")
            .replace(/&quot;/g, "\\\"")
            .replace(/&#39;/g, "\\\'")
            .replace(/&lt;/g, "<")
            .replace(/&gt;/g, ">");
};

var bodyE = document.getElementsByTagName('body')[0]
bodyE.innerHTML = bodyE.innerHTML + '<div style="clear:both"></div>\n\
<iframe id="tiy_iframe_code" style="display:none;position:fixed;background-color:#EEEEEE"></iframe>\n'

+

'<div id="tiy_iframe_code_forDiv" style="display:none;position:fixed;background-color:#EEEEEE">\
\
<div style="width:100%; height:13px; background-color:yellow">实验</div>\
<iframe id="tiyiframe_iframe_forDiv" style="width:100%;height:40%;background-color:#ffffff">\
</iframe>\
<p style="height:8%;margin:0px; padding:0px">编辑代码：\
    <input id="tiyiframe_button_forDiv" type="button" value="查看效果" style="float:right; margin-right:20px"></input>\
</p>\
<textarea id="tiyiframe_textarea_forDiv" style="width:90%; height:35%;"></textarea>\
</br>\
</div>\n\
\
<input id="tiyiframe_button_X" type="button" value="X" \
style="position:fixed; display:none; top:11px;right:19px;width:18px; height:18px;background-color:red"></input>\
<div id="resizeImg" style="cursor:ne-resize;display:none;position:fixed;width:57px; height:57px;\
background-image:url(../i/scale.png);background-repeat:no-repeat;background-position:center center;"></div>'


tiy = {}
tiy.f = 0;
tiy.runHelp = function(tiy_iframe_code){//运行tiy 代码通过tiy_*.html文件载入
	tiy_iframe_code.style.top = "10px";
	tiy_iframe_code.style.right = "18px";
	tiy_iframe_code.style.display = "block"

  var button_x = document.getElementById("tiyiframe_button_X");
  button_x.style.display = "block";

  var resizeImg = document.getElementById("resizeImg");
	resizeImg.style.top = 10 + parseInt(tiy_iframe_code.height.replace("px","")) - 37 + "px";
	resizeImg.style.right = 18 + parseInt(tiy_iframe_code.width.replace("px","")) - 37 + "px";
	resizeImg.style.display = "block";

	var clientX_old, clientY_old;
	resizeImg.onmousedown = function(e){
		clientX_old = e.clientX
		clientY_old = e.clientY

		if(parseInt(resizeImg.style.width) < 1200){
			resizeImg.style.width = parseInt(resizeImg.style.width) + 1200 + "px";
			resizeImg.style.height = parseInt(resizeImg.style.height) + 1200 + "px";
			resizeImg.style.right = parseInt(resizeImg.style.right) - 600 + "px";
			resizeImg.style.top = parseInt(resizeImg.style.top) - 600 + "px";
		}

		resizeImg.onmousemove =  function (e){
			var diffX = e.clientX - clientX_old;
			var diffY = e.clientY - clientY_old;

      var new_width = parseInt(tiy_iframe_code.width.replace("px","")) - diffX + "px";
      var new_height = parseInt(tiy_iframe_code.height.replace("px","")) + diffY + "px";

      //if(new_width == "300px" && ( new_height == "400px" || new_height == "401px"))
      //  new_width == "301px";//避免触发iframe的onresize事件

			tiy_iframe_code.width  = new_width;
			tiy_iframe_code.height = new_height;
      tiy_iframe_code.style.width = new_width;
      tiy_iframe_code.style.height = new_height;

			resizeImg.style.right = parseInt(resizeImg.style.right) - diffX + "px";
			resizeImg.style.top = parseInt(resizeImg.style.top) + diffY + "px";

			clientX_old = e.clientX;
			clientY_old = e.clientY;
		}
	}
	resizeImg.onmouseup = function(e){
		resizeImg.onmousemove = null;
		if(parseInt(resizeImg.style.width) > 1200){
			resizeImg.style.width = parseInt(resizeImg.style.width) - 1200 + "px";
			resizeImg.style.height = parseInt(resizeImg.style.height) - 1200 + "px";
			resizeImg.style.right = parseInt(resizeImg.style.right) + 600 + "px";
			resizeImg.style.top = parseInt(resizeImg.style.top) + 600 + "px";
		}
	}
}

tiy.closeAll = function(){
  var tiy_iframe_code = document.getElementById("tiy_iframe_code");
  tiy_iframe_code.style.display = "none";
  tiy_iframe_code = document.getElementById("tiy_iframe_code_forDiv");
  tiy_iframe_code.style.display = "none";

  var resizeImg = document.getElementById("resizeImg");
  resizeImg.style.display = "none";

  var button_x = document.getElementById("tiyiframe_button_X");
  button_x.style.display = "none";
}

tiy.run = function(cmdStr){
  tiy.closeAll();
  var tiy_iframe_code = document.getElementById("tiy_iframe_code");
  tiy_iframe_code.src = "../tiy/tiy_" + cmdStr.substring(0, cmdStr.search("_")) + ".html#" + cmdStr;

  tiy_iframe_code.width = "300px";
	tiy_iframe_code.height = 400 + tiy.f + "px";  //修改iframe大小以触发onresize事件，执行相应功能
	tiy.f = tiy.f == 0 ? 1 : 0;
  tiy.runHelp(tiy_iframe_code);
}

tiy.runLs = function(scriptStr){//运行tiy 代码通过参数传入
  tiy.closeAll();
  var tiy_iframe_code = document.getElementById("tiy_iframe_code_forDiv");
  tiy_iframe_code.width = "300px";
	tiy_iframe_code.height = "400px";
  tiy_iframe_code.style.width = "300px";
	tiy_iframe_code.style.height = "400px";  //修改iframe大小以触发onresize事件，执行相应功能
  tiy.runHelp(tiy_iframe_code);

  ;(function(){
    var htmlStr =
'<html>\n\
<head>\n\
</head>\n\
<body>\n\
<script>\n'
    + scriptStr   //.replace(/'/g,'\\\'').replace(/"/g,"\\\"").replace(/\r\n/g, "\\r\\n").replace(/\r/g, "\\r").replace(/\n/g, "\\n");
    +
'\n</script>\n\
</body>\n\
</html>\n';

      var iframeTarget = document.getElementById("tiyiframe_iframe_forDiv");
      var textareaE = document.getElementById("tiyiframe_textarea_forDiv");
      textareaE.innerText = htmlStr;
      var buttonE = document.getElementById("tiyiframe_button_forDiv");

      buttonE.onclick = function(){
          var newDoc=iframeTarget.contentDocument.open("text/html","replace");
          newDoc.write(textareaE.value);
          newDoc.close();
      };
      buttonE.onclick();
    })();
}

var tiyiframe_button_X = document.getElementById("tiyiframe_button_X");
tiyiframe_button_X.onclick = tiy.closeAll;


;(function(){
    var menuContent = document.querySelector("div#navsecond div#course");
    var f_onclick = function(event){//菜单内容收放按钮的点击事件
      if(menuContent.style.display == ""){
        menuContent.style.display = "block";
        menuContent.firstElementChild.style.marginTop = "0px";
      }
        else menuContent.style.display = "";
    }

    var firstElementChild_MarginTop = parseInt(menuContent.firstElementChild.style.marginTop.replace("px", "")) || 0;
    menuContent.firstElementChild.style.marginTop = firstElementChild_MarginTop + "px";

    var oldY = -10000;//一个不可能的值
    var oriHeight = menuContent.style.height;
    var oriHeight2 = menuContent.clientHeight;

    var f_onTouchStart = function(touchEvent){
        oldY = -10000;//touchEvent.touches[0].clientY;
    }
    var f_onTouchMove = function(touchEvent){//菜单项内容的滑移事件
      touchEvent.preventDefault();
      var newY = touchEvent.touches[0].clientY;
      if(oldY != -10000){
        var diffY = newY - oldY;
        if(firstElementChild_MarginTop + diffY < 60 && firstElementChild_MarginTop + diffY + menuContent.scrollHeight > 60){
          firstElementChild_MarginTop = firstElementChild_MarginTop + diffY;
            menuContent.firstElementChild.style.marginTop = firstElementChild_MarginTop + "px";
        }
      }
      oldY = newY;
    }
    var f_onTouchEnd = function(touchEvent){
        oldY = -10000;
    }

    var element =  document.querySelector("div#navsecond div#courseMenuKey")
    element.onclick = f_onclick;
    menuContent.ontouchmove = f_onTouchMove;
    menuContent.ontouchstart = f_onTouchStart;
    menuContent.ontouchend = f_onTouchEnd;
})();

;(function(){
    var href = location.href;
    var element = null;
    if(href.indexOf("/html/") >= 0 || href.indexOf("/domref/") >= 0 )
        element = document.querySelector('header nav a[href="/html/html_intro.htm"]');
    else if(href.indexOf("/css/") >= 0 || href.indexOf("/cssref/") >= 0)
        element = document.querySelector('header nav a[href="/css/css_intro.htm"]');
    else if(href.indexOf("/js/") >= 0 || href.indexOf("/jsref/") >= 0)
        element = document.querySelector('header nav a[href="/js/js_intro.htm"]');
    else
        element = document.querySelector('header nav a[href="/other/index.htm"]');;
    element.className  = "currentHeaderNavA";
})();
