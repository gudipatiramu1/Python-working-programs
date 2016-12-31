employee={'ramu':155,'rishi':290,'dsk':123}
new={'sai':1234}
def test(employee,new):
    employee.update(new)
    print("Inside the Function",employee)
    return
test(employee,new)
print("Outside the Function",employee)
