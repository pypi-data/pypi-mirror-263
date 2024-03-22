from cron_parser.constants import EXPRESSION_FIELD_NAMES
from cron_parser.process_cron import ProcessCron
from cron_parser.validate_cron import ValidateCron
from cron_parser.utils.cron_helper import return_output_as_table


class ParseCronExpression:
    def __init__(self, expression: str):
        self.expression = expression
        self.fields = []
        self.command = None

    def evaluate(self):
        string_expression = self.expression.split(' ', 5)

        self.command = string_expression[-1]
        print(self.command)
        if not ValidateCron(self.expression.rsplit(' ', 1)[0]).validate():
            raise Exception(f"Invalid cron expression.")
            
        for i, str_value in enumerate(string_expression[:-1]):
            cron_field_name = EXPRESSION_FIELD_NAMES[i]
            cron_field_value = ProcessCron(str_value, cron_field_name)
            cron_field_value.process()
            self.fields.append(cron_field_value)
        return return_output_as_table(self.fields, self.command)

