import json

# Load the data
with open("datanew.json", "r") as f:
    data = json.load(f)

# Define order of models (parents first, children later)
model_priority = {
    "contenttypes.contenttype": 0,
    "auth.permission": 1,
    "users.user": 2,
    "product.product": 3,
    "product.phone": 4,
    "product.accessory": 4,
    "product.bill": 5,
    "product.billitem": 6,
    "sessions.session": 7,
    "token_blacklist.outstandingtoken": 8,
}

# Default to low priority if not listed
def get_priority(obj):
    return model_priority.get(obj["model"], 100)

# Sort the data
sorted_data = sorted(data, key=get_priority)

# Save reordered data
with open("data.json", "w") as f:
    json.dump(sorted_data, f, indent=2)

print("✅ Reordering complete. Output saved as data_reordered.json")
