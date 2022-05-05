

        const detail={     
           func1:function(name){
               console.log(`hello ${name[0]},from ${name[1]} your age is  ${this.age}`)
           }          
        }
        const access={ 
           age:24,
         
        }
        detail.func1.call(access,['tanka','tikapur'])


 

        