import pandas as pd

#ZADANIE 8
emp_det = pd.read_excel("employee.xlsx", sheet_name="employee_details")
emp_perf = pd.read_excel("employee.xlsx", sheet_name="performance")

emp_det.set_index("name", inplace=True)
emp_perf.set_index("name", inplace=True)

employees = pd.concat([emp_det, emp_perf], axis=1)

employees.columns = [col.capitalize() for col in employees.columns]

print("INFO:")
employees.info()

print("\nSTRUKTURA:")
print(employees.dtypes)

print("\nZAWARTOŚĆ:")
print(employees)

#ZADANIE 9
emp_finance=employees[(employees['Department'].str.lower() == 'finance') & (employees['Income'] > 20000)] 
emp_finance.to_excel("emp_finance.xlsx", sheet_name="employee_finance")