# Student Certificate Download Automation

A Python desktop application that automates the repetitive process of entering student verification codes and downloading certificates from the Armenian government verification website.

The program was created for a teacher who needed to download more than 160 student certificates each year. It has been used for three annual certificate-processing cycles.

## Purpose

Without automation, every student code must be entered manually, and each certificate must be downloaded separately. Failed or missing downloads must then be identified and repeated.

This application:

- reads student verification codes from `TextData.txt`;
- checks which certificate files already exist in the `Files` folder;
- creates a list containing only the missing certificates;
- automatically enters each missing code into the verification website;
- downloads the corresponding certificate;
- allows the process to be repeated without downloading completed certificates again.

## Technologies

- Python
- PyAutoGUI
- pandas
- Tkinter
- File-system processing
- Browser-interface automation

## Requirements

- Python 3
- Internet access
- A web browser
- The required Python packages

Install the packages using:

```bash
pip install pandas pyautogui
