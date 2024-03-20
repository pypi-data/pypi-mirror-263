from .Algorithm import Algorithm
from .cdma2000 import CDMA2000
from .ebu import EBU
from .i_code import I_CODE
from .itu import ITU
from .maxim import MAXIM
from .rohc import ROHC
from ..types.AlgorithmKeys import AlgorithmKeys

algorithms: dict[AlgorithmKeys, Algorithm] = {
   'I-CODE': I_CODE,
   'ROHC': ROHC,
   'CDMA2000': CDMA2000,
   'EBU': EBU,
   'ITU': ITU,
   'MAXIM': MAXIM
}
