from Domain import test_expense, Expense, History
from Service import Service
import sys


class UI:
    def __init__(self):
        self._service = Service()

    @property
    def service(self):
        return self._service

    @staticmethod
    def print_main_menu():
        print('\n'
              '1.add expense\n'
              '2.show list\n'
              '3.filter list\n'
              '4.undo\n'
              '5.exit\n')

    def display_list(self):
        for expense in self.service.expenses:
            print(expense)

    def read_command(self):
        raw_input = input('>')
        commands = {
            '1': self.service.add_expense,
            '2': self.display_list,
            '3': self.service.filter,
            '4': self.service.undo,
            '5': sys.exit
        }
        return commands[raw_input]

    @staticmethod
    def read_add_params():
        day = input('input day: ')
        amount = input('input amount: ')
        exp_type = input('input type: ')
        return day, amount, exp_type

    @staticmethod
    def read_filter_params():
        value = input('input value: ')
        if not value.isdigit():
            raise ValueError('Value must be of type int!')
        return int(value)

    def function_helper_functions(self, function):
        functions = {
            self.service.add_expense: self.read_add_params,
            self.display_list: None,
            self.service.filter: self.read_filter_params,
            self.service.undo: None,
            sys.exit: None,
        }
        if functions[function] is not None:
            return functions[function]()
        else:
            return None

    def start(self):
        while True:
            # we initialize the expense list with the last version of it's
            # self from history
            self.service.expenses = self.service.history_obj.history_list
            try:
                self.print_main_menu()
                function = self.read_command()
                params = self.function_helper_functions(function)
                if params is None:
                    function()
                elif type(params) == int:
                    function(params)
                    # add to expenses to history
                elif type(params) == tuple:
                    function(*params)
                    # add to expenses to history
                else:
                    raise ValueError('Not ok')
                if function != self.service.undo and not self.service.check_changes():
                    self.service.history_obj.history_list_appender(self.service.expenses)

            except ValueError as val_err:
                print(val_err.args[0])
            except KeyError:
                print('wrong choice!')

ui = UI()
ui.start()
