from easyzip import EasyZip

# Create a zip archive
with EasyZip('example.zip') as ez:
    # Add a single file to the archive
    ez.add_file('file1.txt')
    
    # Add an entire directory and its contents to the archive
    ez.add_directory('my_directory')

# Extract the contents of the zip archive
with EasyZip('example.zip') as ez:
    ez.extract_to('extracted_directory')

print("Zip file created and contents extracted successfully!")
