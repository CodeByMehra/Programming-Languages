/*
------------------------------------------------
📘 JavaScript Ternary Operator – VS Code Note
------------------------------------------------

✅ What is it?
The ternary operator is a shorthand way to write if...else conditions.

✅ Syntax:
condition ? expressionIfTrue : expressionIfFalse;

------------------------------------------------
💡 Example 1: Age Check
------------------------------------------------
*/

let age = 18;

// Ternary Operator
let voteMessage = (age >= 18) 
  ? "You are eligible to vote." 
  : "You are not eligible to vote.";

console.log(voteMessage);  // Output: You are eligible to vote.

/*
------------------------------------------------
💡 Example 2: Even or Odd
------------------------------------------------
*/

let number = 7;

let result = (number % 2 === 0) ? "Even" : "Odd Number";
console.log("The number is", result);  // Output: The number is Odd

/*
------------------------------------------------
✅ Notes:
- Compact and readable for simple conditions.
- Not recommended for complex logic.
------------------------------------------------
*/
