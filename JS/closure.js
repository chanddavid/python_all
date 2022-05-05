
        let c=2
        const funcA=(b)=>{
            let a=2
            const funcB=()=>{
                let sum=a+b+c
                console.log(`the answer is ${sum}`)
            }
            funcB()
        }
        funcA(2)

        //const funcA = (name) => {
        //    let a = "what is closure ?"
        //    let b = "what is higher order funtion ?"
        //    let c = "what is IIEF ?"
        //    return (()=>{
        //        if (name === 'tanka') {
        //            console.log(`hello ${name}, ${a}`)
        //        }
        //        if (name === 'prajwol') {  
        //            console.log(`hello ${name}, ${b}`)     
        //        }
        //        if (name === 'tulasa') {  
        //        }
        //    })
        //}
        funcA('tanka')()
  