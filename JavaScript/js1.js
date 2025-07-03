
let concatenate = "NICER";
alert("HI " + concatenate); //ALERTBOX WHEN PAGE LOADED

let word = "MarkChristian";
let length = word.length;

console.log(length); // This will log the length of the string "MarkChristian"

alert("The length of the word is: " + length); //ALERTBOX WHEN PAGE LOADED

let meow = "Sunny";
meow = meow.toLowerCase(); // This will convert the string to lowercase but does not change the original string
console.log(meow); // This will log "sunny"

//REPLACE METHOD .replace() .repalceAll()
let replaceMe = "Dog";
replaceMe = replaceMe.replace("Dog", "Cat"); // This will replace "Dog" with "Cat"
console.log(replaceMe); // This will log "Cat"

// SLICE METHOD .slice()
let sliceMe = "HelloMen";
sliceMe = sliceMe.slice(1,3); // This will extract characters from index 1 to 2 (3 is not included)
alert(sliceMe); // This will alert "el"

// String Template Literals]
let Literals = `Hello, "I can type anything" `;
console.log(Literals); // This will log the string with quotes included
alert(`Hi! ${sliceMe}. Mark!`);