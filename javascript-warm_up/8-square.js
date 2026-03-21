#!/usr/bin/node
const x = process.argv[2];
const num = parseInt(x);

if (isNaN(num) || num < 1) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
