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
import datetime
import json
import logging
import os
import threading
from bstack_utils.helper import bstack11ll111l11_opy_, bstack1lll1l1lll_opy_, get_host_info, bstack11ll11l1l1_opy_, bstack11l1llllll_opy_, bstack11l1111lll_opy_, \
    bstack11l11l1111_opy_, bstack111ll1l1ll_opy_, bstack1ll11111l1_opy_, bstack11l11l11ll_opy_, bstack1lll1lll1_opy_, bstack11lllll111_opy_
from bstack_utils.bstack1lllll11l1l_opy_ import bstack1lllll111ll_opy_
from bstack_utils.bstack1l11111l11_opy_ import bstack11lll1ll1l_opy_
import bstack_utils.bstack111ll111_opy_ as bstack1llll1lll1_opy_
from bstack_utils.constants import bstack11l1l111l1_opy_
bstack1lll1lll1ll_opy_ = [
    bstack111ll11_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩᓢ"), bstack111ll11_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪᓣ"), bstack111ll11_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᓤ"), bstack111ll11_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᓥ"),
    bstack111ll11_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᓦ"), bstack111ll11_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᓧ"), bstack111ll11_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᓨ")
]
bstack1llll11111l_opy_ = bstack111ll11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡣࡰ࡮࡯ࡩࡨࡺ࡯ࡳ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬᓩ")
logger = logging.getLogger(__name__)
class bstack11l1ll1l_opy_:
    bstack1lllll11l1l_opy_ = None
    bs_config = None
    @classmethod
    @bstack11lllll111_opy_(class_method=True)
    def launch(cls, bs_config, bstack1lll1ll111l_opy_):
        cls.bs_config = bs_config
        cls.bstack1lll1lll111_opy_()
        bstack11ll11lll1_opy_ = bstack11ll11l1l1_opy_(bs_config)
        bstack11ll11llll_opy_ = bstack11l1llllll_opy_(bs_config)
        bstack1l1l111l_opy_ = False
        bstack1ll11ll1_opy_ = False
        if bstack111ll11_opy_ (u"࠭ࡡࡱࡲࠪᓪ") in bs_config:
            bstack1l1l111l_opy_ = True
        else:
            bstack1ll11ll1_opy_ = True
        bstack1l1l1l1ll_opy_ = {
            bstack111ll11_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᓫ"): cls.bstack11111l111_opy_() and cls.bstack1lll1lll11l_opy_(bstack1lll1ll111l_opy_.get(bstack111ll11_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩᓬ"), bstack111ll11_opy_ (u"ࠩࠪᓭ"))),
            bstack111ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᓮ"): bstack1llll1lll1_opy_.bstack1ll1111l1_opy_(bs_config),
            bstack111ll11_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪᓯ"): bs_config.get(bstack111ll11_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫᓰ"), False),
            bstack111ll11_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨᓱ"): bstack1ll11ll1_opy_,
            bstack111ll11_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ᓲ"): bstack1l1l111l_opy_
        }
        data = {
            bstack111ll11_opy_ (u"ࠨࡨࡲࡶࡲࡧࡴࠨᓳ"): bstack111ll11_opy_ (u"ࠩ࡭ࡷࡴࡴࠧᓴ"),
            bstack111ll11_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡣࡳࡧ࡭ࡦࠩᓵ"): bs_config.get(bstack111ll11_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᓶ"), bstack111ll11_opy_ (u"ࠬ࠭ᓷ")),
            bstack111ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᓸ"): bs_config.get(bstack111ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᓹ"), os.path.basename(os.path.abspath(os.getcwd()))),
            bstack111ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᓺ"): bs_config.get(bstack111ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᓻ")),
            bstack111ll11_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨᓼ"): bs_config.get(bstack111ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡇࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧᓽ"), bstack111ll11_opy_ (u"ࠬ࠭ᓾ")),
            bstack111ll11_opy_ (u"࠭ࡳࡵࡣࡵࡸࡤࡺࡩ࡮ࡧࠪᓿ"): datetime.datetime.now().isoformat(),
            bstack111ll11_opy_ (u"ࠧࡵࡣࡪࡷࠬᔀ"): bstack11l1111lll_opy_(bs_config),
            bstack111ll11_opy_ (u"ࠨࡪࡲࡷࡹࡥࡩ࡯ࡨࡲࠫᔁ"): get_host_info(),
            bstack111ll11_opy_ (u"ࠩࡦ࡭ࡤ࡯࡮ࡧࡱࠪᔂ"): bstack1lll1l1lll_opy_(),
            bstack111ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡵࡹࡳࡥࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᔃ"): os.environ.get(bstack111ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪᔄ")),
            bstack111ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࡣࡷ࡫ࡲࡶࡰࠪᔅ"): os.environ.get(bstack111ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠫᔆ"), False),
            bstack111ll11_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࡠࡥࡲࡲࡹࡸ࡯࡭ࠩᔇ"): bstack11ll111l11_opy_(),
            bstack111ll11_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭ᔈ"): bstack1l1l1l1ll_opy_,
            bstack111ll11_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡡࡹࡩࡷࡹࡩࡰࡰࠪᔉ"): {
                bstack111ll11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡔࡡ࡮ࡧࠪᔊ"): bstack1lll1ll111l_opy_.get(bstack111ll11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࠬᔋ"), bstack111ll11_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸࠬᔌ")),
                bstack111ll11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩᔍ"): bstack1lll1ll111l_opy_.get(bstack111ll11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫᔎ")),
                bstack111ll11_opy_ (u"ࠨࡵࡧ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬᔏ"): bstack1lll1ll111l_opy_.get(bstack111ll11_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᔐ"))
            }
        }
        config = {
            bstack111ll11_opy_ (u"ࠪࡥࡺࡺࡨࠨᔑ"): (bstack11ll11lll1_opy_, bstack11ll11llll_opy_),
            bstack111ll11_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬᔒ"): cls.default_headers()
        }
        response = bstack1ll11111l1_opy_(bstack111ll11_opy_ (u"ࠬࡖࡏࡔࡖࠪᔓ"), cls.request_url(bstack111ll11_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡶ࡫࡯ࡨࡸ࠭ᔔ")), data, config)
        if response.status_code != 200:
            os.environ[bstack111ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᔕ")] = bstack111ll11_opy_ (u"ࠨࡰࡸࡰࡱ࠭ᔖ")
            os.environ[bstack111ll11_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡉࡏࡎࡒࡏࡉ࡙ࡋࡄࠨᔗ")] = bstack111ll11_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩᔘ")
            os.environ[bstack111ll11_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬᔙ")] = bstack111ll11_opy_ (u"ࠬࡴࡵ࡭࡮ࠪᔚ")
            os.environ[bstack111ll11_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬᔛ")] = bstack111ll11_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᔜ")
            os.environ[bstack111ll11_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩᔝ")] = bstack111ll11_opy_ (u"ࠤࡱࡹࡱࡲࠢᔞ")
            bstack1lll1ll1lll_opy_ = response.json()
            if bstack1lll1ll1lll_opy_ and bstack1lll1ll1lll_opy_[bstack111ll11_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᔟ")]:
                error_message = bstack1lll1ll1lll_opy_[bstack111ll11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᔠ")]
                if bstack1lll1ll1lll_opy_[bstack111ll11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡘࡾࡶࡥࠨᔡ")] == bstack111ll11_opy_ (u"࠭ࡅࡓࡔࡒࡖࡤࡏࡎࡗࡃࡏࡍࡉࡥࡃࡓࡇࡇࡉࡓ࡚ࡉࡂࡎࡖࠫᔢ"):
                    logger.error(error_message)
                elif bstack1lll1ll1lll_opy_[bstack111ll11_opy_ (u"ࠧࡦࡴࡵࡳࡷ࡚ࡹࡱࡧࠪᔣ")] == bstack111ll11_opy_ (u"ࠨࡇࡕࡖࡔࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡅࡇࡑࡍࡊࡊࠧᔤ"):
                    logger.info(error_message)
                elif bstack1lll1ll1lll_opy_[bstack111ll11_opy_ (u"ࠩࡨࡶࡷࡵࡲࡕࡻࡳࡩࠬᔥ")] == bstack111ll11_opy_ (u"ࠪࡉࡗࡘࡏࡓࡡࡖࡈࡐࡥࡄࡆࡒࡕࡉࡈࡇࡔࡆࡆࠪᔦ"):
                    logger.error(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack111ll11_opy_ (u"ࠦࡉࡧࡴࡢࠢࡸࡴࡱࡵࡡࡥࠢࡷࡳࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤ࡙࡫ࡳࡵࠢࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠢࡩࡥ࡮ࡲࡥࡥࠢࡧࡹࡪࠦࡴࡰࠢࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷࠨᔧ"))
            return [None, None, None]
        bstack1lll1ll1lll_opy_ = response.json()
        os.environ[bstack111ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᔨ")] = bstack1lll1ll1lll_opy_[bstack111ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨᔩ")]
        if cls.bstack11111l111_opy_() is True and cls.bstack1lll1lll11l_opy_(bstack1lll1ll111l_opy_.get(bstack111ll11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨᔪ"), bstack111ll11_opy_ (u"ࠨࠩᔫ"))):
            logger.debug(bstack111ll11_opy_ (u"ࠩࡗࡩࡸࡺࠠࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠠࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠦ࠭ᔬ"))
            os.environ[bstack111ll11_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡃࡐࡏࡓࡐࡊ࡚ࡅࡅࠩᔭ")] = bstack111ll11_opy_ (u"ࠫࡹࡸࡵࡦࠩᔮ")
            if bstack1lll1ll1lll_opy_.get(bstack111ll11_opy_ (u"ࠬࡰࡷࡵࠩᔯ")):
                os.environ[bstack111ll11_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧᔰ")] = bstack1lll1ll1lll_opy_[bstack111ll11_opy_ (u"ࠧ࡫ࡹࡷࠫᔱ")]
                os.environ[bstack111ll11_opy_ (u"ࠨࡅࡕࡉࡉࡋࡎࡕࡋࡄࡐࡘࡥࡆࡐࡔࡢࡇࡗࡇࡓࡉࡡࡕࡉࡕࡕࡒࡕࡋࡑࡋࠬᔲ")] = json.dumps({
                    bstack111ll11_opy_ (u"ࠩࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫᔳ"): bstack11ll11lll1_opy_,
                    bstack111ll11_opy_ (u"ࠪࡴࡦࡹࡳࡸࡱࡵࡨࠬᔴ"): bstack11ll11llll_opy_
                })
            if bstack1lll1ll1lll_opy_.get(bstack111ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᔵ")):
                os.environ[bstack111ll11_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫᔶ")] = bstack1lll1ll1lll_opy_[bstack111ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨᔷ")]
            if bstack1lll1ll1lll_opy_.get(bstack111ll11_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫᔸ")):
                os.environ[bstack111ll11_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩᔹ")] = str(bstack1lll1ll1lll_opy_[bstack111ll11_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭ᔺ")])
        return [bstack1lll1ll1lll_opy_[bstack111ll11_opy_ (u"ࠪ࡮ࡼࡺࠧᔻ")], bstack1lll1ll1lll_opy_[bstack111ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᔼ")], bstack1lll1ll1lll_opy_[bstack111ll11_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩᔽ")]]
    @classmethod
    @bstack11lllll111_opy_(class_method=True)
    def stop(cls):
        if not cls.on():
            return
        if os.environ[bstack111ll11_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧᔾ")] == bstack111ll11_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᔿ") or os.environ[bstack111ll11_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᕀ")] == bstack111ll11_opy_ (u"ࠤࡱࡹࡱࡲࠢᕁ"):
            print(bstack111ll11_opy_ (u"ࠪࡉ࡝ࡉࡅࡑࡖࡌࡓࡓࠦࡉࡏࠢࡶࡸࡴࡶࡂࡶ࡫࡯ࡨ࡚ࡶࡳࡵࡴࡨࡥࡲࠦࡒࡆࡓࡘࡉࡘ࡚ࠠࡕࡑࠣࡘࡊ࡙ࡔࠡࡑࡅࡗࡊࡘࡖࡂࡄࡌࡐࡎ࡚࡙ࠡ࠼ࠣࡑ࡮ࡹࡳࡪࡰࡪࠤࡦࡻࡴࡩࡧࡱࡸ࡮ࡩࡡࡵ࡫ࡲࡲࠥࡺ࡯࡬ࡧࡱࠫᕂ"))
            return {
                bstack111ll11_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᕃ"): bstack111ll11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᕄ"),
                bstack111ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᕅ"): bstack111ll11_opy_ (u"ࠧࡕࡱ࡮ࡩࡳ࠵ࡢࡶ࡫࡯ࡨࡎࡊࠠࡪࡵࠣࡹࡳࡪࡥࡧ࡫ࡱࡩࡩ࠲ࠠࡣࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡ࡯࡬࡫࡭ࡺࠠࡩࡣࡹࡩࠥ࡬ࡡࡪ࡮ࡨࡨࠬᕆ")
            }
        else:
            cls.bstack1lllll11l1l_opy_.shutdown()
            data = {
                bstack111ll11_opy_ (u"ࠨࡵࡷࡳࡵࡥࡴࡪ࡯ࡨࠫᕇ"): datetime.datetime.now().isoformat()
            }
            config = {
                bstack111ll11_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪᕈ"): cls.default_headers()
            }
            bstack111lll1111_opy_ = bstack111ll11_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂ࠵ࡳࡵࡱࡳࠫᕉ").format(os.environ[bstack111ll11_opy_ (u"ࠦࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠥᕊ")])
            bstack1lll1lll1l1_opy_ = cls.request_url(bstack111lll1111_opy_)
            response = bstack1ll11111l1_opy_(bstack111ll11_opy_ (u"ࠬࡖࡕࡕࠩᕋ"), bstack1lll1lll1l1_opy_, data, config)
            if not response.ok:
                raise Exception(bstack111ll11_opy_ (u"ࠨࡓࡵࡱࡳࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡴ࡯ࡵࠢࡲ࡯ࠧᕌ"))
    @classmethod
    def bstack1l111ll1ll_opy_(cls):
        if cls.bstack1lllll11l1l_opy_ is None:
            return
        cls.bstack1lllll11l1l_opy_.shutdown()
    @classmethod
    def bstack1l111l1ll_opy_(cls):
        if cls.on():
            print(
                bstack111ll11_opy_ (u"ࠧࡗ࡫ࡶ࡭ࡹࠦࡨࡵࡶࡳࡷ࠿࠵࠯ࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠦࡴࡰࠢࡹ࡭ࡪࡽࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡲࡲࡶࡹ࠲ࠠࡪࡰࡶ࡭࡬࡮ࡴࡴ࠮ࠣࡥࡳࡪࠠ࡮ࡣࡱࡽࠥࡳ࡯ࡳࡧࠣࡨࡪࡨࡵࡨࡩ࡬ࡲ࡬ࠦࡩ࡯ࡨࡲࡶࡲࡧࡴࡪࡱࡱࠤࡦࡲ࡬ࠡࡣࡷࠤࡴࡴࡥࠡࡲ࡯ࡥࡨ࡫ࠡ࡝ࡰࠪᕍ").format(os.environ[bstack111ll11_opy_ (u"ࠣࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠢᕎ")]))
    @classmethod
    def bstack1lll1lll111_opy_(cls):
        if cls.bstack1lllll11l1l_opy_ is not None:
            return
        cls.bstack1lllll11l1l_opy_ = bstack1lllll111ll_opy_(cls.bstack1lll1ll1111_opy_)
        cls.bstack1lllll11l1l_opy_.start()
    @classmethod
    def bstack11llllll1l_opy_(cls, bstack1l111l11l1_opy_, bstack1lll1ll1l11_opy_=bstack111ll11_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨᕏ")):
        if not cls.on():
            return
        bstack11ll11l11_opy_ = bstack1l111l11l1_opy_[bstack111ll11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧᕐ")]
        bstack1lll1llll11_opy_ = {
            bstack111ll11_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᕑ"): bstack111ll11_opy_ (u"࡚ࠬࡥࡴࡶࡢࡗࡹࡧࡲࡵࡡࡘࡴࡱࡵࡡࡥࠩᕒ"),
            bstack111ll11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᕓ"): bstack111ll11_opy_ (u"ࠧࡕࡧࡶࡸࡤࡋ࡮ࡥࡡࡘࡴࡱࡵࡡࡥࠩᕔ"),
            bstack111ll11_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᕕ"): bstack111ll11_opy_ (u"ࠩࡗࡩࡸࡺ࡟ࡔ࡭࡬ࡴࡵ࡫ࡤࡠࡗࡳࡰࡴࡧࡤࠨᕖ"),
            bstack111ll11_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧᕗ"): bstack111ll11_opy_ (u"ࠫࡑࡵࡧࡠࡗࡳࡰࡴࡧࡤࠨᕘ"),
            bstack111ll11_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᕙ"): bstack111ll11_opy_ (u"࠭ࡈࡰࡱ࡮ࡣࡘࡺࡡࡳࡶࡢ࡙ࡵࡲ࡯ࡢࡦࠪᕚ"),
            bstack111ll11_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᕛ"): bstack111ll11_opy_ (u"ࠨࡊࡲࡳࡰࡥࡅ࡯ࡦࡢ࡙ࡵࡲ࡯ࡢࡦࠪᕜ"),
            bstack111ll11_opy_ (u"ࠩࡆࡆ࡙࡙ࡥࡴࡵ࡬ࡳࡳࡉࡲࡦࡣࡷࡩࡩ࠭ᕝ"): bstack111ll11_opy_ (u"ࠪࡇࡇ࡚࡟ࡖࡲ࡯ࡳࡦࡪࠧᕞ")
        }.get(bstack11ll11l11_opy_)
        if bstack1lll1ll1l11_opy_ == bstack111ll11_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪᕟ"):
            cls.bstack1lll1lll111_opy_()
            cls.bstack1lllll11l1l_opy_.add(bstack1l111l11l1_opy_)
        elif bstack1lll1ll1l11_opy_ == bstack111ll11_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪᕠ"):
            cls.bstack1lll1ll1111_opy_([bstack1l111l11l1_opy_], bstack1lll1ll1l11_opy_)
    @classmethod
    @bstack11lllll111_opy_(class_method=True)
    def bstack1lll1ll1111_opy_(cls, bstack1l111l11l1_opy_, bstack1lll1ll1l11_opy_=bstack111ll11_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡢࡶࡦ࡬ࠬᕡ")):
        config = {
            bstack111ll11_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᕢ"): cls.default_headers()
        }
        response = bstack1ll11111l1_opy_(bstack111ll11_opy_ (u"ࠨࡒࡒࡗ࡙࠭ᕣ"), cls.request_url(bstack1lll1ll1l11_opy_), bstack1l111l11l1_opy_, config)
        bstack11l1ll1lll_opy_ = response.json()
    @classmethod
    @bstack11lllll111_opy_(class_method=True)
    def bstack1l1lll11ll_opy_(cls, bstack1l111l1l11_opy_):
        bstack1lll1ll11l1_opy_ = []
        for log in bstack1l111l1l11_opy_:
            bstack1llll1111l1_opy_ = {
                bstack111ll11_opy_ (u"ࠩ࡮࡭ࡳࡪࠧᕤ"): bstack111ll11_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡎࡒࡋࠬᕥ"),
                bstack111ll11_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᕦ"): log[bstack111ll11_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᕧ")],
                bstack111ll11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᕨ"): log[bstack111ll11_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᕩ")],
                bstack111ll11_opy_ (u"ࠨࡪࡷࡸࡵࡥࡲࡦࡵࡳࡳࡳࡹࡥࠨᕪ"): {},
                bstack111ll11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᕫ"): log[bstack111ll11_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᕬ")],
            }
            if bstack111ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᕭ") in log:
                bstack1llll1111l1_opy_[bstack111ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᕮ")] = log[bstack111ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᕯ")]
            elif bstack111ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᕰ") in log:
                bstack1llll1111l1_opy_[bstack111ll11_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᕱ")] = log[bstack111ll11_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᕲ")]
            bstack1lll1ll11l1_opy_.append(bstack1llll1111l1_opy_)
        cls.bstack11llllll1l_opy_({
            bstack111ll11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧᕳ"): bstack111ll11_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨᕴ"),
            bstack111ll11_opy_ (u"ࠬࡲ࡯ࡨࡵࠪᕵ"): bstack1lll1ll11l1_opy_
        })
    @classmethod
    @bstack11lllll111_opy_(class_method=True)
    def bstack1lll1llllll_opy_(cls, steps):
        bstack1lll1ll1ll1_opy_ = []
        for step in steps:
            bstack1lll1ll1l1l_opy_ = {
                bstack111ll11_opy_ (u"࠭࡫ࡪࡰࡧࠫᕶ"): bstack111ll11_opy_ (u"ࠧࡕࡇࡖࡘࡤ࡙ࡔࡆࡒࠪᕷ"),
                bstack111ll11_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᕸ"): step[bstack111ll11_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᕹ")],
                bstack111ll11_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ᕺ"): step[bstack111ll11_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᕻ")],
                bstack111ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᕼ"): step[bstack111ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᕽ")],
                bstack111ll11_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩᕾ"): step[bstack111ll11_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪᕿ")]
            }
            if bstack111ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᖀ") in step:
                bstack1lll1ll1l1l_opy_[bstack111ll11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᖁ")] = step[bstack111ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᖂ")]
            elif bstack111ll11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᖃ") in step:
                bstack1lll1ll1l1l_opy_[bstack111ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᖄ")] = step[bstack111ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᖅ")]
            bstack1lll1ll1ll1_opy_.append(bstack1lll1ll1l1l_opy_)
        cls.bstack11llllll1l_opy_({
            bstack111ll11_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᖆ"): bstack111ll11_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᖇ"),
            bstack111ll11_opy_ (u"ࠪࡰࡴ࡭ࡳࠨᖈ"): bstack1lll1ll1ll1_opy_
        })
    @classmethod
    @bstack11lllll111_opy_(class_method=True)
    def bstack11111ll1l_opy_(cls, screenshot):
        cls.bstack11llllll1l_opy_({
            bstack111ll11_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᖉ"): bstack111ll11_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩᖊ"),
            bstack111ll11_opy_ (u"࠭࡬ࡰࡩࡶࠫᖋ"): [{
                bstack111ll11_opy_ (u"ࠧ࡬࡫ࡱࡨࠬᖌ"): bstack111ll11_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࠪᖍ"),
                bstack111ll11_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬᖎ"): datetime.datetime.utcnow().isoformat() + bstack111ll11_opy_ (u"ࠪ࡞ࠬᖏ"),
                bstack111ll11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᖐ"): screenshot[bstack111ll11_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫᖑ")],
                bstack111ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᖒ"): screenshot[bstack111ll11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᖓ")]
            }]
        }, bstack1lll1ll1l11_opy_=bstack111ll11_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭ᖔ"))
    @classmethod
    @bstack11lllll111_opy_(class_method=True)
    def bstack111l1lll_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack11llllll1l_opy_({
            bstack111ll11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᖕ"): bstack111ll11_opy_ (u"ࠪࡇࡇ࡚ࡓࡦࡵࡶ࡭ࡴࡴࡃࡳࡧࡤࡸࡪࡪࠧᖖ"),
            bstack111ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ᖗ"): {
                bstack111ll11_opy_ (u"ࠧࡻࡵࡪࡦࠥᖘ"): cls.current_test_uuid(),
                bstack111ll11_opy_ (u"ࠨࡩ࡯ࡶࡨ࡫ࡷࡧࡴࡪࡱࡱࡷࠧᖙ"): cls.bstack1l11111ll1_opy_(driver)
            }
        })
    @classmethod
    def on(cls):
        if os.environ.get(bstack111ll11_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨᖚ"), None) is None or os.environ[bstack111ll11_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡐࡗࡕࠩᖛ")] == bstack111ll11_opy_ (u"ࠤࡱࡹࡱࡲࠢᖜ"):
            return False
        return True
    @classmethod
    def bstack11111l111_opy_(cls):
        return bstack1lll1lll1_opy_(cls.bs_config.get(bstack111ll11_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧᖝ"), False))
    @classmethod
    def bstack1lll1lll11l_opy_(cls, framework):
        return framework in bstack11l1l111l1_opy_
    @staticmethod
    def request_url(url):
        return bstack111ll11_opy_ (u"ࠫࢀࢃ࠯ࡼࡿࠪᖞ").format(bstack1llll11111l_opy_, url)
    @staticmethod
    def default_headers():
        headers = {
            bstack111ll11_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫᖟ"): bstack111ll11_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᖠ"),
            bstack111ll11_opy_ (u"࡙ࠧ࠯ࡅࡗ࡙ࡇࡃࡌ࠯ࡗࡉࡘ࡚ࡏࡑࡕࠪᖡ"): bstack111ll11_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᖢ")
        }
        if os.environ.get(bstack111ll11_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡊࡘࡖࠪᖣ"), None):
            headers[bstack111ll11_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᖤ")] = bstack111ll11_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᖥ").format(os.environ[bstack111ll11_opy_ (u"ࠧࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙ࠨᖦ")])
        return headers
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack111ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᖧ"), None)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack111ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᖨ"), None)
    @staticmethod
    def bstack1l111llll1_opy_():
        if getattr(threading.current_thread(), bstack111ll11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᖩ"), None):
            return {
                bstack111ll11_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᖪ"): bstack111ll11_opy_ (u"ࠪࡸࡪࡹࡴࠨᖫ"),
                bstack111ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᖬ"): getattr(threading.current_thread(), bstack111ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᖭ"), None)
            }
        if getattr(threading.current_thread(), bstack111ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᖮ"), None):
            return {
                bstack111ll11_opy_ (u"ࠧࡵࡻࡳࡩࠬᖯ"): bstack111ll11_opy_ (u"ࠨࡪࡲࡳࡰ࠭ᖰ"),
                bstack111ll11_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᖱ"): getattr(threading.current_thread(), bstack111ll11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᖲ"), None)
            }
        return None
    @staticmethod
    def bstack1l11111ll1_opy_(driver):
        return {
            bstack111ll1l1ll_opy_(): bstack11l11l1111_opy_(driver)
        }
    @staticmethod
    def bstack1llll111111_opy_(exception_info, report):
        return [{bstack111ll11_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᖳ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11ll1l11l1_opy_(typename):
        if bstack111ll11_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣᖴ") in typename:
            return bstack111ll11_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢᖵ")
        return bstack111ll11_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣᖶ")
    @staticmethod
    def bstack1lll1llll1l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack11l1ll1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack11llll1l1l_opy_(test, hook_name=None):
        bstack1lll1lllll1_opy_ = test.parent
        if hook_name in [bstack111ll11_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ᖷ"), bstack111ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪᖸ"), bstack111ll11_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩᖹ"), bstack111ll11_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪ࠭ᖺ")]:
            bstack1lll1lllll1_opy_ = test
        scope = []
        while bstack1lll1lllll1_opy_ is not None:
            scope.append(bstack1lll1lllll1_opy_.name)
            bstack1lll1lllll1_opy_ = bstack1lll1lllll1_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1llll1111ll_opy_(hook_type):
        if hook_type == bstack111ll11_opy_ (u"ࠧࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠥᖻ"):
            return bstack111ll11_opy_ (u"ࠨࡓࡦࡶࡸࡴࠥ࡮࡯ࡰ࡭ࠥᖼ")
        elif hook_type == bstack111ll11_opy_ (u"ࠢࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠦᖽ"):
            return bstack111ll11_opy_ (u"ࠣࡖࡨࡥࡷࡪ࡯ࡸࡰࠣ࡬ࡴࡵ࡫ࠣᖾ")
    @staticmethod
    def bstack1lll1ll11ll_opy_(bstack1l1l1lll1_opy_):
        try:
            if not bstack11l1ll1l_opy_.on():
                return bstack1l1l1lll1_opy_
            if os.environ.get(bstack111ll11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠢᖿ"), None) == bstack111ll11_opy_ (u"ࠥࡸࡷࡻࡥࠣᗀ"):
                tests = os.environ.get(bstack111ll11_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠣᗁ"), None)
                if tests is None or tests == bstack111ll11_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᗂ"):
                    return bstack1l1l1lll1_opy_
                bstack1l1l1lll1_opy_ = tests.split(bstack111ll11_opy_ (u"࠭ࠬࠨᗃ"))
                return bstack1l1l1lll1_opy_
        except Exception as exc:
            print(bstack111ll11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡲࡦࡴࡸࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࡀࠠࠣᗄ"), str(exc))
        return bstack1l1l1lll1_opy_
    @classmethod
    def bstack11llll1lll_opy_(cls, event: str, bstack1l111l11l1_opy_: bstack11lll1ll1l_opy_):
        bstack1l1111ll1l_opy_ = {
            bstack111ll11_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᗅ"): event,
            bstack1l111l11l1_opy_.bstack1l111lllll_opy_(): bstack1l111l11l1_opy_.bstack1l111ll11l_opy_(event)
        }
        bstack11l1ll1l_opy_.bstack11llllll1l_opy_(bstack1l1111ll1l_opy_)