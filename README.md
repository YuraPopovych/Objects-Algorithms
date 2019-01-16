# **Computing in Python IV: Objects & Algorithms**
## Georgia Tech University MOOC 

*https://courses.edx.org/courses/course-v1:GTx+CS1301xIV+1T2018/course/*

### **Objects** 
* 5.1.1. Below is a class representing a person. You'll see the
Person class has three instance variables: name, age,
and GTID. The constructor currently sets these values
via a calls to the setters.
Create a new function called same_person. same_person
should take two instances of Person as arguments, and
returns True if they are the same Person, False otherwise.
Two instances of Person are considered to be the same if
and only if they have the same GTID. It does not matter
if their names or ages differ as long as they have the
same GTID. You should not need to modify the Person class.
* 5.1.2. Write a class named "Phone". The Phone class should
have an attribute called "storage" which defaults to
128, and an attribute called "color" which defaults
to "red".
If your function works correctly, this will originally print:
    ```
    128 
    red 
    ```
* 5.1.2.2. Write a class named "number" with one attribute called
"value" which defaults to 0 and another attribute called
"even" which defaults to True. Next, create an instance of this class and assign it to
a variable called "number_instance". Then, set the value attribute to 101 and the even
attribute to False.
* 5.1.4. Imagine you're writing an exercise-tracking app like Fitbit
or MyFitnessPal. Part of your app is that a user can log an
exercise session by naming the exercise, the intensity, and
the duration. Write a class called ExerciseSession. ExerciseSession
should have a constructor that requires two strings and an
integer: the strings represent the exercise name and the
exercise intensity, which will be "Low", "Moderate", or
"High". The integer will represent the length of the
exercise session in minutes. These should be saved in the
instance of the class.Then, add three getters to the class. The getters should
be named get_exercise, get_intensity, and get_duration,
and should return the exercise string, the exercise
intensity, and the duration, respectively.The setters should be named set_exercise, set_intensity,
and set_duration. Each should have one parameter (besides
self), which should be stored as the new value of
exercise, intensity, or duration. You may assume only
valid values will be passed in.
If your code is implemented correctly, the lines below
will run error-free. They will result in the following: 
output to the console:
    ```
    Running
    Low
    60
    Swimming
    High
    30
    ```
* 5.1.4.2. Previously, you wrote a class called ExerciseSession that
had three attributes: an exercise name, an intensity, and a
duration. Add a new method to that class called calories_burned.
calories_burned should have no parameters (besides self, as
every method in a class has). It should return an integer
representing the number of calories burned according to the
following formula: If the intensity is "Low", 4 calories are burned per
minute. If the intensity is "Moderate", 8 calories are burned per minute.If the intensity is "High", 12 calories are burned per minute.If your code is implemented correctly, the lines below will run error-free. They will result in the following output to the console:
    ```
    240
    360
    ```
* 5.1.5. Classes can also have references to other instances of
themselves. Consider this Person class, for example,
that allows for an instance of a father and mother
to be given in the constructor. Create 3 instances of this class. The first should have
the name "Mr. Burdell" with an age of 53. The second
instance should have a name of "Mrs. Burdell" with an age
of 53 as well. Finally, make an instance with the name of
"George P. Burdell" with an age of 25. This final instance
should also have the father attribute set to the instance
of Mr. Burdell, and the mother attribute set to the
instance of Mrs. Burdell. Finally, store the instance of
George P. Burdell in a variable called george_p. (It does
not matter what variable names you use for Mr. and Mrs.
Burdell.)
The code below will let you test your code. It isn't used
for grading, so feel free to modify it. As written, it
should print:
    ```
    George P. Burdell
    Mrs. Burdell
    Mr.Burdell
    ```
