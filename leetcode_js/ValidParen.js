/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    // We are going to mimic a stack data structure
    let parenStack = [];

    
    for (let letter of s) {
        // Push opening brackets to stack
        if ("({[".includes(letter)) {
            parenStack.push(letter);
        }
        // Check for validity
        if(")}]".includes(letter)) {
            lastOpen = parenStack.pop();
            if (lastOpen === "(" && letter === ")") {
                continue;
            } else if (lastOpen === "[" && letter === "]") {
                continue;
            } else if (lastOpen === "{" && letter === "}") {
                continue;
            } else {
                return false;
            }
        }
    }

    // Check if stack is empty
    if (parenStack.length === 0) {
        return true;
    }
    return false;
};

/* Example stacks:
 | [ |
 | ( |
*/

// Tests
console.log(isValid("{[]}"));
console.log(isValid("([)]"));