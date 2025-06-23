/*
------------------------------------------------
📘 JavaScript Switch Statement – VS Code Note
------------------------------------------------

✅ What is it?
Switch statement is used to run different code blocks based on different values.

✅ Syntax:
switch(expression) {
  case value1:
    // code block
    break;
  case value2:
    // code block
    break;
  ...
  default:
    // default code block
}

------------------------------------------------
💡 Example: Days of the Week
------------------------------------------------
*/

let day = 3;

switch (day) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  case 4:
    console.log("Thursday");
    break;
  case 5:
    console.log("Friday");
    break;
  default:
    console.log("Weekend");
}

/*
------------------------------------------------
📝 Notes:
- Uses strict comparison (===).
- break is necessary to stop fall-through.
- default runs if no case matches.
- Useful when checking one variable against many values.
------------------------------------------------
*/
