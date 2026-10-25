
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum = sum + val

        print("hi", self.name, "your avg score is:", sum / 3)


s1 = student("Jhon Doe", [98, 78, 89])

s1.get_avg()
