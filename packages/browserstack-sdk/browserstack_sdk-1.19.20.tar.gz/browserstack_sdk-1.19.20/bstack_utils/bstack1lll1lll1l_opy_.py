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
from browserstack_sdk.bstack1lll1l111l_opy_ import bstack111111ll1_opy_
from browserstack_sdk.bstack11lll11lll_opy_ import RobotHandler
def bstack1l1l111ll_opy_(framework):
    if framework.lower() == bstack111ll11_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᅺ"):
        return bstack111111ll1_opy_.version()
    elif framework.lower() == bstack111ll11_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨᅻ"):
        return RobotHandler.version()
    elif framework.lower() == bstack111ll11_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪᅼ"):
        import behave
        return behave.__version__
    else:
        return bstack111ll11_opy_ (u"ࠫࡺࡴ࡫࡯ࡱࡺࡲࠬᅽ")