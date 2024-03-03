class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.directories = []

class FileSystem:
    def __init__(self):
        self.root = Directory("root")

    def create_file(self, path, content=""):
        filename = path.split("/")[-1]
        directory_path = "/".join(path.split("/")[:-1])
        parent_dir = self._traverse(directory_path)
        if parent_dir:
            parent_dir.files.append(File(filename, content))
        else:
            print("Invalid directory path.")

    def create_directory(self, path):
        dirname = path.split("/")[-1]
        directory_path = "/".join(path.split("/")[:-1])
        parent_dir = self._traverse(directory_path)
        if parent_dir:
            parent_dir.directories.append(Directory(dirname))
        else:
            print("Invalid directory path.")

    def _traverse(self, path):
        components = path.split("/")
        node = self.root
        for component in components:
            if component:
                found = False
                for directory in node.directories:
                    if directory.name == component:
                        node = directory
                        found = True
                        break
                if not found:
                    return None
        return node

    def ls(self, path="/"):
        node = self._traverse(path)
        if node:
            for directory in node.directories:
                print(directory.name + "/")
            for file in node.files:
                print(file.name)
        else:
            print("Invalid path.")

# Usage example
fs = FileSystem()
fs.create_directory("/docs")
fs.create_file("/docs/note.txt", "This is a note.")
fs.ls("/")  # Output: docs
fs.ls("/docs")  # Output: note.txt
