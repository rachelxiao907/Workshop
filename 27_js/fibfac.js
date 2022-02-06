// Team Odin :: Rachel Xiao, Yuqing Wu
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
var fact = (n) => {
  if (n <= 1) { //base case
   return 1;
  } else {
   return fact(n-1) * n; //product of all the previous numbers in the sequence
  }
};

var fib = (n) => {
  if (n <= 1) { //base case
   return n;
  } else {
   return fib(n-1) + fib(n-2); //sum of last two numbers in the sequence
  }
};
