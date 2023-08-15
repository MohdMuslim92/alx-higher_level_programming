#!/usr/bin/node
const args = process.argv.slice(2);
const integerNumber = parseInt(args[0]);
if (Number.isInteger(integerNumber)) {
  console.log('My number: ', args[0]);
} else {
  console.log('Not a number');
}
