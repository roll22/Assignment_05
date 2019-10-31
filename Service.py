from Domain import Expense, History
import copy


class Service:
    def __init__(self):
        self._history = History()
        self._expenses = self.history_obj.history_list

    @property
    def history_obj(self):
        return self._history

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, last_expenses):
        self._expenses = copy.deepcopy(last_expenses)

    def add_expense(self, day, amount, exp_type):
        new_expense = Expense(day, amount, exp_type)
        self._expenses.append(copy.deepcopy(new_expense))

    def filter(self, amount):
        to_delete = []
        for idx, expense in enumerate(self.expenses):
            if expense.amount < amount:
                to_delete.append(idx)

        for offset, idx in enumerate(to_delete):
            idx -= offset
            del self.expenses[idx]

    def undo(self):
        del self.history_obj.history_list

    @staticmethod
    def max_len(len1, len2):
        if len1 > len2:
            return len1
        elif len1 < len2:
            return len2
        else:
            return False

    def check_changes(self):
        are_same = True
        if Service.max_len(len(self.expenses), len(self.history_obj.history_list)):
            are_same = False
        else:
            for idx in range(Service.max_len(len(self.expenses), len(self.history_obj.history_list))):
                if self.expenses[idx] != self.history_obj.history_list[idx]:
                    are_same = False
        return are_same

