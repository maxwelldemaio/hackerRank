/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if (needle === "") {
        return 0;
    }

    const haySize = haystack.length;
    const needleSize = needle.length;

    // Loop over (haystack.len - needle.len)
    for (let i = 0; i < haySize - needleSize + 1; i++) {
        // Check if letter[i + j] in haystack is equal to letter[j] needle
        for (let j = 0; j < needleSize; j++) {
            if (haystack[i + j] != needle[j]) {
                break;
            }
            if (j + 1 === needleSize) {
                return i;
            }
        }
    }

    return -1;
};


// Test cases
console.log(strStr("hello", "ll"));
console.log(strStr("aaaaaa", "bbba"));
console.log(strStr("hi", ""));
