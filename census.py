data = file('urpop0090.txt', 'r')	
for line in data:
    line = line.strip()
    if '%' not in line: 
        continue

blacklist = ['Region', 'Division', 'Table', 'UNITED STATES', 'population']
if 'Region' in line or 'Division' in line or 'UNITED STATES' in line:	 
    continue
 	 
states = ['Maine', 'New Hampshire', 'Vermont', 'Massachusetts', 'Rhode Island', 'Connecticut', 'New York', 'New Jersey', 'Pennsylvania', 'Ohio', 'Indiana', 'Illinois', 'Michigan', 'Wisconsin', 'Minnesota', 'Iowa', 'Missouri', 'North Dakota', 'South Dakota', 'Nebraska', 'Kansas', 'Delaware', 'Maryland', 'Virginia', 'West Virginia', 'North Carolina', 'South Carolina', 'Georgia', 'Florida', 'Kentucky', 'Tennessee', 'Alabama', 'Mississippi', 'Arkansas', 'Louisiana', 'Oklahoma', 'Texas', 'Montana', 'Idaho', 'Wyoming', 'Colorado', 'New Mexico', 'Arizona', 'Utah', 'Nevada', 'Washington', 'Oregon', 'California', 'Alaska', 'Hawaii'] 	 

for state in states: 
    if state in line:
        print line 
        break
print line
print line[:27].strip()
print line[27:38].strip()
print line[86:96].strip()
print line[144:154].strip()
