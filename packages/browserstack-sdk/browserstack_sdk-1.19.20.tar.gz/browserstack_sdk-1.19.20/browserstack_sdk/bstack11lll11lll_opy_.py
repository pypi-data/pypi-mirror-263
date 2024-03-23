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
import os
class RobotHandler():
    def __init__(self, args, logger, bstack11ll1llll1_opy_, bstack11ll1ll111_opy_):
        self.args = args
        self.logger = logger
        self.bstack11ll1llll1_opy_ = bstack11ll1llll1_opy_
        self.bstack11ll1ll111_opy_ = bstack11ll1ll111_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack11llll1l1l_opy_(bstack11ll1l1l1l_opy_):
        bstack11ll1l11ll_opy_ = []
        if bstack11ll1l1l1l_opy_:
            tokens = str(os.path.basename(bstack11ll1l1l1l_opy_)).split(bstack111ll11_opy_ (u"ࠦࡤࠨว"))
            camelcase_name = bstack111ll11_opy_ (u"ࠧࠦࠢศ").join(t.title() for t in tokens)
            suite_name, bstack11ll1l1l11_opy_ = os.path.splitext(camelcase_name)
            bstack11ll1l11ll_opy_.append(suite_name)
        return bstack11ll1l11ll_opy_
    @staticmethod
    def bstack11ll1l11l1_opy_(typename):
        if bstack111ll11_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤษ") in typename:
            return bstack111ll11_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣส")
        return bstack111ll11_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤห")