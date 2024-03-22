from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.presentation.common import *
from spire.presentation import *
from ctypes import *
import abc

class ISmartArt (SpireObject) :
    """

    """
    @property

    def Nodes(self)->'ISmartArtNodeCollection':
        """

        """
        GetDllLibPpt().ISmartArt_get_Nodes.argtypes=[c_void_p]
        GetDllLibPpt().ISmartArt_get_Nodes.restype=c_void_p
        intPtr = CallCFunction(GetDllLibPpt().ISmartArt_get_Nodes,self.Ptr)
        ret = None if intPtr==None else ISmartArtNodeCollection(intPtr)
        return ret


    @property

    def ColorStyle(self)->'SmartArtColorType':
        """

        """
        GetDllLibPpt().ISmartArt_get_ColorStyle.argtypes=[c_void_p]
        GetDllLibPpt().ISmartArt_get_ColorStyle.restype=c_int
        ret = CallCFunction(GetDllLibPpt().ISmartArt_get_ColorStyle,self.Ptr)
        objwraped = SmartArtColorType(ret)
        return objwraped

    @ColorStyle.setter
    def ColorStyle(self, value:'SmartArtColorType'):
        GetDllLibPpt().ISmartArt_set_ColorStyle.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibPpt().ISmartArt_set_ColorStyle,self.Ptr, value.value)

    @property

    def LayoutType(self)->'SmartArtLayoutType':
        """

        """
        GetDllLibPpt().ISmartArt_get_LayoutType.argtypes=[c_void_p]
        GetDllLibPpt().ISmartArt_get_LayoutType.restype=c_int
        ret = CallCFunction(GetDllLibPpt().ISmartArt_get_LayoutType,self.Ptr)
        objwraped = SmartArtLayoutType(ret)
        return objwraped

    @property

    def Style(self)->'SmartArtStyleType':
        """

        """
        GetDllLibPpt().ISmartArt_get_Style.argtypes=[c_void_p]
        GetDllLibPpt().ISmartArt_get_Style.restype=c_int
        ret = CallCFunction(GetDllLibPpt().ISmartArt_get_Style,self.Ptr)
        objwraped = SmartArtStyleType(ret)
        return objwraped

    @Style.setter
    def Style(self, value:'SmartArtStyleType'):
        GetDllLibPpt().ISmartArt_set_Style.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibPpt().ISmartArt_set_Style,self.Ptr, value.value)

    def Reset(self):
        """

        """
        GetDllLibPpt().ISmartArt_Reset.argtypes=[c_void_p]
        CallCFunction(GetDllLibPpt().ISmartArt_Reset,self.Ptr)

