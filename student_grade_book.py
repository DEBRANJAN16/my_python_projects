class Assessment:
    
    def __init__(self,name,score,max_score):
        self.name = name 
        self.score = score
        self.max_score = max_score
        
    def get_percentage(self):
        return (self.score/ self.max_score) * 100
    
class Quiz(Assessment):
    
    def __init__(self,name,score,max_score,time_limit):
        super().__init__(name,score,max_score)
        self.time_limit = time_limit   # in minutes
        
    def __strt__(self):
        return f"Quiz: {self.name},Score: {self.score/self.max_score}, Time_limit: {self.time_limit} minutes"
    
class Assignment(Assessment):
    
    def __init__(self, name, score, max_score, due_date):
        super().__init__(name, score, max_score)
        self.due_date = due_date     # due_date in (yyyy-mm-dd) format
        
    def __str__(self):
        return f"Assignment: {self.name}, Score: {self.score/self.max_score}. Due date: {self.due_date}"
    
class Exam(Assessment):
    
    def __init__(self, name, score, max_score,duration, is_final):
        super().__init__(name, score, max_score)
        self.duration = duration
        self.is_final = is_final  # boolean indicating is its a final exam.
        
    def __str__(self):
        exam_type ="Final Exam" if self.is_final else "Exam"
        return f"{exam_type}: {self.name}, Score: {self.score/self.max_score}, Duration: {self.duration} minutes"
    
class Student:
    
    def __init__(self,name):
        self.name = name
        self.assessments = []
        
    def add_assessment(self, assessment):
        self.assessments.append(assessment)
        
    def get_average_grade(self):
        if not self.assessments:
            return 0
        
        total_score = sum(a.score for a in self.assessments)
        total_max_score = sum(a.max_score for a in self.assessments)
        return (total_score / total_max_score) * 100
    
    def __str__(self):
        assessments_str = "\n".join(str(a) for a in self.assessments)
        return f"Student: {self.name}\nAssessments:\n{assessments_str}"
    
class GradeBook:
    
    def __init__(self):
        self.students = {}
        
    def add_student(self,student):
        self.students[student.name] = student
        
    def get_student_average(self,student_name):
        
        Student = self.students.get(student_name)
        
        if Student:
            return Student.get_average_grade()
        return 0.0
    
    def __str__(self):
        
        students_str = "\n\n".join(str(s) for s in self.students.values())
        return f"GradeBook: \n{students_str}"
    
# Example usage
gradebook = GradeBook()

# Now lets Create Students
Deb = Student("Deb")
Annonymous = Student("Annonymous")

# Add Assessments tro the students
Deb.add_assessment(Quiz("Quiz 1", 85, 100, 30))
Deb.add_assessment(Assignment("Assignment 1", 90, 100, "2024-07-03"))
Deb.add_assessment(Exam("Midterm Exam", 80, 100, 120, False))

Annonymous.add_assessment(Quiz("Quiz 1", 75, 100, 30))
Annonymous.add_assessment(Assignment("Assignment 1", 85, 100, "2024-07-03"))
Annonymous.add_assessment(Exam("Midterm Exam", 70, 100, 120, False))

# Add students to gradebook
gradebook.add_student(Deb)
gradebook.add_student(Annonymous)

# Print student average grades
print(f"Deb's Average Grade: {gradebook.get_student_average('Deb'):.2f}%")
print(f"Annonymous's Average Grade: {gradebook.get_student_average('Annonymous'):.2f}%")

# Print the entire gradebook
print(gradebook)
