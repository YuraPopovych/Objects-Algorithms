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