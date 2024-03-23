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
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1ll111lll_opy_ = {}
        bstack1l11l11ll1_opy_ = os.environ.get(bstack111ll11_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫക"), bstack111ll11_opy_ (u"ࠫࠬഖ"))
        if not bstack1l11l11ll1_opy_:
            return bstack1ll111lll_opy_
        try:
            bstack1l11l11lll_opy_ = json.loads(bstack1l11l11ll1_opy_)
            if bstack111ll11_opy_ (u"ࠧࡵࡳࠣഗ") in bstack1l11l11lll_opy_:
                bstack1ll111lll_opy_[bstack111ll11_opy_ (u"ࠨ࡯ࡴࠤഘ")] = bstack1l11l11lll_opy_[bstack111ll11_opy_ (u"ࠢࡰࡵࠥങ")]
            if bstack111ll11_opy_ (u"ࠣࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧച") in bstack1l11l11lll_opy_ or bstack111ll11_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧഛ") in bstack1l11l11lll_opy_:
                bstack1ll111lll_opy_[bstack111ll11_opy_ (u"ࠥࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳࠨജ")] = bstack1l11l11lll_opy_.get(bstack111ll11_opy_ (u"ࠦࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣഝ"), bstack1l11l11lll_opy_.get(bstack111ll11_opy_ (u"ࠧࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠣഞ")))
            if bstack111ll11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࠢട") in bstack1l11l11lll_opy_ or bstack111ll11_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧഠ") in bstack1l11l11lll_opy_:
                bstack1ll111lll_opy_[bstack111ll11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨഡ")] = bstack1l11l11lll_opy_.get(bstack111ll11_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࠥഢ"), bstack1l11l11lll_opy_.get(bstack111ll11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣണ")))
            if bstack111ll11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳࠨത") in bstack1l11l11lll_opy_ or bstack111ll11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨഥ") in bstack1l11l11lll_opy_:
                bstack1ll111lll_opy_[bstack111ll11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢദ")] = bstack1l11l11lll_opy_.get(bstack111ll11_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠤധ"), bstack1l11l11lll_opy_.get(bstack111ll11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤന")))
            if bstack111ll11_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࠤഩ") in bstack1l11l11lll_opy_ or bstack111ll11_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢപ") in bstack1l11l11lll_opy_:
                bstack1ll111lll_opy_[bstack111ll11_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠣഫ")] = bstack1l11l11lll_opy_.get(bstack111ll11_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࠧബ"), bstack1l11l11lll_opy_.get(bstack111ll11_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠥഭ")))
            if bstack111ll11_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠤമ") in bstack1l11l11lll_opy_ or bstack111ll11_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢയ") in bstack1l11l11lll_opy_:
                bstack1ll111lll_opy_[bstack111ll11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣര")] = bstack1l11l11lll_opy_.get(bstack111ll11_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧറ"), bstack1l11l11lll_opy_.get(bstack111ll11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥല")))
            if bstack111ll11_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣള") in bstack1l11l11lll_opy_ or bstack111ll11_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣഴ") in bstack1l11l11lll_opy_:
                bstack1ll111lll_opy_[bstack111ll11_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤവ")] = bstack1l11l11lll_opy_.get(bstack111ll11_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠦശ"), bstack1l11l11lll_opy_.get(bstack111ll11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦഷ")))
            if bstack111ll11_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠧസ") in bstack1l11l11lll_opy_:
                bstack1ll111lll_opy_[bstack111ll11_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨഹ")] = bstack1l11l11lll_opy_[bstack111ll11_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠢഺ")]
        except Exception as error:
            logger.error(bstack111ll11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡦࡹࡷࡸࡥ࡯ࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡡࡵࡣ࠽ࠤ഻ࠧ") +  str(error))
        return bstack1ll111lll_opy_