var lineColor = "green"
var textColor = "yellow"
function getMaxNumOfLeaf(treeRoot){
	function getDeep(node){
		if(node == null || node.isNull)
			return 0
		var deepLeft = getDeep(node.leftChild);
		var deepRight = getDeep(node.rightChild);
		return Math.max(deepLeft, deepRight) + 1;
	}
	var deep = getDeep(treeRoot);
	return Math.pow(2, deep-2);
}


function drawTree(context, nodeLocation, stepLength, nodeSize, node){
    if(node == null || (node.isNull && !node.color)) {
        context.beginPath();
        context.fillStyle = "gray";
        context.arc(nodeLocation.x, nodeLocation.y, nodeSize * 3 / 16, 0, 2 * Math.PI, false);
        context.fill();
		if(node != null){
			context.fillStyle = textColor;
			context.fillText(node.text, nodeLocation.x, nodeLocation.y);
		}
        return;
    }

	
	var leftChlidLocation = { x: nodeLocation.x - stepLength, y: nodeLocation.y + nodeSize };
	var rightChildLocation = { x: nodeLocation.x + stepLength, y: nodeLocation.y + nodeSize };
	if(!node.isNull){//绘制与子节点的连接线
		context.beginPath();
		context.strokeStyle = lineColor;
		context.moveTo(nodeLocation.x, nodeLocation.y);
		context.lineTo(leftChlidLocation.x, leftChlidLocation.y);
		context.moveTo(nodeLocation.x, nodeLocation.y);
		context.lineTo(rightChildLocation.x, rightChildLocation.y);
		context.stroke();
	}

	context.beginPath();
	context.fillStyle =node.color || "red";
	context.arc(nodeLocation.x, nodeLocation.y, nodeSize * 5/16,  0, 2 * Math.PI, false);
	context.fill();
	
	if(node.text){
		context.fillStyle = textColor;
		context.fillText(node.text, nodeLocation.x, nodeLocation.y);
	}
	if(!node.isNull){
		drawTree(context, leftChlidLocation, stepLength/2, nodeSize, node.leftChild);
		drawTree(context, rightChildLocation, stepLength/2, nodeSize, node.rightChild);
	}
}


function drawTreeMain(context, tree, width, height){
	var maxNumOfLeaf = getMaxNumOfLeaf(tree.treeRoot);
	var maxNumofExtern = maxNumOfLeaf * 2;
	var nodeSizeReal = width / ( (maxNumofExtern < 3? 3:maxNumofExtern)  + 1); //留出一个节点单元大小的空白
	var rootLocation = {x: width/2, y : nodeSizeReal*3/4};
	var stepLength = rootLocation.x/2;
	
	context.fillStyle = "black";
	context.fillText(tree.treeName, 80, 20);
	drawTree(context, {x:rootLocation.x, y: rootLocation.y}, stepLength, nodeSizeReal, tree.treeRoot);
}


function drawGroup(contentDiv, canvases, rTreeGroup){
	contentDiv.innerHTML = ""
	for(var k in rTreeGroup){
		contentDiv.innerHTML +='<canvas id="' + k + '" width="300px" height="300px", style="float:left">eeee</canvas>';
	}
	for(var k in rTreeGroup){
		canvases[k] = document.getElementById(k);
		var canvasContext = canvases[k].getContext("2d");
		canvasContext.font = "bold 14px Arial";
		canvasContext.textAlign = "center";
		canvasContext.textBaseline = "middle";
		drawTreeMain(canvasContext, rTreeGroup[k], canvases[k].width, canvases[k].height);//50 + 300*(i%2), 50 + 200*((i - i%2)/2));
	}
}


