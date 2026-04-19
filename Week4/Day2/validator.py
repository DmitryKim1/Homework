class Validator:
    @staticmethod
    def is_positive(x):
        return x > 0
    
    @staticmethod
    def is_email(text):
        return "@" in text
    
print(Validator.is_positive(10))

print(Validator.is_email("hello"))