# Python_Project for Translation App
This project is a simple translation application with a graphical user interface (GUI) that utilizes the Google Translate API.

# Project Structure
The project is organized as follows:

translation_project/
│
├── data/
│   └── output_data.csv
│
├── translator/
│   └── translator.py
│
├── app_with_better_GUI.py

# Dependencies
Pandas: For data manipulation and storage.
numpy: For handling arrays.
tkinter: For building the graphical user interface.
googletrans: For interfacing with the Google Translate API.

# Setup
1. Navigate to the project directory.
   cd python_translation_project
   
2. Install project dependencies:
   pip install googletrans==4.0.0-rc1

# Usage
1. Run the translation application.
   python app.py
2. The GUI will appear
   a. Enter the text you want to translate in the provided text entry field.
   b. Select the input and target languages from the dropdown menus.
   c. Click the "Translate" button to view the translation result in the output text box.
   d. The translation result is also stored in data/output_data.csv.
