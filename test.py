from models import db, Employee

employees = Employee.query.all()
for employee in employees:
    print(employee.login, employee.name)

new_employee = Employee(login='example', name='John Doe', position='Manager')
db.session.add(new_employee)
db.session.commit()
