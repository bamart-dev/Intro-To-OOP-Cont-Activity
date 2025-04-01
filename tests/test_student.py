from school_schedule.student import Student

# Write your tests here!

def test_student_class_instantiation():
    name = 'David'
    grade = "Junior"
    classes = ['Math', 'Music']

    student = Student(name, grade, classes)

    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes


def test_add_class():
    name = 'David'
    grade = "Junior"
    classes = ['Math', 'Music']
    class_to_add = 'Science'
    student = Student(name, grade, classes)

    result = student.add_class(class_to_add)

    assert result == ['Math', 'Music', 'Science']

def test_get_num_classes():
    name = 'David'
    grade = "Junior"
    classes = ['Math', 'Music', 'Science']
    student = Student(name, grade, classes)

    result = student.get_num_classes()

    assert result == 3

def test_display_classes():
    name = 'David'
    grade = "Junior"
    classes = ['Math', 'Music', 'Science']
    student = Student(name, grade, classes)

    result = student.display_classes()

    assert result == "Math, Music, Science"

def test_summary():
    name = 'David'
    grade = "Junior"
    classes = ['Math', 'Music', 'Science']
    student = Student(name, grade, classes)

    result = student.summary()

    assert result == 'David is a Junior enrolled in 3 classes: Math, Music, Science'
