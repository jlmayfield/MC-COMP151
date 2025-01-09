#  Iteration & Accumulation Practice Problems/Study Guide

1.  *Basic Problems*  Sequences to Non-Sequence Types
    * *Classic Patterns*  Sum,Count,Search,Min/Max,Average
    * *Examples*
        * Count vowels/consonants/specific-letters in a string 
        * Total length of list of strings 
        * Number of strings of a given length or in a length range
        * Shortest/Longest string in a list of strings
        * Location of shortest/longest string in a list 
        * Is there a rect of a given area? 
        * Is there a rect within a given region? 
        * First Rect (Rect or Location of Rect) in a list of Rects with area within a given range
        * Last Rect (Rect or Location of Rect) in a list of Rects with area within a given range
2. *Map-Style Problems*  Sequences to Sequences. 1-to-1 Transformation.
    * *In-Place* Replace list contents with new, transformed values
    * *Functional* Return the transformed list. Do not modify the list argument. 
    * *Examples*
        * List of strings to list of lengths of the strings
        * Double/triple/raise to a power all the numbers in a list
        * Grow or shrink Rect length/width/both by a factor (double, triple, 1.5, etc.) 
        * Fizzbuzz style problems: multi-conditional transformation. 
            * Multiples of 3 -> Fizz, Multiples of 5 -> Buzz, Multiples of 3 and 5 -> Fizzbuzz, otherwise do nothing. 
            * Double integers between 1 and 10, Divide by 2 integers between 10 and 20, Triple integers between 30 and 40, etc. 
            * Strings length less than 3 to "short", between 3 and 6 "average", more than 6 "long".         
3. *Filter-Style Problems* Sequence to Sequence. Keep/Remove based on a condition. 
    * *Note* Basic search and problems have natural filter counterparts (collect the stuff rather than find/count). 
    * *Note* Filters can either collect values or they can collect locations of values. Be ready for both!
    * *Examples*
        * Remove/keep all numbers within/outside a range 
        * Remove/keep odd integers
        * Remove strings based on length 
        * Remove strings that start/end with a given letter 
        * Starting with a string, get a list of all the vowels/consonants. 
        * Remove rectangles based on area (too small, too big)
        * Remove rectangles based on location (inside or outside a region) 
        * Remove rectangles that are colliding with a specific rectangle 
4. *Parallel Traversals*  Working two sequences in parallel
    * *Examples*
        * Given list of Rects (locations) and list of Vectors (velocity), move all the rectangles according to the velocity. 
        * Weighted Average: Given list of numbers and list of weights (floats between 0 and 1 that add to 1), multiple values with associated weights and compute the sum.  
5. *Challenge Problems*
    * Filter+Map Combos (Remove some, transform the rest)
    * Determine if any two rectangles in a list are colliding 
    * Determine if a string/number in a list is repeated 
    * Prefix sum: Make location i be the sum of all the values preceding it. 
    * Palindrome Detection: Does the sequence read the same both forwards and backwards. 