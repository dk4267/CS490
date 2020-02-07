class Employee:
    numEmployees = 0
    totalSalary = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        self.__class__.numEmployees += 1
        self.__class__.totalSalary += salary

    def avg_salary(self):
        return self.__class__.totalSalary / self.__class__.numEmployees


class FulltimeEmployee(Employee):

    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)


emp1 = Employee("Fred", "Smith", 40000, "Accounting")
emp2 = FulltimeEmployee("Bob", "Jones", 50000, "IT")
emp3 = Employee("George", "Harrison", 60000, "Idunno")
print(emp3.avg_salary())

emp4 = FulltimeEmployee("GenericName", "LastName", 70000, "someSortOfMiddleManager")
print(emp4.avg_salary())

