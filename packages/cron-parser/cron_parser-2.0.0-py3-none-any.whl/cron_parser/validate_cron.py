from croniter import croniter

class ValidateCron:
    def __init__(self, expression):
        print(expression)
        self.expression = expression

    def validate(self):
        print(self.expression)
        print(croniter.is_valid(self.expression))
        return croniter.is_valid(self.expression)

            
