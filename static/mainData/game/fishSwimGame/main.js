"use strict"

var chrXInfoE = document.getElementById("chrXInfo");
var chrXCanvas_0E = document.getElementById("chrXCanvas_0");
var chrXCanvasBgE = document.getElementById("chrXCanvasBg");

chrXInfoE.style.display = "none";
if(navigator.onLine){
	chrXInfoE.innerText = "应用在线";
}else{
	chrXInfoE.innerText = "应用离线";
}

console.log("#####" + -3.6 %3);

if(chrXCanvas_0E.getContext){
	drawBg();
	drawBattlefield();
}

function drawBg(){
	var contextBg = chrXCanvasBgE.getContext("2d");
	contextBg.strokeStyle = "red";
	contextBg.fillStyle = "#0000ff";
	contextBg.strokeRect(2, 2, 796, 796);
	contextBg.strokeStyle = "rgba(0, 0, 225, 0.5)";
	contextBg.strokeRect(12, 12, 776, 776);
	contextBg.clearRect(15, 15, 770, 770);
	contextBg.fillStyle = "rgba(150, 224, 150, 0.9)";
	contextBg.fillRect(0,0,800,800);
}
		
function drawBattlefield(){
	var context_0 = chrXCanvas_0E.getContext("2d");
	var circleStyle = ["rgba(255, 0, 0, 0.5)", "rgba(0, 255, 0, 0.5)", "rgba(0, 0, 255, 0.5)", "rgba(255, 255, 0, 0.5)"];
	function Circle(){
		this.location = {x:0, y:0},
		this.radius = 0,
		this.direction = Math.PI/2,
		this.style = "rgba(0, 0, 0, 0.5)"
		this.speed = 0;
	}
	function initACircleRandom(circle){
		circle.location.x = Math.random() * 800;
		circle.location.y = Math.random() * 800;
		circle.radius = Math.random() * 30 + 5;
		circle.direction = Math.random() * 2 * Math.PI;
		circle.style = circleStyle[ Math.floor(Math.random() * circleStyle.length)];
		circle.speed = Math.random() * 10 + 5;
	}
	
	var mainCircle = new Circle();
	mainCircle.location.x = 300;
	mainCircle.location.y = 300;
	mainCircle.radius = 10;
	
	var otherCirclesPool = [];
	var otherCircles = [];
	for(var i = 0; i < 30; i++){
		otherCirclesPool[i] = new Circle();
	}
	for(var i = 0; i < 10; i++){
		var item = otherCirclesPool.pop();
		initACircleRandom(item)
		otherCircles.push(item);
	}
	
	function drawACircle(circle){
		context_0.beginPath();
		context_0.fillStyle = circle.style;
		context_0.arc(circle.location.x, circle.location.y, circle.radius,  0, 2 * Math.PI, false);
		context_0.fill();
		
		context_0.beginPath();
		context_0.fillStyle = "rgba(255,255,255,0.5)";
		context_0.arc(circle.location.x + circle.radius * Math.cos(circle.direction)*2/3,
			circle.location.y + circle.radius * Math.sin(circle.direction)*2/3,
			circle.radius/3,  0, 2 * Math.PI, false);
		context_0.fill();
	}
	
	function isInArea(locationX, locationY, areaX, areaY, areaWidth, areaHeight){
		return  locationX > areaX && locationX < areaX + areaWidth
				  && locationY > areaY && locationY < areaY + areaHeight;
	}
	
	function moveOtherCircles(){
		otherCircles = otherCircles.filter(function(item, index, array){
			//移动
			item.location.x += item.speed * Math.cos(item.direction);
			item.location.y += item.speed * Math.sin(item.direction);  

			//改变方向
			item.direction += Math.pow(Math.random()*2-1, 3);
			item.direction = (item.direction + 2 * Math.PI) % (Math.PI * 2);
			
			//过滤掉跑出战场太远的圈圈
			if(isInArea(item.location.x, item.location.y, -100, -100, 800+100, 800+100)){
				return true;
			}else{
				otherCirclesPool.push(item); //将被过滤掉的圈圈回收掉
				return false;
			}
		});

		var addCirclesNum = Math.random() * (12 - otherCircles.length);
		for(var i = 0; i < addCirclesNum; i++){
			var item = otherCirclesPool.pop();
			initACircleRandom(item)
			otherCircles.push(item);
		}
	}

	function moveMainCircle(){
		//移动
		var predictX = mainCircle.location.x + mainCircle.speed * Math.cos(mainCircle.direction);
		var predictY = mainCircle.location.y + mainCircle.speed * Math.sin(mainCircle.direction);
		if(isInArea(predictX, predictY, 0, 0, 800, 800)){
			mainCircle.location.x = predictX;
			mainCircle.location.y = predictY;
		}
		
		//减速
		if(mainCircle.speed > 0.1)
			mainCircle.speed -= Math.pow(mainCircle.speed,2) / 160 + 0.05;
	}

	function changSpeedDirectionOfMainCircle(vX, vY){
		var jd = Math.atan2(vY, vX) - mainCircle.direction;  //[-π, π]  - [0, 2π] ----> [-3π, π]
		jd = (jd + 4 * Math.PI) % (Math.PI * 2);
		mainCircle.direction += Math.sin(jd);
		item.direction = (item.direction + 2 * Math.PI) % (Math.PI * 2);
		var speedChange = Math.cos(jd) * Math.sqrt(vX * vX + vY * vY) / 800 * 20;
		if(speedChange > 20)
			speedChange = 20;
		if(speedChange > 0){
			mainCircle.speed += ((20 - mainCircle.speed) /20 * speedChange);
		}else{
			mainCircle.speed += (mainCircle.speed / 20 * speedChange);
		}
		chrXInfo.innerText += "\n cc speed current" + mainCircle.speed;
	}
	
	(function handleDargEvent(){
	console.log("event handle");
		var isDarging = false; 
		var vX; var vY; //拖动结束前存储拖动的开始坐标，拖动结束后存储通过拖动得到的向量
		chrXCanvas_0E.onmousedown = function(event){
			console.log("mousedown");
			vX = event.clientX;
			vY = event.clientY;
			isDarging = true;
			chrXCanvas_0E.addEventListener("mousemove", function(){
				//在拖动过程中作处理	
			})
		}
		
		function dargEnd(event){
			console.log("dargEnd");
			if(isDarging){
				isDarging = false;
				vX = event.clientX - vX;
				vY = event.clientY - vY;
				changSpeedDirectionOfMainCircle(vX, vY);
			}
		}
		chrXCanvas_0E.onmouseup = dargEnd;
		chrXCanvas_0E.onmouseout = dargEnd;
	})();
	
	setInterval(function(){
		context_0.clearRect(0,0,800,800);
		drawACircle(mainCircle);
		otherCircles.forEach(function(item){
			drawACircle(item);
		});
		moveOtherCircles();
		moveMainCircle();
	}, 200);

	
}
