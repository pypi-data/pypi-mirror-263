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
from urllib.parse import urlparse
from bstack_utils.messages import bstack111l111lll_opy_
def bstack1llllllllll_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1lllllll1ll_opy_(bstack1llllllll1l_opy_, bstack1lllllll1l1_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1llllllll1l_opy_):
        with open(bstack1llllllll1l_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1llllllllll_opy_(bstack1llllllll1l_opy_):
        pac = get_pac(url=bstack1llllllll1l_opy_)
    else:
        raise Exception(bstack111ll11_opy_ (u"ࠫࡕࡧࡣࠡࡨ࡬ࡰࡪࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺ࠺ࠡࡽࢀࠫᐖ").format(bstack1llllllll1l_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack111ll11_opy_ (u"ࠧ࠾࠮࠹࠰࠻࠲࠽ࠨᐗ"), 80))
        bstack1llllllll11_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1llllllll11_opy_ = bstack111ll11_opy_ (u"࠭࠰࠯࠲࠱࠴࠳࠶ࠧᐘ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1lllllll1l1_opy_, bstack1llllllll11_opy_)
    return proxy_url
def bstack1l1l1l11l_opy_(config):
    return bstack111ll11_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᐙ") in config or bstack111ll11_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᐚ") in config
def bstack1llll1111l_opy_(config):
    if not bstack1l1l1l11l_opy_(config):
        return
    if config.get(bstack111ll11_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᐛ")):
        return config.get(bstack111ll11_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᐜ"))
    if config.get(bstack111ll11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᐝ")):
        return config.get(bstack111ll11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᐞ"))
def bstack1ll11lll_opy_(config, bstack1lllllll1l1_opy_):
    proxy = bstack1llll1111l_opy_(config)
    proxies = {}
    if config.get(bstack111ll11_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᐟ")) or config.get(bstack111ll11_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᐠ")):
        if proxy.endswith(bstack111ll11_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭ᐡ")):
            proxies = bstack1l1lll1l1_opy_(proxy, bstack1lllllll1l1_opy_)
        else:
            proxies = {
                bstack111ll11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᐢ"): proxy
            }
    return proxies
def bstack1l1lll1l1_opy_(bstack1llllllll1l_opy_, bstack1lllllll1l1_opy_):
    proxies = {}
    global bstack1lllllll11l_opy_
    if bstack111ll11_opy_ (u"ࠪࡔࡆࡉ࡟ࡑࡔࡒ࡜࡞࠭ᐣ") in globals():
        return bstack1lllllll11l_opy_
    try:
        proxy = bstack1lllllll1ll_opy_(bstack1llllllll1l_opy_, bstack1lllllll1l1_opy_)
        if bstack111ll11_opy_ (u"ࠦࡉࡏࡒࡆࡅࡗࠦᐤ") in proxy:
            proxies = {}
        elif bstack111ll11_opy_ (u"ࠧࡎࡔࡕࡒࠥᐥ") in proxy or bstack111ll11_opy_ (u"ࠨࡈࡕࡖࡓࡗࠧᐦ") in proxy or bstack111ll11_opy_ (u"ࠢࡔࡑࡆࡏࡘࠨᐧ") in proxy:
            bstack1lllllllll1_opy_ = proxy.split(bstack111ll11_opy_ (u"ࠣࠢࠥᐨ"))
            if bstack111ll11_opy_ (u"ࠤ࠽࠳࠴ࠨᐩ") in bstack111ll11_opy_ (u"ࠥࠦᐪ").join(bstack1lllllllll1_opy_[1:]):
                proxies = {
                    bstack111ll11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᐫ"): bstack111ll11_opy_ (u"ࠧࠨᐬ").join(bstack1lllllllll1_opy_[1:])
                }
            else:
                proxies = {
                    bstack111ll11_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᐭ"): str(bstack1lllllllll1_opy_[0]).lower() + bstack111ll11_opy_ (u"ࠢ࠻࠱࠲ࠦᐮ") + bstack111ll11_opy_ (u"ࠣࠤᐯ").join(bstack1lllllllll1_opy_[1:])
                }
        elif bstack111ll11_opy_ (u"ࠤࡓࡖࡔ࡞࡙ࠣᐰ") in proxy:
            bstack1lllllllll1_opy_ = proxy.split(bstack111ll11_opy_ (u"ࠥࠤࠧᐱ"))
            if bstack111ll11_opy_ (u"ࠦ࠿࠵࠯ࠣᐲ") in bstack111ll11_opy_ (u"ࠧࠨᐳ").join(bstack1lllllllll1_opy_[1:]):
                proxies = {
                    bstack111ll11_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᐴ"): bstack111ll11_opy_ (u"ࠢࠣᐵ").join(bstack1lllllllll1_opy_[1:])
                }
            else:
                proxies = {
                    bstack111ll11_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᐶ"): bstack111ll11_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥᐷ") + bstack111ll11_opy_ (u"ࠥࠦᐸ").join(bstack1lllllllll1_opy_[1:])
                }
        else:
            proxies = {
                bstack111ll11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᐹ"): proxy
            }
    except Exception as e:
        print(bstack111ll11_opy_ (u"ࠧࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤᐺ"), bstack111l111lll_opy_.format(bstack1llllllll1l_opy_, str(e)))
    bstack1lllllll11l_opy_ = proxies
    return proxies