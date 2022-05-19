
        //const funcA=(name)=>{
        //    if (name==="tanka"){
        //        return (){
        //            console.log(`hello ${name}`)
        //        }
        //    }
        //}
        //funcA('tanka')()

        const funcA = (name) => {
            if (name === "tanka") {
                return (age) => {
                    console.log(`hello ${name} your age is ${age}`)
                }
            }
        }
        funcA('tanka')(23)


