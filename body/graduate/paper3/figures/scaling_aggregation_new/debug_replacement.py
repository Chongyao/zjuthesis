import json
import os

REPLACEMENT_FILE = "replacement.txt"
JSON_FILE = "strong-pd_benchmarks.json"

def parse_replacement_file(filename):
    replacements = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'): continue
            parts = line.split(',')
            if len(parts) == 2:
                replacements.append((parts[0].strip(), parts[1].strip()))
    return replacements

def main():
    if not os.path.exists(REPLACEMENT_FILE):
        print("Replacement file not found!")
        return
        
    replacements = parse_replacement_file(REPLACEMENT_FILE)
    print("Replacements:", replacements)
    
    with open(JSON_FILE, 'r') as f:
        data = json.load(f)
        
    # Check first item
    if not data:
        print("No data")
        return
        
    item = data[0]
    steps = item.get('steps', {})
    print("\nOriginal Keys (Sample):", list(steps.keys()))
    
    # Apply logic
    sorted_map = sorted(replacements, key=lambda x: len(x[0]), reverse=True)
    new_keys = []
    
    print("\nTransformation Check:")
    for old_step_name in steps.keys():
        new_step_name = old_step_name
        for old_prefix, new_prefix in sorted_map:
            if new_step_name.startswith(old_prefix):
                new_step_name = new_step_name.replace(old_prefix, new_prefix, 1)
                print(f"  '{old_step_name}' -> '{new_step_name}' (via '{old_prefix}')")
                break
        new_keys.append(new_step_name)
        
    print("\nNew Keys (Sample):", new_keys)

if __name__ == "__main__":
    main()
