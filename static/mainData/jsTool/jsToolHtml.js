;(function() {
    function funcToWorkUrl(func){ //将func函数的体，转化为url所对应虚拟js文件的内容
        functionBodyRegx = /^[^{]+\{([\s\S]*)\}$/;
        var code = func.toString().match(functionBodyRegx)[ 1 ];
        var contentType = { type: "text/javascript; charset=utf-8" };
        var url = window.URL.createObjectURL(
            new Blob([code], contentType)
        );
        return url
    }

    function hhh(){//worker线程执行的内容，
        onmessage = function(event) {
            importScripts(event.data.currentDir + 'highlight/highlight.pack.js');
            var result = self.hljs.highlightAuto(event.data.data);
            postMessage(result.value);
        }
    }
    
    var code = document.querySelector('code');
    var url = funcToWorkUrl(hhh);
    var worker = new Worker(url);
    var currentDir = window.location.href.replace(/jsTool(.html)*$/, "");
    var innerHtmlAfterPM = "";
    var textContentToPM = "";//
    var canRand = true;
    
    function pM(){//定期运行的函数
        if(innerHtmlAfterPM != code.innerHTML && canRand ){
            canRand = false; //为防止渲染频率过高，要等渲染完成，并等待50ms后才可以开始下次渲染
            var selection = window.getSelection();
            var iii = selection.focusOffset;
            var currentFocusNode = selection.focusNode;
            if(currentFocusNode != null){
                var oldContentInFocus = currentFocusNode.textContent;
                currentFocusNode.textContent = oldContentInFocus.substring(0, iii) + '\1\1\1' + oldContentInFocus.substring(iii);//光标会跳,selection.focusNode也可能会变（ie11）
                selection.collapse(currentFocusNode, iii);//让光标及时回到正常位置防止跳动
                /*   已经再键盘事件中添加了\n以及避免了<div>生成
                code.innerHTML = code.innerHTML
                    .replace(/<div>/g, "\n").replace(/<\/div>/g ,"")   //代码去不会有div，div只能时键入换行产生。
                    .replace('\1\1\1\1', '<i id="focusflag" display:"none">\1\1\1</i>'); //光标会跳,在光标正确位置生成一个元素用于光标定位，传人高亮渲染时节点会去掉，节点内容会保留
                var focusflagE = document.getElementById("focusflag");
                selection.collapse(focusflagE, 0);//让光标及时回到正常位置防止跳动
                */
            }
            textContentToPM = code.textContent;
            worker.postMessage({
                currentDir: currentDir,
                data:code.textContent
            });
        }
        code.removeEventListener("keyup", pM);
    }

    worker.onmessage = function(event) { 
        //在将代码送去高亮渲染后，且更新到页面前。如果代码有变化，本次渲染结果不更新到页面，以防光标定位错误。
        //（由于用户不可能一直级快速输入，代码送去高亮渲染后，且更新到页面前，代码有极高的概率是没有发生变化，因此不对程序产生影响）

        if(textContentToPM == code.textContent){ 
            var data = event.data.replace('\1\1\1', '<i id="focusflag"></i>');
            code.contentEditable = "false";
            code.innerHTML = data;
            var focusflagE = document.getElementById("focusflag");
            if(focusflagE != null){
                var selection = window.getSelection();
                var range = selection.getRangeAt(0);
                range.setStartBefore(focusflagE);
                var nodeWillFocus = range.startContainer;
                var offSetWillFocus = range.startOffset;
                focusflagE.remove || (focusflagE.remove = focusflagE.removeNode);
                focusflagE.remove(); //
                code.contentEditable = "true";
                selection.collapse(nodeWillFocus, offSetWillFocus);
            }else{
                code.contentEditable = "true";
            }

            innerHtmlAfterPM = code.innerHTML;
        }
        setTimeout(function(){
            canRand = true;
        }, 50);
    }

    function textInputEventHandlerInCodeE(e){ //有中文输入法时，只有按enter后才会触发
        if(e.keyCode == 13){
            var textSelection = document.getSelection();
            var textRange = textSelection.getRangeAt(0);
            var textNodeLF = document.createTextNode("\n")
            textRange.insertNode(textNodeLF)
            textSelection.collapse(textNodeLF, 1);
            //code.normalize(); //相邻文本节点合并(ie11中会造成光标跳动，需要去掉）；去掉也没什么影响，高亮渲染后都会被替换掉。
            e.preventDefault();
            e.returnValue=false;
        }
        code.addEventListener("keyup", pM) //keyup事件在文本输入到文本框之后才触发。（防止输入中文时无法输入，只在textInput事件之后监听，且触发的函数要移除监听
        return false;
    }

    pM();
    //原来使用的是textInput事件（ie11中事件名为textinput），但该事件在ie11中无法响应单独的enter键键入。所以改为keypress事件。
    code.addEventListener("keypress", textInputEventHandlerInCodeE); 
})();

;(function() {
    var buttonE = document.getElementById("button");
    var codeE = document.querySelector('code');
    buttonE.onclick = function(){
        var scriptE = document.createElement("script");
        scriptE.text = codeE.textContent;
        document.body.appendChild(scriptE);
    }
})();