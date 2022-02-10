// Fire Extinguisher :: Jesse Xie (Polly), Rachel Xiao (Mooana)
// SoftDev pd2
// K29 -- DOMfoolery++
// 2022-02-09w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

// appends an item to the end of the list
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  console.log(newitem)
  list.appendChild(newitem);
};

// remove the nth item of the list, everything else move up
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  console.log(listitems);
  listitems[n].remove();
};

// Turns first and last element of list red
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

// Turns everything blue except the first is red
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB

var fib = function(n) {
  if (n <= 1) {
   return n;
  } else {
   return fib(n-1) + fib(n-2);
  }
};

// FAC

var fact = function(n) {
  if (n <= 1 ) {
   return 1;
  } else {
   return fact(n-1) * n;
  }
};

// GCD

var gcd = function(a,b) {
  if(a < b) return gcd(b,a);
  if(a % b == 0) return b;
  else return gcd(b, a % b);
};



b1 = document.getElementById("b1");
b1.addEventListener("click", function() {
                               addItem("fib(10): "+fib(10));
                             }
                   );
b2 = document.getElementById("b2");
b2.addEventListener("click", function() {
                               addItem("fact(5): "+fact(5));
                             }
                   );
b3 = document.getElementById("b3");
b3.addEventListener("click", function() {
                               addItem("gcd (36,10): "+gcd(36,10));
                             }
                   );
