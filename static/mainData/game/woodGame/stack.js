var ibox_active='game';
var ibox_cur=0;
var ibox_targets=Array();
ibox_targets['game']=0;
ibox_targets['highscore']=-320;
ibox_targets['about']=-640;
var ibox_scroll_timer;
var now = new Date();
var expire = new Date();
expire.setTime(now.getTime() + 1000*60*60*24*90); //90 days

var logh=20;//木头高度
var extraleft = [0, 6, 4, 5, 5];
var extraright=10;

var sceneWidth=308;
var sceneHeight=247;

var logWidth=new Array();//保存每根木头的宽度（初始值均为260，木头放下后会根据情况切割，宽度减少）。
var logMarginLeft=new Array();//保存每根木头左边的偏移（游戏中通过修改该值使木头移动）
var logType=new Array();//保存每根木头的类型（为了显示效果更好，存在多种显示类型）。
var logImgStart=new Array();//显示木头时，开始位置对应的图片位置。
var stinterval;  //保存移动木头用的定时器,用于取消该定时器
var gameisover=1;
var isCanClick=true;
var gamesplayed;//记录已经玩过的次数
var theirbest;//记录当前的最高分数
var stscore=0;
var currentLogNo=0;


logWidth[0]=260; //a ronk maga!
logImgStart[0]=(logWidth[0]-270)*Math.random();
logMarginLeft[0]=(sceneWidth-logWidth[0])/2;
logType[0]=Math.floor(Math.random()*4)+1;

function imgpreload(ims) {
  var myims=new Array(); //图像被载入后会存在浏览器的缓存中，该变量将无需再使用
  ims.push('./i/b_yes.png');
  ims.push('./i/b_no.png');
  ims.push('./i/b_okay.png');
  for(var i in ims) {
    myims[i]=new Image();
    myims[i].src=ims[i];
  }
}


function intervalMoveLog(paddingTarget,stdir){
  var paddingNow = parseInt(document.getElementById('st_scrollarea').style.paddingTop);

  var stack_dothemove = function() {
    var i=currentLogNo;
    if(paddingTarget > paddingNow+1) {//在左右移动木头的同时，顺便根据需要将木头堆下移
      paddingNow=(paddingTarget+paddingNow)/2;
      document.getElementById('st_scrollarea').style.paddingTop=paddingNow+'px';
    }
    logMarginLeft[i] += stdir;
    if(logMarginLeft[i] < 0) {//已经越过左边边缘，需要反向
      logMarginLeft[i]=-logMarginLeft[i];
      stdir*=-1;
    }else if(logMarginLeft[i]+logWidth[i] > sceneWidth) {//已经越过右边边缘，需要反向
      logMarginLeft[i]=sceneWidth-logWidth[i]-logMarginLeft[i]-logWidth[i]+ sceneWidth;
      stdir*=-1;
    }
    document.getElementById('log_'+i).style.marginLeft=logMarginLeft[i]-extraleft[logType[i]]+7+'px';
  };

  return setInterval(stack_dothemove,50);
}

function resumegame() {
	if(gameisover == 0) {
		stinterval=intervalMoveLog(0);//setInterval(stack_dothemove,50, 0, 0);
	}
}

function idismiss() {
  document.getElementById('alertbox').style.display='none';
  resumegame();
}

function ialert(iquestion,idoit) {
  var str_todo = idoit;
  var f_callback_ok = function(){
    idismiss();
    str_todo();
    return false;
  }
  var tmp = document.getElementById('alertbox_content');
  tmp.innerHTML=iquestion+'<br style="clear:both" /><br />\
  <a href="#" class="ialert_a_ok"><img src="./i/b_okay.png" alt="确定" /></a>';
  
  var tmp2 = tmp.getElementsByClassName("ialert_a_ok")[0];
  tmp2.onclick = f_callback_ok;
  tmp2.ontouchstart = f_callback_ok;
  
  document.getElementById('alertbox').style.display='block';
}

function getCookie(Name) {
  var search = Name + "=";
  if (document.cookie.length > 0) {
    var offset = document.cookie.indexOf(search);
    if (offset != -1) {
      offset += search.length;
      var end = document.cookie.indexOf(";", offset);
      if (end == -1)
        end = document.cookie.length;
      return unescape(document.cookie.substring(offset, end));
    }
  }
  return('');
}

function setCookie(name, value) {
  document.cookie = name + "=" + escape(value);
  + ((expire == null) ? "" : ("; expires=" + expire.toGMTString())+';domain=chrx.sinaapp.com;path=/;');
}

function setTI(todos,interval) {
  if(todos.length == 0) {
    return false;
  }
  (todos.shift())();
  setTimeout(setTI,interval, todos,interval);
}

function firstinit() {//第一次玩时初始化
  gamesplayed=getCookie('stack_gamesplayed');
  if(gamesplayed == '') {gamesplayed=0;}

  theirbest=getCookie('stack_bestscore');
  if(theirbest == '') {theirbest=0;}

  imgpreload(['i/dropshadow.png',
              'i/11.png','i/12.png','i/13.png',
              'i/21.png','i/22.png','i/23.png',
              'i/31.png','i/32.png','i/33.png',
              'i/41.png','i/42.png','i/43.png']
            );
  try{
    document.body.addEventListener("touchmove", function(e) {
      e.preventDefault();
    }, false);
  }catch(e){;
           }
           
  var buttonStackLog=document.getElementById('buttonStackLog'); 
  if(typeof(buttonStackLog.ontouchstart) !== 'undefined') {
    buttonStackLog.ontouchstart=handleclick;
  } else {
    buttonStackLog.onmousedown=handleclick;
    buttonStackLog.onclick = function() {return false;};
  }
}

function init() {//重玩游戏（包括第一次玩游戏）的初始化  
  var log0=document.createElement('div');  //创建第0根木头的div
  log0.id='log_0';
  log0.style.position='absolute';
  log0.style.height=logh+'px';
  log0.style.marginTop=sceneHeight-logh+'px';
  log0.style.marginLeft=logMarginLeft[0]-extraleft[logType[0]]+7+'px';
  document.getElementById('st_scrollarea').appendChild(log0);
  showALog('log_0',logType[0],logImgStart[0],logWidth[0]);
  
  document.getElementById('st_scrollarea').style.paddingTop = "0px";
  document.getElementById('st_outerarea').style.visibility = "visible";
  //addshadow();
  logInit();
}

function logInit() {//初始化当前木头
  var paddingtarget = 0;
  var i = currentLogNo;
  if(i>10) { //木头超过10层，需要往下压
		paddingtarget=(i-10)*(logh-4);
		if(i > 15) { //超过15层，可以把前面太早的木头和阴影删除。
		  document.getElementById('st_scrollarea').removeChild(document.getElementById('log_'+(i-16)));
		  if(i % 2 == 0 && i>16) {
        document.getElementById('st_scrollarea').removeChild(document.getElementById('shd_'+(i-16)));
      }
		}
	}
	currentLogNo++; i = currentLogNo;

	logWidth[i]=logWidth[i-1];
	logImgStart[i]=(logWidth[i]-270)*Math.random();
	logMarginLeft[i]=0;

  var stdir=Math.log(i+1)*2;//每次移动的位置
  if(Math.random()>0.5) {
    stdir*=-1;
    logMarginLeft[i]=sceneWidth-logWidth[i];
  }

  document.getElementById('level').innerHTML=Math.floor(i/10)+1+"";
	logType[i]=Math.floor(Math.random()*4)+1;

	var tmp=document.createElement('div');
	tmp.id='log_'+i;
	tmp.style.position='absolute';
	tmp.style.height=logh+'px';
	tmp.style.width=extraleft[logType[i]]+logWidth[i]+extraright/2+'px';
	tmp.style.marginTop=sceneHeight-(i+2)*(logh-4)+"px";
	tmp.style.marginLeft=logMarginLeft[i]-extraleft[logType[i]]+7+'px';

	document.getElementById('st_scrollarea').appendChild(tmp);

	showALog('log_'+i,logType[i],logImgStart[i],logWidth[i]);
	stinterval= intervalMoveLog(paddingtarget, stdir);//setInterval(stack_dothemove,50, paddingtarget, 0);
}

function handleclick() {
	if(isCanClick==false) {return false;}
	isCanClick=false;
	clearTimeout(stinterval); //木棍停止左右移动
	var hcf='';
	if(logMarginLeft[currentLogNo] < logMarginLeft[currentLogNo-1]) {
    logWidth[currentLogNo]-=logMarginLeft[currentLogNo-1]-logMarginLeft[currentLogNo];
    logMarginLeft[currentLogNo]=logMarginLeft[currentLogNo-1];
    hcf='left';//切掉木头左边
  }
	if(logMarginLeft[currentLogNo]+logWidth[currentLogNo] > logMarginLeft[currentLogNo-1]+logWidth[currentLogNo-1]) {
    logWidth[currentLogNo]-= logMarginLeft[currentLogNo]+logWidth[currentLogNo] - logMarginLeft[currentLogNo-1]-logWidth[currentLogNo-1];
    hcf='right';//切掉木头右边
  }
	if(logWidth[currentLogNo] <= 0) {
    hcf='all';//切掉木头两边－－－－游戏将会结束
  }

	cutALog(currentLogNo,hcf);

	if(logWidth[currentLogNo] <= 0) {
    logWidth[currentLogNo]=0;
  }
	if(currentLogNo % 2 == 0 && logWidth[currentLogNo] > 0) {
    addshadow();
	}

	var socreAdd=Math.floor(logWidth[currentLogNo]/10*Math.log(currentLogNo+1));

  //对完美操作提示和强调
	if(Math.abs(logWidth[currentLogNo] - logWidth[currentLogNo-1])<3 && logWidth[currentLogNo]>0) {
  	socreAdd*=2;
  	document.getElementById('combo').innerHTML = parseInt(document.getElementById('combo').innerHTML)+ 1 + "";
  	var tmp=document.createElement('div');
  	tmp.innerHTML='<div style="padding:5px"><b>漂亮 完美!</b></div>';
  	tmp.id='box_perfect';
  	tmp.style.zIndex='10';
  	tmp.style.position='absolute';
  	tmp.style.textAlign='center';
  	tmp.style.width='150px';
  	tmp.style.backgroundColor='#333333';
  	tmp.style.marginLeft='85px';
  	var tmp3=(sceneHeight-(currentLogNo+2)*(logh-4)-16);
  	tmp.style.marginTop=tmp3+'px';
  	document.getElementById('st_scrollarea').appendChild(tmp);

  	var tmp2=new Array();
    tmp2[0]=function(){
    };
    tmp2[1]=function(){
      document.getElementById('score_title').style.color='#ffffff';
      document.getElementById('box_perfect').style.marginTop=tmp3-5 + 'px';
    };
    tmp2[2]=function(){
      document.getElementById('box_perfect').style.marginTop=(tmp3-10) + 'px';
    };
    tmp2[3]=function(){
      document.getElementById('box_perfect').style.marginTop=(tmp3-15) + 'px';
    };
    tmp2[4]=function(){
      document.getElementById('st_scrollarea').removeChild(document.getElementById('box_perfect'));
      document.getElementById('score_title').style.color='';
    };
  	setTI(tmp2,50);
	}

	stscore+=socreAdd;
	document.getElementById('score').innerHTML=stscore + "";
	if(stscore>theirbest) {document.getElementById('score').style.color='#ff0000';}
}

function addshadow() {
  var tmp=document.createElement('img');
  tmp.src='i/dropshadow.png';
  tmp.id='shd_'+currentLogNo;
  tmp.style.zIndex='15';
  tmp.style.position='absolute';
  tmp.style.width=(extraleft[logType[currentLogNo]]+logWidth[currentLogNo]+extraright/2)+'px';
  tmp.style.height='30px';
  tmp.style.marginLeft=(logMarginLeft[currentLogNo]-extraleft[logType[currentLogNo]]+7)+'px';
  tmp.style.marginTop=(sceneHeight-(currentLogNo+1)*(logh-4)-1)+'px';
  document.getElementById('st_scrollarea').appendChild(tmp);
}

