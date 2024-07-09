import csv

def Calculate_grade(marks):
    if 0 <= marks < 40:
        return 'E'
    elif 40 <= marks < 50:
        return 'D'
    elif 50 <= marks < 60:
        return 'C'
    elif 60 <= marks < 70:
        return 'B'
    elif 70 <= marks <= 100:
        return 'A'
    else:
        return 'Invalid Marks'

def get_student_data():
    student_name = input("Enter the student's name: ")
    registration_number = input("Enter the student's registration number: ")

    data = []
    total_marks = 0

    for year in range(1, 5):
        print(f"Grades for year {year}")
        yearly_marks = 0
        yearly_data = []

        for unit in range(1, 4):
            unit_name = input(f"Enter the name of unit {unit}: ")
            marks = float(input(f"Enter marks for Unit {unit_name}: "))
            grade = Calculate_grade(marks)
            yearly_marks += marks
            yearly_data.append({'unit_name': f'Unit {unit_name}', 'marks': marks, 'grade': grade})

        average_marks = yearly_marks / 3
        yearly_grade = Calculate_grade(average_marks)
        total_marks += average_marks

        yearly_data.append({'unit_name': 'Yearly Average', 'marks': average_marks, 'grade': yearly_grade})
        data.append(yearly_data)
        print(f"Year {year} Grade: {yearly_grade}")

    overall_average = total_marks / 4
    overall_grade = Calculate_grade(overall_average)
    print(f"\nTotal Grade for Four Years: {overall_grade}")

    return student_name, registration_number, data, overall_grade

def save_to_csv(student_name, registration_number, data, overall_grade):
    filename = f"{registration_number}_report_card.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Student Name', student_name])
        writer.writerow(['Registration Number', registration_number])
        writer.writerow([])

        for year in range(1, 5):
            writer.writerow([f'Year {year}'])
            writer.writerow(['Unit_name', 'Grade'])
            for item in data[year-1]:
                writer.writerow([item['unit_name'], item['grade']])
            writer.writerow([])

        writer.writerow(['Overall Grade for the four years', overall_grade])

    print(f"\nReport card saved to {filename}")

def main():
    student_name, registration_number, data, overall_grade = get_student_data()
    save_to_csv(student_name, registration_number, data, overall_grade)

if __name__ == "__main__":
    main()
