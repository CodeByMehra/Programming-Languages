// -------------------------------------------
// 🟨 JAVASCRIPT DATA TYPES - DETAILED NOTES
// -------------------------------------------

// ✅ JavaScript supports two categories of data types:
// 1. Primitive Data Types
// 2. Non-Primitive (Reference) Data Types

// -------------------------------------------
// ✅ 1. PRIMITIVE DATA TYPES
// -------------------------------------------
// These hold single values and are immutable.

let name = "Alice";        // String
let age = 25;              // Number
let isStudent = true;      // Boolean
let x = null;              // Null (intentional absence of any value)
let y;                     // Undefined (value not assigned)
let symbol = Symbol("id"); // Symbol (unique and immutable)
let bigInt = 1234567890123456789012345678901234567890n; // BigInt (for large integers)

// --- Type checking using typeof ---
console.log(typeof name);      // string
console.log(typeof age);       // number
console.log(typeof isStudent); // boolean
console.log(typeof x);         // object  ⚠️ special case: typeof null is 'object'
console.log(typeof y);         // undefined
console.log(typeof symbol);    // symbol
console.log(typeof bigInt);    // bigint

// -------------------------------------------
// ✅ 2. NON-PRIMITIVE (REFERENCE) DATA TYPES
// -------------------------------------------
// These hold collections of values and are mutable.

let person = { name: "Alice", age: 25 };     // Object
let numbers = [1, 2, 3, 4, 5];               // Array (special type of object)
let today = new Date();                      // Date object
function greet() { console.log("Hi!"); }     // Function

// --- typeof results for reference types ---
console.log(typeof person);   // object
console.log(typeof numbers);  // object
console.log(typeof greet);    // function
console.log(typeof today);    // object

// -------------------------------------------
// ✅ DYNAMIC TYPING IN JAVASCRIPT
// -------------------------------------------
// Variables are not bound to any specific data type.
// The type of variable can change at runtime.

let data = "hello";       // string
data = 123;               // now it's a number
data = true;              // now it's a boolean

console.log(data);        // Output: true
console.log(typeof data); // Output: boolean

// -------------------------------------------
// ✅ TYPE CONVERSION
// -------------------------------------------

// --- String to Number
let str = "123";
let num = Number(str);   // 123

// --- Number to String
let n = 456;
let str2 = String(n);    // "456"

// --- Boolean Conversion
console.log(Boolean(0));      // false
console.log(Boolean("Hi"));  // true

// -------------------------------------------
// ✅ SUMMARY TABLE
// -------------------------------------------
// | Type        | Example                  | typeof result |
// |-------------|--------------------------|----------------|
// | String      | "hello"                  | "string"       |
// | Number      | 123                      | "number"       |
// | Boolean     | true / false             | "boolean"      |
// | Null        | null                     | "object" ⚠️    |
// | Undefined   | undefined                | "undefined"    |
// | Symbol      | Symbol("id")             | "symbol"       |
// | BigInt      | 12345678901234567890n    | "bigint"       |
// | Object      | {a: 1, b: 2}             | "object"       |
// | Array       | [1, 2, 3]                | "object"       |
// | Function    | function() {}            | "function"     |

// -------------------------------------------
// ✅ NOTES
// -------------------------------------------
// - JavaScript is dynamically typed
// - Arrays and functions are technically objects
// - typeof null === "object" is a known historical bug
// - Always use === for strict comparison (checks value and type)

// Example:
console.log(5 == "5");  // true (type conversion)
console.log(5 === "5"); // false (no conversion)
