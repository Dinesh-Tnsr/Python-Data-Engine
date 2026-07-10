import html
import pandas as pd

# Simulated raw JSON payload from a broken API
dirty_data = [
    {"id": 1, "name": "Alice", "department": "Engineering", "notes": "C &amp; Python"},
    {"id": 2, "name": "Bob", "notes": " Loves Data&#39;s logic \n"}, # Missing department!
    {"id": 3, "name": "Charlie", "department": "HR", "notes": "   All good.  "}
]

print("--- Pipeline Janitor Online ---")
clean_data = []

for record in dirty_data:
    print(record["id"])
    print(record["name"])
    record["department"] = record.get("department","unassigned")
    print(record["department"])
    record["notes"] = html.unescape(record["notes"]).strip()
    print(record["notes"])

    clean_data.append(record)


''' # The Immutable Approach
    clean_record = {
        "id": record["id"],
        "name": record["name"],
        "department": record.get("department", "unassigned"),
        "notes": html.unescape(record.get("notes", "")).strip()
    }
    clean_data.append(clean_record)'''

final_df = pd.DataFrame(clean_data).set_index("id")
print(final_df)

