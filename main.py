import json
import codecs
import os
import logging
import pandas as pd

# MystiqueShade™ 💫 /// Explore the Enigma: Github | [https://github.com/ MystiqueShade]
class Converter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def determine_file_type(self, choice):
        if choice == "1":
            return "text"
        elif choice == "2":
            return "excel"
        else:
            self.logger.error("Invalid choice. Please enter '1' for text files or '2' for Excel files.")
            return None

    def convert_to_json(self, choice, input_file, output_file):
        file_type = self.determine_file_type(choice)
        if file_type == "text":
            self.convert_text_to_json(input_file, output_file)
        elif file_type == "excel":
            self.convert_excel_to_json(input_file, output_file)

    def convert_text_to_json(self, input_file, output_file):
        try:
            with codecs.open(input_file, 'r', encoding='utf-8') as file:
                words = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            self.logger.error(f"Input text file '{input_file}' not found.")
            return
        
        data = {"words": words}

        try:
            with codecs.open(output_file, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
            self.logger.info(f"JSON file successfully saved to {output_file}.")
        except Exception as e:
            self.logger.error(f"An error occurred while writing JSON file: {e}")

    def convert_excel_to_json(self, input_file, output_file):
        try:
            excel_data = pd.read_excel(input_file).to_dict(orient='records')
        except FileNotFoundError:
            self.logger.error(f"Input Excel file '{input_file}' not found.")
            return
        
        data = {"excel_data": excel_data}

        try:
            with codecs.open(output_file, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
            self.logger.info(f"JSON file successfully saved to {output_file}.")
        except Exception as e:
            self.logger.error(f"An error occurred while writing JSON file: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    converter = Converter()
    
    choice = input("Enter '1' for text files or '2' for Excel files: ")
    
    if choice == "1" or choice == "2":
        input_file = input("Enter the path of the input file: ")
        output_file = "output.json"
        converter.convert_to_json(choice, input_file, output_file)
    else:
        print("Invalid choice.")
