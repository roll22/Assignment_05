"""
Manage a list of expenses. Each expense has a day (integer between 1 and 30), amount of money (positive
integer) and expense type (string). Provide the user the following features:
1. Add a new expense read to the list. Expense data is read from the console.
2. Show the list of expenses on the console.
3. Filter the list so that it contains only expenses above a certain value that is read from the console.
4. Undo the last operation that modified program data. This step can be repeated.

"""
import copy


class Expense:
    def __init__(self, day, amount, exp_type):
        self.day = day
        self.amount = amount
        self.exp_type = exp_type

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        if type(day) == int:
            if 1 <= day <= 30:
                self._day = day
            else:
                raise ValueError('Day must be in range 1-30')
        elif type(day) == str:
            if day.isdigit():
                day = int(day)
                if 1 <= day <= 30:
                    self._day = day
                else:
                    raise ValueError('Day must be in range 1-30')

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if type(amount) == int:
            if amount > 0:
                self._amount = amount
            else:
                raise ValueError('Amount must be positive')
        elif type(amount) == str:
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    self._amount = amount
                else:
                    raise ValueError('Amount must be positive')
            else:
                raise ValueError('Amount must be a number')
        else:
            raise ValueError('Amount must be a number')

    @property
    def exp_type(self):
        return self._type

    @exp_type.setter
    def exp_type(self, exp_type):
        if type(exp_type) == str:
            if exp_type.isalpha():
                self._type = exp_type
            else:
                raise ValueError('Type must be a word!')
        else:
            raise ValueError('Type must be str!')

    def __str__(self):
        return 'day: ' + str(self.day) + ', amount: ' + str(self.amount) + ', type: ' + self.exp_type

    def __eq__(self, other):
        return self.day == other.day and self.exp_type == other.exp_type and self.amount == other.amount

    def __ne__(self, other):
        return not self.__eq__(other)


class History:
    def __init__(self):
        self._history_list = [[Expense(1, 1, 'food'),
                               Expense(2, 2, 'transport'),
                               Expense(3, 3, 'fun'),
                               Expense(4, 4, 'drinks'),
                               Expense(5, 5, 'clothes'),
                               Expense(6, 6, 'gadgets'),
                               Expense(7, 7, 'cat'),
                               Expense(8, 8, 'car'),
                               Expense(9, 9, 'phone'),
                               Expense(10, 10, 'cables')],
                              ]

    @property
    def history_list(self):
        return copy.deepcopy(self._history_list[-1])

    def history_list_appender(self, expenses):
        self._history_list.append(copy.deepcopy(expenses))

    @history_list.deleter
    def history_list(self):
        if len(self._history_list) == 1:
            raise ValueError("Can't Undo")
        del self._history_list[-1]


def test_expense():
    new_exp = Expense(1, 1, 'food')
    assert new_exp.day == 1
    assert new_exp.amount == 1
    assert new_exp.exp_type == 'food'
