/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
    let fPointer = 0;
    let sPointer = numbers.length - 1;
    while (numbers[fPointer] + numbers[sPointer] != target) {
        numbers[fPointer] + numbers[sPointer] < target
            ? fPointer++
            : sPointer--;
    }
    return [fPointer + 1, sPointer + 1];
};

console.log(twoSum([5, 25, 75], 100));
