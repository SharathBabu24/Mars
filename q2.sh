#!/bin/bash

# Getting the current date and time
current_date=$(date +"%Y-%m-%d %H:%M:%S")

# Directory where the modified files are located
modified_dir="Modified"

# Going through each file in the directory
for file in "${modified_dir}"/*; do
    # See if it is a file
    if [[ -f "$file" ]]; then
        # Adding the current date and time to the file
        echo -e "\nDate and Time: ${current_date}" >> "$file"
        echo "Appended date and time to file: ${file}"
    fi
done

echo "Date and time appended to all files in the 'Modified' directory."
