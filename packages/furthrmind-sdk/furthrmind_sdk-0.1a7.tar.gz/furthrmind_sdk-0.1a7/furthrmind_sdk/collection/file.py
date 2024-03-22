from furthrmind_sdk.collection.baseclass import BaseClass
import os

class File(BaseClass):
    id = ""
    name = ""

    _attr_definition = {
    }

    def __init__(self, id=None, data=None):
        super().__init__(id, data)

    @classmethod
    def get(cls, id=None):
        raise TypeError("Not implemented")

    @classmethod
    def get_all(cls):
        raise TypeError("Not implemented")


    def download(self, folder, overwrite=False):
        """
        Method to download a file
        :param folder: the folder where the file should be saved
        """
        from furthrmind_sdk.file_loader import FileLoader
        fl = FileLoader(self.fm.host, self.fm.api_key)

        if not os.path.isdir(folder):
            raise ValueError("Folder does not exist")
        fl.downloadFile(self.id, folder, overwrite)

    def update_file(self, file_path, file_name=None):
        from furthrmind_sdk.file_loader import FileLoader
        fl = FileLoader(self.fm.host, self.fm.api_key)

        if not os.path.isfile(file_path):
            raise ValueError("File does not exist")

        fl.updateFile(self.id, file_path, file_name)




