<<<<<<< HEAD
#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2]));
}
=======
if (isNaN(process.argv[2])) {
    console.log('Not a number');
  } else {
    console.log('My number:' + parseInt(process.argv[2]));
  }
  
  
>>>>>>> 23b188e5acd68dfd9a585eb9383523b4d6dee24c
