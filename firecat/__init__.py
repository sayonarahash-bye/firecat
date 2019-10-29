import platform

class firecat:
    """
    Mess files like an cat.
    """
    def __init__(self):
        pass

    def read(self, file):
        """
        param file: the file to be read
        return -> io: the file's content
        """

        with open(file) as fl:
            read = fl.read()
            return read

    def copytextto(self, filesrc, filedest):
        """param filesrc: the original file.
        param filedest: the denstination file.
        return -> bool: returns true if everything is correct,
            else, return the error and false."""

        with open(filesrc) as file:
            readdest = file.read()
        try:
            with open(filedest, mode="a") as file:
                file.write(str(readdest))
            return True
        except Exception as err:
            return err, False

    def touch(self, filename):
        """
        Again, Inspired on Linux's terminal command.
        param filename: the name to the file
        return -> bool: returns true if everything is correct,
            else, return the error and false.
        """
        try:
            with open(filename, mode="w") as file:
                file.write("")
                return True
        except:
            return False

    def apnd(self, filename, content):
        md = None
        try:
            if platform.system() == 'Windows':
                md = "a"
            elif platform.system() == 'Linux':
                md = "x"
            with open(filename, md) as file:
                file.write(str(content))
                return True

        except(FileNotFoundError):
            return False

    def find(self, filename, content):
        """
        Find an content on the file.
        """
        with open(filename) as file:
            readed = file.read()
            if content in readed:
                return True
            else:
                return

    def fndfile(self, dirc, target):
        """Find an file on a directory"""
        from os import listdir
        
        lstdir = listdir(dirc)
        if target in lstdir:
            return True
        else:
            return
                


