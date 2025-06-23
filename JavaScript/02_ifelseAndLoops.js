/*
=======================================================
📘 JavaScript Control Statements & Loops – VS Code Note
=======================================================

🔹 CONTROL STATEMENTS:
Control how the flow of code execution happens.

1️⃣ if statement
2️⃣ if...else statement
3️⃣ if...else if...else ladder
4️⃣ switch statement (already covered in a separate note)
5️⃣ ternary operator (already covered in a separate note)

-------------------------------------------------------
🔸 Example 1: if...else
-------------------------------------------------------
*/

let marks = 85;

if (marks >= 90) {
  console.log("Grade: A");
} else if (marks >= 75) {
  console.log("Grade: B");
} else if (marks >= 60) {
  console.log("Grade: C");
} else {
  console.log("Grade: F");
}

/*
-------------------------------------------------------
🔹 LOOPS IN JAVASCRIPT:
Used to repeat code until a condition is met.

1️⃣ for loop
2️⃣ while loop
3️⃣ do...while loop
4️⃣ for...of loop (for arrays, strings)
5️⃣ for...in loop (for objects)
-------------------------------------------------------
*/

/*
-------------------------------------------------------
🔸 Example 2: for loop
-------------------------------------------------------
*/
for (let i = 1; i <= 5; i++) {
  console.log("Iteration:", i);
}

/*
-------------------------------------------------------
🔸 Example 3: while loop
-------------------------------------------------------
*/
let count = 1;
while (count <= 3) {
  console.log("While count:", count);
  count++;
}

/*
-------------------------------------------------------
🔸 Example 4: do...while loop
-------------------------------------------------------
*/
let num = 1;
do {
  console.log("Do-While number:", num);
  num++;
} while (num <= 2);

/*
-------------------------------------------------------
🔸 Example 5: for...of loop (used for arrays, strings)
-------------------------------------------------------
*/
let fruits = ["apple", "banana", "cherry"];

for (let fruit of fruits) {
  console.log("Fruit:", fruit);
}

/*
-------------------------------------------------------
🔸 Example 6: for...in loop (used for objects)
-------------------------------------------------------
*/
let person = {
  name: "Vishal",
  age: 21,
  city: "Delhi"
};

for (let key in person) {
  console.log(key + ":", person[key]);
}

/*
-------------------------------------------------------
✅ Summary:
✔ Control Statements help decide what to execute.
✔ Loops help repeat tasks efficiently.
✔ Use for...in with objects and for...of with arrays.
=======================================================
*/
