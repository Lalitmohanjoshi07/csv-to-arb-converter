import json
import pandas as pd

# Load the .arb file
arb_file_path = 'app_en.arb'
with open(arb_file_path, 'r', encoding='utf-8') as f:
    arb_data = json.load(f)

# Load the untranslated messages file
untranslated_file_path = 'untranslated_messages.txt'
with open(untranslated_file_path, 'r', encoding='utf-8-sig') as f:
    untranslated_data = json.load(f)

# Extract untranslated messages for 'es' locale
untranslated_keys = untranslated_data.get("cs", [])

# Prepare data for the Excel sheet
excel_data = []
for key in untranslated_keys:
    value = arb_data.get(key, "")
    description_key = f"@{key}"
    description = arb_data.get(description_key, {}).get("description", "")
    excel_data.append({
        "Key": key,
        "Value": value,
        "Description": description
    })

# # Create a DataFrame
# df = pd.DataFrame(excel_data)

print(excel_data)

# # Save to Excel
output_excel_path = 'untranslated_messages_created.txt'
# df.to_excel(output_excel_path, index=False)
with open(output_excel_path, "w") as file:
    file.write(excel_data.__str__())


print(f"Untranslated messages have been saved to {output_excel_path}")
