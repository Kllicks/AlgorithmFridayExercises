// in JavaScript write an algorithm that takes a string of multiple words and returns the longest word

// function longestWord(string) {
//     string = string.split(' ');
//     let num = 0;
//     let longest = string[num];
//     for(let num=0; num<string.length; num++){
//         if(string[num].length > longest.length) {
//             longest = string[num];
//         }
//     }
//     console.log(longest);
// }
// longestWord("hello this is kyle and this is a string");

const string = "this is a string with different length words";

function longestWord(string) {
    let words = string.split(' ');
    const longest = words.sort(function (a, b) {
        return b.length - a.length;
    });
    return longest[0];
}
console.log(longestWord(string));