/* Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
 */ 


function toCamelCase(str){
  array = str.split(/[-_]/);
  for (let i = 0; i < array.length; i++) {
    if (i > 0) {
      console.log(array[i])
      word = array[i].split("");
      copy = word;
      firstLetter = copy[0].toUpperCase();
      word.splice(0, 1, firstLetter);
      array[i] = word.join("");
    }
  }
  return array.join("");
  
}

console.log(toCamelCase("the-stealth-warrior"))
console.log(toCamelCase("The_Stealth_Warrior"))
console.log(toCamelCase("The_Stealth-Warrior"))