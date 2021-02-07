/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length == 1) {
        return strs[0];
    }
    if (strs.length == 0) {
        return "";
    }

    let count = "";
    let i = 0;
    // Find smallest string in array (index 0)
    strs.sort(function(a, b){
        return a.length - b.length;
    });

    for (let j = 0; j < strs[0].length; j++) {
        for (let k = 1; k < strs.length; k++) {
            if(strs[0][i] == strs[k][j]) {
                if(k == strs.length - 1){
                    count += strs[0][i]
                    i++;
                }
            } else {
                return count;
            }
        }
    }
    return count;
};

// Test cases
// console.log(longestCommonPrefix(strs = ["flower","flow","flight"]));
console.log(longestCommonPrefix(["aca", "cba"]));
