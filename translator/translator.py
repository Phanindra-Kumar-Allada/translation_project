from googletrans import Translator

class MyTranslator:
    def __init__(self):
        self.translator = Translator()
    
    # Translate the given text from the input language to the target language.
    def translate(self, text, target_language, input_language='auto'):
        """
        Parameters:
        text (str): The text to be translated.
        target_language (str): The language code of the target language.
        input_language (str): The language code of the input language. Default is 'auto'.
        """
        translation = self.translator.translate(text, dest=target_language, src=input_language)
       
        # Returns: - str: The translated text.
        return translation.text
