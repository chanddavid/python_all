//constructor

function Book(name, author, type) {
    this.name = name;
    this.author = author;
    this.type = type;
}


// add sumbit event listener

let addbook = document.getElementById('addbook')
addbook, addEventListener('submit', function SubmitForm(e) {
    e.preventDefault()

    let name = document.getElementById('BookName').value;
    let author = document.getElementById('AuthorName').value;

    if (document.getElementById('Mathematics').checked) {
        var type = document.getElementById('Mathematics').value;
    }
    else if (document.getElementById('Science').checked) {
        var type = document.getElementById('Science').value;
    }
    else {
        (document.getElementById('History').checked)
        var type = document.getElementById('History').value;
    }
    let book = new Book(name, author, type)
    
    if (book.validate(book)){
        book.add(book);
        // storing in localstorage
        data = localStorage.getItem("notes");
        if (data == null) {
            note = []
        }
        else {
 
            note = JSON.parse(data);
        }
        note.push(book);
        localStorage.setItem("notes", JSON.stringify(note));

        book.clear();
        book.showmsg('success','Book has been successfully added')
    }
    else{
        book.showmsg('warning','Field has validation,must contain Text')
    }
})

// add method to display prototype
Book.prototype.add=function(book){
    let html=`
                        <tr>
                            <td>${book.name}</td>
                            <td>${book.author}</td>
                            <td>${book.type}</td>
                        </tr>   
    `
    let tableBody=document.getElementById('tableBody')  
    tableBody.innerHTML+=html

}
Book.prototype.clear=function(){
    let addbook = document.getElementById('addbook')
    addbook.reset()
}
Book.prototype.validate=function(book){
    if(book.name.length<2 || book.author.length<2){
        return false
    }
    else{
        return true
    }
}

Book.prototype.showmsg=function(type,messageElem){
    let message=document.getElementById('message')
    message.innerHTML=` 
                <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                <strong>Message:</strong> ${messageElem}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>`
            setTimeout(() => {
                message.innerHTML=''
            }, 3000);
}



// display details 

function Display(){

}












// //constructor

// function Book(name, author, type) {
//     this.name = name;
//     this.author = author;
//     this.type = type;
// }


// // add sumbit event listener

// let addbook = document.getElementById('addbook')
// addbook, addEventListener('submit', function SubmitForm(e) {
//     e.preventDefault()

//     let name = document.getElementById('BookName').value;
//     let author = document.getElementById('AuthorName').value;

//     if (document.getElementById('Mathematics').checked) {
//         var type = document.getElementById('Mathematics').value;
//     }
//     else if (document.getElementById('Science').checked) {
//         var type = document.getElementById('Science').value;
//     }
//     else {
//         (document.getElementById('History').checked)
//         var type = document.getElementById('History').value;
//     }
//     let book = new Book(name, author, type)
//     console.log(book)
//     let display=new Display()
//     display.add(book);
//     display.clear();
  
// })

// // add method to display prototype
// Display.prototype.add=function(){
//     console.log("added")
// }
// Display.prototype.clear=function(){
//     let addbook = document.getElementById('addbook')
//     addbook.reset()
// }


// // display details 

// function Display(){


// }
