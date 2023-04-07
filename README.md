
# Markov Algorithm

Using a list of rules
Turn an input string
Into a result string
With a list of rules used

This algorithm should be *deterministic*

Hash the 
- result.json
- rules.json
- steps.json

Why? Proof of work.


## TODO

allow to wrap tokens in a class
like a regex
:number ::= [123456789][1234567890]*

that way we can do something like
:numer:1 + :number:2 -> add(:number:1, :number:2)

using something like backus naur form
https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form

Make an interactive debugger?
Just step through the steps.

### MAYBE DO

This should be parallelizable.
Try all the rules in parallel
Only keep the first one


### DONT DO THIS

use regex instead
there should be a way to optimize this
so that we only try rules that are applicable
