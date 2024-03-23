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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.helper import bstack11l111l111_opy_, bstack1l1llll1l_opy_, bstack1ll1l1l1_opy_, bstack1ll1ll1l11_opy_, \
    bstack111llll1l1_opy_
def bstack111111l1l_opy_(bstack1llll1ll1l1_opy_):
    for driver in bstack1llll1ll1l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1lll11_opy_(driver, status, reason=bstack111ll11_opy_ (u"ࠪࠫᑰ")):
    bstack1l1ll1l1l1_opy_ = Config.bstack1lll111ll_opy_()
    if bstack1l1ll1l1l1_opy_.bstack11ll1l1ll1_opy_():
        return
    bstack1111ll11_opy_ = bstack1llll11l_opy_(bstack111ll11_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᑱ"), bstack111ll11_opy_ (u"ࠬ࠭ᑲ"), status, reason, bstack111ll11_opy_ (u"࠭ࠧᑳ"), bstack111ll11_opy_ (u"ࠧࠨᑴ"))
    driver.execute_script(bstack1111ll11_opy_)
def bstack111lllll1_opy_(page, status, reason=bstack111ll11_opy_ (u"ࠨࠩᑵ")):
    try:
        if page is None:
            return
        bstack1l1ll1l1l1_opy_ = Config.bstack1lll111ll_opy_()
        if bstack1l1ll1l1l1_opy_.bstack11ll1l1ll1_opy_():
            return
        bstack1111ll11_opy_ = bstack1llll11l_opy_(bstack111ll11_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᑶ"), bstack111ll11_opy_ (u"ࠪࠫᑷ"), status, reason, bstack111ll11_opy_ (u"ࠫࠬᑸ"), bstack111ll11_opy_ (u"ࠬ࠭ᑹ"))
        page.evaluate(bstack111ll11_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᑺ"), bstack1111ll11_opy_)
    except Exception as e:
        print(bstack111ll11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡾࢁࠧᑻ"), e)
def bstack1llll11l_opy_(type, name, status, reason, bstack11ll11111_opy_, bstack1llllll11_opy_):
    bstack1ll11l111_opy_ = {
        bstack111ll11_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨᑼ"): type,
        bstack111ll11_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᑽ"): {}
    }
    if type == bstack111ll11_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬᑾ"):
        bstack1ll11l111_opy_[bstack111ll11_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᑿ")][bstack111ll11_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᒀ")] = bstack11ll11111_opy_
        bstack1ll11l111_opy_[bstack111ll11_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᒁ")][bstack111ll11_opy_ (u"ࠧࡥࡣࡷࡥࠬᒂ")] = json.dumps(str(bstack1llllll11_opy_))
    if type == bstack111ll11_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᒃ"):
        bstack1ll11l111_opy_[bstack111ll11_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᒄ")][bstack111ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨᒅ")] = name
    if type == bstack111ll11_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᒆ"):
        bstack1ll11l111_opy_[bstack111ll11_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᒇ")][bstack111ll11_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᒈ")] = status
        if status == bstack111ll11_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᒉ") and str(reason) != bstack111ll11_opy_ (u"ࠣࠤᒊ"):
            bstack1ll11l111_opy_[bstack111ll11_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᒋ")][bstack111ll11_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪᒌ")] = json.dumps(str(reason))
    bstack1l1ll1ll11_opy_ = bstack111ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩᒍ").format(json.dumps(bstack1ll11l111_opy_))
    return bstack1l1ll1ll11_opy_
def bstack1111lllll_opy_(url, config, logger, bstack1l1ll1ll1l_opy_=False):
    hostname = bstack1l1llll1l_opy_(url)
    is_private = bstack1ll1ll1l11_opy_(hostname)
    try:
        if is_private or bstack1l1ll1ll1l_opy_:
            file_path = bstack11l111l111_opy_(bstack111ll11_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᒎ"), bstack111ll11_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬᒏ"), logger)
            if os.environ.get(bstack111ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬᒐ")) and eval(
                    os.environ.get(bstack111ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ᒑ"))):
                return
            if (bstack111ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᒒ") in config and not config[bstack111ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᒓ")]):
                os.environ[bstack111ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩᒔ")] = str(True)
                bstack1llll1ll11l_opy_ = {bstack111ll11_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧᒕ"): hostname}
                bstack111llll1l1_opy_(bstack111ll11_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬᒖ"), bstack111ll11_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬᒗ"), bstack1llll1ll11l_opy_, logger)
    except Exception as e:
        pass
def bstack1l1lll1ll_opy_(caps, bstack1llll1ll111_opy_):
    if bstack111ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᒘ") in caps:
        caps[bstack111ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᒙ")][bstack111ll11_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩᒚ")] = True
        if bstack1llll1ll111_opy_:
            caps[bstack111ll11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᒛ")][bstack111ll11_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᒜ")] = bstack1llll1ll111_opy_
    else:
        caps[bstack111ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫᒝ")] = True
        if bstack1llll1ll111_opy_:
            caps[bstack111ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᒞ")] = bstack1llll1ll111_opy_
def bstack1lllll1ll11_opy_(bstack11lllll1l1_opy_):
    bstack1llll1l1lll_opy_ = bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬᒟ"), bstack111ll11_opy_ (u"ࠩࠪᒠ"))
    if bstack1llll1l1lll_opy_ == bstack111ll11_opy_ (u"ࠪࠫᒡ") or bstack1llll1l1lll_opy_ == bstack111ll11_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᒢ"):
        threading.current_thread().testStatus = bstack11lllll1l1_opy_
    else:
        if bstack11lllll1l1_opy_ == bstack111ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᒣ"):
            threading.current_thread().testStatus = bstack11lllll1l1_opy_