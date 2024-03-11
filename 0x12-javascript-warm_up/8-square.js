#!/usr/bin/node
if (isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    let txt = '';
    for (let j = 0; j < Number(process.argv[2]); j++) {
      txt += 'X';
    }
    console.log(txt);
  }
}
