/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length != t.length) {
        // Lengths don't match
        return false;
    }

    let myHash = {};

    // Create hashmap from s
    for (let letter of s) {
        if (myHash[letter] === undefined) {
            myHash[letter] = 1;
        } else {
            myHash[letter]++;
        }
    }

    // Compare t and hashmap
    for (let letter of t) {
        if (myHash[letter] === undefined) {
            // Letter not in hashmap
            return false;
        }

        if (myHash[letter] < 1) {
            // This letter count in t exceeds s
            return false;
        }
        // Instance found in hashmap, now decrement
        myHash[letter]--;
    }
    return true;
};

// Tests
console.log(isAnagram("acc", "abc"));
console.log(isAnagram("car", "rat"));
console.log(isAnagram("cinema", "iceman"));
