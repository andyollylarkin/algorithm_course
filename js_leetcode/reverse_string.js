/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function (s) {
    /* Time complexity O(n/2) */
    let left = 0;
    let right = s.length - 1;
    while (left < right) {
        let tmp = s[left];
        s[left] = s[right];
        s[right] = tmp;
        right -= 1;
        left += 1;
    }
};

// reverseString(["H", "a", "n", "n", "a", "h"]);
reverseString(["H", "e", "l", "l", "o"]);
