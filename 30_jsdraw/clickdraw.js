var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var mode = "rect";

var toggleMode = (e) => {
  console.log("toggling...");
  if (mode == "rect") {
    return;
  }
  return;
}

var drawRect = function(e) {
  var mouseX = 300;
  var mouseY = 300;
  console.log("mouseClick registered at ", mouseX, mouseY);
  ctx.fillStyle = "red";
  ctx.fillRect(0, 0, 100, 200);
}
