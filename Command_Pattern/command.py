import os

verbose = True

class RenameFile:
    """Class to execute command to rename file"""

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        if verbose:
            print(f'[renaming "{self.src}" to "{self.dest}"]')
        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print(f"[renaming '{self.dest}' back to '{self.src}']")
        os.rename(self.dest, self.src)


class CreateFile:
    """Class to execute command to create a file"""

    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        if verbose:
            print(f"[creating file '{self.path}']")
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile:
    """Class to execute command to read a file"""

    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print(f'[reading file "{self.path}"]')
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')

    
def delete_file(path):
    if verbose:
        print(f'deleting file {path}')
    os.remove(path)


def main():

    original_name, new_name = 'file_1', 'file_2'

    commands = (CreateFile(original_name),
                ReadFile(original_name),
                RenameFile(original_name, new_name))

    [c.execute() for c in commands]

    answer = input('Reverse the executed commands? [y/n] ').lower()

    if answer != 'y':
        print(f'the result is {new_name}')
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            print('Error', str(e))


if __name__ == '__main__':
    main()