# Imagine you're writing an exercise-tracking app like Fitbit
# or MyFitnessPal. Part of your app is that a user can log an
# exercise session by naming the exercise, the intensity, and
# the duration.
#
# Write a class called ExerciseSession. ExerciseSession
# should have a constructor that requires two strings and an
# integer: the strings represent the exercise name and the
# exercise intensity, which will be "Low", "Moderate", or
# "High". The integer will represent the length of the
# exercise session in minutes. These should be saved in the
# instance of the class.
#
# Then, add three getters to the class. The getters should
# be named get_exercise, get_intensity, and get_duration,
# and should return the exercise string, the exercise
# intensity, and the duration, respectively.
#
# The setters should be named set_exercise, set_intensity,
# and set_duration. Each should have one parameter (besides
# self), which should be stored as the new value of
# exercise, intensity, or duration. You may assume only
# valid values will be passed in.
#
# HINT: You don't have to do any logging like you saw in
# the video! That was just an example of one benefit of
# using getters and setters, but this problem does not ask
# you to do that.


# Add your code here!
class ExerciseSession:
    def __init__(self, exercise_name, exercise_intensity, exercise_length):
        self.exercise_name = exercise_name
        self.exercise_intensity = exercise_intensity
        self.exercise_length = exercise_length

    def get_exercise(self):
        return self.exercise_name

    def get_intensity(self):
        return self.exercise_intensity

    def get_duration(self):
        return self.exercise_length

    def set_exercise(self, exercise_name):
        self.exercise_name = exercise_name

    def set_intensity(self, exercise_intensity):
        self.exercise_intensity = exercise_intensity

    def set_duration(self, exercise_length):
        self.exercise_length = exercise_length


# If your code is implemented correctly, the lines below
# will run error-free. They will result in the following
# output to the console:
# Running
# Low
# 60
# Swimming
# High
# 30
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())




