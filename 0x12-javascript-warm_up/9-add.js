#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const args = process.argv.slice(2);
const firstNumber = parseInt(args[0]);
const secondNumber = parseInt(args[1]);
const result = add(firstNumber, secondNumber);
console.log(result);
