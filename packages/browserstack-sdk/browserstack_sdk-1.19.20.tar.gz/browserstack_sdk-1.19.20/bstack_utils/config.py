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
conf = {
    bstack111ll11_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ໦"): False,
    bstack111ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ໧"): True,
    bstack111ll11_opy_ (u"ࠨࡵ࡮࡭ࡵࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡴࡶࡤࡸࡺࡹࠧ໨"): False
}
class Config(object):
    instance = None
    def __init__(self):
        self._11l1l1l1ll_opy_ = conf
    @classmethod
    def bstack1lll111ll_opy_(cls):
        if cls.instance:
            return cls.instance
        return Config()
    def get_property(self, property_name):
        return self._11l1l1l1ll_opy_.get(property_name, None)
    def bstack1lll11llll_opy_(self, property_name, bstack11l1l1l1l1_opy_):
        self._11l1l1l1ll_opy_[property_name] = bstack11l1l1l1l1_opy_
    def bstack1111l111_opy_(self, val):
        self._11l1l1l1ll_opy_[bstack111ll11_opy_ (u"ࠩࡶ࡯࡮ࡶ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡵࡷࡥࡹࡻࡳࠨ໩")] = bool(val)
    def bstack11ll1l1ll1_opy_(self):
        return self._11l1l1l1ll_opy_.get(bstack111ll11_opy_ (u"ࠪࡷࡰ࡯ࡰࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡶࡸࡦࡺࡵࡴࠩ໪"), False)