function cutALog(currentLogNo,crfrom) {
  var i=currentLogNo;
  var logDivId = "log_" + i;

  var logDiv = document.getElementById(logDivId);
  var logImgDiv = logDiv.getElementsByTagName('div')[0];
  var midImg = logImgDiv.getElementsByTagName('div')[0];

  var midImgWidth=parseInt(midImg.style.width);
  if(crfrom == 'right') {
    midImg.style.width=logWidth[i]+'px';
    logImgDiv.getElementsByTagName('img')[0].style.marginLeft=extraleft[logType[i]]+logWidth[i]-extraright/2+'px';
    showALog(logDivId,logType[i],logImgStart[i]-logWidth[i],midImgWidth-logWidth[i]);
    logDiv.childNodes[1].style.marginLeft=logWidth[i]+'px';
    logDiv.childNodes[1].style.zIndex='12';
  } else if(crfrom == 'left'){
    midImg.style.width=logWidth[i]+'px';
    midImg.style.marginLeft=extraleft[logType[i]]+midImgWidth-logWidth[i]+1+'px';
    midImg.style.backgroundPosition=logImgStart[i]+logWidth[i]-midImgWidth+'px';
    logImgDiv.getElementsByTagName('img')[1].style.marginLeft=midImgWidth-logWidth[i]+'px';
    showALog(logDivId,logType[i],logImgStart[i],midImgWidth-logWidth[i]);
    document.getElementById(logDivId).childNodes[1].style.zIndex=(currentLogNo % 2 == 1)?(14):(16);
  }

  if(crfrom !='') {
    var tmp=new Array();
    var g_f = function(v){
      return function(){
        logDiv.childNodes[v[0]].style.opacity=1-0.25*v[1] + '';
        logDiv.childNodes[v[0]].style.marginTop= 2+5*v[1] + 'px';
      }
    };

    if(crfrom == 'left' || crfrom == 'right') {
      tmp[0]=function(){
        logDiv.style.marginTop= (sceneHeight-(currentLogNo+1)*(logh-4))+'px';//木头下移到木头堆
        logDiv.childNodes[0].style.zIndex=((currentLogNo % 2)?(13):(16))+"";//跳转与下方木头的显示前后顺序
        logDiv.childNodes[1].style.marginTop='2px';
      };
      tmp = tmp.concat([[1,1],[1,2],[1,3]].map(g_f));
      tmp[4]=function(){
        logDiv.removeChild(logDiv.childNodes[1]);
      };
    } else if(crfrom =='all') {
      tmp[0]=function(){
        logDiv.childNodes[0].style.marginTop='2px';
      };

      tmp = tmp.concat([[0,1],[0,2],[0,3]].map(g_f));
      tmp[4]=function(){
        logDiv.removeChild(logDiv.childNodes[0]);
      };
    }

    var f_tmp4 = tmp[4];
    tmp[4]=function(){ //此函数执行时tmp[4]已经被修改，所以需要将tmp[4]的原始值保存在其它变量中
      if(f_tmp4){
        f_tmp4();
      }
      if(logWidth[currentLogNo] >0) {
        logInit();
        isCanClick=true;
      }else {
        gameover();
      }
    };

    setTI(tmp,50);
  } else {/*
    logDiv.style.marginTop=(sceneHeight-(currentLogNo+1)*(logh-4))+'px';
    document.getElementById(logDivId).childNodes[0].style.zIndex=((currentLogNo % 2)?(13):(16));
    logInit();
    */
  }
}

//显示一根木头
function showALog(logDivId,logType,srstart,srsize) {//logType：木头类型
  var srt='i/'+ logType;
  var tmp=document.createElement('div');//一根木头三个图片的容器
  tmp.style.position='absolute';
  tmp.style.width=extraleft[logType]+srsize+extraright/2+'px';
  tmp.style.height=logh+'px';
  tmp.style.zIndex="15";

  var tmp2=document.createElement('div');//中间图片
  tmp2.style.position='absolute';
  tmp2.style.width=srsize+'px';
  tmp2.style.height=logh+'px';
  tmp2.style.marginLeft=extraleft[logType]+'px';
  tmp2.style.backgroundImage='url('+srt+'2.png)';
  tmp2.style.backgroundPosition=srstart+'px 0';
  tmp.appendChild(tmp2);

  var imgRight=document.createElement('img');//右边图片
  imgRight.src=srt+'3.png';
  imgRight.style.marginLeft= extraleft[logType]+srsize-extraright/2 +"px";
  imgRight.style.position='absolute';
  tmp.appendChild(imgRight);

  var imgLeft=document.createElement('img');//左边图片
  imgLeft.src=srt+'1.png';
  imgLeft.style.position='absolute';
  tmp.appendChild(imgLeft);

  document.getElementById(logDivId).appendChild(tmp);
}

