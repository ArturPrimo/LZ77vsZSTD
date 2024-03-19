import ujson
import zstd
import lz4.block
from random import choice
from random import randint

keys = (
    "Alter", "Bravo", "Count", "Delta", "Enter", "Fetch", "Grade", "Hotel", "India", 
    "Julie", "Kilos", "Lemon", "Menlo", "Night", "Oscar", "Panda", "Quack", "Romeo", 
    "Sound", "Tango", "Unity", "Vitor", "Wooly", "X-ray", "Yanks", "Zebra"
)

data = {}

for i in range(2):
    d = {}
    for k in range(randint(10, 100)):
        d[choice(keys)] = k
    data[str(i)] = d



dataset = ujson.dumps(data).encode()


data = zstd.compress(dataset, 6)
zstd.compress(dataset, 6)
print("Test data has length", len(dataset))
print("Compressed data length for Zstandard is", len(data), ", ratio is", len(dataset) / len(data))

data = lz4.block.compress(dataset)
lz4.block.compress(dataset)
print("Compressed data length for LZ77 is", len(data), ", ratio is", len(dataset) / len(data))