import zipfile
import os

class EasyZip:
    def __init__(self, filename, mode='w'):
        self.filename = filename
        self.mode = mode
        self.zipfile = None

    def __enter__(self):
        self.zipfile = zipfile.ZipFile(self.filename, self.mode)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.zipfile:
            self.zipfile.close()

    def add_file(self, file_path):
        if self.zipfile:
            self.zipfile.write(file_path, os.path.basename(file_path))


    def add_directory(self, directory_path):
        if self.zipfile:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, directory_path)
                    self.zipfile.write(file_path, arcname)


    def close(self):
        """
        Close the zip file. Use this method when you're finished with the zip archive.
        """
        self.zip_file.close()

    def extract_to(self, extract_path):
        if self.zipfile:
            self.zipfile.extractall(extract_path)
if __name__ == "__main__":
    # Example usage
    with EasyZip('example.zip') as ez:
        ez.add_file('file1.txt')
        ez.add_directory('my_directory')

    with EasyZip('example.zip') as ez:
        ez.extract_to('extracted_directory')
