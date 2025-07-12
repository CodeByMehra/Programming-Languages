/*
====================================================
📘 JavaScript DOM (Document Object Model) – VS Code Note
====================================================

✅ What is DOM?
-------------------------
DOM stands for **Document Object Model**. It represents the **structure of an HTML document** as a tree of objects.

📄 Browser loads HTML ➜ creates a DOM ➜ JavaScript can access and modify HTML/CSS through it.

✅ DOM Hierarchy:
-------------------------
- document
  └── html
      ├── head
      └── body
          ├── h1, p, div, etc.

----------------------------------------------------
🔹 Accessing Elements in DOM
----------------------------------------------------
*/

// By ID
let heading = document.getElementById("main-heading");

// By Class Name
let boxes = document.getElementsByClassName("box");

// By Tag Name
let paragraphs = document.getElementsByTagName("p");

// By CSS Selector
let firstDiv = document.querySelector("div");
let allBoxes = document.querySelectorAll(".box");

/*
----------------------------------------------------
🔹 Modifying Elements
----------------------------------------------------
*/

let title = document.getElementById("main-heading");
title.innerText = "Updated Heading";         // Change text
title.style.color = "black";                 // Change style
title.style.fontSize = "30px";              // CSS manipulation

/*
----------------------------------------------------
🔹 Adding and Removing Elements
----------------------------------------------------
*/

// Create a new element
let newPara = document.createElement("p");
newPara.innerText = "This is a new paragraph";

// Append to body
document.body.appendChild(newPara);

// Remove an element
let toRemove = document.getElementById("remove-me");
toRemove.remove();

/*
----------------------------------------------------
🔹 DOM Events (Interaction)
----------------------------------------------------
*/

let btn = document.getElementById("click-btn");

btn.addEventListener("click", function () {
  alert("Button was clicked!");
});


/*
----------------------------------------------------
✅ Common DOM Properties:
----------------------------------------------------
- innerText → text inside element
- innerHTML → HTML inside element
- style → access CSS styles
- classList → add/remove/toggle CSS classes
- value → for input fields
====================================================
*/
