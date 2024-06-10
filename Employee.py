class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, position: {self.position}, Salary: {self.salary}"
    
    def update_position(self, new_position):
        self.position = new_position

    
    def update_salary(self, new_salary):
        self.salary = new_salary

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, position, salary):
        new_employee = Employee(name, age, position, salary)
        self.employees.append(new_employee)

    def remove_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                return
            print("Employee not found")

    def update_employee(self, name, age=None, position=None, salary=None):
        for employee in self.employees:
            if employee.name == name:
                if age:
                    employee.age = age
                if position:
                    employee.update_position(position)
                if salary:
                    employee.update_salary(salary)
                return
        print("Empoyee not found")

    def view_all_employees(self):
        for employee in self.employees:
            print(employee)

    def find_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None 
    
    def main():
        company = Company()

        while True:
            print("\n1. Add Employee\n2. Remove Employee\n3. Update Employee\n4. View All Employees\n5. Find Employee\n6. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter Employee name:")
                age = int(input("Enter employee age: "))
                position = input("Enter employee position: ")
                salary = float(input("Enter employee salary: "))
                company.add_employee(name, age, position, salary)
            elif choice =="2":
                name = input("Enter employee name to remove:")
                company.remove_employee(name)
            elif choice == "3":
                name = input("Enter employee name to update: ")
                age = input("Enter new age")
                position = input("Enter new position")
                salary = input("Enter new salary")
                company.update_employee(name, age, position, salary)
            elif choice == "4":
                company.view_all_employees()
            elif choice == "5":
                name = input("Enter employee name to find:")
                employee = company.find_employee(name)
                if employee:
                    print(employee)
                else:
                    print("Employee not found")
            elif choice == "6":
                break
            else:
                print("Invalid option. Please choose a valid option.")

        #if __name__ == "__main__":
         #   main()

company = Company()
#Add employee
company.add_employee("Muteeat", 30, "Backend Developer", 1000000)
company.add_employee("Sarat", 24, "Stylist", 800000)
company.add_employee("Ayo", 20, "Data Analyst", 700000)



#remove employee
company.remove_employee("Ayo")

#view employees
company.view_all_employees()

#find an employee by name
employee = company.find_employee("Muteeat")
print(employee)

#update employee's details
company.update_employee("Muteeat", age=35, position="Senior Developer", salary=1500000)

        

