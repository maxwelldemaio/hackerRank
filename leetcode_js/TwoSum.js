/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    if (nums.length == 2) {
        // Only one solution, so must be both elements
        return [0, 1];
    }

    myHash = {};
    for (let i = 0; i < nums.length; i++) {
        // Check if number in our hashmap
        if (nums[i] in myHash) {
            return [i, myHash[nums[i]]];
        } else {
            // Add its compliment and index
            myHash[target - nums[i]] = i;
        }
    }
    return -1;
};

// Tests
console.log(twoSum([2,7,11,15], 9));