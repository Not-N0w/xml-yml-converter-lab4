import time

from nec import *
from ext1 import *
from ext2 import *
from ext3 import *

start_time = time.time()
for _ in range(100):
    xml_to_yaml_base("input.xml", "output.yml")

end_time = time.time()

print("Время выполнения парсинга и конвертации (x100) в обязательном задании: ", end_time - start_time)


start_time = time.time()
for _ in range(100):
    xml_to_yaml_lib("input.xml", "output1.yml")

end_time = time.time()

print("Время выполнения парсинга и конвертации (x100) в дополнительном задании 1: ", end_time - start_time)

start_time = time.time()
for _ in range(100):
    xml_to_yaml_re("input.xml", "output2.yml")

end_time = time.time()

print("Время выполнения парсинга и конвертации (x100) в дополнительном задании 2: ", end_time - start_time)

start_time = time.time()
for _ in range(100):
    xml_to_yaml_rec("input.xml", "output3.yml")

end_time = time.time()

print("Время выполнения парсинга и конвертации (x100) в дополнительном задании 3: ", end_time - start_time)