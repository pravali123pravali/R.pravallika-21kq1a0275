import pandas as pd
s = []
f=[]
m=[]
hr=[]
bp=[]
sl=[]
m_age=[]
f_age=[]


def patient(patient_name, gender, age, heart_rate, blood_pressure, sugar_level):
    details = {
        'patient_name': patient_name,
        'gender': gender,
        'age': age,
        'heart_rate': heart_rate,
        'blood_pressure': blood_pressure,
        'sugar_level': sugar_level
    }
    s.append(details)
    if gender=="female":
        f.append(gender)
    else:
        m.append(gender)    
n = int(input("Enter the number of patients: "))
for i in range(n):
    patient_name = input("Enter patient name: ")
    gender = input("Enter gender: ")
    age = int(input("Enter age: "))
    heart_rate = int(input("Enter heart rate: "))
    blood_pressure = int(input("Enter blood pressure: "))
    sugar_level = int(input("Enter sugar level: "))
    patient(patient_name, gender, age, heart_rate, blood_pressure, sugar_level)
for i in range(n):
    hr.append(s[i]['heart_rate'])
    bp.append(s[i]['blood_pressure'])
    sl.append(s[i]['sugar_level'])
for j in range(n):
    m_age.append(s[j]['age'])
    f_age.append(s[j]['age'])
    

sorted_s = sorted(s,key=lambda x: x['patient_name'])
for i in sorted_s:
    print(i['patient_name'])




# Display patient details in tabular format
print("patient_name\tgender\tage\theart_rate\tblood_pressure\tsugar_levels")
for details in s:
    print(f"{details['patient_name']}\t\t{details['gender']}\t{details['age']}\t{details['heart_rate']}\t\t{details['blood_pressure']}\t\t{details['sugar_level']}")
df=pd.DataFrame(s)
print(df)
print({len(f)})
print({len(m)})
print(sorted_s)
print(max(hr))
print(min(hr))
print(max(bp))
print(min(bp))
print(max(sl))
print(min(sl))
print(max(m_age))
print(min(f_age))
