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
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
from urllib.parse import urlparse
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import bstack11l1l1l111_opy_, bstack1lllll11l_opy_, bstack111l11l1_opy_, bstack1ll1l11l1l_opy_
from bstack_utils.messages import bstack1lll111111_opy_, bstack11ll1l1l_opy_
from bstack_utils.proxy import bstack1ll11lll_opy_, bstack1llll1111l_opy_
bstack1l1ll1l1l1_opy_ = Config.bstack1lll111ll_opy_()
def bstack11ll11l1l1_opy_(config):
    return config[bstack111ll11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧᅾ")]
def bstack11l1llllll_opy_(config):
    return config[bstack111ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩᅿ")]
def bstack1l1l1ll1l1_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack11l11l1l1l_opy_(obj):
    values = []
    bstack111lll1lll_opy_ = re.compile(bstack111ll11_opy_ (u"ࡲࠣࡠࡆ࡙ࡘ࡚ࡏࡎࡡࡗࡅࡌࡥ࡜ࡥ࠭ࠧࠦᆀ"), re.I)
    for key in obj.keys():
        if bstack111lll1lll_opy_.match(key):
            values.append(obj[key])
    return values
def bstack11l1111lll_opy_(config):
    tags = []
    tags.extend(bstack11l11l1l1l_opy_(os.environ))
    tags.extend(bstack11l11l1l1l_opy_(config))
    return tags
def bstack11l11ll11l_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack11l111lll1_opy_(bstack111lll1l11_opy_):
    if not bstack111lll1l11_opy_:
        return bstack111ll11_opy_ (u"ࠨࠩᆁ")
    return bstack111ll11_opy_ (u"ࠤࡾࢁࠥ࠮ࡻࡾࠫࠥᆂ").format(bstack111lll1l11_opy_.name, bstack111lll1l11_opy_.email)
def bstack11ll111l11_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack111ll1lll1_opy_ = repo.common_dir
        info = {
            bstack111ll11_opy_ (u"ࠥࡷ࡭ࡧࠢᆃ"): repo.head.commit.hexsha,
            bstack111ll11_opy_ (u"ࠦࡸ࡮࡯ࡳࡶࡢࡷ࡭ࡧࠢᆄ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack111ll11_opy_ (u"ࠧࡨࡲࡢࡰࡦ࡬ࠧᆅ"): repo.active_branch.name,
            bstack111ll11_opy_ (u"ࠨࡴࡢࡩࠥᆆ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack111ll11_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡴࡦࡴࠥᆇ"): bstack11l111lll1_opy_(repo.head.commit.committer),
            bstack111ll11_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࡣࡩࡧࡴࡦࠤᆈ"): repo.head.commit.committed_datetime.isoformat(),
            bstack111ll11_opy_ (u"ࠤࡤࡹࡹ࡮࡯ࡳࠤᆉ"): bstack11l111lll1_opy_(repo.head.commit.author),
            bstack111ll11_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࡢࡨࡦࡺࡥࠣᆊ"): repo.head.commit.authored_datetime.isoformat(),
            bstack111ll11_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᆋ"): repo.head.commit.message,
            bstack111ll11_opy_ (u"ࠧࡸ࡯ࡰࡶࠥᆌ"): repo.git.rev_parse(bstack111ll11_opy_ (u"ࠨ࠭࠮ࡵ࡫ࡳࡼ࠳ࡴࡰࡲ࡯ࡩࡻ࡫࡬ࠣᆍ")),
            bstack111ll11_opy_ (u"ࠢࡤࡱࡰࡱࡴࡴ࡟ࡨ࡫ࡷࡣࡩ࡯ࡲࠣᆎ"): bstack111ll1lll1_opy_,
            bstack111ll11_opy_ (u"ࠣࡹࡲࡶࡰࡺࡲࡦࡧࡢ࡫࡮ࡺ࡟ࡥ࡫ࡵࠦᆏ"): subprocess.check_output([bstack111ll11_opy_ (u"ࠤࡪ࡭ࡹࠨᆐ"), bstack111ll11_opy_ (u"ࠥࡶࡪࡼ࠭ࡱࡣࡵࡷࡪࠨᆑ"), bstack111ll11_opy_ (u"ࠦ࠲࠳ࡧࡪࡶ࠰ࡧࡴࡳ࡭ࡰࡰ࠰ࡨ࡮ࡸࠢᆒ")]).strip().decode(
                bstack111ll11_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᆓ")),
            bstack111ll11_opy_ (u"ࠨ࡬ࡢࡵࡷࡣࡹࡧࡧࠣᆔ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack111ll11_opy_ (u"ࠢࡤࡱࡰࡱ࡮ࡺࡳࡠࡵ࡬ࡲࡨ࡫࡟࡭ࡣࡶࡸࡤࡺࡡࡨࠤᆕ"): repo.git.rev_list(
                bstack111ll11_opy_ (u"ࠣࡽࢀ࠲࠳ࢁࡽࠣᆖ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack11l111ll1l_opy_ = []
        for remote in remotes:
            bstack11l111llll_opy_ = {
                bstack111ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᆗ"): remote.name,
                bstack111ll11_opy_ (u"ࠥࡹࡷࡲࠢᆘ"): remote.url,
            }
            bstack11l111ll1l_opy_.append(bstack11l111llll_opy_)
        return {
            bstack111ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᆙ"): bstack111ll11_opy_ (u"ࠧ࡭ࡩࡵࠤᆚ"),
            **info,
            bstack111ll11_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪࡹࠢᆛ"): bstack11l111ll1l_opy_
        }
    except Exception as err:
        print(bstack111ll11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡰࡲࡸࡰࡦࡺࡩ࡯ࡩࠣࡋ࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥᆜ").format(err))
        return {}
def bstack1lll1l1lll_opy_():
    env = os.environ
    if (bstack111ll11_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡘࡖࡑࠨᆝ") in env and len(env[bstack111ll11_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢᆞ")]) > 0) or (
            bstack111ll11_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣࡍࡕࡍࡆࠤᆟ") in env and len(env[bstack111ll11_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥᆠ")]) > 0):
        return {
            bstack111ll11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᆡ"): bstack111ll11_opy_ (u"ࠨࡊࡦࡰ࡮࡭ࡳࡹࠢᆢ"),
            bstack111ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᆣ"): env.get(bstack111ll11_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦᆤ")),
            bstack111ll11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᆥ"): env.get(bstack111ll11_opy_ (u"ࠥࡎࡔࡈ࡟ࡏࡃࡐࡉࠧᆦ")),
            bstack111ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᆧ"): env.get(bstack111ll11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᆨ"))
        }
    if env.get(bstack111ll11_opy_ (u"ࠨࡃࡊࠤᆩ")) == bstack111ll11_opy_ (u"ࠢࡵࡴࡸࡩࠧᆪ") and bstack1lll1lll1_opy_(env.get(bstack111ll11_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡄࡋࠥᆫ"))):
        return {
            bstack111ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᆬ"): bstack111ll11_opy_ (u"ࠥࡇ࡮ࡸࡣ࡭ࡧࡆࡍࠧᆭ"),
            bstack111ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᆮ"): env.get(bstack111ll11_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡤࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᆯ")),
            bstack111ll11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᆰ"): env.get(bstack111ll11_opy_ (u"ࠢࡄࡋࡕࡇࡑࡋ࡟ࡋࡑࡅࠦᆱ")),
            bstack111ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᆲ"): env.get(bstack111ll11_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࠧᆳ"))
        }
    if env.get(bstack111ll11_opy_ (u"ࠥࡇࡎࠨᆴ")) == bstack111ll11_opy_ (u"ࠦࡹࡸࡵࡦࠤᆵ") and bstack1lll1lll1_opy_(env.get(bstack111ll11_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࠧᆶ"))):
        return {
            bstack111ll11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᆷ"): bstack111ll11_opy_ (u"ࠢࡕࡴࡤࡺ࡮ࡹࠠࡄࡋࠥᆸ"),
            bstack111ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᆹ"): env.get(bstack111ll11_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࡡࡅ࡙ࡎࡒࡄࡠ࡙ࡈࡆࡤ࡛ࡒࡍࠤᆺ")),
            bstack111ll11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᆻ"): env.get(bstack111ll11_opy_ (u"࡙ࠦࡘࡁࡗࡋࡖࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᆼ")),
            bstack111ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᆽ"): env.get(bstack111ll11_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᆾ"))
        }
    if env.get(bstack111ll11_opy_ (u"ࠢࡄࡋࠥᆿ")) == bstack111ll11_opy_ (u"ࠣࡶࡵࡹࡪࠨᇀ") and env.get(bstack111ll11_opy_ (u"ࠤࡆࡍࡤࡔࡁࡎࡇࠥᇁ")) == bstack111ll11_opy_ (u"ࠥࡧࡴࡪࡥࡴࡪ࡬ࡴࠧᇂ"):
        return {
            bstack111ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇃ"): bstack111ll11_opy_ (u"ࠧࡉ࡯ࡥࡧࡶ࡬࡮ࡶࠢᇄ"),
            bstack111ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᇅ"): None,
            bstack111ll11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᇆ"): None,
            bstack111ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᇇ"): None
        }
    if env.get(bstack111ll11_opy_ (u"ࠤࡅࡍ࡙ࡈࡕࡄࡍࡈࡘࡤࡈࡒࡂࡐࡆࡌࠧᇈ")) and env.get(bstack111ll11_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡃࡐࡏࡐࡍ࡙ࠨᇉ")):
        return {
            bstack111ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇊ"): bstack111ll11_opy_ (u"ࠧࡈࡩࡵࡤࡸࡧࡰ࡫ࡴࠣᇋ"),
            bstack111ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᇌ"): env.get(bstack111ll11_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡋࡎ࡚࡟ࡉࡖࡗࡔࡤࡕࡒࡊࡉࡌࡒࠧᇍ")),
            bstack111ll11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᇎ"): None,
            bstack111ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᇏ"): env.get(bstack111ll11_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᇐ"))
        }
    if env.get(bstack111ll11_opy_ (u"ࠦࡈࡏࠢᇑ")) == bstack111ll11_opy_ (u"ࠧࡺࡲࡶࡧࠥᇒ") and bstack1lll1lll1_opy_(env.get(bstack111ll11_opy_ (u"ࠨࡄࡓࡑࡑࡉࠧᇓ"))):
        return {
            bstack111ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᇔ"): bstack111ll11_opy_ (u"ࠣࡆࡵࡳࡳ࡫ࠢᇕ"),
            bstack111ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᇖ"): env.get(bstack111ll11_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡎࡌࡒࡐࠨᇗ")),
            bstack111ll11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᇘ"): None,
            bstack111ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᇙ"): env.get(bstack111ll11_opy_ (u"ࠨࡄࡓࡑࡑࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᇚ"))
        }
    if env.get(bstack111ll11_opy_ (u"ࠢࡄࡋࠥᇛ")) == bstack111ll11_opy_ (u"ࠣࡶࡵࡹࡪࠨᇜ") and bstack1lll1lll1_opy_(env.get(bstack111ll11_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࠧᇝ"))):
        return {
            bstack111ll11_opy_ (u"ࠥࡲࡦࡳࡥࠣᇞ"): bstack111ll11_opy_ (u"ࠦࡘ࡫࡭ࡢࡲ࡫ࡳࡷ࡫ࠢᇟ"),
            bstack111ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᇠ"): env.get(bstack111ll11_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࡡࡒࡖࡌࡇࡎࡊ࡜ࡄࡘࡎࡕࡎࡠࡗࡕࡐࠧᇡ")),
            bstack111ll11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᇢ"): env.get(bstack111ll11_opy_ (u"ࠣࡕࡈࡑࡆࡖࡈࡐࡔࡈࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᇣ")),
            bstack111ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᇤ"): env.get(bstack111ll11_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡊࡐࡄࡢࡍࡉࠨᇥ"))
        }
    if env.get(bstack111ll11_opy_ (u"ࠦࡈࡏࠢᇦ")) == bstack111ll11_opy_ (u"ࠧࡺࡲࡶࡧࠥᇧ") and bstack1lll1lll1_opy_(env.get(bstack111ll11_opy_ (u"ࠨࡇࡊࡖࡏࡅࡇࡥࡃࡊࠤᇨ"))):
        return {
            bstack111ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᇩ"): bstack111ll11_opy_ (u"ࠣࡉ࡬ࡸࡑࡧࡢࠣᇪ"),
            bstack111ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᇫ"): env.get(bstack111ll11_opy_ (u"ࠥࡇࡎࡥࡊࡐࡄࡢ࡙ࡗࡒࠢᇬ")),
            bstack111ll11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᇭ"): env.get(bstack111ll11_opy_ (u"ࠧࡉࡉࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᇮ")),
            bstack111ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᇯ"): env.get(bstack111ll11_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡊࡆࠥᇰ"))
        }
    if env.get(bstack111ll11_opy_ (u"ࠣࡅࡌࠦᇱ")) == bstack111ll11_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᇲ") and bstack1lll1lll1_opy_(env.get(bstack111ll11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࠨᇳ"))):
        return {
            bstack111ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᇴ"): bstack111ll11_opy_ (u"ࠧࡈࡵࡪ࡮ࡧ࡯࡮ࡺࡥࠣᇵ"),
            bstack111ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᇶ"): env.get(bstack111ll11_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᇷ")),
            bstack111ll11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᇸ"): env.get(bstack111ll11_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡒࡁࡃࡇࡏࠦᇹ")) or env.get(bstack111ll11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨᇺ")),
            bstack111ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᇻ"): env.get(bstack111ll11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡏࡎ࡚ࡅࡠࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢᇼ"))
        }
    if bstack1lll1lll1_opy_(env.get(bstack111ll11_opy_ (u"ࠨࡔࡇࡡࡅ࡙ࡎࡒࡄࠣᇽ"))):
        return {
            bstack111ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᇾ"): bstack111ll11_opy_ (u"ࠣࡘ࡬ࡷࡺࡧ࡬ࠡࡕࡷࡹࡩ࡯࡯ࠡࡖࡨࡥࡲࠦࡓࡦࡴࡹ࡭ࡨ࡫ࡳࠣᇿ"),
            bstack111ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧሀ"): bstack111ll11_opy_ (u"ࠥࡿࢂࢁࡽࠣሁ").format(env.get(bstack111ll11_opy_ (u"ࠫࡘ࡟ࡓࡕࡇࡐࡣ࡙ࡋࡁࡎࡈࡒ࡙ࡓࡊࡁࡕࡋࡒࡒࡘࡋࡒࡗࡇࡕ࡙ࡗࡏࠧሂ")), env.get(bstack111ll11_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡓࡖࡔࡐࡅࡄࡖࡌࡈࠬሃ"))),
            bstack111ll11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣሄ"): env.get(bstack111ll11_opy_ (u"ࠢࡔ࡛ࡖࡘࡊࡓ࡟ࡅࡇࡉࡍࡓࡏࡔࡊࡑࡑࡍࡉࠨህ")),
            bstack111ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢሆ"): env.get(bstack111ll11_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤሇ"))
        }
    if bstack1lll1lll1_opy_(env.get(bstack111ll11_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࠧለ"))):
        return {
            bstack111ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤሉ"): bstack111ll11_opy_ (u"ࠧࡇࡰࡱࡸࡨࡽࡴࡸࠢሊ"),
            bstack111ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤላ"): bstack111ll11_opy_ (u"ࠢࡼࡿ࠲ࡴࡷࡵࡪࡦࡥࡷ࠳ࢀࢃ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂࠨሌ").format(env.get(bstack111ll11_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢ࡙ࡗࡒࠧል")), env.get(bstack111ll11_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡆࡉࡃࡐࡗࡑࡘࡤࡔࡁࡎࡇࠪሎ")), env.get(bstack111ll11_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡓࡍࡗࡊࠫሏ")), env.get(bstack111ll11_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨሐ"))),
            bstack111ll11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢሑ"): env.get(bstack111ll11_opy_ (u"ࠨࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥሒ")),
            bstack111ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨሓ"): env.get(bstack111ll11_opy_ (u"ࠣࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤሔ"))
        }
    if env.get(bstack111ll11_opy_ (u"ࠤࡄ࡞࡚ࡘࡅࡠࡊࡗࡘࡕࡥࡕࡔࡇࡕࡣࡆࡍࡅࡏࡖࠥሕ")) and env.get(bstack111ll11_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧሖ")):
        return {
            bstack111ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤሗ"): bstack111ll11_opy_ (u"ࠧࡇࡺࡶࡴࡨࠤࡈࡏࠢመ"),
            bstack111ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤሙ"): bstack111ll11_opy_ (u"ࠢࡼࡿࡾࢁ࠴ࡥࡢࡶ࡫࡯ࡨ࠴ࡸࡥࡴࡷ࡯ࡸࡸࡅࡢࡶ࡫࡯ࡨࡎࡪ࠽ࡼࡿࠥሚ").format(env.get(bstack111ll11_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫማ")), env.get(bstack111ll11_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࠧሜ")), env.get(bstack111ll11_opy_ (u"ࠪࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠪም"))),
            bstack111ll11_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨሞ"): env.get(bstack111ll11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡌࡈࠧሟ")),
            bstack111ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧሠ"): env.get(bstack111ll11_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠢሡ"))
        }
    if any([env.get(bstack111ll11_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨሢ")), env.get(bstack111ll11_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡘࡅࡔࡑࡏ࡚ࡊࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣሣ")), env.get(bstack111ll11_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡓࡐࡗࡕࡇࡊࡥࡖࡆࡔࡖࡍࡔࡔࠢሤ"))]):
        return {
            bstack111ll11_opy_ (u"ࠦࡳࡧ࡭ࡦࠤሥ"): bstack111ll11_opy_ (u"ࠧࡇࡗࡔࠢࡆࡳࡩ࡫ࡂࡶ࡫࡯ࡨࠧሦ"),
            bstack111ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤሧ"): env.get(bstack111ll11_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡔ࡚ࡈࡌࡊࡅࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨረ")),
            bstack111ll11_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥሩ"): env.get(bstack111ll11_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢሪ")),
            bstack111ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤራ"): env.get(bstack111ll11_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤሬ"))
        }
    if env.get(bstack111ll11_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡨࡵࡪ࡮ࡧࡒࡺࡳࡢࡦࡴࠥር")):
        return {
            bstack111ll11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦሮ"): bstack111ll11_opy_ (u"ࠢࡃࡣࡰࡦࡴࡵࠢሯ"),
            bstack111ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦሰ"): env.get(bstack111ll11_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡓࡧࡶࡹࡱࡺࡳࡖࡴ࡯ࠦሱ")),
            bstack111ll11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧሲ"): env.get(bstack111ll11_opy_ (u"ࠦࡧࡧ࡭ࡣࡱࡲࡣࡸ࡮࡯ࡳࡶࡍࡳࡧࡔࡡ࡮ࡧࠥሳ")),
            bstack111ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦሴ"): env.get(bstack111ll11_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦስ"))
        }
    if env.get(bstack111ll11_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࠣሶ")) or env.get(bstack111ll11_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥሷ")):
        return {
            bstack111ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢሸ"): bstack111ll11_opy_ (u"࡛ࠥࡪࡸࡣ࡬ࡧࡵࠦሹ"),
            bstack111ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢሺ"): env.get(bstack111ll11_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤሻ")),
            bstack111ll11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣሼ"): bstack111ll11_opy_ (u"ࠢࡎࡣ࡬ࡲࠥࡖࡩࡱࡧ࡯࡭ࡳ࡫ࠢሽ") if env.get(bstack111ll11_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࡡࡐࡅࡎࡔ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡖࡘࡆࡘࡔࡆࡆࠥሾ")) else None,
            bstack111ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣሿ"): env.get(bstack111ll11_opy_ (u"࡛ࠥࡊࡘࡃࡌࡇࡕࡣࡌࡏࡔࡠࡅࡒࡑࡒࡏࡔࠣቀ"))
        }
    if any([env.get(bstack111ll11_opy_ (u"ࠦࡌࡉࡐࡠࡒࡕࡓࡏࡋࡃࡕࠤቁ")), env.get(bstack111ll11_opy_ (u"ࠧࡍࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨቂ")), env.get(bstack111ll11_opy_ (u"ࠨࡇࡐࡑࡊࡐࡊࡥࡃࡍࡑࡘࡈࡤࡖࡒࡐࡌࡈࡇ࡙ࠨቃ"))]):
        return {
            bstack111ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧቄ"): bstack111ll11_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡅ࡯ࡳࡺࡪࠢቅ"),
            bstack111ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧቆ"): None,
            bstack111ll11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧቇ"): env.get(bstack111ll11_opy_ (u"ࠦࡕࡘࡏࡋࡇࡆࡘࡤࡏࡄࠣቈ")),
            bstack111ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ቉"): env.get(bstack111ll11_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣቊ"))
        }
    if env.get(bstack111ll11_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࠥቋ")):
        return {
            bstack111ll11_opy_ (u"ࠣࡰࡤࡱࡪࠨቌ"): bstack111ll11_opy_ (u"ࠤࡖ࡬࡮ࡶࡰࡢࡤ࡯ࡩࠧቍ"),
            bstack111ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ቎"): env.get(bstack111ll11_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥ቏")),
            bstack111ll11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢቐ"): bstack111ll11_opy_ (u"ࠨࡊࡰࡤࠣࠧࢀࢃࠢቑ").format(env.get(bstack111ll11_opy_ (u"ࠧࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡎࡔࡈ࡟ࡊࡆࠪቒ"))) if env.get(bstack111ll11_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠦቓ")) else None,
            bstack111ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣቔ"): env.get(bstack111ll11_opy_ (u"ࠥࡗࡍࡏࡐࡑࡃࡅࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧቕ"))
        }
    if bstack1lll1lll1_opy_(env.get(bstack111ll11_opy_ (u"ࠦࡓࡋࡔࡍࡋࡉ࡝ࠧቖ"))):
        return {
            bstack111ll11_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ቗"): bstack111ll11_opy_ (u"ࠨࡎࡦࡶ࡯࡭࡫ࡿࠢቘ"),
            bstack111ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ቙"): env.get(bstack111ll11_opy_ (u"ࠣࡆࡈࡔࡑࡕ࡙ࡠࡗࡕࡐࠧቚ")),
            bstack111ll11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦቛ"): env.get(bstack111ll11_opy_ (u"ࠥࡗࡎ࡚ࡅࡠࡐࡄࡑࡊࠨቜ")),
            bstack111ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥቝ"): env.get(bstack111ll11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢ቞"))
        }
    if bstack1lll1lll1_opy_(env.get(bstack111ll11_opy_ (u"ࠨࡇࡊࡖࡋ࡙ࡇࡥࡁࡄࡖࡌࡓࡓ࡙ࠢ቟"))):
        return {
            bstack111ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧበ"): bstack111ll11_opy_ (u"ࠣࡉ࡬ࡸࡍࡻࡢࠡࡃࡦࡸ࡮ࡵ࡮ࡴࠤቡ"),
            bstack111ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧቢ"): bstack111ll11_opy_ (u"ࠥࡿࢂ࠵ࡻࡾ࠱ࡤࡧࡹ࡯࡯࡯ࡵ࠲ࡶࡺࡴࡳ࠰ࡽࢀࠦባ").format(env.get(bstack111ll11_opy_ (u"ࠫࡌࡏࡔࡉࡗࡅࡣࡘࡋࡒࡗࡇࡕࡣ࡚ࡘࡌࠨቤ")), env.get(bstack111ll11_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤࡘࡅࡑࡑࡖࡍ࡙ࡕࡒ࡚ࠩብ")), env.get(bstack111ll11_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡖࡐࡢࡍࡉ࠭ቦ"))),
            bstack111ll11_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤቧ"): env.get(bstack111ll11_opy_ (u"ࠣࡉࡌࡘࡍ࡛ࡂࡠ࡙ࡒࡖࡐࡌࡌࡐ࡙ࠥቨ")),
            bstack111ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣቩ"): env.get(bstack111ll11_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠥቪ"))
        }
    if env.get(bstack111ll11_opy_ (u"ࠦࡈࡏࠢቫ")) == bstack111ll11_opy_ (u"ࠧࡺࡲࡶࡧࠥቬ") and env.get(bstack111ll11_opy_ (u"ࠨࡖࡆࡔࡆࡉࡑࠨቭ")) == bstack111ll11_opy_ (u"ࠢ࠲ࠤቮ"):
        return {
            bstack111ll11_opy_ (u"ࠣࡰࡤࡱࡪࠨቯ"): bstack111ll11_opy_ (u"ࠤ࡙ࡩࡷࡩࡥ࡭ࠤተ"),
            bstack111ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨቱ"): bstack111ll11_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࢀࢃࠢቲ").format(env.get(bstack111ll11_opy_ (u"ࠬ࡜ࡅࡓࡅࡈࡐࡤ࡛ࡒࡍࠩታ"))),
            bstack111ll11_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣቴ"): None,
            bstack111ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨት"): None,
        }
    if env.get(bstack111ll11_opy_ (u"ࠣࡖࡈࡅࡒࡉࡉࡕ࡛ࡢ࡚ࡊࡘࡓࡊࡑࡑࠦቶ")):
        return {
            bstack111ll11_opy_ (u"ࠤࡱࡥࡲ࡫ࠢቷ"): bstack111ll11_opy_ (u"ࠥࡘࡪࡧ࡭ࡤ࡫ࡷࡽࠧቸ"),
            bstack111ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢቹ"): None,
            bstack111ll11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢቺ"): env.get(bstack111ll11_opy_ (u"ࠨࡔࡆࡃࡐࡇࡎ࡚࡙ࡠࡒࡕࡓࡏࡋࡃࡕࡡࡑࡅࡒࡋࠢቻ")),
            bstack111ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨቼ"): env.get(bstack111ll11_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࠢች"))
        }
    if any([env.get(bstack111ll11_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࠧቾ")), env.get(bstack111ll11_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࡥࡕࡓࡎࠥቿ")), env.get(bstack111ll11_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠤኀ")), env.get(bstack111ll11_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡖࡈࡅࡒࠨኁ"))]):
        return {
            bstack111ll11_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦኂ"): bstack111ll11_opy_ (u"ࠢࡄࡱࡱࡧࡴࡻࡲࡴࡧࠥኃ"),
            bstack111ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦኄ"): None,
            bstack111ll11_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦኅ"): env.get(bstack111ll11_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦኆ")) or None,
            bstack111ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥኇ"): env.get(bstack111ll11_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡎࡊࠢኈ"), 0)
        }
    if env.get(bstack111ll11_opy_ (u"ࠨࡇࡐࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦ኉")):
        return {
            bstack111ll11_opy_ (u"ࠢ࡯ࡣࡰࡩࠧኊ"): bstack111ll11_opy_ (u"ࠣࡉࡲࡇࡉࠨኋ"),
            bstack111ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧኌ"): None,
            bstack111ll11_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧኍ"): env.get(bstack111ll11_opy_ (u"ࠦࡌࡕ࡟ࡋࡑࡅࡣࡓࡇࡍࡆࠤ኎")),
            bstack111ll11_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ኏"): env.get(bstack111ll11_opy_ (u"ࠨࡇࡐࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡈࡕࡕࡏࡖࡈࡖࠧነ"))
        }
    if env.get(bstack111ll11_opy_ (u"ࠢࡄࡈࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠧኑ")):
        return {
            bstack111ll11_opy_ (u"ࠣࡰࡤࡱࡪࠨኒ"): bstack111ll11_opy_ (u"ࠤࡆࡳࡩ࡫ࡆࡳࡧࡶ࡬ࠧና"),
            bstack111ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨኔ"): env.get(bstack111ll11_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥን")),
            bstack111ll11_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢኖ"): env.get(bstack111ll11_opy_ (u"ࠨࡃࡇࡡࡓࡍࡕࡋࡌࡊࡐࡈࡣࡓࡇࡍࡆࠤኗ")),
            bstack111ll11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨኘ"): env.get(bstack111ll11_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨኙ"))
        }
    return {bstack111ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣኚ"): None}
def get_host_info():
    return {
        bstack111ll11_opy_ (u"ࠥ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠧኛ"): platform.node(),
        bstack111ll11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨኜ"): platform.system(),
        bstack111ll11_opy_ (u"ࠧࡺࡹࡱࡧࠥኝ"): platform.machine(),
        bstack111ll11_opy_ (u"ࠨࡶࡦࡴࡶ࡭ࡴࡴࠢኞ"): platform.version(),
        bstack111ll11_opy_ (u"ࠢࡢࡴࡦ࡬ࠧኟ"): platform.architecture()[0]
    }
def bstack1ll11l1l1_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111ll1l1ll_opy_():
    if bstack1l1ll1l1l1_opy_.get_property(bstack111ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩአ")):
        return bstack111ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨኡ")
    return bstack111ll11_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠩኢ")
def bstack11l11l1111_opy_(driver):
    info = {
        bstack111ll11_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪኣ"): driver.capabilities,
        bstack111ll11_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩኤ"): driver.session_id,
        bstack111ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧእ"): driver.capabilities.get(bstack111ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬኦ"), None),
        bstack111ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪኧ"): driver.capabilities.get(bstack111ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪከ"), None),
        bstack111ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࠬኩ"): driver.capabilities.get(bstack111ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪኪ"), None),
    }
    if bstack111ll1l1ll_opy_() == bstack111ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫካ"):
        info[bstack111ll11_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧኬ")] = bstack111ll11_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ክ") if bstack1l11l1l1l_opy_() else bstack111ll11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪኮ")
    return info
