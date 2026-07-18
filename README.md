# Student Certificate Download and Sorting Automation

This project contains two Python programs that automate the processing of student certificates.

The first program enters student verification codes into the Armenian government verification website and downloads the corresponding certificates.

The second program matches the downloaded PDF filenames with student records stored in an Excel file, renames each certificate using the student's name, and separates the certificates into folders according to class.

The system was created for a teacher who needed to process more than 160 student certificates each year. It has been used during three consecutive annual certificate-processing cycles.

## Main Workflow

The complete process consists of two stages:

1. Download the certificates using the student verification codes.
2. Rename and organise the downloaded certificates using student information from Excel.

## Technologies

- Python
- PyAutoGUI
- pandas
- Tkinter
- openpyxl
- Browser-interface automation
- Excel file processing
- Text and CSV file processing
- File-system automation

## Requirements

- Python 3
- Internet access
- A web browser
- A display setup compatible with the configured screen coordinates
- The required Python packages

Install the packages using:

```bash
pip install pandas pyautogui openpyxl
```

Tkinter is normally included with Python.

## Project Structure

```text
Student-Certificate-Download-Automation/
├── certificate_downloader.py
├── certificate_sorter.py
├── README.md
├── requirements.txt
├── TextData.txt
├── Data
├── Files/
├── Students/
│   └── data.xlsx
└── Sorted_pdfs/
```

## Files and Folders

### `certificate_downloader.py`

The first program checks which certificates are missing and automatically enters the missing verification codes into the government verification website.

### `certificate_sorter.py`

The second program matches downloaded PDF files with the student records in the Excel file.

It then:

- finds the student connected to each certificate ID;
- renames the PDF using the student's full name;
- creates a separate folder for each class;
- copies the renamed certificate into the correct class folder;
- preserves the original PDF files.

### `TextData.txt`

Contains the student verification codes, with one code on each line.

Example:

```text
EXAMPLE-CODE-001
EXAMPLE-CODE-002
EXAMPLE-CODE-003
```

The same file is used by both programs.

The downloader uses it as the complete list of certificates that must be downloaded.

The sorter uses it as the list of PDF files that must be renamed and organised.

The codes must be written without the `.pdf` extension.

### `Data`

This file is automatically created by the first program.

It contains only the verification codes whose certificates have not yet been downloaded.

### `Files`

Contains all successfully downloaded certificate PDF files.

The filename of each PDF must be its student verification code.

Example:

```text
EXAMPLE-CODE-001.pdf
EXAMPLE-CODE-002.pdf
```

### `Students/data.xlsx`

Contains the student information used to rename and organise the certificates.

The Excel file must contain the following exact column names:

```text
First name
Middle name
Last name
Class
ID
```

The value in the `ID` column must match the filename of the corresponding PDF.

Example:

```text
Excel ID:       EXAMPLE-CODE-001
PDF filename:   EXAMPLE-CODE-001.pdf
```

### `Sorted_pdfs`

Contains the renamed and organised certificates.

The program creates a separate folder for every class.

Example:

```text
Sorted_pdfs/
├── 10A/
│   ├── Anna Maria Smith.pdf
│   └── David John Brown.pdf
└── 11B/
    ├── Edgar Mikaelyan.pdf
    └── Michael Green.pdf
```

## Stage 1: Downloading the Certificates

### 1. Prepare the files

Empty the `Files` folder before beginning a new annual certificate-processing cycle.

Place all student verification codes in `TextData.txt`, with one code on each line.

Do not modify the program files.

### 2. Open the verification website

Open the following website:

```text
https://verify.e-gov.am/am/
```

Run the certificate downloader:

```bash
python certificate_downloader.py
```

### 3. Prepare the missing-code data

Press **Prepare the data**.

The program compares the codes in `TextData.txt` with the PDF filenames already present in the `Files` folder.

It then displays how many certificates are still missing.

### 4. Begin the automated download

When the number of missing files is not zero, press **Compile**.

Immediately switch to the browser tab containing:

```text
https://verify.e-gov.am/am/
```

Press `F11`, or `Fn + F11`, to enter fullscreen mode.

The program waits five seconds before beginning, so the browser tab must be opened quickly.

