/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
    /* Time complexity O(n+m) */
    s = s.split(" ");
    const result = [];
    /**  @param {string} i  */
    for (i of s) {
        word = i.split("");
        let left = 0;
        let right = word.length - 1;
        while (left < right) {
            tmp = word[left];
            word[left] = word[right];
            word[right] = tmp;
            left += 1;
            right -= 1;
        }
        result.push(word.join(""));
    }
    return result.join(" ");
};

console.log(reverseWords("Let's take LeetCode contest"));
