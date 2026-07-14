import os
import json

# useful functions 
def add_array_in_json(filename):
    try:
        # If file doesn't exist, create it with []
        if not os.path.exists(filename):
            with open(filename, "w") as file:
                json.dump([], file, indent=4)
            return "File created"

        # If file exists
        with open(filename, "r") as file:
            content = file.read().strip()

        # Empty file
        if content == "":
            with open(filename, "w") as file:
                json.dump([], file, indent=4)
            return "Empty file fixed"

        # Try reading JSON
        try:
            data = json.loads(content)

            # Keep only if it's a list
            if isinstance(data, list):
                return "File is valid"

            # Anything else (object, number, string, etc.)
            with open(filename, "w") as file:
                json.dump([], file, indent=4)
            return "Invalid JSON type fixed"

        except json.JSONDecodeError:
            # Invalid JSON ("trash")
            with open(filename, "w") as file:
                json.dump([], file, indent=4)
            return "Corrupted JSON fixed"

    except Exception as e:
        return f"Error: {e}"


def dump_in_json(filename,object): 
    with open(filename, "r") as f:
        data = json.load(f)

    # Add the new object
    data.append(object)

    # Write the updated list back
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