* 5.1.5.2. We've given you a class called "Song" that represents
some basic information about a song. We also wrote a
class called "Artist" which contains some basic
information about an artist. Your job is to create three instances of the song class,
called song_1, song_2, and song_3. song_1 should have the following attributes:
    ```
    name = "You Belong With Me"
    album = "Fearless"
    year = 2008
    artist.name = "Taylor Swift"
    artist.label = "Big Machine Records, LLC"

    song_2 should have the following attributes:
    name = "All Too Well"
    album = "Red"
    year = 2012
    artist.name = "Taylor Swift"
    artist.label = "Big Machine Records, LLC"

    song_3 should have the following attributes:
    name = "Up We Go"
    album = "Midnight Machines"
    year = 2016
    artist.name = "LIGHTS"
    artist.label = "Warner Bros. Records Inc."
    ```
    Notice, though, that song_1 and song_2 have the same
    artist and label. That means they should each have the
    SAME instance of artist: do not create separate instances
    of artist for each song. When your code is done running, there should exist three
    variables: song_1, song_2, and song_3, according to the requirements above.
    Below are the two class definitions we supplied previously:
Artist and Song.

* 5.1.5.3 Write a function called "get_song_string". It should accept
one argument which will be a Song object. It should return a string in the following format:
    ```
    "<song name>" - <artist name> (<song year>)
    e.g:
    "You Belong With Me" - Taylor Swift (2008)
    ```
    The quotation marks around the song title should be *part*
    of the string.
    Hint: You're writing a function, not a method.
* 5.1.5.4. In this problem, you're going to use that class to calculate
the net force from a list of forces.Write a function called find_net_force. find_net_force should
have one parameter: a list of instances of Force. The function should return new instance of Force with the total
net magnitude and net angle as the values for its magnitude and angle attributes.
As a reminder:
To find the magnitude of the net force, sum all the horizontal components and sum all the verticalcomponents.
The net force is the square root of the sum ofthe squares
of the horizontal forces and the vertical foces (i.e.
(total_horizontal ** 2 + total_vertical ** 2) ** 0.5)
To find the angle of the net force, call atan2 with two
arguments: the total vertical and total horizontal
forces (in that order).
Remember to round both the magnitude and direction to one
decimal place. This can be done using round(magnitude, 1)
and round(angle, 1).
The Force class has three methods: get_horizontal returns
a single force's horizontal component. get_vertical
returns a single force's vertical component. get_angle
returns a single force's angle in degrees (or in radiansif you call get_angle(use_degrees = False.

* 5.1.6. Here's a long one -- you can do it! Rewrite the following class so that it uses getters and setters for all three variables (title, description, completed). The getters should be called: getTitle, getDescription,  getCompleted. The setters should be
called: setTitle, setDescription, setCompleted.
In addition, the setter should check to make sure that
the new value is the correct type: title and description
should always be of type str, and completed should always
be of type bool. If the value is not the right type, set
the value of the corresponding attribute to None (the
keyword, not the string "None"). 

    To summarize (and give a to-do list):
  - Create getters and setters for each variable.
  - Check the type of the new value inside the setters,
  and print an error if it's the wrong type.

    If your class works correctly, this will originally print:

    ```
    Mow
    Mow the lawn
    False
    True
    None
    ```
* 5.1.7. 
Below we've started a class called FibSeq. At any time,
FibSeq holds two values from the Fibonacci sequence:
back1 and back2. Create a new method inside FibSeq called next_number. The next_number method should: 
   - Calculate and return the next number in the sequence,
  based on the previous 2.
  - Update back2 with the former value of back1, and update
  back1 with the new next item in the sequence.
    

    The code below will test your method. As written, it should print:
    ```
    1, 2, 3, 5, and 8.
    ```

* 5.1.8. Write a class called "Burrito". A Burrito should have the 
following attributes (instance variables):
    - meat
    - to_go
    - rice 
    - beans 
    - extra_meat (default: False)
    - guacamole (default: False)
    - cheese (default: False)
    - pico (default: False)
    - corn (default: False)
    ```
    The code below will test your class. If it is written
    correctly, this will print True, then False. Note,
    though, that we'll test your code against more complex
    test cases when you submit.
    ```
