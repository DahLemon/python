This README.md file contains documentation for the 'insertion_sort.py' file in this directory.

What is Sorting in Python Testing?
Sorting in Python involves putting a collection of elements (example: an array of number values), into a particular order,
like arranging number values from smallest to largest or vice versa. This is often done using built-in functions or
algorithms to make data more structured and accessible. 

What is Insertion Sorting?
Insertion Sorting is a simple method of arranging or re-arranging a list of elements such as number values in a specific order,
typically ascending in value. The idea is to iterate through the list and, at each step, insert the current value into its
correct position relative to already sorted values. An easier and more visual example of this would be to have a hand of playing cards.

In one hand, aptly named hand X, you have one card with a certain value. For this example we'll take the value of '6'.
In the other hand, aptly named hand Y, you have all the remaining values (usually in random order). For this example we'll take 
the following values: 2,4,5,3,1. So the full array of values would be: 6,2,4,5,3,1. Value 6 being in hand X and the rest in
hand Y. As the sorting commences, you'll take the next value in hand Y, from left to right, in our example this would be value '2'.
We check if '2' is a higher or lower value than '6' in hand X, '2' is lower than '6' in value so the card will be placed to the left of the '6' card.
We then do the same for the next value in hand Y. If the value we're checking is higher than the most right value in hand X then 
the card will be placed on the right of the value in hand X. Once there's multiple values/cards in hand X, the next card value we check
will have to check if it's value is higher or lower for every card from right to left in hand X. 
Our 'insertion_sort.py' file is an example of this in Python code using unittest.

So what does our code mean to portray our playing cards example from above?
Firstly we define our actual sorting algorithm, which will do the checking and positioning of the values in our array.

In this case we coded the following (our code includes some very simple information, which we've removed here for better clarification): 

    def insertion_sort(A, n):
        for i in range(1, n):
            key = A[i]
            j = i - 1
            while j >= 0 and A[j] > key:
                print('Key:', key, 'Array:', A, 'Pre Pos. checker:', j)
                A[j + 1] = A[j]
                j = j - 1
                print('Pos.Checker:', j, """
                """)
            A[j + 1] = key

'A' stands for our Array of number values, as example in our code lower in the file: A = [6, 5, 2, 1, 3, 4]
'n' is the highest possible value in our array.
'i' stands for the range of values between 1 and 'n'.
'j' is the number we use to check whether the value we're sorting is ready to be positioned relative to the neighbouring values.
We use the 'print' function to print our values, so we can visually see what's happening.
Our created value 'j' is used to loop our positioning algorithm if the value is no in the correct position.

So what does our code actually do?
Our code finds our array, listed below: 

    def test_insertion_sort_basic(self):
        A = [6, 5, 2, 1, 3, 4]
        insertion_sort(A, len(A))
        self.assertEqual(A, [1, 2, 3, 4, 5, 6])

Our Array in this sorting test is 'A= [6, 5, 2, 1, 3, 4]".
It takes the most left value, in this case '6' and uses that as reference to position the next values.
Our code then takes the next number value in the array, being '5' and creates our checking value 'j' from it, so it can
start the loop of checking its value compared to '6'. 
We can see what it does from the print in our log.

    Key: 5 Array: [6, 5, 2, 1, 3, 4] Pre Pos. checker: 0
    Pos.Checker: -1 
            
    Key: 2 Array: [5, 6, 2, 1, 3, 4] Pre Pos. checker: 1

What we see here is it taking '5' as the next key to position and it showing it hasn't moved before we compare the key to '6'.
Hence the 'Pre Pos. checker' being 0, we can then see that after we've compared the value our 'Pos.Checker' is equal to -1,
which means the key has been positioned 1 place to the left from where it originally was.
We can check the Array's new list when it makes '2' the next key to position, as we can see it says 'Array: [5,6,2,1,3,4]'.
If we compare the new sorted Array for 'key = 5' to the original Array, we can see it has sorted '5' correctly into the position
in front of '6'.

    This will happen for each next key, if the key has to move more than on position then the 'Pos.Checker' will change into a value
    of lower or higher than -1, 0 or 1. This is clear when we check the full print in our log for the Sorting Test.
    Key: 5 Array: [6, 5, 2, 1, 3, 4] Pre Pos. checker: 0
    Pos.Checker: -1 
            
    Key: 2 Array: [5, 6, 2, 1, 3, 4] Pre Pos. checker: 1
    Pos.Checker: 0 
            
    Key: 2 Array: [5, 6, 6, 1, 3, 4] Pre Pos. checker: 0
    Pos.Checker: -1 
            
    Key: 1 Array: [2, 5, 6, 1, 3, 4] Pre Pos. checker: 2
    Pos.Checker: 1 
            
    Key: 1 Array: [2, 5, 6, 6, 3, 4] Pre Pos. checker: 1
    Pos.Checker: 0 
            
    Key: 1 Array: [2, 5, 5, 6, 3, 4] Pre Pos. checker: 0
    Pos.Checker: -1 
            
    Key: 3 Array: [1, 2, 5, 6, 3, 4] Pre Pos. checker: 3
    Pos.Checker: 2 
            
    Key: 3 Array: [1, 2, 5, 6, 6, 4] Pre Pos. checker: 2
    Pos.Checker: 1 
            
    Key: 4 Array: [1, 2, 3, 5, 6, 4] Pre Pos. checker: 4
    Pos.Checker: 3 
            
    Key: 4 Array: [1, 2, 3, 5, 6, 6] Pre Pos. checker: 3
    Pos.Checker: 2 
            
    Key: 26 Array: [31, 41, 59, 26, 41, 58] Pre Pos. checker: 2
    Pos.Checker: 1 
            
    Key: 26 Array: [31, 41, 59, 59, 41, 58] Pre Pos. checker: 1
    Pos.Checker: 0 

We hope this lets you understand the basics of Insertion Sorting in Python with the use of unittest.