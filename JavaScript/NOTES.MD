
/* sript tag allows is to write JS code of our HTML
 read from TOP to BOTTOM
<script>
    console.log("Day 1: Javascript!");
</script>
*/
console.log("Day 1: Javascript!");
/*
console.log(); 
   - print or display the output
   - console.log("Day 1: Javascript!");
*/

/*  
document.getElementById();
   - retrieves an element from HTML using its ID and let manipulate its properties/attributes.
   - document.getElementById("someid");
*/

/*
EXTERNAL JAVASCRIPT
   - script.js (JavaScript FILE)
               console.log("Hello World!")

   - index.html(HTML FILE)
               <html>
                 <script src="script.js"></script
               </html>
*/
alert("ALERT!") //ALERBOX WHEN PAGE LOADED


4 WAYS FO DECLARING A VARIABLES
  
   1. Automatically
   2. var
   3. let
   4. const

Using let
  > prefered to use by default
    let x = 5;
    let y = 10.2;
    let z = "Hello World";

Using const
  > using const means it cannot be change or reassign once declared 
  const x = 5;
  const y = 10.2;
  const z = "Hello World!";

  What you canot do:
    const x = 5;
    x = 10;   ! YOU CANNOT CHANGE THE VALUE ONCE DECLARED

Using var
  > using var should only use if you want to support older version of browsers
    var x = 5;

