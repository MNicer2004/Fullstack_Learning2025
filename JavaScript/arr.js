//let name1 = "Alenere";
//let name2 = "David";
//let gender = "she";
//let drink = "coffee";

//console.log(`${name1}, the friendly neighbor, waved at ${name2} as ${gender} walked by ${name2}'s house. ${name2} smiled back and invited ${name1} in for a cup of ${drink}.`);

// A R R A Y S []
let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let names = ["Alenere", "David", "John", "Jane", "Doe"];
let floats = [1.1, 2.2, 3.3, 4.4, 5.5];

//LENGTH
arr = arr.length;
console.log(arr); // Output: 10

//UPDATING ARRAY

names = names[0] = "mark";
console.log(names); 

arr = arr[2] = 1000;
console.log(arr);

//adding elements to an array
names.push("Alenere");
console.log(names); // Output: ["mark", "David", "John", "Jane", "Doe", "Alenere"]  

names.unshift("Deku");  
console.log(names); // Output: ["Deku", "mark", "David", "John", "Jane", "Doe", "Alenere"]

//deleting elements from an array
names.pop();
console.log(names); // Output: ["Deku", "mark", "David", "John", "Jane", "Doe"]
names.shift();
console.log(names); // Output: ["mark", "David", "John", "Jane", "Doe"] 
