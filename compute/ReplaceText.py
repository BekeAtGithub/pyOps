# Define the input file path and the output file path
input_file = 'C:\File\Input\Path'   # Replace with your actual file name 
output_file = 'C:\File\Output\Path' # This will save the modified content to a new file

# Open the input file, read the content, and perform the replacement
with open(input_file, 'r') as file:
    content = file.read()

# Replace all a's with b's
modified_content = content.replace('a', 'b')

# Write the modified content to the output file
with open(output_file, 'w') as file:
    file.write(modified_content)

print(f"All a's have been replaced with b's in '{output_file}'.")
