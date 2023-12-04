import os
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
from translator.translator import MyTranslator
from googletrans import LANGUAGES, Translator

class TranslationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Translation App")

        # GUI components setup
        self.text_label = ttk.Label(master, text="Enter the text to translate:")
        self.text_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Set up input text entry with word wrap
        self.text_entry = tk.Text(master, wrap=tk.WORD, height=3, width=50)
        self.text_entry.grid(row=0, column=1, padx=10, pady=10)

        self.input_language_label = ttk.Label(master, text="Select the input language:")
        self.input_language_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Get the list of languages from Googletrans
        self.languages = list(LANGUAGES.values())

        # Set up input language dropdown
        self.language_var = tk.StringVar(value='')
        self.input_language_menu = ttk.Combobox(master, textvariable=self.language_var, values=[lang.capitalize() for lang in self.languages])  # Display in title case
        self.input_language_menu.grid(row=1, column=1, padx=10, pady=10)

        self.target_language_label = ttk.Label(master, text="Select the target language:")
        self.target_language_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Set up target language dropdown
        self.target_language_var = tk.StringVar(value='')
        self.target_language_menu = ttk.Combobox(master, textvariable=self.target_language_var, values=[lang.capitalize() for lang in self.languages])  # Display in title case
        self.target_language_menu.grid(row=2, column=1, padx=10, pady=10)

        # Translate button
        self.translate_button = ttk.Button(master, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Result text box
        self.result_textbox = tk.Text(master, wrap=tk.WORD, height=5, width=50)
        self.result_textbox.grid(row=4, column=0, columnspan=2, pady=10)

    def translate_text(self):
        # Get user input
        text = self.text_entry.get("1.0", tk.END).strip()  # Get text from the Text widget
        input_language = self.language_var.get().capitalize()
        target_language = self.target_language_var.get().capitalize()

        # Translate using MyTranslator
        translator = MyTranslator()
        translation = translator.translate(text, target_language, input_language)

        # Display translation result in the text box without "Translation:" label
        result_text = f"{translation}"
        self.result_textbox.delete(1.0, tk.END)  # Clear previous content
        self.result_textbox.insert(tk.END, result_text)

        # Output file path
        output_file = 'data/output_data.csv'

        # Create a NumPy array for the new translation
        new_data = np.array([[text, translation, input_language, target_language]])

        # Check if the file exists
        if not os.path.exists(output_file):
            # If the file doesn't exist, create a new DataFrame
            columns = ["Text", "Translation", "InputLanguage", "TargetLanguage"]
            new_df = pd.DataFrame(new_data, columns=columns)
            new_df.to_csv(output_file, index=False)
        else:
            # If the file exists, read it as a DataFrame and append the new data
            existing_data = pd.read_csv(output_file)
            updated_data = pd.concat([existing_data, pd.DataFrame(new_data, columns=existing_data.columns)], ignore_index=True)
            updated_data.to_csv(output_file, index=False)

def main():
    # Run the GUI
    root = tk.Tk()
    app = TranslationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()