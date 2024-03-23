from time import sleep
from os import uname


class Filesyncer:
    def __init__(self) -> None:
        self.run()
        return
    
    def run(self):
        sleep(3)
        print(uname()[0])
        return
    