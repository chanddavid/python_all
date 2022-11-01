function Func(a, b) {

    // let lst = []
    // let data = { 'a': a, 'b': b }
    // lst.push(data)
    window.localStorage.setItem("Data", JSON.stringify({ 'a': a, 'b': b }));
    var acct = JSON.parse(window.localStorage.getItem("Data"));

    // acct.push(data)
    // localStorage.setItem("Data", JSON.stringify(acct));
    // var result = JSON.parse(localStorage.getItem("Data"));

    alert(acct['a'], acct['b'])

}