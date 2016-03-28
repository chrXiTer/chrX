var canvases = {};

;(function(){
	content_rt_iL.innerHTML = ""
	content_rt_iL.innerHTML += '<canvas id="canvaseTest" width="600px" height="800px" style="position:absolute; top: 0px; left: 0px; z-index:100">chrX canvas</canvas>';
	var canvasTest = document.getElementById("canvaseTest");
	if(!canvasTest.getContext) return;

	drawGroup(content_rt_iL, canvases, rt_iL);
	drawGroup(content_rt_iR, canvases, rt_iR);
	drawGroup(content_rt_Lb, canvases, rt_rb);
	drawGroup(content_rt_Rb, canvases, rt_lb);


})();