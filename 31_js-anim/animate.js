// Team Odin :: Yuqing Wu, Rachel Xiao
// SoftDev pd2
// K31 -- Paint Paint Paint...
// 2022-02-15t

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = document.getElementById('playground');
var dotButton = document.getElementById('buttonCircle');
var stopButton = document.getElementById('buttonStop');

//prepare to interact with canvas in 2D
var ctx = c.getContext('2d');

//set fill color to team color
ctx.fillStyle = "blue";

var requestID;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0, 0, c.clientWidth , c.clientHeight);
};


var radius = 0;
var growing = true;


//var drawDot = function() {
var drawDot = () => {
  clear();
  console.log("drawDot invoked...")
  //start drawing circle from the center
  var mouseX = c.clientWidth / 2;
  var mouseY = c.clientHeight / 2;
  console.log("mouseClick registered at ", mouseX, mouseY);

  //draw circle
  ctx.strokeStyle = "black";
  ctx.beginPath();
  ctx.arc(mouseX, mouseY, radius, 0, 2*Math.PI);
  ctx.fill();
  ctx.stroke();

  //circle shouldn't be drawn outside of the bounds of the canvas
  //circle will start getting smaller when it hits the edges
  if (radius == Math.min(c.clientWidth, c.clientHeight) / 2) {
    growing = false;
  }
  //circle will get bigger if it is at its smallest
  if (radius == 0) {
    growing = true;
  }

  // YOUR CODE HERE
  if (growing) {
    radius++;
  } else {
    radius--;
  }

  // YOUR CODE HERE

  requestID = window.requestAnimationFrame(drawDot);

  /*
    ...to
    Wipe the canvas,
    Repaint the circle,
    ...and somewhere (where/when is the right time?)
    Update requestID to propagate the animation.
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()
   */
};


//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );
  window.cancelAnimationFrame(requestID);

  /*
    ...to
    Stop the animation
    You will need
    window.cancelAnimationFrame()
  */
};


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
