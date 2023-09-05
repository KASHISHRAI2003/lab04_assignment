class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, operator, age):
        result = []
        for emp in self.employees:
            if operator == '>' and emp.age > age:
                result.append(emp)
            elif operator == '<' and emp.age < age:
                result.append(emp)
            elif operator == '>=' and emp.age >= age:
                result.append(emp)
            elif operator == '<=' and emp.age <= age:
                result.append(emp)
        return result

    def search_by_salary(self, operator, salary):
        result = []
        for emp in self.employees:
            if operator == '>' and emp.salary > salary:
                result.append(emp)
            elif operator == '<' and emp.salary < salary:
                result.append(emp)
            elif operator == '>=' and emp.salary >= salary:
                result.append(emp)
            elif operator == '<=' and emp.salary <= salary:
                result.append(emp)
        return result

    def search_by_employee_id(self, emp_id):
        result = []
        for emp in self.employees:
            if emp.emp_id == emp_id:
                result.append(emp)
        return result

def main():
    database = EmployeeDatabase()

    
    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    while True:
        print("\nMenu:")
        print("1. Search by Age")
        print("2. Search by Salary")
        print("3. Search by Employee ID")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            operator = input("Enter operator (>, <, <=, >=): ")
            age = int(input("Enter age: "))
            results = database.search_by_age(operator, age)
            print("\nSearch results:")
            for emp in results:
                print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

        elif choice == '2':
            operator = input("Enter operator (>, <, <=, >=): ")
            salary = float(input("Enter salary: "))
            results = database.search_by_salary(operator, salary)
            print("\nSearch results:")
            for emp in results:
                print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

        elif choice == '3':
            emp_id = input("Enter Employee ID: ")
            results = database.search_by_employee_id(emp_id)
            if results:
                emp = results[0]
                print("\nSearch result:")
                print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
            else:
                print("Employee not found.")

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
