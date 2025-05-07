// //ChartAt (index)
// let str = 'hello';
// console.log(str.charAt(1));



// //chareCodeAt(index)
// let  str1 = 'hello';
// console.log(str1.charCodeAt(4));//Uni code = 72



// //cocat()
// let str2 = 'hello';
// let str3 = 'world';
// console.log(str2.concat(' ',str3)) 


// //includes(string,index)

// let str4 = 'Hello world';
// console.log(str4.includes("world",0));//true
// console.log(str4.includes("as",0));//false

// // endWith(string,length)
// let str5 = 'Hello world and ';
// console.log(str5.endsWith("and "))//true
// console.log(str5.endsWith("and"))//false






//1
let text1 = 'no problem';
console.log(text1.charAt(3));
let qwe = 'hello its weee';
console.log(qwe.charAt(2));
//2
let text2 = 'here is information';
console.log(text2.charCodeAt(3));

let rty = 'hand up mother father';
console.log(rty.charCodeAt(4));
//3
console.log(text1.concat(' ', text2));
console.log(qwe.concat(' ', rty));
//4
console.log(text2.includes('is'));
console.log(text2.includes('heres'));
console.log(qwe.includes('hello'));
console.log(qwe.includes('op'));
//5
console.log(text1.endsWith('lem'));
console.log(text1.endsWith('lem '));
console.log(qwe.endsWith('weee'));
console.log(qwe.endsWith('wee'));