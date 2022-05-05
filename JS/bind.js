// const obj1={
//     name:'tanka',
//     age:'23',
//     funcA:function(address){
//         console.log(` hello ${this.name} your age is ${this.age} and your address is ${address}`)
//     }
// }
// const obj2={
//     name:'david',
//     age:'20',
// } 

// const commonfunc=obj1.funcA.bind(obj2)
// commonfunc('tikapur')

const obj1={
    name:'tanka',
    age:'23',
}
const obj2={
    name:'david',
    age:'20',
} 
const obj3={
    name:'kalu',
    age:'22',
} 

function funcA(address){
    console.log(` hello ${this.name} your age is ${this.age} and your address is ${address}`)
}

const commonfunc=funcA.bind(obj1)
commonfunc('tikapur')