from typing import Union
from .algorithms.Algorithms import algorithms
from .types.AlgorithmKeys import AlgorithmKeys

def crc8(algorithm: AlgorithmKeys, data: Union[str, bytes]):
    if isinstance(data, str):
        data = data.encode()
    init = algorithms[algorithm]["init"]
    xor_out = algorithms[algorithm]["xorOut"]
    table = algorithms[algorithm]["table"]
    crc = init
    for byte in data:
        crc = table[crc ^ byte]
    return crc ^ xor_out & 0xFF
