import re
import pandas as pd

data = """    
 
         """

pattern = re.compile(
    r"(?P<status>[❌✔️])\s*(?P<category>[A-Za-z]+)\((?P<severity>[A-Za-z]+)\):\s*(?P<resource_type>[A-Za-z\s]+)'(?P<resource_name>[^']+)'\s*(?P<policy>.*)"
)

records = []

for match in pattern.finditer(data):
    records.append({
        "Service Name": match.group("resource_type").strip(),
        "Resource Name": match.group("resource_name").strip(),
        "Compliance Check": match.group("policy").strip(),
        "Status": "Fail" if match.group("status") == "❌" else "Pass",
        "IMG/Custom": match.group("category"),
        "Mandatory/Optional": match.group("severity"),
    })


df = pd.DataFrame(records)
output_path = "C:/Users/OOF3KOR/Downloads/PT/rego1.xlsx"
df.to_excel(output_path, index=False)

print(f" Excel report: {output_path}")
