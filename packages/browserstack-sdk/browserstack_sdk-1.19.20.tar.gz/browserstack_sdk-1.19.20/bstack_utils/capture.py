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
import sys
class bstack11llll1l11_opy_:
    def __init__(self, handler):
        self._11l1l1llll_opy_ = sys.stdout.write
        self._11l1l1ll11_opy_ = sys.stderr.write
        self.handler = handler
        self._started = False
    def start(self):
        if self._started:
            return
        self._started = True
        sys.stdout.write = self.bstack11l1l1lll1_opy_
        sys.stdout.error = self.bstack11l1l1ll1l_opy_
    def bstack11l1l1lll1_opy_(self, _str):
        self._11l1l1llll_opy_(_str)
        if self.handler:
            self.handler({bstack111ll11_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭໠"): bstack111ll11_opy_ (u"ࠨࡋࡑࡊࡔ࠭໡"), bstack111ll11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ໢"): _str})
    def bstack11l1l1ll1l_opy_(self, _str):
        self._11l1l1ll11_opy_(_str)
        if self.handler:
            self.handler({bstack111ll11_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ໣"): bstack111ll11_opy_ (u"ࠫࡊࡘࡒࡐࡔࠪ໤"), bstack111ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭໥"): _str})
    def reset(self):
        if not self._started:
            return
        self._started = False
        sys.stdout.write = self._11l1l1llll_opy_
        sys.stderr.write = self._11l1l1ll11_opy_