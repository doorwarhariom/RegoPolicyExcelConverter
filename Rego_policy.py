import re
import pandas as pd

data = """      "paste data here"           """

pattern = re.compile(
    r"(?P<status>[❌✔️])\s*(?P<category>[A-Za-z]+)\((?P<severity>[A-Za-z]+)\):\s*(?P<resource_type>[A-Za-z\s]+)'(?P<resource_name>[^']+)'\s*(?P<policy>.*)"
)

records = []

for match in pattern.finditer(data):
    records.append({
        "Status": "Fail" if match.group("status") == "❌" else "Pass",
        "Category": match.group("category"),
        "Severity": match.group("severity"),
        "Resource Type": match.group("resource_type").strip(),
        "Resource Name": match.group("resource_name").strip(),
        "Policy Description": match.group("policy").strip(),
    })


df = pd.DataFrame(records)
output_path = "Rego.xlsx"
df.to_excel(output_path, index=False)

print(f" Excel report: {output_path}")
