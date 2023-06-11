#!/bin/bash

# Take the current working directory as input
current_dir="$(pwd)"

# Create a new directory called "Modified"
modified_dir="${current_dir}/Modified"
mkdir -p "$modified_dir"

# Recursively search for files with a ".txt" extension
find "$current_dir" -type f -name "*.txt" -print0 | while IFS= read -r -d '' file; do
    # Get the file name without the extension
    filename=$(basename "$file")
    filename_no_ext="${filename%.*}"

    # Create the new file name with the ".bak" extension
    new_filename="${filename_no_ext}.bak"

    # Copy the file to the "Modified" directory with the new file name
    cp "$file" "${modified_dir}/${new_filename}"
done

echo "Files with '.txt' extension have been copied to the 'Modified' directory with '.bak' extension."
