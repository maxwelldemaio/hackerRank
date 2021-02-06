/**
 * @param {string} pattern
 * @param {array}
*/
const makePatternArr = function(pattern) {
    let i = 0;
    let j = 1;
    let pattArr = [];
    pattArr[0] = 0;

    while (j < pattern.length) {
        if (pattern[i] == pattern[j]) {
            // Prefix/Suffix pair found
            // Place value of (i + 1) at pattern[j]
            pattArr[j] = i + 1;
            i++, j++;
        }
        else {
            if (i != 0) {
                i = pattArr[i - 1];
            } else {
                // No prefix/suffix pair found, assign 0
                pattArr[j] = 0;
                j++;
            }
        }
    }
    return pattArr;
}


/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if (needle === "") {
        return 0;
    }
    if (haystack === needle) {
        return 0;
    }
    // Create pattern suffix/prefix array 
    pattArr = makePatternArr(needle);

    // Initialize pointers for needle/haystack
    let i = 0;
    let j = 0;

    while (i < haystack.length) {
        if (haystack[i] == needle[j]) {
            // Match found, keep matching
            i++, j++;
        } else {
            // Not a match, check pattern array for value at (i - 1)
            // This value tells us the length of the longest prefix/suffix pair
            // That value also tells us our next comparison pt in the pattern
            if (j != 0) {
                j = pattArr[j - 1];
            } else {
                i++;
            }
        }
        if (j == needle.length) {
            // Pattern completely matched
            return i - j;
        }
    }
    return -1;
};


// Test cases
console.log(makePatternArr("aabaaac"));
console.log(strStr("aabaaabaaac", "aabaaac"));
