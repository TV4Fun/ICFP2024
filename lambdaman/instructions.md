Welcome to the Lambda-Man course.

It was the year 2014, and many members of our community worked hard to control Lambda-Man. Now, ten years later, this wonderful event is still memorized by holding a small Lambda-Man competition.

This course will teach you how to optimally control Lambda-Man to eat all pills. There is no fruit involved (neither low-hanging nor high-hanging), and even better: no ghosts! The input to each problem is a simple rectangular grid such as the following:

```
###.#...
...L..##
.#######
```

The grid contains exactly one `L` character, which is the starting position of Lambda-Man. There will be one or more `.` characters indicating the locations of pills to be eaten, and `#` characters are walls. The outside boundary of the grid is considered to consist of walls as well.

A solution should be a string of `U`, `R`, `D` and `L` characters (up, right, down, left, respectively) indicating the path to take. For example, a possible solution to the above example grid is the following path:
```
LLLDURRRUDRRURR
```
When Lambda-Man is instructed to move into a square containing a wall, nothing happens and the instruction is skipped. Your solution may consist of at most `1,000,000` characters.

The following levels are available:
* [lambdaman1] Your score: 33. Best score: 33.
* [lambdaman2] Your score: 44. Best score: 44.
* [lambdaman3] Your score: 64. Best score: 58.
* [lambdaman4] Your score: 1634. Best score: 126.
* [lambdaman5] Your score: 2012. Best score: 130.
* [lambdaman6] Your score: 75. Best score: 73.
* [lambdaman7] Your score: 2010. Best score: 125.
* [lambdaman8] Your score: 4917. Best score: 113.
* [lambdaman9] Your score: 171. Best score: 110.
* [lambdaman10] Your score: 25403. Best score: 127.
* [lambdaman11] Your score: 340583. Best score: 154.
* [lambdaman12] Your score: 267103. Best score: 154.
* [lambdaman13] Your score: 332243. Best score: 165.
* [lambdaman14] Your score: 406839. Best score: 165.
* [lambdaman15] Your score: 360419. Best score: 154.
* [lambdaman16] Your score: 8209. Best score: 153.
* [lambdaman17] Your score: 62357. Best score: 127.
* [lambdaman18] Your score: 404801. Best score: 191.
* [lambdaman19] Your score: 740683. Best score: 273.
* [lambdaman20] Your score: 851621. Best score: 201.
* [lambdaman21] Your score: 403695. Best score: 143.

To submit a solution, send an ICFP expression that evaluates to:

```
solve lambdamanX path
```

Your score is number of bytes that the ICFP expressions consists of (i.e. the size of the POST body), so a lower score is better.