number=0
with open('log_files\201811123008.log',encoding='utf8') as f:
    for line in f:
        student_id=line.split(',')[1].split(': ')[1]
        print(student_id)
        if(student_id=='201811123008'):
            number=number+1
print(number)