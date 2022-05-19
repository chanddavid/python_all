const score = document.getElementById('score')
const startbox = document.getElementById('startbox')
let car = document.getElementById('car')
const line = document.getElementById('line')

startbox.addEventListener('click', startclicked = () => {
  startbox.className = 'visually-hidden'

  car.classList.remove('invisible');
  car.classList.add('visible');
  // console.log(car)
  line.classList.remove('invisible')
  line.classList.add('visible');
  window.requestAnimationFrame(gameplay);
})

function gameplay() {
  x = window.requestAnimationFrame(gameplay);
  score.innerHTML = `Your Score is ${x}`
}

let keys = {
  ArrowRight: false,
  ArrowLeft: false,
  ArrowUp: false,
  ArrowDown: false
}

//This event is fired when a key is pressed. When you hold down the key without releasing, it fires repeatedly.
document.addEventListener('keydown', (e) => {
  keys[e.key] = true
  // console.log(e.key)
  // console.log(keys)
  movecar()
}, false);

//This event is fired when you release the key that was pressed.
document.addEventListener('keyup', (e) => {
  keys[e.key] = false
  // console.log(e.key)
  // console.log(keys)
  stopcar()
}, false);

movecar = () => {
  let x = car.offsetTop
  let y = car.offsetLeft
  let speed = 5
  if (keys.ArrowLeft == true) {
    y = y - speed
  }
  if (keys.ArrowRight == true) {
    y = y + speed
  }
  if (keys.ArrowUp == true) {
    x = y - speed
  }
  if (keys.ArrowDown == true) {
    x = x + speed
  }
  car.style.top = y + "px"
  car.style.left = x + "px"

  console.log("top top", x)
  console.log("top left", y)

}
stopcar = () => {
  console.log("i ma stoping")
}