* 5.1.9. Copy your Burrito class from the last exercise. Now,
write a getter and a setter method for each attribute. 
Each setter should accept a value as an argument. If the 
value is a valid value, it should set the corresponding 
attribute to the given value. Otherwise, it should set the 
attribute to False.

    Edit the constructor to use these new setters and getters.
    In other words, if we were to call:

    new_burrito = Burrito("spaghetti", True, True, False)

    new_burrito.meat would be False because "spaghetti" is not
    one of the valid options. Note that you should NOT try to
    check if the new value is valid in both the constructor and
    the setter: instead, just call the setter from the
    constructor using something like self.set_meat(meat).

    Valid values for each setter are as follows:

    - set_meat: "chicken", "pork", "steak", "tofu", False
    - set_to_go: True, False
    - set_rice: "brown", "white", False
    - set_beans: "black", "pinto", False
    - set_extra_meat: True, False
    - set_guacamole: True, False
    - set_cheese: True, False
    - set_pico: True, False
    - set_corn: True, False

* 5.10. Now, add
a method called "get_cost" to the Burrito class. It should
accept zero arguments (except for "self", of course) and
it will return a float. Here's how the cost should be
computed:

    - The base cost of a burrito is $5.00
    - If the burrito's meat is "chicken", "pork" or "tofu", 
    add $1.00 to the cost
    - If the burrito's meat is "steak", add $1.50 to the cost
    - If extra_meat is True and meat is not set to False, add
    $1.00 to the cost
    - If guacamole is True, add $0.75 to the cost

If your function works correctly, this will originally
```
print: 7.75
```

* 5.1.11. Copy your Burrito class from the last exercise. Below,
We've given you three additional classes named "Meat",  
"Rice" and "Beans." We've gone ahead and built getters
and setters in these classes to check if the incoming
values are valid, so you'll be able to remove those
from your original code. First, edit the constructor of your Burrito class.
Instead of calling setters to set the values of the
attributes self.meat, self.rice, and self.beans, it
should instead create new instances of Meat, Rice, and
Beans. The arguments to these new instances should be
the same as the arguments you were sending to the
setters previously (e.g. self.rice = Rice("brown")
instead of set_rice("brown")).
If your function works correctly, this will originally
    ```
    print: 7.75
    ```
* 5.1.12. Write function get_total which will calculate total cost of burritos.

### **Algorithms**

* Insert sort
* Linear search
* Recursive binary search 
 Example, imagine if listOfdays had three instances of date: one for January 1st 2016, one for January 1st 2017,
 and one for January 1st 2018.Then:
  ```
   binary_search_year(listOfdays, 2016) -> True
   binary_search_year(listOfdays, 2015) -> False
  ```
* Recursive Fibonacci
* Reverse merge sort. Example 1, we gave you the code for
merge_sort. You may copy that code into this problem and modify it. Change it such that instead of sorting from lowest to highest, it sorts from highest to lowest.
Name your function sort_with_merge(). For example:
    ```
    if you call merge_sort([5, 3, 1, 2, 4]),
    you would get [5, 4, 3, 2, 1].
    ```
    Do not use Python's sort or reverse methods to complete this.
* Search for string. Write a function called search_for_string() that takes two
parameters, a list of strings, and a string. This function
should return a list of all the indices at which the
string is found within the list.You may assume that you do not need to search inside the
items in the list; for examples:
    ```
    search_for_string(["bob", "burgers", "tina", "bob"], "bob")
        -> [0,3]
    search_for_string(["bob", "burgers", "tina", "bob"], "bae")
        -> []
    search_for_string(["bob", "bobby", "bob"])
        -> [0, 2]
    ```     
    If  function works correctly, this will originally
    print:

    ```
    [1, 4, 5]
    ```

