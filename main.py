import os.path
import sys
import shlex
import subprocess
import pathlib


class FileSystem:
    def __init__(self):
        self.pwd = pathlib.Path().resolve()
        self.logfile_path = f"{pathlib.Path().resolve()}/filesystem_data.log"

    def monitor_filesystem(self):
        try:

            command = shlex.split(f'''{self.pwd}/bash/filesystem.sh {self.logfile_path}''')
            res = subprocess.run(command)
            if res.returncode != 0:
                print("*** Error: Failed to run the command to fetch filesystem details ***")
                raise Exception("Command execution failed")
            data = []
            if not os.path.exists(self.logfile_path):
                print("*** Error: The logfile is not present to fetch the filesystem monitoring data ***")
                raise Exception(f"Log file is not present - {self.logfile_path}")

            with open(self.logfile_path) as f:
                data = f.readlines()
            print(data)
            for i in range(1, len(data)):
                filesystem, used, mounted_on = data[i].split(" ")
                print(f'FileSystem:{filesystem}, Used:{used}, MountedOn:{mounted_on}')
        except Exception as e:
            print(f"*** Error: error occurred while fetching filesystem monitoring data: {str(e)} ***")


if __name__ == "__main__":
    obj = FileSystem()
    obj.monitor_filesystem()
