# Student Certificate Download Automation

A Python desktop application that automates the repetitive process of entering student verification codes and downloading certificates from the Armenian government verification website.

The program was created for a teacher who needed to download more than 160 student certificates each year. It has been used for three consecutive annual certificate-processing cycles.

## Purpose

Without automation, each student verification code must be entered manually, and every certificate must be downloaded separately. Afterward, the user must check which certificates were not downloaded successfully and repeat the process for those students.

This application:

- reads student verification codes from `TextData.txt`;
- checks which certificate files already exist in the `Files` folder;
- identifies the certificates that are still missing;
- creates a new data file containing only the missing verification codes;
- automatically enters each missing code into the verification website;
- downloads the corresponding certificate;
- allows unsuccessful downloads to be retried without repeating completed downloads.

## Technologies

- Python
- PyAutoGUI
- pandas
- Tkinter
- File-system processing
- Browser-interface automation
- Text and CSV data processing

## Requirements

- Python 3
- Internet access
- A web browser
- A 1920 × 1080 display resolution, or a sufficiently similar setup
- The required Python packages

Install the required packages using:

```bash
pip install pandas pyautogui
```

Tkinter is normally included with Python.

## Project Structure

```text
Student-Certificate-Download-Automation/
├── main.py
├── README.md
├── requirements.txt
├── TextData.txt
└── Files/
```

### `main.py`

Contains the complete application and graphical user interface.

### `TextData.txt`

Contains the student verification codes, with one code on each line.

Example:

```text
EXAMPLE-CODE-001
EXAMPLE-CODE-002
EXAMPLE-CODE-003
```

Only fictional example codes should be included in the public GitHub repository.

### `Files`

Contains the certificates that have already been downloaded should be included in the public GitHub repository.

### `Files`

Contains.

The application compares the filenames in this folder with the codes in `TextData.txt` to identify certificates that are still missing.

## Instructions

### 1. Prepare the files

Empty the `Files` folder.

Place all required verification codes inside `TextData.txt`, with one code on each line.

Do not change the names or contents of the program files.

### 2. Open the verification website

Open the following website in a browser:

```text
https://verify.e-gov.am/am/
```

Then run the Python program:

```bash
python main.py
```

### 3. Prepare the data

Press the **Prepare the data** button.

The application will compare the codes in `TextData.txt` with the certificate files already present in the `Files` folder.

It will then display the number of certificates that are still missing.

### 4. Start the automated download process

When the number of missing certificates is not zero, press **Compile**.

Immediately switch to the browser tab containing:

```text
https://verify.e-gov.am/am/
```

Press `F11`, or `Fn + F11`, to enter fullscreen mode.

The program waits only five seconds before beginning, so the browser tab must be opened quickly.

Do not move the mouse or use the keyboard while the automation is running.

### 5. Move the downloaded files

After the automated process finishes, move all downloaded certificate files into the `Files` folder.

### 6. Check for missing certificates

Press **Prepare the data** again.

The application will compare the downloaded files with the complete list of verification codes and report how many certificates are still missing.

When some certificates are still missing, repeat the process.

The program will attempt to download only the missing certificates and will not repeat certificates that have already been downloaded successfully.

Continue until the missing certificate count reaches zero.

## Important Notes

- Do not make changes to the program files.
- Keep the verification website open in fullscreen mode while the program is running.
- Do not move the mouse or use the keyboard during the automated process.
- The program uses screen coordinates based on a 1920 × 1080 reference resolution.
- Changes to browser zoom, display scaling, website layout, window position, or screen resolution may cause the program to click incorrect locations.
- The program may require modification if the verification website changes its interface.
- The five-second delay begins immediately after pressing **Compile**.

## How the Missing-File Check Works

The application reads the complete list of verification codes from `TextData.txt`.

It then reads the filenames of certificates already present in the `Files` folder.

Codes that do not have a corresponding downloaded file are collected into a new data file. During the next automated run, only those missing codes are entered into the verification website.

This makes the process recoverable when some downloads fail because of connection problems, browser delays, or website errors.

## Impact

The application has been used by a teacher for three consecutive years.

It supports the annual processing of more than 160 student certificates and reduces the amount of repetitive manual work required.

Instead of manually entering every verification code, checking every download, and repeating the entire process when some certificates are missing, the user can automatically process the codes and retry only unsuccessful downloads.

Across three annual cycles, the application has supported the processing of at least 480 certificates.

## Limitations

The application relies on browser-interface automation rather than direct communication with the website's server.

Because of this:

- it depends on the position of buttons and input fields;
- it may fail when the website loads slowly;
- it depends on the selected screen resolution and browser layout;
- it requires the user to move downloaded files into the `Files` folder;
- it may need several runs when some downloads are unsuccessful.

These limitations are partially addressed by the missing-file detection system, which allows unsuccessful downloads to be identified and repeated.

## Privacy

The public repository must not contain:

- real student names;
- real verification codes;
- downloaded certificates;
- passwords;
- browser cookies;
- login credentials;
- personal or confidential information.

Only fictional sample data should be included in `TextData.txt`, and the public `Files` folder should remain empty.

## Author

Developed by Edgar Mikaelyan as a practical automation tool for repeated real-world use.
