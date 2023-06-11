#!/bin/bash

# Get the current date and time
current_date=$(date +"%Y-%m-%d %H:%M:%S")

# Specify the directory where the modified files are located
modified_dir="Modified"

# Iterate over each file in the directory
for file in "${modified_dir}"/*; do
    # Check if the item is a file
    if [[ -f "$file" ]]; then
        # Append the current date and time to the file
        echo -e "\nDate and Time: ${current_date}" >> "$file"
        echo "Appended date and time to file: ${file}"
    fi
done

echo "Date and time appended to all files in the 'Modified' directory."
