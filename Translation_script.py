import csv
import json
import os

def csv_to_arb(csv_file_path, output_dir):
    # Read the CSV file
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)

        # Create a dictionary for each language
        translations = {}
        for field in reader.fieldnames[1:]:  # Skip the first column (Key)
            translations[field] = {}
    
        # Fill the dictionaries with data from the CSV
        string_count = 0
        for row in reader:
            string_count += 1
            name = row['Name'].strip()
            key = name[:1].lower() + name[1:]
            for lang in translations.keys():
                if key != "@@locale" and key.startswith('@'):
                    continue
                translations[lang][key] = row[lang]
                if key == "@@locale":
                    continue
                metadata_key = '@'+key
                metadata_value = " ".join(key.split('_')[1:])
                translations[lang][metadata_key] = {}
                translations[lang][metadata_key]['description'] = metadata_value+" string"

        # Write each language's data to an ARB file
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        for lang, strings in translations.items():
            print(strings['@@locale'])
            if strings['@@locale'] == "":
                continue
            arb_file_path = os.path.join(output_dir, f"app_{strings['@@locale']}.arb")
            with open(arb_file_path, 'w', encoding='utf-8') as arbfile:
                json.dump(strings, arbfile, ensure_ascii=False, indent=2)
            print(f"Generated {arb_file_path}")
        print(string_count,'Srings generated')

# usage replace input csv file path if your csv file has different name
csv_file_path = './translations.csv'
output_dir = './'
csv_to_arb(csv_file_path, output_dir)
