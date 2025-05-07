//JS Date()
let currentDate = new Date();
console.log(currentDate.getMonth());
console.log(currentDate.getDate());
console.log(currentDate.getDay());
console.log(currentDate.getFullYear());
console.log(currentDate.getHours());
console.log(currentDate.getMinutes());
console.log(currentDate.getSeconds());
console.log(currentDate.getMilliseconds())
console.log(currentDate.getHours() + ":" + currentDate.getMinutes() + ":" + currentDate.getSeconds());
console.log(currentDate.getUTCDate());
console.log(currentDate.getUTCMonth());
console.log(currentDate.getUTCDay());


const cars = ["BMW", "Volvo", "Mini"];

 let text = "";
 for (let x of cars) {
     text += x + "br";
 }
 document.getElementById("demo").innerHTML = text;
let qwe = new Date();
console.log(qwe.getDate() + "." + qwe.getMonth() + "  " + qwe.getHours() + ":" + qwe.getMinutes());

let asd = new Date();
console.log(asd.getHours() + ":" + asd.getMinutes() + ":" + asd.getSeconds());

const fruits = ["Apple", "Banana", "Kiwi", "ETC"]
let erty = "";
for (let x of fruits) {
    erty += x + "<br>";
}
document.getElementById("fruits").innerHTML = erty;