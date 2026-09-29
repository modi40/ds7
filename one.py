import matplotlib.pyplot as plt

courses = ["BCA", "BBA", "B.Com", "B.Sc", "BA"]
students = [60, 45, 75, 50, 35]
colors = ['skyblue', 'salmon', 'lightgreen', 'orange', 'plum']

plt.figure(figsize=(8, 5))
plt.bar(courses, students, color=colors)
plt.title("Student Enrollment in Different Courses")
plt.xlabel("Courses")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()
