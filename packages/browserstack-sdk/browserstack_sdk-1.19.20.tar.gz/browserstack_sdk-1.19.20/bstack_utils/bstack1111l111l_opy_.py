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
import re
from bstack_utils.bstack1l1lllll1_opy_ import bstack1lllll1ll11_opy_
def bstack1lllll1llll_opy_(fixture_name):
    if fixture_name.startswith(bstack111ll11_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᐻ")):
        return bstack111ll11_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᐼ")
    elif fixture_name.startswith(bstack111ll11_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᐽ")):
        return bstack111ll11_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮࡯ࡲࡨࡺࡲࡥࠨᐾ")
    elif fixture_name.startswith(bstack111ll11_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᐿ")):
        return bstack111ll11_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᑀ")
    elif fixture_name.startswith(bstack111ll11_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᑁ")):
        return bstack111ll11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮࡯ࡲࡨࡺࡲࡥࠨᑂ")
def bstack1llllll1l11_opy_(fixture_name):
    return bool(re.match(bstack111ll11_opy_ (u"ࠧ࡟ࡡࡻࡹࡳ࡯ࡴࡠࠪࡶࡩࡹࡻࡰࡽࡶࡨࡥࡷࡪ࡯ࡸࡰࠬࡣ࠭࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࡼ࡮ࡱࡧࡹࡱ࡫ࠩࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᑃ"), fixture_name))
def bstack1lllll1ll1l_opy_(fixture_name):
    return bool(re.match(bstack111ll11_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᑄ"), fixture_name))
def bstack1lllll1l1ll_opy_(fixture_name):
    return bool(re.match(bstack111ll11_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᑅ"), fixture_name))
def bstack1lllllll111_opy_(fixture_name):
    if fixture_name.startswith(bstack111ll11_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᑆ")):
        return bstack111ll11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᑇ"), bstack111ll11_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᑈ")
    elif fixture_name.startswith(bstack111ll11_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᑉ")):
        return bstack111ll11_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳࡭ࡰࡦࡸࡰࡪ࠭ᑊ"), bstack111ll11_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡃࡏࡐࠬᑋ")
    elif fixture_name.startswith(bstack111ll11_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᑌ")):
        return bstack111ll11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᑍ"), bstack111ll11_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨᑎ")
    elif fixture_name.startswith(bstack111ll11_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᑏ")):
        return bstack111ll11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮࡯ࡲࡨࡺࡲࡥࠨᑐ"), bstack111ll11_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡁࡍࡎࠪᑑ")
    return None, None
def bstack1llllll1lll_opy_(hook_name):
    if hook_name in [bstack111ll11_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧᑒ"), bstack111ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫᑓ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1llllll1ll1_opy_(hook_name):
    if hook_name in [bstack111ll11_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫᑔ"), bstack111ll11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪᑕ")]:
        return bstack111ll11_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᑖ")
    elif hook_name in [bstack111ll11_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬᑗ"), bstack111ll11_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬᑘ")]:
        return bstack111ll11_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡃࡏࡐࠬᑙ")
    elif hook_name in [bstack111ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᑚ"), bstack111ll11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬᑛ")]:
        return bstack111ll11_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨᑜ")
    elif hook_name in [bstack111ll11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧᑝ"), bstack111ll11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠧᑞ")]:
        return bstack111ll11_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡁࡍࡎࠪᑟ")
    return hook_name
def bstack1llllll1l1l_opy_(node, scenario):
    if hasattr(node, bstack111ll11_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪᑠ")):
        parts = node.nodeid.rsplit(bstack111ll11_opy_ (u"ࠤ࡞ࠦᑡ"))
        params = parts[-1]
        return bstack111ll11_opy_ (u"ࠥࡿࢂ࡛ࠦࡼࡿࠥᑢ").format(scenario.name, params)
    return scenario.name
def bstack1llllll111l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack111ll11_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭ᑣ")):
            examples = list(node.callspec.params[bstack111ll11_opy_ (u"ࠬࡥࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡩࡽࡧ࡭ࡱ࡮ࡨࠫᑤ")].values())
        return examples
    except:
        return []
def bstack1llllll11ll_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1llllll1111_opy_(report):
    try:
        status = bstack111ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᑥ")
        if report.passed or (report.failed and hasattr(report, bstack111ll11_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤᑦ"))):
            status = bstack111ll11_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᑧ")
        elif report.skipped:
            status = bstack111ll11_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᑨ")
        bstack1lllll1ll11_opy_(status)
    except:
        pass
def bstack11l1l1l11_opy_(status):
    try:
        bstack1lllll1lll1_opy_ = bstack111ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᑩ")
        if status == bstack111ll11_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᑪ"):
            bstack1lllll1lll1_opy_ = bstack111ll11_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᑫ")
        elif status == bstack111ll11_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᑬ"):
            bstack1lllll1lll1_opy_ = bstack111ll11_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᑭ")
        bstack1lllll1ll11_opy_(bstack1lllll1lll1_opy_)
    except:
        pass
def bstack1llllll11l1_opy_(item=None, report=None, summary=None, extra=None):
    return