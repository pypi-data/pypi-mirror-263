# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111l1ll_opy_ = 2048
bstack1lllll1_opy_ = 7
def bstack111ll11_opy_ (bstack1l_opy_):
    global bstack11l1l11_opy_
    bstack1l1ll1_opy_ = ord (bstack1l_opy_ [-1])
    bstack11l1l1_opy_ = bstack1l_opy_ [:-1]
    bstack1l111l1_opy_ = bstack1l1ll1_opy_ % len (bstack11l1l1_opy_)
    bstack1l11ll1_opy_ = bstack11l1l1_opy_ [:bstack1l111l1_opy_] + bstack11l1l1_opy_ [bstack1l111l1_opy_:]
    if bstack111111l_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack111l1ll_opy_ - (bstack1l1_opy_ + bstack1l1ll1_opy_) % bstack1lllll1_opy_) for bstack1l1_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack111l1ll_opy_ - (bstack1l1_opy_ + bstack1l1ll1_opy_) % bstack1lllll1_opy_) for bstack1l1_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack11l1ll_opy_)
from collections import deque
from bstack_utils.constants import *
class bstack1l11l11l_opy_:
    def __init__(self):
        self._1111111l1l_opy_ = deque()
        self._111111l1l1_opy_ = {}
        self._11111111l1_opy_ = False
    def bstack111111111l_opy_(self, test_name, bstack11111111ll_opy_):
        bstack111111l1ll_opy_ = self._111111l1l1_opy_.get(test_name, {})
        return bstack111111l1ll_opy_.get(bstack11111111ll_opy_, 0)
    def bstack111111ll1l_opy_(self, test_name, bstack11111111ll_opy_):
        bstack1111111l11_opy_ = self.bstack111111111l_opy_(test_name, bstack11111111ll_opy_)
        self.bstack111111l11l_opy_(test_name, bstack11111111ll_opy_)
        return bstack1111111l11_opy_
    def bstack111111l11l_opy_(self, test_name, bstack11111111ll_opy_):
        if test_name not in self._111111l1l1_opy_:
            self._111111l1l1_opy_[test_name] = {}
        bstack111111l1ll_opy_ = self._111111l1l1_opy_[test_name]
        bstack1111111l11_opy_ = bstack111111l1ll_opy_.get(bstack11111111ll_opy_, 0)
        bstack111111l1ll_opy_[bstack11111111ll_opy_] = bstack1111111l11_opy_ + 1
    def bstack1l1llll11_opy_(self, bstack111111lll1_opy_, bstack1111111lll_opy_):
        bstack1111111ll1_opy_ = self.bstack111111ll1l_opy_(bstack111111lll1_opy_, bstack1111111lll_opy_)
        bstack1111111111_opy_ = bstack11l1l1l11l_opy_[bstack1111111lll_opy_]
        bstack111111ll11_opy_ = bstack111ll11_opy_ (u"ࠥࡿࢂ࠳ࡻࡾ࠯ࡾࢁࠧᐕ").format(bstack111111lll1_opy_, bstack1111111111_opy_, bstack1111111ll1_opy_)
        self._1111111l1l_opy_.append(bstack111111ll11_opy_)
    def bstack1l1ll11l_opy_(self):
        return len(self._1111111l1l_opy_) == 0
    def bstack1l1ll1111_opy_(self):
        bstack111111l111_opy_ = self._1111111l1l_opy_.popleft()
        return bstack111111l111_opy_
    def capturing(self):
        return self._11111111l1_opy_
    def bstack1lll1l11l_opy_(self):
        self._11111111l1_opy_ = True
    def bstack1l1llll1ll_opy_(self):
        self._11111111l1_opy_ = False