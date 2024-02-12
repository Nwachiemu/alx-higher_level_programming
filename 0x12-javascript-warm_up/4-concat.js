
  
  if (process.argv[2] === '-c' && process.argv[6] === '-cool'){
    console.log('c is cool');   

  }else if (process.argv[2] === '-c' ){
    console.log('c is'+process.argv[2] );   

  }else{
       console.log(process.argv[2] +' is  '+process.argv[6] );
     
  }

     
