from application.db import people
from application import salary
import datetime
from prettytable import PrettyTable


if __name__ == "__main__":
    print(people.get_employees())
    print(salary.calculate_payroll())
    print(datetime.datetime.now())
    x = PrettyTable()
    x.field_names = ["Country", "Capital", "is_russia"]
    x.add_row(["Russia", "Moscow", True])
    x.add_rows([["Argentina", "Buenos Aires", False], ["Jamaica", "Kingston", False]])
    x.add_column("Starts with A", [False, True, False])

    print(x)
