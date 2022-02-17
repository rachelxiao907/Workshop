// Team Player :: Qina Liu, Rachel Xiao
// SoftDev pd2
// K32 -- More Moving Parts
// 2022-02-17r

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = document.getElementById('playground');
var dotButton = document.getElementById('buttonCircle');
var dvdButton = document.getElementById('buttonDVD');
var stopButton = document.getElementById('buttonStop');

//prepare to interact with canvas in 2D
var ctx = c.getContext('2d');

//set fill color to team color
ctx.fillStyle = "skyblue";

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
  clear(); //wipe canvas
  stopIt(); //to propagate your animations, you must pop off existing frames from the stack
            //cancelAnimationFrame first to make sure there is one animation frame running
  console.log("drawDot invoked...");
  //start drawing circle from the center
  var mouseX = c.clientWidth / 2;
  var mouseY = c.clientHeight / 2;
  console.log("mouseClick registered at ", mouseX, mouseY);

  //repaint circle
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

  if (growing) {
    radius++;
  } else {
    radius--;
  }

  requestID = window.requestAnimationFrame(drawDot); //and provide a callback to continue animating

  cont = true;
};


var down = true; //default direction is down right
var right = true;
var cont = false; //tracks whether to have image placed at a new location or continue where it left off
// placed outside of drawDVD because the x and y should not be randomized each call,
// allowing animation to continue from where it left
var width = 100;
var height = 50;
var x = Math.floor(Math.random() * (c.clientWidth - width)); //so image can't spawn out of canvas
var y = Math.floor(Math.random() * (c.clientHeight - height));

/*
TO DO:
when dvd button is pressed, (i think this was in the demo but my memory is kinda failing me),
instead of dvd being placed at randomly and animation restarting, nothing happens, the animation continues on
*/


var drawDVD = () => {
  clear();
  window.cancelAnimationFrame(requestID);
  console.log("drawDVD invoked...");
  console.log("dvd registered at ", x, y);

  var dvdImage = new Image();
  dvdImage.src = "logo_dvd.jpg";
  ctx.drawImage(dvdImage, x, y, width, height);

  // dvd hit right side and bounces to move left
  if (x === c.clientWidth - width) {
    right = false;
  }
  // dvd hit left side and bounces to move right
  if (x === 0) {
    right = true;
  }
  // dvd hit bottom side and bounces to move up
  if (y === c.clientHeight - height) {
    down = false;
  }
  // dvd hit up side and bounces to move down
  if (y === 0) {
    down = true;
  }

  // (0, 0) is the top left of the canvas
  if (down) { y++; } // dvd goes down, down is upward y
  else { y--; } // dvd goes up
  if (right) { x++; } // dvd goes to right
  else { x --; } // dvd goes to left

  requestID = window.requestAnimationFrame(drawDVD);
}


//var stopIt = function() {
var stopIt = () => {
  /*
    ...to
    Stop the animation
    You will need
    window.cancelAnimationFrame()
  */
  console.log("stopIt invoked...")
  console.log( requestID );
  window.cancelAnimationFrame(requestID);
  cont = true;
};


dotButton.addEventListener( "click", drawDot );
dvdButton.addEventListener( "click",  function() {
                                        if (!cont) {
                                          x = Math.floor(Math.random() * (c.clientWidth - width));
                                          y = Math.floor(Math.random() * (c.clientHeight - height));
                                          console.log("random location");
                                        }
                                        cont = false; //consecutive clicks means image starts at new location
                                        drawDVD();
} );
stopButton.addEventListener( "click", stopIt );
