import os
import shutil
import datetime
import glob


class Sorting_file():
    def __init__(self, source, aim):
        self.source = source
        self.aim = aim

    def file_path(self):
        symbol = '/**/*.*'
        fileList = glob.glob(self.source + symbol, recursive=True)
        return fileList

    def day_month_year(self):  # Day-Month-Year
        fileList = self.file_path()
        for data in fileList:
            time = datetime.datetime.fromtimestamp(os.stat(data).st_mtime)
            timeinfo = datetime.datetime.strftime(time, '%d.%m.%Y')
            self.sorting_func(data,timeinfo)
        return ("sorting completed")

    def sorting_extension(self):
        fileList = self.file_path()
        for data in fileList:
            index = data.rfind(".")
            extension_type = data[index:]
            filename = f'{extension_type} extension Folder'
            self.sorting_func(data, filename)
        return ("sorting completed")

    def chosen_extension(self):
        fileList = self.file_path()
        extensionList = ["""İnput the extension
                            you want to sort""" ]
        fileName = "chosen extensions"
        for data in fileList:
            result = os.path.split(data)
            type = os.path.splitext(result[1])
            if type in extensionList:
                self.sorting_func(data, fileName)
        return ("sorting completed")

    def sorting_func(self, info1, info2):
        file_directory = self.aim + "\\" + info2
        if os.path.isdir(file_directory):
            shutil.copy(info1, file_directory)
        else:
            os.makedirs(file_directory)
            shutil.copy(info1, file_directory)
