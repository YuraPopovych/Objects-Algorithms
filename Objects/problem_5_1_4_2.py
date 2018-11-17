# Previously, you wrote a class called ExerciseSession that
# had three attributes: an exercise name, an intensity, and a
# duration.
#
# Add a new method to that class called calories_burned.
# calories_burned should have no parameters (besides self, as
# every method in a class has). It should return an integer
# representing the number of calories burned according to the
# following formula:
#
# - If the intensity is "Low", 4 calories are burned per
#   minute.
# - If the intensity is "Moderate", 8 calories are burned
#   per minute.
# - If the intensity is "High", 12 calories are burned per
#   minute.
#
# You may copy your class from the previous exercise and just
# add to it.


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

    def calories_burned(self):
        if self.exercise_intensity == "Low":
            return 4 * self.exercise_length
        if self.exercise_intensity == "Moderate":
            return 8 * self.exercise_length
        if self.exercise_intensity == "High":
            return 12 * self.exercise_length


# If your code is implemented correctly, the lines below
# will run error-free. They will result in the following
# output to the console:
# 240
# 360
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())