def bstack1l11l1l1l_opy_():
    if bstack1l1ll1l1l1_opy_.get_property(bstack111ll11_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨኯ")):
        return True
    if bstack1lll1lll1_opy_(os.environ.get(bstack111ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫኰ"), None)):
        return True
    return False
def bstack1ll11111l1_opy_(bstack11l11l1lll_opy_, url, data, config):
    headers = config.get(bstack111ll11_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ኱"), None)
    proxies = bstack1ll11lll_opy_(config, url)
    auth = config.get(bstack111ll11_opy_ (u"ࠬࡧࡵࡵࡪࠪኲ"), None)
    response = requests.request(
            bstack11l11l1lll_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1l11lllll_opy_(bstack1lll1l1l_opy_, size):
    bstack1l1l111l11_opy_ = []
    while len(bstack1lll1l1l_opy_) > size:
        bstack11l11l1l1_opy_ = bstack1lll1l1l_opy_[:size]
        bstack1l1l111l11_opy_.append(bstack11l11l1l1_opy_)
        bstack1lll1l1l_opy_ = bstack1lll1l1l_opy_[size:]
    bstack1l1l111l11_opy_.append(bstack1lll1l1l_opy_)
    return bstack1l1l111l11_opy_
def bstack11l11l11ll_opy_(message, bstack11l11111l1_opy_=False):
    os.write(1, bytes(message, bstack111ll11_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬኳ")))
    os.write(1, bytes(bstack111ll11_opy_ (u"ࠧ࡝ࡰࠪኴ"), bstack111ll11_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧኵ")))
    if bstack11l11111l1_opy_:
        with open(bstack111ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠯ࡲ࠵࠶ࡿ࠭ࠨ኶") + os.environ[bstack111ll11_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩ኷")] + bstack111ll11_opy_ (u"ࠫ࠳ࡲ࡯ࡨࠩኸ"), bstack111ll11_opy_ (u"ࠬࡧࠧኹ")) as f:
            f.write(message + bstack111ll11_opy_ (u"࠭࡜࡯ࠩኺ"))
def bstack111llll11l_opy_():
    return os.environ[bstack111ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪኻ")].lower() == bstack111ll11_opy_ (u"ࠨࡶࡵࡹࡪ࠭ኼ")
def bstack1ll11l11l_opy_(bstack111lll1111_opy_):
    return bstack111ll11_opy_ (u"ࠩࡾࢁ࠴ࢁࡽࠨኽ").format(bstack11l1l1l111_opy_, bstack111lll1111_opy_)
def bstack1lll1l1l11_opy_():
    return datetime.datetime.utcnow().isoformat() + bstack111ll11_opy_ (u"ࠪ࡞ࠬኾ")
def bstack11l111l1l1_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack111ll11_opy_ (u"ࠫ࡟࠭኿"))) - datetime.datetime.fromisoformat(start.rstrip(bstack111ll11_opy_ (u"ࠬࡠࠧዀ")))).total_seconds() * 1000
def bstack11l1111111_opy_(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat() + bstack111ll11_opy_ (u"࡚࠭ࠨ዁")
def bstack111lll1ll1_opy_(bstack11l1111ll1_opy_):
    date_format = bstack111ll11_opy_ (u"࡛ࠧࠦࠨࡱࠪࡪࠠࠦࡊ࠽ࠩࡒࡀࠥࡔ࠰ࠨࡪࠬዂ")
    bstack11l11l1l11_opy_ = datetime.datetime.strptime(bstack11l1111ll1_opy_, date_format)
    return bstack11l11l1l11_opy_.isoformat() + bstack111ll11_opy_ (u"ࠨ࡜ࠪዃ")
def bstack111llllll1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack111ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩዄ")
    else:
        return bstack111ll11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪዅ")
def bstack1lll1lll1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack111ll11_opy_ (u"ࠫࡹࡸࡵࡦࠩ዆")
def bstack11l11ll1ll_opy_(val):
    return val.__str__().lower() == bstack111ll11_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ዇")
def bstack11lllll111_opy_(bstack11l11111ll_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack11l11111ll_opy_ as e:
                print(bstack111ll11_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨወ").format(func.__name__, bstack11l11111ll_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack11l11lll1l_opy_(bstack11l111l1ll_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack11l111l1ll_opy_(cls, *args, **kwargs)
            except bstack11l11111ll_opy_ as e:
                print(bstack111ll11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡽࢀࠤ࠲ࡄࠠࡼࡿ࠽ࠤࢀࢃࠢዉ").format(bstack11l111l1ll_opy_.__name__, bstack11l11111ll_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack11l11lll1l_opy_
    else:
        return decorator
def bstack1l1l11l1l_opy_(bstack11ll1llll1_opy_):
    if bstack111ll11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬዊ") in bstack11ll1llll1_opy_ and bstack11l11ll1ll_opy_(bstack11ll1llll1_opy_[bstack111ll11_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ዋ")]):
        return False
    if bstack111ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬዌ") in bstack11ll1llll1_opy_ and bstack11l11ll1ll_opy_(bstack11ll1llll1_opy_[bstack111ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ው")]):
        return False
    return True
def bstack1l1llll1l1_opy_():
    try:
        from pytest_bdd import reporting
        return True
    except Exception as e:
        return False
def bstack1lll11l11_opy_(hub_url):
    if bstack1l111lll1_opy_() <= version.parse(bstack111ll11_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬዎ")):
        if hub_url != bstack111ll11_opy_ (u"࠭ࠧዏ"):
            return bstack111ll11_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣዐ") + hub_url + bstack111ll11_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧዑ")
        return bstack111l11l1_opy_
    if hub_url != bstack111ll11_opy_ (u"ࠩࠪዒ"):
        return bstack111ll11_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧዓ") + hub_url + bstack111ll11_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧዔ")
    return bstack1ll1l11l1l_opy_
def bstack111lll111l_opy_():
    return isinstance(os.getenv(bstack111ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫዕ")), str)
def bstack1l1llll1l_opy_(url):
    return urlparse(url).hostname
def bstack1ll1ll1l11_opy_(hostname):
    for bstack1ll1lll1l1_opy_ in bstack1lllll11l_opy_:
        regex = re.compile(bstack1ll1lll1l1_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11l111l111_opy_(bstack111lll11ll_opy_, file_name, logger):
    bstack11l1l1lll_opy_ = os.path.join(os.path.expanduser(bstack111ll11_opy_ (u"࠭ࡾࠨዖ")), bstack111lll11ll_opy_)
    try:
        if not os.path.exists(bstack11l1l1lll_opy_):
            os.makedirs(bstack11l1l1lll_opy_)
        file_path = os.path.join(os.path.expanduser(bstack111ll11_opy_ (u"ࠧࡿࠩ዗")), bstack111lll11ll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack111ll11_opy_ (u"ࠨࡹࠪዘ")):
                pass
            with open(file_path, bstack111ll11_opy_ (u"ࠤࡺ࠯ࠧዙ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1lll111111_opy_.format(str(e)))
def bstack111llll1l1_opy_(file_name, key, value, logger):
    file_path = bstack11l111l111_opy_(bstack111ll11_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪዚ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1l11ll111_opy_ = json.load(open(file_path, bstack111ll11_opy_ (u"ࠫࡷࡨࠧዛ")))
        else:
            bstack1l11ll111_opy_ = {}
        bstack1l11ll111_opy_[key] = value
        with open(file_path, bstack111ll11_opy_ (u"ࠧࡽࠫࠣዜ")) as outfile:
            json.dump(bstack1l11ll111_opy_, outfile)
def bstack111l1111_opy_(file_name, logger):
    file_path = bstack11l111l111_opy_(bstack111ll11_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ዝ"), file_name, logger)
    bstack1l11ll111_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack111ll11_opy_ (u"ࠧࡳࠩዞ")) as bstack1ll1l1ll_opy_:
            bstack1l11ll111_opy_ = json.load(bstack1ll1l1ll_opy_)
    return bstack1l11ll111_opy_
def bstack1l1l1l1l1l_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack111ll11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬዟ") + file_path + bstack111ll11_opy_ (u"ࠩࠣࠫዠ") + str(e))
def bstack1l111lll1_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack111ll11_opy_ (u"ࠥࡀࡓࡕࡔࡔࡇࡗࡂࠧዡ")
def bstack1l11111l_opy_(config):
    if bstack111ll11_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪዢ") in config:
        del (config[bstack111ll11_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫዣ")])
        return False
    if bstack1l111lll1_opy_() < version.parse(bstack111ll11_opy_ (u"࠭࠳࠯࠶࠱࠴ࠬዤ")):
        return False
    if bstack1l111lll1_opy_() >= version.parse(bstack111ll11_opy_ (u"ࠧ࠵࠰࠴࠲࠺࠭ዥ")):
        return True
    if bstack111ll11_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨዦ") in config and config[bstack111ll11_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩዧ")] is False:
        return False
    else:
        return True
def bstack111ll11ll_opy_(args_list, bstack11l11ll1l1_opy_):
    index = -1
    for value in bstack11l11ll1l1_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1l11111l1l_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1l11111l1l_opy_ = bstack1l11111l1l_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack111ll11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪየ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack111ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫዩ"), exception=exception)
    def bstack11ll1l11l1_opy_(self):
        if self.result != bstack111ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬዪ"):
            return None
        if bstack111ll11_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤያ") in self.exception_type:
            return bstack111ll11_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣዬ")
        return bstack111ll11_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤይ")
    def bstack11l11ll111_opy_(self):
        if self.result != bstack111ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩዮ"):
            return None
        if self.bstack1l11111l1l_opy_:
            return self.bstack1l11111l1l_opy_
        return bstack111llll1ll_opy_(self.exception)
def bstack111llll1ll_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111lllll1l_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1ll1l1l1_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1l11l1l1ll_opy_(config, logger):
    try:
        import playwright
        bstack11l11l111l_opy_ = playwright.__file__
        bstack11l11lll11_opy_ = os.path.split(bstack11l11l111l_opy_)
        bstack11l111ll11_opy_ = bstack11l11lll11_opy_[0] + bstack111ll11_opy_ (u"ࠪ࠳ࡩࡸࡩࡷࡧࡵ࠳ࡵࡧࡣ࡬ࡣࡪࡩ࠴ࡲࡩࡣ࠱ࡦࡰ࡮࠵ࡣ࡭࡫࠱࡮ࡸ࠭ዯ")
        os.environ[bstack111ll11_opy_ (u"ࠫࡌࡒࡏࡃࡃࡏࡣࡆࡍࡅࡏࡖࡢࡌ࡙࡚ࡐࡠࡒࡕࡓ࡝࡟ࠧደ")] = bstack1llll1111l_opy_(config)
        with open(bstack11l111ll11_opy_, bstack111ll11_opy_ (u"ࠬࡸࠧዱ")) as f:
            bstack1111llll1_opy_ = f.read()
            bstack111lllllll_opy_ = bstack111ll11_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠬዲ")
            bstack11l11l11l1_opy_ = bstack1111llll1_opy_.find(bstack111lllllll_opy_)
            if bstack11l11l11l1_opy_ == -1:
              process = subprocess.Popen(bstack111ll11_opy_ (u"ࠢ࡯ࡲࡰࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠦዳ"), shell=True, cwd=bstack11l11lll11_opy_[0])
              process.wait()
              bstack11l11llll1_opy_ = bstack111ll11_opy_ (u"ࠨࠤࡸࡷࡪࠦࡳࡵࡴ࡬ࡧࡹࠨ࠻ࠨዴ")
              bstack111ll1llll_opy_ = bstack111ll11_opy_ (u"ࠤࠥࠦࠥࡢࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࡠࠧࡁࠠࡤࡱࡱࡷࡹࠦࡻࠡࡤࡲࡳࡹࡹࡴࡳࡣࡳࠤࢂࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠪ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠩࠬ࠿ࠥ࡯ࡦࠡࠪࡳࡶࡴࡩࡥࡴࡵ࠱ࡩࡳࡼ࠮ࡈࡎࡒࡆࡆࡒ࡟ࡂࡉࡈࡒ࡙ࡥࡈࡕࡖࡓࡣࡕࡘࡏ࡙࡛ࠬࠤࡧࡵ࡯ࡵࡵࡷࡶࡦࡶࠨࠪ࠽ࠣࠦࠧࠨድ")
              bstack11l11l1ll1_opy_ = bstack1111llll1_opy_.replace(bstack11l11llll1_opy_, bstack111ll1llll_opy_)
              with open(bstack11l111ll11_opy_, bstack111ll11_opy_ (u"ࠪࡻࠬዶ")) as f:
                f.write(bstack11l11l1ll1_opy_)
    except Exception as e:
        logger.error(bstack11ll1l1l_opy_.format(str(e)))
def bstack1ll1ll111_opy_():
  try:
    bstack111lllll11_opy_ = os.path.join(tempfile.gettempdir(), bstack111ll11_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠴ࡪࡴࡱࡱࠫዷ"))
    bstack11l1111l1l_opy_ = []
    if os.path.exists(bstack111lllll11_opy_):
      with open(bstack111lllll11_opy_) as f:
        bstack11l1111l1l_opy_ = json.load(f)
      os.remove(bstack111lllll11_opy_)
    return bstack11l1111l1l_opy_
  except:
    pass
  return []
def bstack1ll1llll1l_opy_(bstack1l1ll111l_opy_):
  try:
    bstack11l1111l1l_opy_ = []
    bstack111lllll11_opy_ = os.path.join(tempfile.gettempdir(), bstack111ll11_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬዸ"))
    if os.path.exists(bstack111lllll11_opy_):
      with open(bstack111lllll11_opy_) as f:
        bstack11l1111l1l_opy_ = json.load(f)
    bstack11l1111l1l_opy_.append(bstack1l1ll111l_opy_)
    with open(bstack111lllll11_opy_, bstack111ll11_opy_ (u"࠭ࡷࠨዹ")) as f:
        json.dump(bstack11l1111l1l_opy_, f)
  except:
    pass
def bstack1l11l1l11l_opy_(logger, bstack111ll1l1l1_opy_ = False):
  try:
    test_name = os.environ.get(bstack111ll11_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪዺ"), bstack111ll11_opy_ (u"ࠨࠩዻ"))
    if test_name == bstack111ll11_opy_ (u"ࠩࠪዼ"):
        test_name = threading.current_thread().__dict__.get(bstack111ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡅࡨࡩࡥࡴࡦࡵࡷࡣࡳࡧ࡭ࡦࠩዽ"), bstack111ll11_opy_ (u"ࠫࠬዾ"))
    bstack111ll1ll11_opy_ = bstack111ll11_opy_ (u"ࠬ࠲ࠠࠨዿ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack111ll1l1l1_opy_:
        bstack1lll1ll1l1_opy_ = os.environ.get(bstack111ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ጀ"), bstack111ll11_opy_ (u"ࠧ࠱ࠩጁ"))
        bstack1l1l11l11_opy_ = {bstack111ll11_opy_ (u"ࠨࡰࡤࡱࡪ࠭ጂ"): test_name, bstack111ll11_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨጃ"): bstack111ll1ll11_opy_, bstack111ll11_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩጄ"): bstack1lll1ll1l1_opy_}
        bstack111llll111_opy_ = []
        bstack111lll1l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack111ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡵࡶࡰࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪጅ"))
        if os.path.exists(bstack111lll1l1l_opy_):
            with open(bstack111lll1l1l_opy_) as f:
                bstack111llll111_opy_ = json.load(f)
        bstack111llll111_opy_.append(bstack1l1l11l11_opy_)
        with open(bstack111lll1l1l_opy_, bstack111ll11_opy_ (u"ࠬࡽࠧጆ")) as f:
            json.dump(bstack111llll111_opy_, f)
    else:
        bstack1l1l11l11_opy_ = {bstack111ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫጇ"): test_name, bstack111ll11_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ገ"): bstack111ll1ll11_opy_, bstack111ll11_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧጉ"): str(multiprocessing.current_process().name)}
        if bstack111ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭ጊ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1l1l11l11_opy_)
  except Exception as e:
      logger.warn(bstack111ll11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡶࡹࡵࡧࡶࡸࠥ࡬ࡵ࡯ࡰࡨࡰࠥࡪࡡࡵࡣ࠽ࠤࢀࢃࠢጋ").format(e))
def bstack111l1lll1_opy_(error_message, test_name, index, logger):
  try:
    bstack111lll11l1_opy_ = []
    bstack1l1l11l11_opy_ = {bstack111ll11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩጌ"): test_name, bstack111ll11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫግ"): error_message, bstack111ll11_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬጎ"): index}
    bstack11l1111l11_opy_ = os.path.join(tempfile.gettempdir(), bstack111ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨጏ"))
    if os.path.exists(bstack11l1111l11_opy_):
        with open(bstack11l1111l11_opy_) as f:
            bstack111lll11l1_opy_ = json.load(f)
    bstack111lll11l1_opy_.append(bstack1l1l11l11_opy_)
    with open(bstack11l1111l11_opy_, bstack111ll11_opy_ (u"ࠨࡹࠪጐ")) as f:
        json.dump(bstack111lll11l1_opy_, f)
  except Exception as e:
    logger.warn(bstack111ll11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧ጑").format(e))
def bstack111l1111l_opy_(bstack11ll11ll_opy_, name, logger):
  try:
    bstack1l1l11l11_opy_ = {bstack111ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨጒ"): name, bstack111ll11_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪጓ"): bstack11ll11ll_opy_, bstack111ll11_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫጔ"): str(threading.current_thread()._name)}
    return bstack1l1l11l11_opy_
  except Exception as e:
    logger.warn(bstack111ll11_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡤࡨ࡬ࡦࡼࡥࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥጕ").format(e))
  return
def bstack111ll1ll1l_opy_():
    return platform.system() == bstack111ll11_opy_ (u"ࠧࡘ࡫ࡱࡨࡴࡽࡳࠨ጖")
def bstack1ll11ll11l_opy_(bstack11l111111l_opy_, config, logger):
    bstack11l111l11l_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack11l111111l_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack111ll11_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡬ࡵࡧࡵࠤࡨࡵ࡮ࡧ࡫ࡪࠤࡰ࡫ࡹࡴࠢࡥࡽࠥࡸࡥࡨࡧࡻࠤࡲࡧࡴࡤࡪ࠽ࠤࢀࢃࠢ጗").format(e))
    return bstack11l111l11l_opy_