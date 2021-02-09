/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let myArr = [];
    for (let i = 1; i < n + 1; i++) {
        // Cases
        if (i % 3 == 0 && i % 5 != 0) {
            myArr.push("Fizz")
        } else if (i % 5 == 0 && i % 3 != 0) {
            myArr.push("Buzz");
        } else if (i % 5 == 0 && i % 3 == 0) {
            myArr.push("FizzBuzz");
        } else {
            myArr.push(String(i));
        }
    }
    return myArr;
};

console.log(fizzBuzz(15));