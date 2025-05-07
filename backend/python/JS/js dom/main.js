// document.getElementById("btn").addEventListener("click", function(){
//     document.getElementById("text").innerHTML= "matn ozgardi"
//     document.querySelector("#text").style = "color:red"
// })








document.querySelector("#qwe").addEventListener("click", function () {
    var qwer = document.createElement("li")
    qwer.textContent = "yangi element"
    document.querySelector("#list").appendChild(qwer)

})

document.querySelector("#qwerty").addEventListener("click", function () {
    let list = document.querySelector("#list")
    if (list.children.length > 0) {
        //ohirgi elementni ochirish
        list.removeChild(list.lastElementChild)
    } else {
        alert("ochirish uchun element mavjud emas")
    }
})

document.querySelector("#showbtn").addEventListener("click", function () {
    let inputText = document.querySelector("#userinp").value
    document.querySelector("#output").textContent = inputText
})
// let rand = Math.floor(Math.random() * 10) + 1 
// console.log(rand)  
function getRamdomcolor() {
    let letters = '0123456789ABCDEF'
    let color = '#'
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)]
    }
    return color
}
getRamdomcolor()

document.querySelector("#runcolor").addEventListener("click", function () {
    document.querySelector("#colorBox").style.backgroundColor = getRamdomcolor()
})
let modal = document.querySelector("#mumodal")
document.querySelector("#opnmodalbtn").addEventListener("click", function () {
    modal.style.display = "block"
})
document.querySelector("#close").addEventListener("click", function () {
    modal.style.display = "none"
})


let count = 0
document.querySelector("#posCountBtn").addEventListener("click", function () {
    // count = count + 1
    // count += 1
    count++
    document.querySelector("#count").innerHTML = count
})
document.querySelector("#pos2").addEventListener("click", function () {
    count = count - 1
    document.querySelector("#count").innerHTML = count
})