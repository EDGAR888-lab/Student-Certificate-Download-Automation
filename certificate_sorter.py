import os
import re
import shutil
import pandas as pd


excel_file = "Students/data.xlsx"
pdf_folder = "Files"
output_folder = "Sorted_pdfs"
text_file = "TextData.txt"

first_name_column = "First name"
last_name_column = "Last name"
middle_name_column = "Middle name"
class_column = "Class"
id_column = "ID"


def clean_name(value):
    if pd.isna(value):
        return ""

    value = str(value)
    value = value.replace(",", " ")
    value = " ".join(value.split())

    return value.strip()


def clean_class(value):
    if pd.isna(value):
        return "UnknownClass"

    value = str(value).strip()
    value = value.replace(" ", "")

    if value == "":
        return "UnknownClass"

    return value


def clean_id(value):
    if pd.isna(value):
        return ""

    value = str(value)
    value = value.strip()
    value = value.lower()

    return value


def safe_filename(value):
    value = value.strip()

    bad_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

    for character in bad_characters:
        value = value.replace(character, "_")

    while value.endswith(".") or value.endswith(" "):
        value = value[:-1]

    if value == "":
        return "Unnamed"

    return value


def make_unique_path(folder, filename):
    destination = os.path.join(folder, filename)

    if not os.path.exists(destination):
        return destination

    name, extension = os.path.splitext(filename)
    number = 2

    while os.path.exists(destination):
        new_filename = name + " (" + str(number) + ")" + extension
        destination = os.path.join(folder, new_filename)
        number += 1

    return destination


def main():
    if not os.path.exists(excel_file):
        print("Excel file was not found:")
        print(excel_file)
        return

    if not os.path.exists(pdf_folder):
        print("PDF folder was not found:")
        print(pdf_folder)
        return

    if not os.path.exists(text_file):
        print("TextData.txt was not found.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    students = pd.read_excel(
        excel_file,
        dtype=str,
        keep_default_na=False
    )

    new_columns = []

    for column in students.columns:
        new_columns.append(str(column).strip())

    students.columns = new_columns

    required_columns = [
        first_name_column,
        last_name_column,
        middle_name_column,
        class_column,
        id_column
    ]

    for column in required_columns:
        if column not in students.columns:
            print("Missing Excel column:", column)
            return

    students_by_id = {}

    for row_number in range(len(students)):
        row = students.iloc[row_number]

        student_id = clean_id(row[id_column])

        if student_id == "":
            print("Skipped Excel row", row_number + 2, "- empty ID")
            continue

        first_name = clean_name(row[first_name_column])
        middle_name = clean_name(row[middle_name_column])
        last_name = clean_name(row[last_name_column])
        student_class = clean_class(row[class_column])

        full_name = ""

        if first_name != "":
            full_name = first_name

        if middle_name != "":
            if full_name != "":
                full_name += " "
            full_name += middle_name

        if last_name != "":
            if full_name != "":
                full_name += " "
            full_name += last_name

        if full_name == "":
            print(
                "Skipped Excel row",
                row_number + 2,
                "- student has no name"
            )
            continue

        if student_id in students_by_id:
            print(
                "Warning: duplicate ID",
                student_id,
                "- the last row will be used"
            )

        students_by_id[student_id] = {
            "name": full_name,
            "class": student_class
        }

    files_to_process = []

    file = open(text_file, "r", encoding="utf-8")

    for line in file:
        line = line.strip()

        if line != "":
            files_to_process.append(line)

    file.close()

    processed = 0
    missing_files = 0
    unmatched_ids = 0

    for file_name in files_to_process:
        if not file_name.lower().endswith(".pdf"):
            file_name = file_name + ".pdf"

        source_path = os.path.join(pdf_folder, file_name)

        if not os.path.exists(source_path):
            print("PDF file was not found:", file_name)
            missing_files += 1
            continue

        pdf_id = os.path.splitext(file_name)[0]
        pdf_id = clean_id(pdf_id)

        if pdf_id not in students_by_id:
            print("No matching student ID for:", file_name)
            unmatched_ids += 1
            continue

        student = students_by_id[pdf_id]

        class_name = safe_filename(student["class"])
        class_folder = os.path.join(output_folder, class_name)

        if not os.path.exists(class_folder):
            os.makedirs(class_folder)

        new_file_name = safe_filename(student["name"]) + ".pdf"

        destination = make_unique_path(
            class_folder,
            new_file_name
        )

        shutil.copy2(source_path, destination)

        print(
            file_name,
            "->",
            student["class"] + "\\" + os.path.basename(destination)
        )

        processed += 1

    print()
    print("Finished.")
    print("Successfully processed:", processed)
    print("Files not found:", missing_files)
    print("Files without matching student IDs:", unmatched_ids)
    print("Output folder:", output_folder)


main()
