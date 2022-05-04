let arr=document.getElementById('arr')
let textarea=document.getElementById('floatingTextarea2')
let btn=document.getElementById('btn')
let result=document.getElementById('result')
let items = ["Hello this is software developer tanka sodari", "I am having trouble nowadays and got anxity", "Yesterday i found a wallet full of paper's money", "Could u bring a glass of water for me", "Show me the deck of card and tell which one is ace and which one of spades"];
function random_item(items){
    let rand=Math.floor(Math.random()*items.length);   
    arr.innerText=items[rand]
    let date=new Date()
    starttime=date.getTime();
    btn.innerText="Done"   

}
function wordcounter(totalword){
    let textareaword=totalword.split(" ").length
    return textareaword
}
function nextfunc() {
    let date=new Date()
    endtime=date.getTime();
    let total_time=(endtime-starttime)/1000
    let textareavalue=textarea.value;
    let wordcount= wordcounter(textareavalue)
    
    let speed=Math.floor((wordcount/total_time)*60)
    
    const{count,errorword}=calculate(arr.innerText,textareavalue)
  
    result.innerHTML=` you typing speed is ${speed} word per minute and you take ${total_time} second and total correct word is ${count} and error word is ${errorword}` 

}
function calculate(str1,str2){
    let word1=str1.split(" ");
    let word2=str2.split(" ");
    let count=0
    word1.forEach((item,index) => {
        if (item==word2[index]){
            count++
            
        }
    });
    let errorword=(word1.length-count)
    return {count:count,errorword:errorword}

}
// callback function doesn't have their own 'this' or 'args' binding
btn.addEventListener('click',()=>{ 
    if (btn.innerText=='Start'){
        textarea.disabled=false;
        result.innerHTML=``
        random_item(items);

    }else if(btn.innerText=='Done'){
        textarea.disabled=true;
        btn.innerText='Start'
        nextfunc();
        
    }   
// btn.addEventListener('click',function(){ 
//     if (this.innerText=='Start'){
//         textarea.disabled=false;
//         random_item(items);

//     }else if(this.innerText=='Done'){
//         textarea.disabled=true;
//         btn.innerText='Start'
//          nextfunc();
//     }
      
})





