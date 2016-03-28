;(function(){
    var scriptE = document.getElementById("replaceDivMainContent");
    if(scriptE === null){
        return;
    }
    var xhr = new XMLHttpRequest();
    var path = window.location.pathname;
    path = path + "Data"
    xhr.open("GET", path);
    xhr.send();
    xhr.onload = function (e) {
        var result = ooo(xhr.responseText)
        scriptE.outerHTML = result.htmlStr;
        result.scriptUrls.map(function(value){
            var scriptE = document.createElement("script")
            scriptE.src = value;
            document.body.appendChild(scriptE);
        });   
    }
})();

;(function(){
    var xhr = new XMLHttpRequest();
    var path = "/mainData/menuData";
    xhr.open("GET", path);
    xhr.send();
    xhr.onload = function (e) {
        var scriptE = document.getElementById("replaceDivMenu");
        var result = ooo(xhr.responseText)
        scriptE.outerHTML = result.htmlStr;    
    }
})();


function  ooo(str){
    var reg = /<script\s*[^>]*src\s*=\s*(["'])([^"']*)(\1)[^>]*><\/script>/g;
    var result;
    var scriptUrls = []
    while( (result = reg.exec(str)) !== null){
        var url = result[2];
        if(url.indexOf("./") != -1){
            var path = window.location.pathname;
            path = path.replace(/\/[^\/]*$/, "/");
            url = path + url.replace("./", "");
        }
        scriptUrls.push(url);
    }
    
    return {
        htmlStr:str.replace(reg, ""),
        scriptUrls:scriptUrls
    }
}