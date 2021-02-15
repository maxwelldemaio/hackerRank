/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    sumIfNoneMissing = nums.length;
    actualSum = 0;

    for (let i = 0; i < nums.length; i++) {
        actualSum += nums[i];
        sumIfNoneMissing += i;
    }

    return sumIfNoneMissing - actualSum;
};