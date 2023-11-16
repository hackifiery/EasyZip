import zipfile
import os

class EasyZip:
    def __init__(self, zip_filename, mode='w'):
        """
        Constructor for EasyZip class.

        Args:
            zip_filename (str): The name of the zip file to create.
        """
        self.zip_filename = filename
        self.zip_filename = zip_filename
        self.zip_file = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)
    def __enter__(self):
        self.zipfile = zipfile.ZipFile(self.filename, self.mode)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.zipfile:
            self.zipfile.close()

    def add_file(self, file_path, arcname=None):
        """
        Add a file to the zip archive.

        Args:
            file_path (str): The path to the file to be added.
            arcname (str, optional): The name of the file in the archive. 
                If not provided, the base name of the file is used.
        """
        if not arcname:
            arcname = os.path.basename(file_path)
        self.zip_file.write(file_path, arcname)

    def add_directory(self, directory_path):
        """
        Add all files within a directory and its subdirectories to the zip archive.

        Args:
            directory_path (str): The path to the directory to be added.
        """
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory_path)
                self.add_file(file_path, arcname)

    def close(self):
        """
        Close the zip file. Use this method when you're finished with the zip archive.
        """
        self.zip_file.close()

    def extract_to(self, extract_path):
        """
        Extract the contents of the zip archive to a specified directory.

        Args:
            extract_path (str): The path where the archive contents will be extracted.
        """
        with zipfile.ZipFile(self.zip_filename, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

if __name__ == "__main__":
    # Example usage
    with EasyZip('example.zip') as ez:
        ez.add_file('file1.txt')
        ez.add_directory('my_directory')

    with EasyZip('example.zip') as ez:
        ez.extract_to('extracted_directory')
