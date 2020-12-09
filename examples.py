# import os, platform, logging
# if platform.platform().startswith('Windows'):
#     logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
# else:
#     logging_file = os.path.join(os.getenv('HOME'), 'test.log')
#     print("Сохраняем лог в", logging_file)
#
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s', filename = logging_file, filemode = 'w',)
# logging.debug("Начало программы")
# logging.info("Какие-то действия")
# logging.warning("Программа умирает")

class RepeaterIterator:
    def __init__(self, source):
        self.source = source
    def __next__(self):
        return self.source.value

class Repeater:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return RepeaterIterator(self)


repeater = Repeater('Hello')
print(repeater)
for item in repeater:
    print(item)
