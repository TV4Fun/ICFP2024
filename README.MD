# Team Dimetrodon

Woohoo ICFP 2024! This was a really fun project and I am amazed at how much puzzle solving the three of us have managed
to do in the last three days, and I'm sure we'll continue to poke at these problems in the coming weeks to see if we can
improve our results.

# Code Overview

The dates on our various commits should be reasonably accurate as to when the code was written.
The last commit in the lightning round
was [8787105](https://github.com/TV4Fun/ICFP2024/commit/87871051b3f48742bda4952c5d46813c16b1c5e1).
We had at that point implemented an ICFP interpreter
that was good enough to pass the language test, but broke for more complex expressions of lambdas and
variable capture. We had brute-force solvers for Lambdaman and Spaceship. We were treating Lambdaman as
a traveling salesman problem and using `networkx` to solve it.

On the second day, we made improvements

## Root directory

In the root directory, you will find our basic interface and test code. We completed [terminal](terminal.py) within the
first few hours and used that to get to the other challenges. In subsequent days, we added the ability to send more
complex expressions directly by enclosing in curly braces, to show the raw response from the communication channel, and
to decode numeric strings returned by `U$`

## ICFP

The [icfp](icfp/) folder contains our coded related to ICFP expression encoding and decoding. The meat of the reader
and evaluator can be found in [decode.py](icfp/decode.py), and that is the one that has gone through the most iterations
throughout the contest.

On the first day, we created a simple if a bit hacky interpreter that passed `language-test`, but failed for more
complex expressions. We also created [encode.py](icfp/encode.py) to encode commands to send over the communication
channel. Most of [encode.py](icfp/encode.py) was created within the first few hours of the contest, and it has undergone
relatively minor changes since then.

On the second day, we rewrote the decoder to resolve variable scope statically at parse time. This solved some problems,
but created others, and we ultimately scrapped most of this code and returned to our initial approach. We finally found
a good solution by using Python's version of currying, `functools.partial` to capture the variables for a lambda when it
is instantiated rather than when it is called. To solve more complex expressions, including `efficiency1`, we added
memoization using Python's inbuild `functools.cache` method. In order to do this, we needed all of the arguments of each
fuction to be hashable, including the variables, which we had stored in a `dict`. `dict`s in Python are not hashable,
so we ended up having to write [frozen_dict](icfp/frozen_dict.py) to store the variable state for each lambda.

On the third day we created basic assemblers and disassemblers to try and make ICFP expressions more human-readable.
[assemble.py](icfp/assemble.py) can take basic decimal expressions like `#I{34}` and convert them to their equivalent
base-94 representation. Similarly, it can take an ASCII string like `#S{hello}` and convert it into its equivalend Bound
Variable encoding. [disassemble.py](icfp/disassemble.py) can reverse this process and convert them back into their more
human-readable forms. It also has functionality to automatically split ICFP expressions into lines and indent them based
on their call stack depth, which was invaluable for debugging. We did similar indentations by hand on days 1 and 2
before automating it on day 3.

There were several more complex expressions, including `lambdaman10`, `lambdaman21`, and
`efficiency2` that were causing recursion depth exceeded errors in Python. Some of these, like `lambdaman6`, we were
able to resolve just by increasing the recursion depth limits, but others I think ultimately were just too much for
Python to handle. Ultimately, Python is not a great choice for functional programming, as it has no tail call
optimization, and its stack frames use up a lot of memory. By the third evening, we decided it was too late to try and
rewrite our decoder in another language, so we just solved as many problems as we could with the decoder we had.

## Lambdaman

For the first 24 hours, I focused on ways to represent the lambdaman text maps as a graph. I tried a variety of methods
to try and combine the fact that it was a covering problem and a path problem. Christofides provided some decent
results, but the loops were causing trouble in finding a Hamiltonian path as one did not always exist.

I also created a few helper methods to output the paths as a string as my edges were not named.

Some of my time was also spent recognizing that the shortest solution may not have the fewest steps, so I looked at
how to write repeating characters efficiently in the custom language.

After this, I shifted to using a bitwise map to note edges after that time and implemented a brute force strategy in 
order to provide solutions for problems not yet solved. I was able to get some slightly more refined solutions after, 
using Christofides again, which is noted in commits.

## Spaceship

@Jazhikho, please add some remarks here.

## 3d

Solutions to 3d were written by hand. I wrote them out on graph paper then carefully typed them in.

## Test

The [test](test/) folder contains unit tests for the encoders and decoders in the [icfp](icfp/) folders. We employed a
semi-test driven approach. Every time we ran into a bug with the encoder or decoder, we tried to produce the shortest
expression we could that would recreate it, and then wrote a unit test with it. We were reasonably sure our decoder was
working properly when it passed all the unit tests, or at least we had fixed all the bugs we had identified so far.

# Acknowledgements

Thank you so much to @deilann, and @Jazhikho for all the incredible work they put in over the last few days.
While we all collaborated and made contributions to one another's work, the bulk of the [icfp](icfp/) module was written
by @TV4Fun, the bulk of the [lambdaman](lambdaman/) code was written by @deilann, and the bulk of the
[spaceship](spaceship/) code was written by @Jazhikho. Solutions for [3d](3d/solutions) were written by @TV4Fun. Every
member of our team was integral to our success, and I am truly gratified at how well we came together to solve these
problems. ---@TV4Fun
