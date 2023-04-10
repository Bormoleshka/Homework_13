class StudentException(Exception):
    pass


class StudentTypeStrError(StudentException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Значение {self.value} должно быть текстом'


class StudentTypeTextError(StudentException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if not self.value.isalpha():
            return f'Значение {self.value} должно содержать только буквы'
        elif not self.value.istitle():
            return f'Значение {self.value} должно начинаться с заглавной буквы'


class StudentLessonsError(StudentException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'"Предмет {self.value} не изучается данным студентом"'
