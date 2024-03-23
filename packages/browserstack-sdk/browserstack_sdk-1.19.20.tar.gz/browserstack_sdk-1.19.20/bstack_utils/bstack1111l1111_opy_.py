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
class bstack1llll1l1_opy_:
    def __init__(self, handler):
        self._1llll1ll1ll_opy_ = None
        self.handler = handler
        self._1llll1lll11_opy_ = self.bstack1llll1llll1_opy_()
        self.patch()
    def patch(self):
        self._1llll1ll1ll_opy_ = self._1llll1lll11_opy_.execute
        self._1llll1lll11_opy_.execute = self.bstack1llll1lll1l_opy_()
    def bstack1llll1lll1l_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack111ll11_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࠣᑮ"), driver_command, None, this, args)
            response = self._1llll1ll1ll_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack111ll11_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࠣᑯ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1llll1lll11_opy_.execute = self._1llll1ll1ll_opy_
    @staticmethod
    def bstack1llll1llll1_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver