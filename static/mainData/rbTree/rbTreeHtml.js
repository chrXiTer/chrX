;(function(){
    var canvases = {}
	function f(ts){
		for(var k in ts){
			canvases[k] = document.getElementById(k);
			var canvasContext = canvases[k].getContext("2d");
			canvasContext.font = "bold 14px Arial";
			canvasContext.textAlign = "center";
			canvasContext.textBaseline = "middle";
			drawTreeMain(canvasContext, ts[k], canvases[k].width, canvases[k].height);//50 + 300*(i%2), 50 + 200*((i - i%2)/2));
		}
	}
    function exec(){
        f(rt_iL);
        f(rt_iR);
        f(rt_rb);
        f(rt_lb);
    }
    
    function to(){
        if(rt_iL && rt_iR && rt_rb && rt_lb){
            exec()
        }else{
            setTimeout(to, 50);
        }
    }
    
    to();

})();
