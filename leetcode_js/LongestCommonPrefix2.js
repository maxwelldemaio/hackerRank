var longestCommonPrefix = function(strs) {
    if (strs.length == 0) {
        return '';
    }
    if (strs.length == 1) {
        return strs[0];
    }

    let longest = '';
    let comparWord = strs[0];
    let comparIndex = 0;

    // Loop over each letter in strs[0]
    for (let comparLetter of comparWord) {
        // Loop over every word from strs[1:]
        for (let i = 1; i < strs.length; i++) {
            // Check for match
            // Also check if we're going out of bounds
            currLetter = strs[i][comparIndex];
            if (comparIndex > strs[i].length || 
                    comparLetter != currLetter) {
                return longest;
            }
        }
        // Check next set of chars at strs[1:]
        // Add to longest commmon prefix
        comparIndex++;
        longest += comparLetter
    }
    return longest;
}

// Tests
console.log(longestCommonPrefix(['flower', 'flow', 'flowing']));