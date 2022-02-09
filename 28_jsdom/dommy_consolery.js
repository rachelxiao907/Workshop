// Team Odin :: Yuqing Wu, Rachel Xiao
// SoftDev pd2
// K28 -- Manipulating the DOM
// 2022-02-08t
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

var fib = (n) =>{
  if (n<=1){
   return n;
  }else{
   return fib(n-1) +  fib(n-2);
  }
};

// FAC

var fact = (n) =>{
  if (n<=1){
   return 1;
  }else{
   return fact(n-1) *  n;
  }
};

// GCD

var gcd = function(a,b){
  var divisor = a;
  var dividend = b;
  if(a>b){
    dividend = a;
    divisor = b;
  }
  while(divisor != 0){
    var rem = dividend % divisor;
    dividend = divisor;
    divisor = rem;
  }
  return dividend;
}

addItem("fib(10): "+fib(10));
addItem("fact(5): "+fact(5));
addItem("gcd (36,10): "+gcd(36,10));
