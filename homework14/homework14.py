import unittest


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # def salary(self):
    #     pass

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


class TestAtribute(unittest.TestCase):
    def test_attribute_name(self):
        lead = TeamLead("fjghh", "123", "123", "123", "Python")
        assert hasattr(lead, "name") is True, "no element name"

    def test_attribute(self):
        lead = TeamLead("fjghh", "123", "123", "123", "Python")
        assert hasattr(lead, "salary") is True, "no element salary"

    def test_attribute_department(self):
        lead = TeamLead("fjghh", "123", "123", "123", "Python")
        assert hasattr(lead, "department") is True, "no element department"

    def test_attribute_programming_language(self):
        lead = TeamLead("fjghh", "123", "123", "123", "Python")
        assert hasattr(lead, "programming_language") is True, "no element programming_language"

