
showdata()
//if a user add a note then add to the local storage
let addBtn = document.getElementById("addBtn");
addBtn.addEventListener("click", function (e) {
    let addTxt = document.getElementById("floatingTextarea2");

    let data = localStorage.getItem("notes");

    // if (data == null) {
    //     note = [];
    // }
    // else {
    //     note = JSON.parse(data);

    // }
    // or this
    note = JSON.parse(data);
    // array has push operator 
    note.push(addTxt.value);
    localStorage.setItem("notes", JSON.stringify(note));
    addTxt.value = " ";
    console.log(note);
    showdata()

})
// function to show data
function showdata() {
    let data = localStorage.getItem("notes");
    // if (data == null) {
    //     note = [];
    // }
    // else {
    //     note = JSON.parse(data);
    // }
    note = JSON.parse(data);
    let html=''
   
    // array has forEach operator
    note.forEach((element, index) => {
        html+=`
        <div class="col-md-3 notecard mb-5">
            <div class="card" style="width: 18rem;">
                <div class="card-body ">
                    <h5 class="card-title">Note ${index+1}</h5>
                    <hr>
                    <p class="card-text">${element}
                    </p>
                    <a href="#" class="btn btn-danger" onclick=deleteNote(this.id) id="${index}">Delete Notes</a>
                </div>
            </div>
        </div>
`
    });
    let display=document.getElementById("notes")
    if (note!=0){
        display.innerHTML=html;
    }
    else{
        display.innerHTML=` You dont have any Notes. Please Add Some`
    }
}
// to delete
// Parse the string in localStorage to JSON 
// Remove the item you don't want (with slice() )
// Make the JSON to string
// Re-set it in the localStorage

function deleteNote(index) {
    let data = localStorage.getItem("notes");
    note = JSON.parse(data);
    note.splice(index,1);
    localStorage.setItem("notes", JSON.stringify(note));
    showdata();
}


// search
let search= document.getElementById("mysearch")
search.addEventListener("input",function(e){
    let input_value=search.value

    let notecard=document.getElementsByClassName("notecard")
    // element lai nikalda array.from user garne
    Array.from(notecard).forEach((element)=>{
        let text=element.getElementsByTagName('p')[0].innerText

        if(text.includes(input_value)){
            element.style.display="block"
        }
        else{
            element.style.display="none"

        }
    })
})
    