#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const array = [];
  const range = process.argv.length;
  for (let i = 2; i < range; i++) {
    array.push(process.argv[i]);
  }
  array.sort();
  console.log(array[range - 4]);
}