function restartgame() {
	clearInterval(stinterval);
	gameisover=0;
	logWidth=new Array();
	logMarginLeft=new Array();
	logType=new Array();
	logImgStart=new Array();
	stscore=0;
	currentLogNo=0;
	logWidth[0]=260; //a ronk maga!
	logImgStart[0]=(logWidth[0]-270)*Math.random();
	logMarginLeft[0]=(sceneWidth-logWidth[0])/2; //ronk margoja!
	logType[0]=Math.floor(Math.random()*4)+1;
	isCanClick=true;
	document.getElementById('combo').innerHTML="0";
	document.getElementById('level').innerHTML="1";
	document.getElementById('score').innerHTML=stscore + "";
	document.getElementById('score').style.color='#ffffff';
	document.getElementById('st_scrollarea').innerHTML='';
	init();
}

function gameover() {
	gameisover=1;
	gamesplayed++;
	setCookie('stack_gamesplayed',gamesplayed);
	if(stscore>theirbest) {
		setCookie('stack_bestscore',stscore);
		theirbest=stscore;
		ialert('<h1>游戏结束: '+stscore+'分</h1>厉害，你又破纪录了',restartgame);
	} else {
		ialert('<h1>游戏结束: '+stscore+'</h1>再来一次?', restartgame);
	}
  document.getElementById('st_outerarea').style.visibility = "hidden";
	return false;
}


		firstinit();
		ialert('<h1>堆木头</h1>\
<p style="margin: 0 20px 0 20px; text-align:left;">\
	<img src="i/icon.png" alt="堆木头!" style="width:64px; height:64px;float:left; margin-right:5px;"/>\
当木头移动到木头堆正上方时，按下按钮放木头，尽可能的对齐木头.\
</p>\
<div style="width:110px; margin:30px auto -30px auto;"></div>', restartgame);

///////////////////////////////////////////////////

/*

function iconfirm(iquestion,idoit) {
  var str_todo = idoit;
  var f_callback_ok = function(){
    idismiss();
    str_todo();
    return false;
  }

  var f_callback_cancel = function(){
    idismiss();
    return false;
  }
  
  document.getElementById('alertbox_content').innerHTML=
  iquestion+'<br style="clßear:both" /><br /><a href="#"><img src="./i/b_yes.png" alt="Yes" /></a>\
  <a href="#"><img src="./i/b_no.png" alt="No" /></a>';
  
  
  var tmp2 = tmp.getElementsByClassName("ialert_a_ok")[0];
  tmp2.onclick = f_callback_ok;
  tmp2.ontouchstart = f_callback_ok;
  
  var tmp3 = tmp.getElementsByClassName("ialert_a_ok")[0];
  tmp3.onclick = f_callback_cancel;
  tmp3.ontouchstart = f_callback_cancel;
  
  document.getElementById('alertbox').style.display='block';
}


function menuswitch(obj) {
  var whereto=obj.href.split('#')[1];
  if(whereto=='game' && ibox_active == 'game') {pausegame();iconfirm('<h1>新游戏</h1>确定要<br />重新开始游戏吗?','restartgame();'); return false;}
  if(ibox_active == 'game' && whereto!='game') {pausegame();}
  var mse=null;
  if(ibox_active != 'game' && whereto=='game') {
    mse=function(){resumegame();};
  }

  var tmp=new Array('game','highscore','about');
  var tmp2=new Array();
  tmp2['game']=0;
  tmp2['highscore']='-72px';
  tmp2['about']='-182px';
  for(var i in tmp) {
    document.getElementById('button_'+tmp[i]).style.backgroundPosition=tmp2[tmp[i]]+' '+((tmp[i]==whereto)?(0):('-41px'));
  }

  if(whereto == ibox_active) {
    return false;
  }

  var ibox_start=ibox_targets[ibox_active];
  ibox_active=whereto;

  for(i in ibox_targets) {
    document.getElementById('button_'+i).className=(i==whereto)?('active'):('');
  }
  obj.className='active';
  tmp2=new Array();
  tmp=ibox_start;
  for(i=0;i<=5;i++) {
    var mlStr =(tmp+ibox_targets[whereto])/2 + 'px';
    tmp2.push(function(){
      document.getElementById('container_scroller').style.marginLeft = mlStr +'px';
      });
  }
  tmp2.push('document.getElementById(\'container_scroller\').style.marginLeft=\''+ibox_targets[whereto]+'px\';');
  if(mse!='') {
    tmp2.push(mse);
   }
  setTI(tmp2,50);
  return false;
}

function pausegame() {
	clearTimeout(stinterval);
}

*/
