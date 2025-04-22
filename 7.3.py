employees = {
    "HR": [(101, 50000), (102, 60000), (103, 55000)],
    "IT": [(201, 80000), (202, 90000), (203, 75000)],
    "Sales": [(301, 40000), (302, 45000), (303, 42000)]
}

min_max_salaries = {dept: (min(sal for _, sal in emp_list), max(sal for _, sal in emp_list)) for dept, emp_list in employees.items()}

print("Department-wise Min and Max Salaries:", min_max_salaries)