* String search. Find len of string without len function and with recursion.
* Twist recursion. For this problem, implement Fibonacci recursively, with a twist! Imagine that we want to create a new number sequence called Fibonacci-3. In Fibonacci-3, each number in the sequence is the sum of the previous three numbers. The sequence will start with three 1s, so the fourth Fibonacci-3 number would be 3 (1+1+1), the fifth would be 5 (1+1+3),the sixth would be 9 (1+3+5), the seventh would be 17
(3+5+9), etc.

### **Final problem set**

* nation. Write a function called to_dictionaries that will take as
input a list of instances of this class. It should return a
dictionary of dictionaries. The keys for the dictionaries
should be the short names of the nations. The values should
be additional dictionaries, each with five keys: long_name,
iso_code, iso_short, iso_long, and capital. 
For example, if we created two instances of Nation like this:

    new_nation_1 = Nation("Albania", "Republic of Albania", 8, "AL", "ALB", "Tirana")
    new_nation_2 = Nation("Angola", "Republic of Angola", 24, "AO", "AGO", "Luanda")

    ...then made them into a list like this:
n   ation_list = [new_nation_1, new_nation_2]

    ...then called the function:
new_dict = to_dictionaries(nation_list)
    ```
    {"Albania": {"long_name": "Republic of Albania", "iso_code": 8, "iso_short": "AL", "iso_long": "ALB", "capital": "Tirana"},
    "Angola": {"long_name": "Republic of Angola", "iso_code": 24, "iso_short": "AO", "iso_long": "AGO", "capital": "Luanda"}}
    ```
* nameGenerator. A common meme on social media is the name generator. These
are usually images where they map letters, months, days,
etc. to parts of fictional names, and then based on your
own name, birthday, etc., you determine your own.
For example, here's one such image for "What's your
superhero name?": https://i.imgur.com/TogK8id.png
Write a function called generate_name. generate_name should
have two parameters, both strings. The first string will
represent a filename from which to read name parts. The
second string will represent an individual person's name,
which will always be a first and last name separate by a space.If your function works correctly, this will originally
print: Captain Hawk, Doctor Yellow Jacket, and Moon Moon,
each on their own line.
    ```
    print(generate_name("heronames.txt", "Addison Zook"))
    print(generate_name("heronames.txt", "Uma Irwin"))
    print(generate_name("heronames.txt", "David Joyner"))
    ```
* blackJack. In this problem, we're going to explore a little of how
game AI works. We'll do this with a simple problem: building
an agent to play the popular card game Blackjack.
Blackjack is a card game played with a standard 52-card
deck. Suits do not matter in Blackjack, and so we'll just
use letters to indicate the different cards: A, 2, 3, 4, 5,
6, 7, 8, 9, 10, J, Q, K.
The goal of Blackjack is to get as close to 21 points as
possible without going higher. Each of the thirteen cards
above has a point total attached: the numerals are worth
their given value (2 points for 2, 7 points for 7, etc.).
J, Q, and K are worth 10 points. A is worth either 1 or 11
points, whichever is better for the player.
At any time, the player has some number of cards in their
hand. They must then make a decision of whether to Hit or
Stay. Hit means they request an additional card, Stay means
they stop with their current total. Players generally try
to Hit until it is likely that another card will push them
over 21. For example, if a player has a 5 and a 7, there is
a relatively low chance that another card would push them
over 21 (only J, Q, and K would do so, since 12 + 10 = 22).
On the other hand, if they have a 5, a 6, and a 7, they will
likely stay because any card above 3 will push them over 21
points.
The specific goal in Blackjack is to get closer to 21 than
the dealer. Dealers must follow a set of prescribed rules
for when to Hit and Stay. These are the rules we'll use for
our Blackjack-playing AI.

    The rules are:

  - The dealer must Hit if their total is below 17.
  - The dealer must Stay as soon as their total is 17 or
    higher.
  - An Ace (A) should be counted as 11 if it puts the
  dealer between 17 and 21 points. If it puts them over
  21, though, it should be counted as 1.
    
  Write a function called next_move. next_move should have
