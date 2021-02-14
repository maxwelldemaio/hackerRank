/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    // The stack to keep track of opening brackets.
    let stack = [];
    // Hash map for keeping track of mappings.
    const mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for (let char of s) {
        // If the character is an closing bracket
        if (mapping[char]) {
            // Pop the topmost element from the stack
            let topElement = stack.pop();

            // The mapping for the opening bracket in our hash and the top
            // element of the stack don't match, return False
            if (mapping[char] !== topElement) {
                return false;
            } 
        } else {
            // We have an opening bracket, simply push it onto the stack.
            stack.push(char);
        }
    }

    // Check if stack is empty
    if (stack.length === 0) {
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