#!/usr/bin/node
const args = process.argv.slice(2);
const integerNumber = parseInt(args[0]);
if (Number.isInteger(integerNumber)) {
  for (let i = 0; i < integerNumber; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
