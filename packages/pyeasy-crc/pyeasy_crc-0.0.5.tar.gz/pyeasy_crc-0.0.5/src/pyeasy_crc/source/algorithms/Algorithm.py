from array import array
from typing import Optional, TypedDict

class Algorithm(TypedDict):
   init: int
   invertedInit: Optional[int]
   xorOut: int
   refOut: bool
   refIn: bool
   table: array
