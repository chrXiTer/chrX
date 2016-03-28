var canvases = {};

;(function(){
	rbTreeAllDiv.innerHTML = ""
	rbTreeAllDiv.innerHTML += '<canvas id="canvaseTest" width="600px" height="600px" style="position:absolute; top: 0px; left: 0px; z-index:100">chrX canvas</canvas>';
	var canvasTest = document.getElementById("canvaseTest");
	if(!canvasTest.getContext) return;

	drawGroup(rbTreeAllDiv, canvases, a);


})();