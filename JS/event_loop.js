// console.log("hey")
// setTimeout(function func(){
//     console.log('hello')
// },0)
// console.log('hi')

function f1() {
    setTimeout(function func(){
        console.log('hello')
    },5000)
  }
  function f2() {
    console.log('hi')
  }
  function f3() {
    console.log('hiiiii')
  }
  
  // Invoke the functions one by one
  f1();
  f2();
  f3();