class Employee:
    def _init_(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def _init_(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search(self, key, value, operator):
        results = []
        for employee in self.employees:
            if operator == '<' and getattr(employee, key) < value:
                results.append(employee)
            elif operator == '>' and getattr(employee, key) > value:
                results.append(employee)
            elif operator == '<=' and getattr(employee, key) <= value:
                results.append(employee)
            elif operator == '>=' and getattr(employee, key) >= value:
                results.append(employee)
        return results

    def display_employees(self, employees):
        if not employees:
            print("No matching records found.")
        else:
            print("Employee ID\tName\tAge\tSalary")
            for employee in employees:
                print(f"{employee.employee_id}\t{employee.name}\t{employee.age}\t{employee.salary}")

def main():
    db = EmployeeDatabase()

    db.add_employee(Employee("161E90", "Raman", 41, 56000))
    db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    while True:
        print("\nMenu:")
        print("1. Search by Age")
        print("2. Search by Salary")
        print("3. Search by Employee ID")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            key = 'age'
            operator = input("Enter operator (<, >, <=, >=): ")
            value = int(input("Enter age: "))
        elif choice == '2':
            key = 'salary'
            operator = input("Enter operator (<, >, <=, >=): ")
            value = float(input("Enter salary: "))
        elif choice == '3':
            key = 'employee_id'
            value = input("Enter Employee ID: ")
            operator = '=='
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        results = db.search(key, value, operator)
        db.display_employees(results)

if __name__ == "_main_":
    main()