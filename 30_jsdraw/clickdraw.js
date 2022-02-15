// Team Odin :: Yuqing Wu, Rachel Xiao
// SoftDev pd2
// K30 -- JS Draw with Canvas
// 2022-02-14m

//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instatiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

var toggleMode = (e) => {
  console.log("toggling..." + mode);
  if (mode == "rect") {
    mode = "circle";
  }
  else {
    mode = "rect";
  }
}

var drawRect = function(e) {
  var mouseX = e.offsetX;
  var mouseY = e.offsetY;
  console.log("mouseClick registered at ", mouseX, mouseY);
  ctx.fillStyle = "red";
  ctx.fillRect(mouseX, mouseY, 100, 200);
}

var drawCircle = function(e) {
  var mouseX = e.offsetX;
  var mouseY = e.offsetY;
  console.log("mouseClick registered at ", mouseX, mouseY);
  ctx.fillStyle = "red";
  ctx.beginPath();
  ctx.arc(mouseX, mouseY, 50, 0, 2*Math.PI);
  ctx.fill();
}

var draw = function(e) {
  if (mode == "rect") {
    drawRect(e);
  }
  else {
    drawCircle(e);
  }
}

//var wipeCanvas = () => {}
var wipeCanvas = function() {
  ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
}

c.addEventListener('click', draw);

var bToggler = document.getElementById("buttonToggle"); //rect|circ button
bToggler.addEventListener('click', function() {
                                    toggleMode();
                                    if (mode == "rect") {
                                      bToggler.innerHTML = "Rectangle";
                                    }
                                    else {
                                      bToggler.innerHTML = "Circle";
                                    }
                                  }
                         ); //switch between rectange and circle

var clearB = document.getElementById("buttonClear"); //wipe button
clearB.addEventListener('click', wipeCanvas); //doesn't need () because just fxnName
