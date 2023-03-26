# Create your classes here
class Student:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __repr__(self):
        return f'<first_name={self.first_name} last_name={self.last_name} address={self.address}>'


class Question:
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def __repr__(self):
        return f'<question={self.question} correct_answer={self.correct_answer}>'

    def ask_and_evaluate(self):
        print(self.question)
        user_answer = input('> ').lower()
        return user_answer == self.correct_answer.lower()


class Exam:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def __repr__(self):
        return f'<name={self.name} questions={self.questions}>'

    def add_question(self, Question):
        self.questions.append(Question)

    def administer(self):
        num_correct = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                num_correct += 1

        return num_correct / len(self.questions) * 100


class StudentExam():
    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None

    def __repr__(self):
        return f'<student={self.student} exam={self.exam} score={self.score}>'

    def take_test(self):
        self.score = self.exam.administer()

        print(self.score)


class Quiz(Exam):
    def administer(self):
        num_correct = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                num_correct += 1

        score = num_correct / len(self.questions) * 100

        if score >= 50:
            return 1
        else:
            return 0


def example_exam():
    ex_exam = Exam('example_exam')
    q1 = Question('What is 1 + 1?', '2')
    q2 = Question('What letter is after a?', 'b')
    q3 = Question('What is the opposite of up?', 'down')

    ex_questions = [q1, q2, q3]

    for question in ex_questions:
        ex_exam.add_question(question)

    ex_student = Student('example', 'student', '123 Real St.')

    ex_student_exam = StudentExam(ex_student, ex_exam)

    ex_student_exam.take_test()

    print(f'ex_student_exam is: {ex_student_exam}')


def example_quiz():
    ex_exam = Exam('example_exam')
    q1 = Question('What is 1 + 1?', '2')
    q2 = Question('What letter is after a?', 'b')
    q3 = Question('What is the opposite of up?', 'down')

    ex_questions = [q1, q2, q3]

    for question in ex_questions:
        ex_exam.add_question(question)

    ex_student = Student('example', 'student', '123 Real St.')

    ex_student_exam = StudentExam(ex_student, ex_exam)

    ex_student_exam.take_test()

    print(f'ex_student_exam is: {ex_student_exam}')