one parameter, a string. Each character of the string will
be a card in the dealer's current hand, such as "AK" or
"175". The function should return one of three strings:

  - "Hit" if the dealer should take another card.
  - "Stay" if the dealer should not take another card.
  - "Bust" if the sum is already over 21.



### **Exam**
* name. Create a class called Name. Name should have two attributes
(instance variables): first_name and last_name. Make sure
the variable names match those words. Both will be strings.
    Name should have a constructor with two required parameters,
    one for each of those attributes (first_name and last_name,
    in that order).
    Name should also have two methods. The first should be
    called find_printed_name, and should return the first and
    last name with a space in between, e.g. "David Joyner". The
    second method should be called find_sortable_name, and
    should return the last name, then a comma and space, and
    then only the first initial, e.g. "Joyner, D".
    Neither sortable_name nor printed_name should be attributes:
    both should be created and returned when those methods are
    called. Neither method will have any parameters besides self. If it's written correctly, It's print:
    
    ```
    David
    Joyner
    David Joyner
    Joyner, D
    ```

* joynernacci. where every number is the sum of the previous two numbers.Joynernacci numbers are similar to Fibonacci numbers, but
with two differences:
  - Fibonacci numbers are famous, Joynernacci numbers are
  not (yet).
  - In Joynernacci numbers, even-indexed numbers are the
  sum of the previous two numbers, while odd-indexed
  numbers are the absolute value of the difference
  between the previous two numbers.
For example: the Joynernacci sequence starts with 1 and 1
as the numbers at index 1 and 2. 3 is an odd index, so
the third number would be 0 (1 - 1 = 0). 4 is an even
index, so the fourth number would be 1 (0 + 1). 5 is an
odd index, so the fifth number would be 1 (1 - 0). And
so on.
The first several Joynernacci numbers (and their indices)
are thus:

    ```
        1  1  0  1  1  2  1  3  2   5   3  8  5  13  8  21 13 34 21

        1  2  3  4  5  6  7  8  9   10  11 12 13 14  15 16 17 18 19
    ```
    Below are some lines of code that will test your function.
    You can change the value of the variable(s) to test your
    function with different inputs. If your function works correctly, this will originally
    print:
    ```
    1
    8
    ```

* checkAvailability. Imagine you're writing a program to check if a person is
available at a certain time. To do this, you want to write a function called check_availability. check_availability will have two parameters: a list of instances of the Meeting class, and proposed_time, a particular date and time. check_availability should return True (meaning the person
is available) if there are no instances of Meeting that
conflict with the proposed_time. In other words, it should
return False if proposed_time is between the start_time and
end_time for any meeting in the list of meetings. The Meeting class is defined below. It has two attributes:
start_time and end_time. start_time is an instance of the
datetime class showing when the meeting starts, and
end_time is an instance of the datetime class indicating
when the meeting ends.
If your function works correctly, this will originally
print: 
    ```
    True
    False
    ```

    horse. The game HORSE is a popular basketball shooting game.
    It can be played with any number of players. One-by-one,
    each player takes a shot from anywhere they want. If they
    make the shot, the next person must make the same shot.
    If they do not, they receive a letter: H, then O, then R,
    then S, then E. Once a player receives all 5 letters, they
    are out of the game. The game continues until all but one player has all five
    letters. Write a function called check_horse_winner. This function
    will take as input a tuple of at least two, but potentially
    more, strings. check_horse_winner should return the following:
    - If only one player is left with fewer than 5 letters,
    return "Player X wins!", where X is the index of the
    player in the list (which could be 0).
    - If more than one player has fewer than 5 letters,
    return "Players X, Y: keep playing!", where X, Y, and
    potentially more numbers are the indices of all players
    who have not yet been eliminated.
    - If no player has 5 letters, return "Everyone: keep
    playing!"

    If your function works correctly, this will originally
    print:
    ```
    Everyone: keep playing!
    Players 1, 2: keep playing!
    Player 2 wins!
    ```
        
