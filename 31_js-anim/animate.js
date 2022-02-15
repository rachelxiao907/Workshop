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
ctx.fillStyle = "blue"; // YOUR CODE HERE

var requestID;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...")

  // YOUR CODE HERE
};


var radius = 0;
var growing = true;


//var drawDot = function() {
var drawDot = () => {
  console.log("drawDot invoked...")
  var mouseX = 250;
  var mouseY = 250;
  console.log("mouseClick registered at ", mouseX, mouseY);
  ctx.strokeStyle = "black";
  ctx.beginPath();
  ctx.arc(mouseX, mouseY, 50, 0, 2*Math.PI);
  ctx.fill();
  ctx.stroke();

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

  // YOUR CODE HERE
  /*
    ...to
    Stop the animation
    You will need
    window.cancelAnimationFrame()
  */
};


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
