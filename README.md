# Python_Project for Translation App
This project is a language translation application with a graphical user interface (GUI) that utilizes the Google Translate API.

<!--# Video Explanation
Have to attach the video link or maybe generate a new video-->


# Project Structure
The project is organized as follows:

translation_project
1. data/output_data.csv
2. translator/translator.py
3. app.py

# Dependencies
Pandas: For data manipulation and storage.
numpy: For handling arrays.
tkinter: This is used to build the graphical user interface.
googletrans: This is for interfacing with the Google Translate API.

# Setup
1. Navigate to the project directory:
   cd translation_project
   
2. Install project dependencies:
   pip install googletrans==4.0.0-rc1

# Usage
1. Run the translation application:
   python app.py
2. The GUI will appear.
3. Enter the text you want to translate in the provided text entry field.
4. Select the input and target languages from the drop-down menus.
5. Click the "Translate" button to view the translation result in the output text box.
6. The translation result is also stored in data/output_data.csv.
