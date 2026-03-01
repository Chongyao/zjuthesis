import json
import os

# Files
COMBINED_FILE = "all_benchmarks_combined.json"
NEW_GT_FILE = "weak-gt_benchmarks.json"

# Output files to restore
RESTORE_FILES = {
    "weak-pd": "weak-pd_benchmarks.json",
    "weak-sp": "weak-sp_benchmarks.json",
    "strong-pd": "strong-pd_benchmarks.json",
    "strong-sp": "strong-sp_benchmarks.json",
    "strong-gt": "strong-gt_benchmarks.json"
    # weak-gt will be handled separately
}

def main():
    # 1. Load the big combined file (Source of Truth for old data)
    print(f"Loading {COMBINED_FILE}...")
    with open(COMBINED_FILE, 'r') as f:
        combined_data = json.load(f)

    # 2. Restore the individual files that were wiped
    for key, filename in RESTORE_FILES.items():
        if key in combined_data:
            print(f"Restoring {filename} ({len(combined_data[key])} items)...")
            with open(filename, 'w') as f:
                json.dump(combined_data[key], f, indent=2)
        else:
            print(f"Warning: Key {key} not found in combined data!")

    # 3. Handle weak-gt (Merge Old + New)
    print("Merging weak-gt data...")
    old_gt_data = combined_data.get("weak-gt", [])
    
    # Load new GT data (contains nx202)
    # Check if NEW_GT_FILE exists and is not empty/broken
    if os.path.exists(NEW_GT_FILE) and os.path.getsize(NEW_GT_FILE) > 10:
        with open(NEW_GT_FILE, 'r') as f:
            new_gt_data = json.load(f)
    else:
        print(f"Warning: {NEW_GT_FILE} is missing or empty. Skipping merge.")
        new_gt_data = []
    
    print(f"Old weak-gt items: {len(old_gt_data)}")
    print(f"New weak-gt items: {len(new_gt_data)}")

    # Merge: Create a map by run_key to avoid duplicates, prioritize new?
    # Actually, new file only has nx202. Old file has everything else.
    # Just append new items that are not in old.
    
    existing_keys = set(item['run_key'] for item in old_gt_data)
    merged_gt_data = list(old_gt_data)
    
    for item in new_gt_data:
        # Check run_key or uniqueness
        rkey = item.get('run_key', '')
        if rkey not in existing_keys:
            print(f"Adding new item: {rkey}")
            merged_gt_data.append(item)
            existing_keys.add(rkey)
        else:
            print(f"Skipping duplicate: {rkey}")
            
    # Save merged weak-gt
    print(f"Saving merged weak-gt_benchmarks.json ({len(merged_gt_data)} items)...")
    with open("weak-gt_benchmarks.json", 'w') as f:
        json.dump(merged_gt_data, f, indent=2)
        
    # 4. Update the combined data structure
    combined_data["weak-gt"] = merged_gt_data
    
    # 5. Save the updated combined file
    print(f"Saving updated {COMBINED_FILE}...")
    with open(COMBINED_FILE, 'w') as f:
        json.dump(combined_data, f, indent=2)

    print("Recovery and Merge Complete!")

if __name__ == "__main__":
    main()