Do not move the mouse or use the keyboard while the program is controlling the browser.

### 5. Move the downloaded files

After the program finishes, move all downloaded certificate PDFs into the `Files` folder.

### 6. Check for unsuccessful downloads

Press **Prepare the data** again.

The program will check which certificates are still missing.

When some files are missing, repeat the download process. The program will enter only the missing codes instead of repeating every completed download.

Continue until the missing-file count reaches zero.

## Stage 2: Renaming and Organising the Certificates

Before running the second program, confirm that:

- the downloaded PDFs are inside the `Files` folder;
- the PDF filenames are the corresponding student IDs;
- `TextData.txt` contains the IDs or PDF filenames to be processed;
- `Students/data.xlsx` contains the required student information;
- the values in the Excel `ID` column match the PDF filenames.

Run the certificate sorter:

```bash
python certificate_sorter.py
```

The program will:

1. Read the student records from `Students/data.xlsx`.
2. Read the required certificate filenames from `TextData.txt`.
3. Find each PDF inside the `Files` folder.
4. Match the PDF filename with the Excel `ID` column.
5. Build the student's full name in this order:

```text
First name Middle name Last name
```

6. Create a folder for the student's class inside `Sorted_pdfs`.
7. Copy and rename the certificate inside the correct class folder.
8. Display how many certificates were processed successfully.
9. Report any missing PDF files or IDs without matching Excel records.

The original certificate files inside `Files` are preserved.

## Duplicate Names

When a certificate with the same student name already exists in a class folder, the program does not overwrite it.

Instead, it creates filenames such as:

```text
Student Name.pdf
Student Name (2).pdf
Student Name (3).pdf
```

Therefore, `Sorted_pdfs` should normally be emptied before beginning a new complete processing cycle.

## Important Notes

- Do not modify the program files while processing certificates.
- Do not move the mouse or use the keyboard while browser automation is running.
- Keep the government verification website in fullscreen mode during downloads.
- The download program uses coordinates based on a 1920 × 1080 reference resolution.
- Browser zoom, display scaling, website layout, window position, or screen resolution may affect the browser automation.
- The download program may need adjustment if the government website changes its interface.
- Keep the Excel `ID` column formatted as text when IDs contain leading zeroes.
- The Excel column names must match the required names exactly.
- PDF filenames must match the corresponding student IDs.
- The sorter processes only the certificates listed in `TextData.txt`.

## Error Handling

The sorting program reports several possible problems:

- Excel file not found;
- PDF folder not found;
- `TextData.txt` not found;
- required Excel column missing;
- student row with an empty ID;
- student row with no name;
- duplicate student ID;
- PDF file not found;
- PDF filename without a matching student ID.

The program prints a summary when processing is finished:

```text
Finished.
Successfully processed: ...
Files not found: ...
Files without matching student IDs: ...
Output folder: Sorted_pdfs
```

## Impact

The system has been used by a teacher for three consecutive years.

It supports the annual processing of more than 160 student certificates. Across three annual cycles, it has supported the processing of at least 480 certificates.

The project reduces repetitive manual work by automating:

- entering student verification codes;
- downloading certificates;
- identifying unsuccessful downloads;
- retrying only missing certificates;
- matching certificate IDs with student records;
- renaming certificates;
- creating class folders;
- sorting certificates into the correct folders.

## Limitations

The certificate downloader uses browser-interface automation rather than direct communication with the website server.

Because of this, it depends on:

- the position of website buttons and fields;
- the speed at which the website loads;
- the screen resolution;
- the browser layout;
- the browser being in fullscreen mode.

The missing-file checking system helps manage unsuccessful downloads by allowing only missing certificates to be retried.

The sorting program requires the PDF filenames and Excel IDs to match correctly.

## Privacy

The public repository must not contain:

- real student names;
- real student verification codes;
- real student IDs;
- downloaded certificates;
- private Excel records;
- passwords;
- browser cookies;
- login credentials;
- other personal or confidential information.

The public `TextData.txt` and Excel file should contain only fictional example data.

The public `Files` and `Sorted_pdfs` folders should not contain real certificates.

## Author

Developed by Edgar Mikaelyan as a practical automation system for repeated real-world use.
