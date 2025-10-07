import csv

class Student:
    def __init__(self, name, major, gpa):
        self.name, self.major, self.gpa = name, major, float(gpa)
    def __str__(self): return f"{self.name} | {self.major} | GPA: {self.gpa:.2f}"

class StudentManager:
    def __init__(self, file): self.file, self.students = file, []
    def load(self):
        try:
            with open(self.file) as f:
                self.students = [Student(*r) for r in csv.reader(f) if len(r)==3]
            print(f"Loaded {len(self.students)} students.")
        except FileNotFoundError:
            print(f"File '{self.file}' not found.")
    def show(self): [print(s) for s in self.students]
    def filter_gpa(self, min_gpa): return [s for s in self.students if s.gpa >= min_gpa]
    def export(self, out, data):
        with open(out, 'w', newline='') as f:
            csv.writer(f).writerows([[s.name, s.major, s.gpa] for s in data])
        print(f"Saved filtered students to '{out}'.")