from abc import ABCMeta, abstractmethod
from typing import Callable, Union
import bisect

class TimeFunc(metaclass=ABCMeta):
    '''时变函数'''
    @abstractmethod
    def __call__(self,time:int)->float: ...
    @abstractmethod
    def __str__(self)->str: ...
    def __add__(self,other:'FloatLike')->'TimeFunc':
        return calcFunc(self,other,'+')
    def __sub__(self,other:'TimeFunc')->'TimeFunc':
        return calcFunc(self,other,'-')
    def __mul__(self,other)->'TimeFunc':
        return calcFunc(self,other,'*')
    def __truediv__(self,other)->'TimeFunc':
        return calcFunc(self,other,'/')

FloatLike = Union[TimeFunc,float]

class PlusFunc(TimeFunc):
    '''和函数'''
    def __init__(self,f1:TimeFunc,f2:TimeFunc): self._f1=f1; self._f2=f2
    def __call__(self,_t:int)->float: return self._f1(_t)+self._f2(_t)
    def __str__(self)->str: return f"<{self._f1}+{self._f2}>"

class MinusFunc(TimeFunc):
    '''差函数'''
    def __init__(self,f1:TimeFunc,f2:TimeFunc): self._f1=f1; self._f2=f2
    def __call__(self,_t:int)->float: return self._f1(_t)-self._f2(_t)
    def __str__(self)->str: return f"<{self._f1}-{self._f2}>"

class MulFunc(TimeFunc):
    '''积函数'''
    def __init__(self,f1:TimeFunc,f2:TimeFunc): self._f1=f1; self._f2=f2
    def __call__(self,_t:int)->float: return self._f1(_t)*self._f2(_t)
    def __str__(self)->str: return f"<{self._f1}*{self._f2}>"

class DivFunc(TimeFunc):
    '''商函数'''
    def __init__(self,f1:TimeFunc,f2:TimeFunc): self._f1=f1; self._f2=f2
    def __call__(self,_t:int)->float: return self._f1(_t)/self._f2(_t)
    def __str__(self)->str: return f"<{self._f1}/{self._f2}>"

class ConstFunc(TimeFunc):
    '''常数函数'''
    def __init__(self,const:float): self._val:float=const
    def __call__(self,time:int)->float: return self._val
    def __str__(self)->str: return f"Const<{self._val}>"

class SegFunc(TimeFunc):
    '''分段常数函数'''
    def __init__(self,time_line:'list[int]',data:'list[float]'):
        if len(time_line) != len(data): raise ValueError(f"时间线长度{len(time_line)}和数据长度{len(data)}不一致")
        for i in range(1,len(time_line)):
            if time_line[i]<=time_line[i-1]:
                raise ValueError(f"时间必须严格递增: [{i}]={time_line[i]}<=[{i-1}]={time_line[i-1]}")
        self._tl = time_line
        self._d = data   
    
    def __call__(self,time:int)->float:
        if time < self._tl[0]: raise ValueError(f"时间{time}必须在开始时间{self._tl[0]}之后")
        return self._d[bisect.bisect_right(self._tl, time) - 1]
    def __str__(self)->str: return f"SegF<{len(self._d)} segs>"

class TimeImplictFunc(TimeFunc):
    '''隐式时变函数, 即调用的时机决定了时间, 而无需在__call__时指定。__call__的参数time无效'''
    def __init__(self,func:'Callable[[],float]'):self._f=func
    def __call__(self,time:int)->float:return self._f()
    def __str__(self)->str:return f"TImpF<{self._f}>"

class ComFunc(TimeFunc):
    '''将普通Python函数包装成可运算函数'''
    def __init__(self,func:'Callable[[int],float]'):self._f=func
    def __call__(self,time:int)->float:return self._f(time)
    def __str__(self)->str:return f"TImpF<{self._f}>"

class ManualFunc(TimeFunc):
    '''手动指定常数函数'''
    def __init__(self,init_val:float):self._v=init_val
    def setManual(self,val:float):self._v=val
    def __call__(self,time:int)->float:return self._v
    def __str__(self)->str:return f"ManF<{self._v}>"

def __calc_c0(f1:Union[ConstFunc,float],f2:float,op:str)->float:
    if isinstance(f1,float):
        if op=='+': return f1+f2
        elif op=='-': return f1-f2
        elif op=='*': return f1*f2
        elif op=='/': return f1/f2
        else: raise ValueError(op)
    elif isinstance(f1,ConstFunc):
        if op=='+': return f1._val+f2
        elif op=='-': return f1._val-f2
        elif op=='*': return f1._val*f2
        elif op=='/': return f1._val/f2
        else: raise ValueError(op)
    else: raise TypeError(f1)

def __calc_c1(f1:SegFunc,f2:float,op:str)->SegFunc:
    if op=='+': return SegFunc(f1._tl,[d+f2 for d in f1._d])
    elif op=='-': return SegFunc(f1._tl,[d-f2 for d in f1._d])
    elif op=='*': return SegFunc(f1._tl,[d*f2 for d in f1._d])
    elif op=='/': return SegFunc(f1._tl,[d/f2 for d in f1._d])
    else: raise ValueError(op)

def __calc_c2(f1:TimeImplictFunc,f2:float,op:str)->TimeImplictFunc:
    if op=='+': return TimeImplictFunc(lambda: f1._f() + f2)
    elif op=='-': return TimeImplictFunc(lambda: f1._f() - f2)
    elif op=='*': return TimeImplictFunc(lambda: f1._f() * f2)
    elif op=='/': return TimeImplictFunc(lambda: f1._f() / f2)
    else: raise ValueError(op)

def calcFunc(f1:FloatLike,f2:FloatLike,op:str)->TimeFunc:
    if isinstance(f2,ConstFunc): f2=f2._val
    if isinstance(f2,float):
        if isinstance(f1,(ConstFunc,float)): return ConstFunc(__calc_c0(f1,f2,op))
        elif isinstance(f1,SegFunc): return __calc_c1(f1,f2,op)
        elif isinstance(f1,TimeImplictFunc): return __calc_c2(f1,f2,op)
    if isinstance(f1,float): f1=ConstFunc(f1)
    if isinstance(f1,ConstFunc) and op in ['+','*']:
        if isinstance(f2,SegFunc): return __calc_c1(f2,f1._val,op)
        elif isinstance(f2,TimeImplictFunc): return __calc_c2(f2,f1._val,op)
    assert isinstance(f1,TimeFunc) and isinstance(f2,TimeFunc)
    if op=='+': return PlusFunc(f1,f2)
    elif op=='-': return MinusFunc(f1,f2)
    elif op=='*': return MulFunc(f1,f2)
    elif op=='/': return DivFunc(f1,f2)
    else: raise ValueError(op)

def makeFunc(time_line:'list[int]',data:list)->TimeFunc:
    '''生成分段常数函数或常数函数'''
    if len(time_line)!=len(data): raise ValueError(f"时间线长度{len(time_line)}和数据长度{len(data)}不一致")
    if len(data)==1: return ConstFunc(data[0])
    else: return SegFunc(time_line,data)
