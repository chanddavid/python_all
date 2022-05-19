

        //const detail={     
        //    func1:function(name){
        //        console.log(`hello ${name}, your age is  ${this.age}`)
        //    }          
        //}
        //const access={ 
        //    age:24,
        //    address:'tkp',  
        //}
        //detail.func1.call(access,"tanka")


        const detail={    
            func1:function(){
                console.log(`hello ${this.name}, your age is  ${this.age}`)
            }
           
        }
        const access={
            name:"tanka",
            age:24,
            address:'tkp', 
        }
        detail.func1.call(access)
 

