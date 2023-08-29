class Student:
    def __init__(self, name, cohort):
        self.student_name = name
        self.student_cohort = cohort

    def talk(self):
        return "I can talk!"
    
    def say_favourite_language(self, language):
        return "I love" + " " + language
        # alternative: return f"I love {language}"

