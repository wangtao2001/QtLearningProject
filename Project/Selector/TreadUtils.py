from PyQt5.QtCore import QThread, pyqtSignal


class NoFileException(ValueError):
    pass


class WriteThread(QThread):
    finishSignal = pyqtSignal()

    def __init__(self, li):
        super().__init__()
        self.li = li

    def run(self):
        """
        子线程执行内容
        :return:
        """
        with open("data.txt", "w") as f:
            f.write(" ".join([str(i) for i in self.li]))
        self.finishSignal.emit()


class ReadThread(QThread):
    finishSignal = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        try:
            with open("data.txt", "r") as f:
                nums = list(map(int, f.readline().split()))
            self.finishSignal.emit(nums)
        except IOError:
            raise NoFileException("文件不存在")
