show()

class Book{
    constructor(name, author, type) {
        this.name = name;
        this.author = author;
        this.type = type;
    }
}

class Display{
    add(book){
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
    clear(){
        let addbook = document.getElementById('addbook')
        addbook.reset()
    }
    validate(book){
        if(book.name.length<2 || book.author.length<2){
            return false
        }
        else{
            return true
        }
    }
    showmsg(type,messageElem){
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
}
// add sumbit event listener

let addbook = document.getElementById('addbook')
addbook, addEventListener('submit', function SubmitForm(e) {
    
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
    
    let display=new Display()

        data = localStorage.getItem("notes");
        if (data == null) {
            note = []
        }
        else {
            
            note = JSON.parse(data);
        }
        note.push(book);
        
        localStorage.setItem("notes", JSON.stringify(note));

    
    
    if (display.validate(book)){
        display.add(book);
        // storing in localstorage
       
        
        display.clear();
        display.showmsg('success','Book has been successfully added')
    }
    else{
        display.showmsg('warning','Field has validation,must contain Text')
    }
    e.preventDefault()
})

function show(){
    data = localStorage.getItem("notes");
    if (data == null) {
        note = []
    }
    else {
            
        note = JSON.parse(data);
    }
    html=''
    note.forEach((element) => {
        html+=`
        <tr>
            <td>${element.name}</td>
            <td>${element.author}</td>
            <td>${element.type}</td>
        </tr>   
        `
    })
    let tableBody=document.getElementById('tableBody')  
    tableBody.innerHTML=html
} 