# Safe Combinations

This project computes all possible safe combinations and corresponding pegs locations for this toy: https://ugearsmodels.com/safe.html

This project is written in Python programming language and requires a working python 2.7 installation to run.

It produces the output in 2 forms: standard console output and ".txt" file

The generated list of combinations is in the "_combinations_list.txt_" file and it has a following format:
* 1st Column: Safe locking combination
* 2nd Column: Washer Peg combination _first number corresponds to cog I, second to II, third to III_
* 3rd Column: Lock knob position

UPDATE:
The file "_unique_combinations_list.txt_" new contains the safe code combinations that are defined by one and only one Cog Wheel peg combination, thus these 34 combinations should be the most failure-proof combinations to use while building your safe.
The same formatting scheme applies to this file as described above.