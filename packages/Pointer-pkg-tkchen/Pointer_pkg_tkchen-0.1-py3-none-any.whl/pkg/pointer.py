import _pointer
from typing import *

class Pointer(object):
	_p:_pointer=None
	_type:str=str()

	def __new__(cls,obj:Any) -> Self:
		return super(Pointer,cls).__new__(cls)
	
	def __init__(self:Self,obj:Any):
		self._p=_pointer._create(obj)
		if self._p is None: 
			raise MemoryError("Out of Memory!")
		self._type=type(obj).__name__

	def get(self:Self) -> Any:
		return _pointer._get(self._p)

	def address(self:Self) -> str:
		return _pointer._getaddr(self._p)

	def set(self:Self,obj:Any) -> bool:
		return _pointer._set(self._p,obj)
	
	def __eq__(self:Self,other:Any) -> bool:
		if not type(other) == Pointer:
			return False
		return _pointer._get(self._p) is other.get()
	
	def __len__(self:Self) -> int:
		return self._p.__sizeof__()
	
	def __sizeof__(self:Self) -> int:
		return self._p.__sizeof__()
	
	def __nonzero__(self:Self) -> bool:
		if self._p is None:
			return False
		return True

	def __del__(self:Self):
		_pointer._free(self._p)

	def __str__(self:Self) -> str:
		return str("<Pointer Object>")

def sizeof(obj:Pointer) -> int:
	if not type(obj) == Pointer:
		raise TypeError("sizeof can only use by Pointer!")
	return obj.__sizeof__()
