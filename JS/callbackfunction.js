
        // const funA=()=>{
        //     setTimeout(()=>{
        //         console.log("func A")
        //         funB()
        //     },3000)
           
        // }
        // const funB=()=>{
        //     console.log("func B")
        // }
        // funA()
        

        const funA=(friend,funcback)=>{
            console.log(`hello tulasa i am talking to ${friend}, i will call you back`)
            funcback()
        }
        const funB=()=>{
            console.log("Hello tulasa how are u okay")
        }
        funA("prajwol",funB)
        
