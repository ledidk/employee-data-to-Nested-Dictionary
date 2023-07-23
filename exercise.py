dict = {}

file = open('data.txt', 'r')
with open('data.txt', 'r') as dataFile:
    for line in dataFile:
        lines = line.split('\t')
        first_name = lines[0]
        last_name = lines[1]
        email = lines[2]
        password = lines[3]
        ip_address = lines[4]
        department = lines[5]
        employer = lines[6].strip()

        if employer == 'employer':
            continue

        if employer not in dict:
            dict[employer] = []
        employeeDetails = {}
        employeeDetails['department'] = department
        employeeDetails['email'] = email
        employeeDetails['ip_address'] = ip_address
        employeeDetails['password'] = password
        fullName = {}
        fullName[first_name + ' ' + last_name] = employeeDetails
        dict[employer].append(fullName)



        # print(lines)
print(dict)