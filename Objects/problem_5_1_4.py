

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




