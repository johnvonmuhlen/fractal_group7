import unittest

class Person:
    def __init__(self, first_name, middle_name, last_name, age):
        self.name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age
    
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
            
    def __repr__(self):
        return f'<Person first_name="{self.name}" middle_name="{self.middle_name}" last_name="{self.last_name}">"'
    
class Student:
    def __init__(self, first_name, middle_name, last_name, age, hours_slept, student_id):
        super().__init__(first_name, middle_name, last_name, age, hours_slept, student_id)
        self.student_id = student_id
        
    def is_enrolled():
        return True
    
    def sleep(self):
        if isinstance(self.hours_slept, int):
            if self.hours < 8:
                return f'{self.first_name} is gonna be tired'
            else:
                return f'{self.first_name} is not gonna be tired'
            
                
john = Student('John', 'von', "Muhlen", 19, 9)
print(john.sleep())
        
        
