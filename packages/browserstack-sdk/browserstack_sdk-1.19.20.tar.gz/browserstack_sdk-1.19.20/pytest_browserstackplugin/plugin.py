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
import atexit
import datetime
import inspect
import logging
import os
import signal
import sys
import threading
from uuid import uuid4
from bstack_utils.percy_sdk import PercySDK
import tempfile
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack111ll1ll1_opy_, bstack1ll11l1111_opy_, update, bstack111lll11l_opy_,
                                       bstack1ll1l1l1ll_opy_, bstack111ll1l1l_opy_, bstack1ll1l11111_opy_, bstack1ll11111l_opy_,
                                       bstack1l111l1l_opy_, bstack1l1l11llll_opy_, bstack1l1llllll1_opy_, bstack1l1ll111_opy_,
                                       bstack1ll11111ll_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1l1l111l1l_opy_)
from browserstack_sdk.bstack1lll1l111l_opy_ import bstack111111ll1_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack1l11l111l_opy_
from bstack_utils.capture import bstack11llll1l11_opy_
from bstack_utils.config import Config
from bstack_utils.constants import bstack111l111ll_opy_, bstack1ll11l11l1_opy_, bstack1ll11lll11_opy_, \
    bstack1lllll1lll_opy_
from bstack_utils.helper import bstack1ll1l1l1_opy_, bstack1ll11l1l1_opy_, bstack111llll11l_opy_, bstack1lll1l1l11_opy_, \
    bstack111llllll1_opy_, \
    bstack11l11ll11l_opy_, bstack1l111lll1_opy_, bstack1lll11l11_opy_, bstack111lll111l_opy_, bstack1l1llll1l1_opy_, Notset, \
    bstack1l11111l_opy_, bstack11l111l1l1_opy_, bstack111llll1ll_opy_, Result, bstack11l1111111_opy_, bstack111lllll1l_opy_, bstack11lllll111_opy_, \
    bstack1ll1llll1l_opy_, bstack1l11l1l11l_opy_, bstack1lll1lll1_opy_, bstack111ll1ll1l_opy_
from bstack_utils.bstack111ll11l11_opy_ import bstack111l1ll1ll_opy_
from bstack_utils.messages import bstack1l11111l1_opy_, bstack1ll1lllll_opy_, bstack1ll11ll1ll_opy_, bstack1llll1l11_opy_, bstack1llllll1l_opy_, \
    bstack11ll1l1l_opy_, bstack1l11l1lll_opy_, bstack1ll1ll1111_opy_, bstack1ll1ll11l1_opy_, bstack1l1ll11ll1_opy_, \
    bstack1lllll111l_opy_, bstack11llll11l_opy_
from bstack_utils.proxy import bstack1llll1111l_opy_, bstack1l1lll1l1_opy_
from bstack_utils.bstack1111l111l_opy_ import bstack1llllll11l1_opy_, bstack1llllll1lll_opy_, bstack1llllll1ll1_opy_, bstack1lllll1ll1l_opy_, \
    bstack1lllll1l1ll_opy_, bstack1llllll1l1l_opy_, bstack1llllll11ll_opy_, bstack11l1l1l11_opy_, bstack1llllll1111_opy_
from bstack_utils.bstack1111l1111_opy_ import bstack1llll1l1_opy_
from bstack_utils.bstack1l1lllll1_opy_ import bstack1llll11l_opy_, bstack1111lllll_opy_, bstack1l1lll1ll_opy_, \
    bstack1l1lll11_opy_, bstack111lllll1_opy_
from bstack_utils.bstack1l11111l11_opy_ import bstack11lll1lll1_opy_
from bstack_utils.bstack1111111ll_opy_ import bstack11l1ll1l_opy_
import bstack_utils.bstack111ll111_opy_ as bstack1llll1lll1_opy_
from bstack_utils.bstack1lll11ll1_opy_ import bstack1lll11ll1_opy_
bstack1l111ll1l_opy_ = None
bstack1ll1lll1ll_opy_ = None
bstack1l111l11_opy_ = None
bstack1l111l1l1_opy_ = None
bstack11l1111l1_opy_ = None
bstack1ll1lll1l_opy_ = None
bstack1111111l_opy_ = None
bstack11lll111l_opy_ = None
bstack11l1111ll_opy_ = None
bstack1llllllll_opy_ = None
bstack1ll1l11lll_opy_ = None
bstack1ll111111l_opy_ = None
bstack1l11lll11l_opy_ = None
bstack11l11llll_opy_ = bstack111ll11_opy_ (u"ࠩࠪᗆ")
CONFIG = {}
bstack1l1l111111_opy_ = False
bstack1l1ll1l1l_opy_ = bstack111ll11_opy_ (u"ࠪࠫᗇ")
bstack1lll1l1111_opy_ = bstack111ll11_opy_ (u"ࠫࠬᗈ")
bstack111ll1l11_opy_ = False
bstack1111llll_opy_ = []
bstack1ll1111lll_opy_ = bstack111l111ll_opy_
bstack1lll1l11l1l_opy_ = bstack111ll11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᗉ")
bstack1lll1l1l1l1_opy_ = False
bstack1lll1l11ll_opy_ = {}
bstack1l11111ll_opy_ = False
logger = bstack1l11l111l_opy_.get_logger(__name__, bstack1ll1111lll_opy_)
store = {
    bstack111ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᗊ"): []
}
bstack1lll1l1l111_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_11lll1l1l1_opy_ = {}
current_test_uuid = None
def bstack11l1llll_opy_(page, bstack111l111l1_opy_):
    try:
        page.evaluate(bstack111ll11_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣᗋ"),
                      bstack111ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠬᗌ") + json.dumps(
                          bstack111l111l1_opy_) + bstack111ll11_opy_ (u"ࠤࢀࢁࠧᗍ"))
    except Exception as e:
        print(bstack111ll11_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥࢁࡽࠣᗎ"), e)
def bstack11ll11lll_opy_(page, message, level):
    try:
        page.evaluate(bstack111ll11_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧᗏ"), bstack111ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪᗐ") + json.dumps(
            message) + bstack111ll11_opy_ (u"࠭ࠬࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠩᗑ") + json.dumps(level) + bstack111ll11_opy_ (u"ࠧࡾࡿࠪᗒ"))
    except Exception as e:
        print(bstack111ll11_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡦࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠡࡽࢀࠦᗓ"), e)
def pytest_configure(config):
    bstack1l1ll1l1l1_opy_ = Config.bstack1lll111ll_opy_()
    config.args = bstack11l1ll1l_opy_.bstack1lll1ll11ll_opy_(config.args)
    bstack1l1ll1l1l1_opy_.bstack1111l111_opy_(bstack1lll1lll1_opy_(config.getoption(bstack111ll11_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ᗔ"))))
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack1lll11lll1l_opy_ = item.config.getoption(bstack111ll11_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᗕ"))
    plugins = item.config.getoption(bstack111ll11_opy_ (u"ࠦࡵࡲࡵࡨ࡫ࡱࡷࠧᗖ"))
    report = outcome.get_result()
    bstack1lll11l11ll_opy_(item, call, report)
    if bstack111ll11_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡴࡱࡻࡧࡪࡰࠥᗗ") not in plugins or bstack1l1llll1l1_opy_():
        return
    summary = []
    driver = getattr(item, bstack111ll11_opy_ (u"ࠨ࡟ࡥࡴ࡬ࡺࡪࡸࠢᗘ"), None)
    page = getattr(item, bstack111ll11_opy_ (u"ࠢࡠࡲࡤ࡫ࡪࠨᗙ"), None)
    try:
        if (driver == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack1lll11ll1l1_opy_(item, report, summary, bstack1lll11lll1l_opy_)
    if (page is not None):
        bstack1lll11lllll_opy_(item, report, summary, bstack1lll11lll1l_opy_)
def bstack1lll11ll1l1_opy_(item, report, summary, bstack1lll11lll1l_opy_):
    if report.when == bstack111ll11_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧᗚ") and report.skipped:
        bstack1llllll1111_opy_(report)
    if report.when in [bstack111ll11_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣᗛ"), bstack111ll11_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧᗜ")]:
        return
    if not bstack111llll11l_opy_():
        return
    try:
        if (str(bstack1lll11lll1l_opy_).lower() != bstack111ll11_opy_ (u"ࠫࡹࡸࡵࡦࠩᗝ")):
            item._driver.execute_script(
                bstack111ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪᗞ") + json.dumps(
                    report.nodeid) + bstack111ll11_opy_ (u"࠭ࡽࡾࠩᗟ"))
        os.environ[bstack111ll11_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪᗠ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack111ll11_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧ࠽ࠤࢀ࠶ࡽࠣᗡ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111ll11_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦᗢ")))
    bstack11l1ll1l1_opy_ = bstack111ll11_opy_ (u"ࠥࠦᗣ")
    bstack1llllll1111_opy_(report)
    if not passed:
        try:
            bstack11l1ll1l1_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack111ll11_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡲࡦࡣࡶࡳࡳࡀࠠࡼ࠲ࢀࠦᗤ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack11l1ll1l1_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack111ll11_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢᗥ")))
        bstack11l1ll1l1_opy_ = bstack111ll11_opy_ (u"ࠨࠢᗦ")
        if not passed:
            try:
                bstack11l1ll1l1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111ll11_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡵࡩࡦࡹ࡯࡯࠼ࠣࡿ࠵ࢃࠢᗧ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack11l1ll1l1_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack111ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤ࠯ࠤࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡩࡧࡴࡢࠤ࠽ࠤࠬᗨ")
                    + json.dumps(bstack111ll11_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠣࠥᗩ"))
                    + bstack111ll11_opy_ (u"ࠥࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࠨᗪ")
                )
            else:
                item._driver.execute_script(
                    bstack111ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࠬࠡ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡦࡤࡸࡦࠨ࠺ࠡࠩᗫ")
                    + json.dumps(str(bstack11l1ll1l1_opy_))
                    + bstack111ll11_opy_ (u"ࠧࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠣᗬ")
                )
        except Exception as e:
            summary.append(bstack111ll11_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡦࡴ࡮ࡰࡶࡤࡸࡪࡀࠠࡼ࠲ࢀࠦᗭ").format(e))
def bstack1lll11l1111_opy_(test_name, error_message):
    try:
        bstack1lll1l1lll1_opy_ = []
        bstack1lll1ll1l1_opy_ = os.environ.get(bstack111ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᗮ"), bstack111ll11_opy_ (u"ࠨ࠲ࠪᗯ"))
        bstack1l1l11l11_opy_ = {bstack111ll11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᗰ"): test_name, bstack111ll11_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᗱ"): error_message, bstack111ll11_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᗲ"): bstack1lll1ll1l1_opy_}
        bstack1lll1l1l11l_opy_ = os.path.join(tempfile.gettempdir(), bstack111ll11_opy_ (u"ࠬࡶࡷࡠࡲࡼࡸࡪࡹࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪᗳ"))
        if os.path.exists(bstack1lll1l1l11l_opy_):
            with open(bstack1lll1l1l11l_opy_) as f:
                bstack1lll1l1lll1_opy_ = json.load(f)
        bstack1lll1l1lll1_opy_.append(bstack1l1l11l11_opy_)
        with open(bstack1lll1l1l11l_opy_, bstack111ll11_opy_ (u"࠭ࡷࠨᗴ")) as f:
            json.dump(bstack1lll1l1lll1_opy_, f)
    except Exception as e:
        logger.debug(bstack111ll11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡩࡷࡹࡩࡴࡶ࡬ࡲ࡬ࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡴࡾࡺࡥࡴࡶࠣࡩࡷࡸ࡯ࡳࡵ࠽ࠤࠬᗵ") + str(e))
def bstack1lll11lllll_opy_(item, report, summary, bstack1lll11lll1l_opy_):
    if report.when in [bstack111ll11_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢᗶ"), bstack111ll11_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࠦᗷ")]:
        return
    if (str(bstack1lll11lll1l_opy_).lower() != bstack111ll11_opy_ (u"ࠪࡸࡷࡻࡥࠨᗸ")):
        bstack11l1llll_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111ll11_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᗹ")))
    bstack11l1ll1l1_opy_ = bstack111ll11_opy_ (u"ࠧࠨᗺ")
    bstack1llllll1111_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack11l1ll1l1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111ll11_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨᗻ").format(e)
                )
        try:
            if passed:
                bstack111lllll1_opy_(getattr(item, bstack111ll11_opy_ (u"ࠧࡠࡲࡤ࡫ࡪ࠭ᗼ"), None), bstack111ll11_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣᗽ"))
            else:
                error_message = bstack111ll11_opy_ (u"ࠩࠪᗾ")
                if bstack11l1ll1l1_opy_:
                    bstack11ll11lll_opy_(item._page, str(bstack11l1ll1l1_opy_), bstack111ll11_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤᗿ"))
                    bstack111lllll1_opy_(getattr(item, bstack111ll11_opy_ (u"ࠫࡤࡶࡡࡨࡧࠪᘀ"), None), bstack111ll11_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧᘁ"), str(bstack11l1ll1l1_opy_))
                    error_message = str(bstack11l1ll1l1_opy_)
                else:
                    bstack111lllll1_opy_(getattr(item, bstack111ll11_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬᘂ"), None), bstack111ll11_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢᘃ"))
                bstack1lll11l1111_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack111ll11_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡵࡱࡦࡤࡸࡪࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽ࠳ࢁࠧᘄ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack111ll11_opy_ (u"ࠤ࠰࠱ࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨᘅ"), default=bstack111ll11_opy_ (u"ࠥࡊࡦࡲࡳࡦࠤᘆ"), help=bstack111ll11_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡩࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠥᘇ"))
    parser.addoption(bstack111ll11_opy_ (u"ࠧ࠳࠭ࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᘈ"), default=bstack111ll11_opy_ (u"ࠨࡆࡢ࡮ࡶࡩࠧᘉ"), help=bstack111ll11_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡪࡥࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠨᘊ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack111ll11_opy_ (u"ࠣ࠯࠰ࡨࡷ࡯ࡶࡦࡴࠥᘋ"), action=bstack111ll11_opy_ (u"ࠤࡶࡸࡴࡸࡥࠣᘌ"), default=bstack111ll11_opy_ (u"ࠥࡧ࡭ࡸ࡯࡮ࡧࠥᘍ"),
                         help=bstack111ll11_opy_ (u"ࠦࡉࡸࡩࡷࡧࡵࠤࡹࡵࠠࡳࡷࡱࠤࡹ࡫ࡳࡵࡵࠥᘎ"))
def bstack1l1111lll1_opy_(log):
    if not (log[bstack111ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᘏ")] and log[bstack111ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᘐ")].strip()):
        return
    active = bstack1l111llll1_opy_()
    log = {
        bstack111ll11_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᘑ"): log[bstack111ll11_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᘒ")],
        bstack111ll11_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬᘓ"): datetime.datetime.utcnow().isoformat() + bstack111ll11_opy_ (u"ࠪ࡞ࠬᘔ"),
        bstack111ll11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᘕ"): log[bstack111ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᘖ")],
    }
    if active:
        if active[bstack111ll11_opy_ (u"࠭ࡴࡺࡲࡨࠫᘗ")] == bstack111ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᘘ"):
            log[bstack111ll11_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᘙ")] = active[bstack111ll11_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᘚ")]
        elif active[bstack111ll11_opy_ (u"ࠪࡸࡾࡶࡥࠨᘛ")] == bstack111ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࠩᘜ"):
            log[bstack111ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᘝ")] = active[bstack111ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᘞ")]
    bstack11l1ll1l_opy_.bstack1l1lll11ll_opy_([log])
def bstack1l111llll1_opy_():
    if len(store[bstack111ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᘟ")]) > 0 and store[bstack111ll11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᘠ")][-1]:
        return {
            bstack111ll11_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᘡ"): bstack111ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᘢ"),
            bstack111ll11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᘣ"): store[bstack111ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᘤ")][-1]
        }
    if store.get(bstack111ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᘥ"), None):
        return {
            bstack111ll11_opy_ (u"ࠧࡵࡻࡳࡩࠬᘦ"): bstack111ll11_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᘧ"),
            bstack111ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᘨ"): store[bstack111ll11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᘩ")]
        }
    return None
bstack1l11l1111l_opy_ = bstack11llll1l11_opy_(bstack1l1111lll1_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        global bstack1lll1l1l1l1_opy_
        item._1lll1l1ll11_opy_ = True
        bstack1lllll1ll1_opy_ = bstack1llll1lll1_opy_.bstack1lllll11ll_opy_(CONFIG, bstack11l11ll11l_opy_(item.own_markers))
        item._a11y_test_case = bstack1lllll1ll1_opy_
        if bstack1lll1l1l1l1_opy_:
            driver = getattr(item, bstack111ll11_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬᘪ"), None)
            item._a11y_started = bstack1llll1lll1_opy_.bstack1l11ll1ll1_opy_(driver, bstack1lllll1ll1_opy_)
        if not bstack11l1ll1l_opy_.on() or bstack1lll1l11l1l_opy_ != bstack111ll11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᘫ"):
            return
        global current_test_uuid, bstack1l11l1111l_opy_
        bstack1l11l1111l_opy_.start()
        bstack11lllllll1_opy_ = {
            bstack111ll11_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᘬ"): uuid4().__str__(),
            bstack111ll11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᘭ"): datetime.datetime.utcnow().isoformat() + bstack111ll11_opy_ (u"ࠨ࡜ࠪᘮ")
        }
        current_test_uuid = bstack11lllllll1_opy_[bstack111ll11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᘯ")]
        store[bstack111ll11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᘰ")] = bstack11lllllll1_opy_[bstack111ll11_opy_ (u"ࠫࡺࡻࡩࡥࠩᘱ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _11lll1l1l1_opy_[item.nodeid] = {**_11lll1l1l1_opy_[item.nodeid], **bstack11lllllll1_opy_}
        bstack1lll1l111ll_opy_(item, _11lll1l1l1_opy_[item.nodeid], bstack111ll11_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᘲ"))
    except Exception as err:
        print(bstack111ll11_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡸࡵ࡯ࡶࡨࡷࡹࡥࡣࡢ࡮࡯࠾ࠥࢁࡽࠨᘳ"), str(err))
def pytest_runtest_setup(item):
    global bstack1lll1l1l111_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack111lll111l_opy_():
        atexit.register(bstack111111l1l_opy_)
        if not bstack1lll1l1l111_opy_:
            try:
                bstack1lll11ll11l_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack111ll1ll1l_opy_():
                    bstack1lll11ll11l_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1lll11ll11l_opy_:
                    signal.signal(s, bstack1lll1l11111_opy_)
                bstack1lll1l1l111_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack111ll11_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩ࡬࡯ࡳࡵࡧࡵࠤࡸ࡯ࡧ࡯ࡣ࡯ࠤ࡭ࡧ࡮ࡥ࡮ࡨࡶࡸࡀࠠࠣᘴ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1llllll11l1_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack111ll11_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᘵ")
    try:
        if not bstack11l1ll1l_opy_.on():
            return
        bstack1l11l1111l_opy_.start()
        uuid = uuid4().__str__()
        bstack11lllllll1_opy_ = {
            bstack111ll11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᘶ"): uuid,
            bstack111ll11_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᘷ"): datetime.datetime.utcnow().isoformat() + bstack111ll11_opy_ (u"ࠫ࡟࠭ᘸ"),
            bstack111ll11_opy_ (u"ࠬࡺࡹࡱࡧࠪᘹ"): bstack111ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᘺ"),
            bstack111ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᘻ"): bstack111ll11_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᘼ"),
            bstack111ll11_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬᘽ"): bstack111ll11_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᘾ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack111ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨᘿ")] = item
        store[bstack111ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᙀ")] = [uuid]
        if not _11lll1l1l1_opy_.get(item.nodeid, None):
            _11lll1l1l1_opy_[item.nodeid] = {bstack111ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᙁ"): [], bstack111ll11_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩᙂ"): []}
        _11lll1l1l1_opy_[item.nodeid][bstack111ll11_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᙃ")].append(bstack11lllllll1_opy_[bstack111ll11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᙄ")])
        _11lll1l1l1_opy_[item.nodeid + bstack111ll11_opy_ (u"ࠪ࠱ࡸ࡫ࡴࡶࡲࠪᙅ")] = bstack11lllllll1_opy_
        bstack1lll1l1llll_opy_(item, bstack11lllllll1_opy_, bstack111ll11_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᙆ"))
    except Exception as err:
        print(bstack111ll11_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡹࡥࡵࡷࡳ࠾ࠥࢁࡽࠨᙇ"), str(err))
def pytest_runtest_teardown(item):
    try:
        global bstack1lll1l11ll_opy_
        if CONFIG.get(bstack111ll11_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬᙈ"), False):
            if CONFIG.get(bstack111ll11_opy_ (u"ࠧࡱࡧࡵࡧࡾࡉࡡࡱࡶࡸࡶࡪࡓ࡯ࡥࡧࠪᙉ"), bstack111ll11_opy_ (u"ࠣࡣࡸࡸࡴࠨᙊ")) == bstack111ll11_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦᙋ"):
                bstack1lll1l1l1ll_opy_ = bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠪࡴࡪࡸࡣࡺࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᙌ"), None)
                bstack11111llll_opy_ = bstack1lll1l1l1ll_opy_ + bstack111ll11_opy_ (u"ࠦ࠲ࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᙍ")
                driver = getattr(item, bstack111ll11_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ᙎ"), None)
                PercySDK.screenshot(driver, bstack11111llll_opy_)
        if getattr(item, bstack111ll11_opy_ (u"࠭࡟ࡢ࠳࠴ࡽࡤࡹࡴࡢࡴࡷࡩࡩ࠭ᙏ"), False):
            bstack111111ll1_opy_.bstack1lllllll1_opy_(getattr(item, bstack111ll11_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨᙐ"), None), bstack1lll1l11ll_opy_, logger, item)
        if not bstack11l1ll1l_opy_.on():
            return
        bstack11lllllll1_opy_ = {
            bstack111ll11_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᙑ"): uuid4().__str__(),
            bstack111ll11_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᙒ"): datetime.datetime.utcnow().isoformat() + bstack111ll11_opy_ (u"ࠪ࡞ࠬᙓ"),
            bstack111ll11_opy_ (u"ࠫࡹࡿࡰࡦࠩᙔ"): bstack111ll11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᙕ"),
            bstack111ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩᙖ"): bstack111ll11_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᙗ"),
            bstack111ll11_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫᙘ"): bstack111ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫᙙ")
        }
        _11lll1l1l1_opy_[item.nodeid + bstack111ll11_opy_ (u"ࠪ࠱ࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ᙚ")] = bstack11lllllll1_opy_
        bstack1lll1l1llll_opy_(item, bstack11lllllll1_opy_, bstack111ll11_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᙛ"))
    except Exception as err:
        print(bstack111ll11_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡷࡻ࡮ࡵࡧࡶࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࠺ࠡࡽࢀࠫᙜ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack11l1ll1l_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack1lllll1ll1l_opy_(fixturedef.argname):
        store[bstack111ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡪࡶࡨࡱࠬᙝ")] = request.node
    elif bstack1lllll1l1ll_opy_(fixturedef.argname):
        store[bstack111ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡥ࡯ࡥࡸࡹ࡟ࡪࡶࡨࡱࠬᙞ")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack111ll11_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᙟ"): fixturedef.argname,
            bstack111ll11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᙠ"): bstack111llllll1_opy_(outcome),
            bstack111ll11_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬᙡ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack111ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨᙢ")]
        if not _11lll1l1l1_opy_.get(current_test_item.nodeid, None):
            _11lll1l1l1_opy_[current_test_item.nodeid] = {bstack111ll11_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧᙣ"): []}
        _11lll1l1l1_opy_[current_test_item.nodeid][bstack111ll11_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨᙤ")].append(fixture)
    except Exception as err:
        logger.debug(bstack111ll11_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡴࡧࡷࡹࡵࡀࠠࡼࡿࠪᙥ"), str(err))
if bstack1l1llll1l1_opy_() and bstack11l1ll1l_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _11lll1l1l1_opy_[request.node.nodeid][bstack111ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᙦ")].bstack1llll11ll11_opy_(id(step))
        except Exception as err:
            print(bstack111ll11_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲ࠽ࠤࢀࢃࠧᙧ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _11lll1l1l1_opy_[request.node.nodeid][bstack111ll11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ᙨ")].bstack11llllll11_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack111ll11_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡴࡶࡨࡴࡤ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠨᙩ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack1l11111l11_opy_: bstack11lll1lll1_opy_ = _11lll1l1l1_opy_[request.node.nodeid][bstack111ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨᙪ")]
            bstack1l11111l11_opy_.bstack11llllll11_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack111ll11_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡶࡸࡪࡶ࡟ࡦࡴࡵࡳࡷࡀࠠࡼࡿࠪᙫ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1lll1l11l1l_opy_
        try:
            if not bstack11l1ll1l_opy_.on() or bstack1lll1l11l1l_opy_ != bstack111ll11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫᙬ"):
                return
            global bstack1l11l1111l_opy_
            bstack1l11l1111l_opy_.start()
            driver = bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ᙭"), None)
            if not _11lll1l1l1_opy_.get(request.node.nodeid, None):
                _11lll1l1l1_opy_[request.node.nodeid] = {}
            bstack1l11111l11_opy_ = bstack11lll1lll1_opy_.bstack1llll111l11_opy_(
                scenario, feature, request.node,
                name=bstack1llllll1l1l_opy_(request.node, scenario),
                bstack1l1111llll_opy_=bstack1lll1l1l11_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack111ll11_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫ᙮"),
                tags=bstack1llllll11ll_opy_(feature, scenario),
                bstack1l1111ll11_opy_=bstack11l1ll1l_opy_.bstack1l11111ll1_opy_(driver) if driver and driver.session_id else {}
            )
            _11lll1l1l1_opy_[request.node.nodeid][bstack111ll11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ᙯ")] = bstack1l11111l11_opy_
            bstack1lll111ll1l_opy_(bstack1l11111l11_opy_.uuid)
            bstack11l1ll1l_opy_.bstack11llll1lll_opy_(bstack111ll11_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᙰ"), bstack1l11111l11_opy_)
        except Exception as err:
            print(bstack111ll11_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱ࠽ࠤࢀࢃࠧᙱ"), str(err))
def bstack1lll1l1111l_opy_(bstack1lll111llll_opy_):
    if bstack1lll111llll_opy_ in store[bstack111ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᙲ")]:
        store[bstack111ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᙳ")].remove(bstack1lll111llll_opy_)
def bstack1lll111ll1l_opy_(bstack1lll11lll11_opy_):
    store[bstack111ll11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᙴ")] = bstack1lll11lll11_opy_
    threading.current_thread().current_test_uuid = bstack1lll11lll11_opy_
@bstack11l1ll1l_opy_.bstack1lll1llll1l_opy_
def bstack1lll11l11ll_opy_(item, call, report):
    global bstack1lll1l11l1l_opy_
    bstack11l11lll_opy_ = bstack1lll1l1l11_opy_()
    if hasattr(report, bstack111ll11_opy_ (u"ࠩࡶࡸࡴࡶࠧᙵ")):
        bstack11l11lll_opy_ = bstack11l1111111_opy_(report.stop)
    if hasattr(report, bstack111ll11_opy_ (u"ࠪࡷࡹࡧࡲࡵࠩᙶ")):
        bstack11l11lll_opy_ = bstack11l1111111_opy_(report.start)
    try:
        if getattr(report, bstack111ll11_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩᙷ"), bstack111ll11_opy_ (u"ࠬ࠭ᙸ")) == bstack111ll11_opy_ (u"࠭ࡣࡢ࡮࡯ࠫᙹ"):
            bstack1l11l1111l_opy_.reset()
        if getattr(report, bstack111ll11_opy_ (u"ࠧࡸࡪࡨࡲࠬᙺ"), bstack111ll11_opy_ (u"ࠨࠩᙻ")) == bstack111ll11_opy_ (u"ࠩࡦࡥࡱࡲࠧᙼ"):
            if bstack1lll1l11l1l_opy_ == bstack111ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᙽ"):
                _11lll1l1l1_opy_[item.nodeid][bstack111ll11_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᙾ")] = bstack11l11lll_opy_
                bstack1lll1l111ll_opy_(item, _11lll1l1l1_opy_[item.nodeid], bstack111ll11_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᙿ"), report, call)
                store[bstack111ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ ")] = None
            elif bstack1lll1l11l1l_opy_ == bstack111ll11_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦᚁ"):
                bstack1l11111l11_opy_ = _11lll1l1l1_opy_[item.nodeid][bstack111ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᚂ")]
                bstack1l11111l11_opy_.set(hooks=_11lll1l1l1_opy_[item.nodeid].get(bstack111ll11_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᚃ"), []))
                exception, bstack1l11111l1l_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1l11111l1l_opy_ = [call.excinfo.exconly(), getattr(report, bstack111ll11_opy_ (u"ࠪࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠩᚄ"), bstack111ll11_opy_ (u"ࠫࠬᚅ"))]
                bstack1l11111l11_opy_.stop(time=bstack11l11lll_opy_, result=Result(result=getattr(report, bstack111ll11_opy_ (u"ࠬࡵࡵࡵࡥࡲࡱࡪ࠭ᚆ"), bstack111ll11_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᚇ")), exception=exception, bstack1l11111l1l_opy_=bstack1l11111l1l_opy_))
                bstack11l1ll1l_opy_.bstack11llll1lll_opy_(bstack111ll11_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᚈ"), _11lll1l1l1_opy_[item.nodeid][bstack111ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᚉ")])
        elif getattr(report, bstack111ll11_opy_ (u"ࠩࡺ࡬ࡪࡴࠧᚊ"), bstack111ll11_opy_ (u"ࠪࠫᚋ")) in [bstack111ll11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᚌ"), bstack111ll11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧᚍ")]:
            bstack1l11l111l1_opy_ = item.nodeid + bstack111ll11_opy_ (u"࠭࠭ࠨᚎ") + getattr(report, bstack111ll11_opy_ (u"ࠧࡸࡪࡨࡲࠬᚏ"), bstack111ll11_opy_ (u"ࠨࠩᚐ"))
            if getattr(report, bstack111ll11_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᚑ"), False):
                hook_type = bstack111ll11_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨᚒ") if getattr(report, bstack111ll11_opy_ (u"ࠫࡼ࡮ࡥ࡯ࠩᚓ"), bstack111ll11_opy_ (u"ࠬ࠭ᚔ")) == bstack111ll11_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬᚕ") else bstack111ll11_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᚖ")
                _11lll1l1l1_opy_[bstack1l11l111l1_opy_] = {
                    bstack111ll11_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᚗ"): uuid4().__str__(),
                    bstack111ll11_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᚘ"): bstack11l11lll_opy_,
                    bstack111ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ᚙ"): hook_type
                }
            _11lll1l1l1_opy_[bstack1l11l111l1_opy_][bstack111ll11_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᚚ")] = bstack11l11lll_opy_
            bstack1lll1l1111l_opy_(_11lll1l1l1_opy_[bstack1l11l111l1_opy_][bstack111ll11_opy_ (u"ࠬࡻࡵࡪࡦࠪ᚛")])
            bstack1lll1l1llll_opy_(item, _11lll1l1l1_opy_[bstack1l11l111l1_opy_], bstack111ll11_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ᚜"), report, call)
            if getattr(report, bstack111ll11_opy_ (u"ࠧࡸࡪࡨࡲࠬ᚝"), bstack111ll11_opy_ (u"ࠨࠩ᚞")) == bstack111ll11_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨ᚟"):
                if getattr(report, bstack111ll11_opy_ (u"ࠪࡳࡺࡺࡣࡰ࡯ࡨࠫᚠ"), bstack111ll11_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᚡ")) == bstack111ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᚢ"):
                    bstack11lllllll1_opy_ = {
                        bstack111ll11_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᚣ"): uuid4().__str__(),
                        bstack111ll11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᚤ"): bstack1lll1l1l11_opy_(),
                        bstack111ll11_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᚥ"): bstack1lll1l1l11_opy_()
                    }
                    _11lll1l1l1_opy_[item.nodeid] = {**_11lll1l1l1_opy_[item.nodeid], **bstack11lllllll1_opy_}
                    bstack1lll1l111ll_opy_(item, _11lll1l1l1_opy_[item.nodeid], bstack111ll11_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᚦ"))
                    bstack1lll1l111ll_opy_(item, _11lll1l1l1_opy_[item.nodeid], bstack111ll11_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᚧ"), report, call)
    except Exception as err:
        print(bstack111ll11_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡦࡴࡤ࡭ࡧࡢࡳ࠶࠷ࡹࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸ࠿ࠦࡻࡾࠩᚨ"), str(err))
def bstack1lll11ll111_opy_(test, bstack11lllllll1_opy_, result=None, call=None, bstack11ll11l11_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1l11111l11_opy_ = {
        bstack111ll11_opy_ (u"ࠬࡻࡵࡪࡦࠪᚩ"): bstack11lllllll1_opy_[bstack111ll11_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᚪ")],
        bstack111ll11_opy_ (u"ࠧࡵࡻࡳࡩࠬᚫ"): bstack111ll11_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᚬ"),
        bstack111ll11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᚭ"): test.name,
        bstack111ll11_opy_ (u"ࠪࡦࡴࡪࡹࠨᚮ"): {
            bstack111ll11_opy_ (u"ࠫࡱࡧ࡮ࡨࠩᚯ"): bstack111ll11_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬᚰ"),
            bstack111ll11_opy_ (u"࠭ࡣࡰࡦࡨࠫᚱ"): inspect.getsource(test.obj)
        },
        bstack111ll11_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫᚲ"): test.name,
        bstack111ll11_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࠧᚳ"): test.name,
        bstack111ll11_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩᚴ"): bstack11l1ll1l_opy_.bstack11llll1l1l_opy_(test),
        bstack111ll11_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ᚵ"): file_path,
        bstack111ll11_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭ᚶ"): file_path,
        bstack111ll11_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᚷ"): bstack111ll11_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧᚸ"),
        bstack111ll11_opy_ (u"ࠧࡷࡥࡢࡪ࡮ࡲࡥࡱࡣࡷ࡬ࠬᚹ"): file_path,
        bstack111ll11_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᚺ"): bstack11lllllll1_opy_[bstack111ll11_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᚻ")],
        bstack111ll11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᚼ"): bstack111ll11_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷࠫᚽ"),
        bstack111ll11_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡗ࡫ࡲࡶࡰࡓࡥࡷࡧ࡭ࠨᚾ"): {
            bstack111ll11_opy_ (u"࠭ࡲࡦࡴࡸࡲࡤࡴࡡ࡮ࡧࠪᚿ"): test.nodeid
        },
        bstack111ll11_opy_ (u"ࠧࡵࡣࡪࡷࠬᛀ"): bstack11l11ll11l_opy_(test.own_markers)
    }
    if bstack11ll11l11_opy_ in [bstack111ll11_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᛁ"), bstack111ll11_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᛂ")]:
        bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠪࡱࡪࡺࡡࠨᛃ")] = {
            bstack111ll11_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭ᛄ"): bstack11lllllll1_opy_.get(bstack111ll11_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧᛅ"), [])
        }
    if bstack11ll11l11_opy_ == bstack111ll11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧᛆ"):
        bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᛇ")] = bstack111ll11_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᛈ")
        bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᛉ")] = bstack11lllllll1_opy_[bstack111ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᛊ")]
        bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᛋ")] = bstack11lllllll1_opy_[bstack111ll11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᛌ")]
    if result:
        bstack1l11111l11_opy_[bstack111ll11_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᛍ")] = result.outcome
        bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨᛎ")] = result.duration * 1000
        bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᛏ")] = bstack11lllllll1_opy_[bstack111ll11_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᛐ")]
        if result.failed:
            bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᛑ")] = bstack11l1ll1l_opy_.bstack11ll1l11l1_opy_(call.excinfo.typename)
            bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᛒ")] = bstack11l1ll1l_opy_.bstack1llll111111_opy_(call.excinfo, result)
        bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᛓ")] = bstack11lllllll1_opy_[bstack111ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᛔ")]
    if outcome:
        bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᛕ")] = bstack111llllll1_opy_(outcome)
        bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩᛖ")] = 0
        bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᛗ")] = bstack11lllllll1_opy_[bstack111ll11_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᛘ")]
        if bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᛙ")] == bstack111ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᛚ"):
            bstack1l11111l11_opy_[bstack111ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬᛛ")] = bstack111ll11_opy_ (u"ࠧࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠨᛜ")  # bstack1lll11l1ll1_opy_
            bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩᛝ")] = [{bstack111ll11_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᛞ"): [bstack111ll11_opy_ (u"ࠪࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠧᛟ")]}]
        bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᛠ")] = bstack11lllllll1_opy_[bstack111ll11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᛡ")]
    return bstack1l11111l11_opy_
def bstack1lll1l1ll1l_opy_(test, bstack1l111lll1l_opy_, bstack11ll11l11_opy_, result, call, outcome, bstack1lll11l1lll_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack1l111lll1l_opy_[bstack111ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩᛢ")]
    hook_name = bstack1l111lll1l_opy_[bstack111ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡴࡡ࡮ࡧࠪᛣ")]
    hook_data = {
        bstack111ll11_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᛤ"): bstack1l111lll1l_opy_[bstack111ll11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᛥ")],
        bstack111ll11_opy_ (u"ࠪࡸࡾࡶࡥࠨᛦ"): bstack111ll11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩᛧ"),
        bstack111ll11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᛨ"): bstack111ll11_opy_ (u"࠭ࡻࡾࠩᛩ").format(bstack1llllll1lll_opy_(hook_name)),
        bstack111ll11_opy_ (u"ࠧࡣࡱࡧࡽࠬᛪ"): {
            bstack111ll11_opy_ (u"ࠨ࡮ࡤࡲ࡬࠭᛫"): bstack111ll11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ᛬"),
            bstack111ll11_opy_ (u"ࠪࡧࡴࡪࡥࠨ᛭"): None
        },
        bstack111ll11_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࠪᛮ"): test.name,
        bstack111ll11_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬᛯ"): bstack11l1ll1l_opy_.bstack11llll1l1l_opy_(test, hook_name),
        bstack111ll11_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩᛰ"): file_path,
        bstack111ll11_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠩᛱ"): file_path,
        bstack111ll11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᛲ"): bstack111ll11_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪᛳ"),
        bstack111ll11_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨᛴ"): file_path,
        bstack111ll11_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᛵ"): bstack1l111lll1l_opy_[bstack111ll11_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᛶ")],
        bstack111ll11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᛷ"): bstack111ll11_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩᛸ") if bstack1lll1l11l1l_opy_ == bstack111ll11_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬ᛹") else bstack111ll11_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩ᛺"),
        bstack111ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭᛻"): hook_type
    }
    bstack1lll11l1l1l_opy_ = bstack11lll11ll1_opy_(_11lll1l1l1_opy_.get(test.nodeid, None))
    if bstack1lll11l1l1l_opy_:
        hook_data[bstack111ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡩࡥࠩ᛼")] = bstack1lll11l1l1l_opy_
    if result:
        hook_data[bstack111ll11_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ᛽")] = result.outcome
        hook_data[bstack111ll11_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ᛾")] = result.duration * 1000
        hook_data[bstack111ll11_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ᛿")] = bstack1l111lll1l_opy_[bstack111ll11_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᜀ")]
        if result.failed:
            hook_data[bstack111ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᜁ")] = bstack11l1ll1l_opy_.bstack11ll1l11l1_opy_(call.excinfo.typename)
            hook_data[bstack111ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᜂ")] = bstack11l1ll1l_opy_.bstack1llll111111_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack111ll11_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᜃ")] = bstack111llllll1_opy_(outcome)
        hook_data[bstack111ll11_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ᜄ")] = 100
        hook_data[bstack111ll11_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᜅ")] = bstack1l111lll1l_opy_[bstack111ll11_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᜆ")]
        if hook_data[bstack111ll11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᜇ")] == bstack111ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᜈ"):
            hook_data[bstack111ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᜉ")] = bstack111ll11_opy_ (u"࡚ࠫࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠬᜊ")  # bstack1lll11l1ll1_opy_
            hook_data[bstack111ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᜋ")] = [{bstack111ll11_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩᜌ"): [bstack111ll11_opy_ (u"ࠧࡴࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠫᜍ")]}]
    if bstack1lll11l1lll_opy_:
        hook_data[bstack111ll11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᜎ")] = bstack1lll11l1lll_opy_.result
        hook_data[bstack111ll11_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪᜏ")] = bstack11l111l1l1_opy_(bstack1l111lll1l_opy_[bstack111ll11_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᜐ")], bstack1l111lll1l_opy_[bstack111ll11_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᜑ")])
        hook_data[bstack111ll11_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᜒ")] = bstack1l111lll1l_opy_[bstack111ll11_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᜓ")]
        if hook_data[bstack111ll11_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺ᜔ࠧ")] == bstack111ll11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ᜕"):
            hook_data[bstack111ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨ᜖")] = bstack11l1ll1l_opy_.bstack11ll1l11l1_opy_(bstack1lll11l1lll_opy_.exception_type)
            hook_data[bstack111ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ᜗")] = [{bstack111ll11_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧ᜘"): bstack111llll1ll_opy_(bstack1lll11l1lll_opy_.exception)}]
    return hook_data
def bstack1lll1l111ll_opy_(test, bstack11lllllll1_opy_, bstack11ll11l11_opy_, result=None, call=None, outcome=None):
    bstack1l11111l11_opy_ = bstack1lll11ll111_opy_(test, bstack11lllllll1_opy_, result, call, bstack11ll11l11_opy_, outcome)
    driver = getattr(test, bstack111ll11_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭᜙"), None)
    if bstack11ll11l11_opy_ == bstack111ll11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ᜚") and driver:
        bstack1l11111l11_opy_[bstack111ll11_opy_ (u"ࠧࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸ࠭᜛")] = bstack11l1ll1l_opy_.bstack1l11111ll1_opy_(driver)
    if bstack11ll11l11_opy_ == bstack111ll11_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩ᜜"):
        bstack11ll11l11_opy_ = bstack111ll11_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ᜝")
    bstack1l1111ll1l_opy_ = {
        bstack111ll11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ᜞"): bstack11ll11l11_opy_,
        bstack111ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ᜟ"): bstack1l11111l11_opy_
    }
    bstack11l1ll1l_opy_.bstack11llllll1l_opy_(bstack1l1111ll1l_opy_)
def bstack1lll1l1llll_opy_(test, bstack11lllllll1_opy_, bstack11ll11l11_opy_, result=None, call=None, outcome=None, bstack1lll11l1lll_opy_=None):
    hook_data = bstack1lll1l1ll1l_opy_(test, bstack11lllllll1_opy_, bstack11ll11l11_opy_, result, call, outcome, bstack1lll11l1lll_opy_)
    bstack1l1111ll1l_opy_ = {
        bstack111ll11_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩᜠ"): bstack11ll11l11_opy_,
        bstack111ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨᜡ"): hook_data
    }
    bstack11l1ll1l_opy_.bstack11llllll1l_opy_(bstack1l1111ll1l_opy_)
def bstack11lll11ll1_opy_(bstack11lllllll1_opy_):
    if not bstack11lllllll1_opy_:
        return None
    if bstack11lllllll1_opy_.get(bstack111ll11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᜢ"), None):
        return getattr(bstack11lllllll1_opy_[bstack111ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᜣ")], bstack111ll11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᜤ"), None)
    return bstack11lllllll1_opy_.get(bstack111ll11_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᜥ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack11l1ll1l_opy_.on():
            return
        places = [bstack111ll11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᜦ"), bstack111ll11_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᜧ"), bstack111ll11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᜨ")]
        bstack1l111l1l11_opy_ = []
        for bstack1lll11l111l_opy_ in places:
            records = caplog.get_records(bstack1lll11l111l_opy_)
            bstack1lll1l11ll1_opy_ = bstack111ll11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᜩ") if bstack1lll11l111l_opy_ == bstack111ll11_opy_ (u"ࠨࡥࡤࡰࡱ࠭ᜪ") else bstack111ll11_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᜫ")
            bstack1lll11l1l11_opy_ = request.node.nodeid + (bstack111ll11_opy_ (u"ࠪࠫᜬ") if bstack1lll11l111l_opy_ == bstack111ll11_opy_ (u"ࠫࡨࡧ࡬࡭ࠩᜭ") else bstack111ll11_opy_ (u"ࠬ࠳ࠧᜮ") + bstack1lll11l111l_opy_)
            bstack1lll11lll11_opy_ = bstack11lll11ll1_opy_(_11lll1l1l1_opy_.get(bstack1lll11l1l11_opy_, None))
            if not bstack1lll11lll11_opy_:
                continue
            for record in records:
                if bstack111lllll1l_opy_(record.message):
                    continue
                bstack1l111l1l11_opy_.append({
                    bstack111ll11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩᜯ"): datetime.datetime.utcfromtimestamp(record.created).isoformat() + bstack111ll11_opy_ (u"࡛ࠧࠩᜰ"),
                    bstack111ll11_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᜱ"): record.levelname,
                    bstack111ll11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᜲ"): record.message,
                    bstack1lll1l11ll1_opy_: bstack1lll11lll11_opy_
                })
        if len(bstack1l111l1l11_opy_) > 0:
            bstack11l1ll1l_opy_.bstack1l1lll11ll_opy_(bstack1l111l1l11_opy_)
    except Exception as err:
        print(bstack111ll11_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡨࡵ࡮ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧ࠽ࠤࢀࢃࠧᜳ"), str(err))
def bstack1l11ll1ll_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1l11111ll_opy_
    bstack1l1l111ll1_opy_ = bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ᜴"), None) and bstack1ll1l1l1_opy_(
            threading.current_thread(), bstack111ll11_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ᜵"), None)
    bstack1ll1l1llll_opy_ = getattr(driver, bstack111ll11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭᜶"), None) != None and getattr(driver, bstack111ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ᜷"), None) == True
    if sequence == bstack111ll11_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨ᜸") and driver != None:
      if not bstack1l11111ll_opy_ and bstack111llll11l_opy_() and bstack111ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ᜹") in CONFIG and CONFIG[bstack111ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ᜺")] == True and bstack1lll11ll1_opy_.bstack11l1l11l1_opy_(driver_command) and (bstack1ll1l1llll_opy_ or bstack1l1l111ll1_opy_) and not bstack1l1l111l1l_opy_(args):
        try:
          bstack1l11111ll_opy_ = True
          logger.debug(bstack111ll11_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡿࢂ࠭᜻").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack111ll11_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡨࡶ࡫ࡵࡲ࡮ࠢࡶࡧࡦࡴࠠࡼࡿࠪ᜼").format(str(err)))
        bstack1l11111ll_opy_ = False
    if sequence == bstack111ll11_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬ᜽"):
        if driver_command == bstack111ll11_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠫ᜾"):
            bstack11l1ll1l_opy_.bstack11111ll1l_opy_({
                bstack111ll11_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧ᜿"): response[bstack111ll11_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨᝀ")],
                bstack111ll11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᝁ"): store[bstack111ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᝂ")]
            })
def bstack111111l1l_opy_():
    global bstack1111llll_opy_
    bstack1l11l111l_opy_.bstack11l11l111_opy_()
    logging.shutdown()
    bstack11l1ll1l_opy_.bstack1l111ll1ll_opy_()
    for driver in bstack1111llll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1lll1l11111_opy_(*args):
    global bstack1111llll_opy_
    bstack11l1ll1l_opy_.bstack1l111ll1ll_opy_()
    for driver in bstack1111llll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1l11lll1_opy_(self, *args, **kwargs):
    bstack1l1l1lll1l_opy_ = bstack1l111ll1l_opy_(self, *args, **kwargs)
    bstack11l1ll1l_opy_.bstack111l1lll_opy_(self)
    return bstack1l1l1lll1l_opy_
def bstack1ll1l1ll11_opy_(framework_name):
    global bstack11l11llll_opy_
    global bstack1lll111l11_opy_
    bstack11l11llll_opy_ = framework_name
    logger.info(bstack11llll11l_opy_.format(bstack11l11llll_opy_.split(bstack111ll11_opy_ (u"ࠬ࠳ࠧᝃ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack111llll11l_opy_():
            Service.start = bstack1ll1l11111_opy_
            Service.stop = bstack1ll11111l_opy_
            webdriver.Remote.__init__ = bstack1llll11l1l_opy_
            webdriver.Remote.get = bstack11llll1ll_opy_
            if not isinstance(os.getenv(bstack111ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡁࡓࡃࡏࡐࡊࡒࠧᝄ")), str):
                return
            WebDriver.close = bstack1l111l1l_opy_
            WebDriver.quit = bstack1ll111llll_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        if not bstack111llll11l_opy_() and bstack11l1ll1l_opy_.on():
            webdriver.Remote.__init__ = bstack1l1l11lll1_opy_
        bstack1lll111l11_opy_ = True
    except Exception as e:
        pass
    bstack1l1ll1l1_opy_()
    if os.environ.get(bstack111ll11_opy_ (u"ࠧࡔࡇࡏࡉࡓࡏࡕࡎࡡࡒࡖࡤࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡌࡒࡘ࡚ࡁࡍࡎࡈࡈࠬᝅ")):
        bstack1lll111l11_opy_ = eval(os.environ.get(bstack111ll11_opy_ (u"ࠨࡕࡈࡐࡊࡔࡉࡖࡏࡢࡓࡗࡥࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡍࡓ࡙ࡔࡂࡎࡏࡉࡉ࠭ᝆ")))
    if not bstack1lll111l11_opy_:
        bstack1l1llllll1_opy_(bstack111ll11_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦᝇ"), bstack1lllll111l_opy_)
    if bstack11ll111l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._get_proxy_url = bstack11111l11_opy_
        except Exception as e:
            logger.error(bstack11ll1l1l_opy_.format(str(e)))
    if bstack111ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᝈ") in str(framework_name).lower():
        if not bstack111llll11l_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack1ll1l1l1ll_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack111ll1l1l_opy_
            Config.getoption = bstack1l1lll1l11_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack111l11l1l_opy_
        except Exception as e:
            pass
def bstack1ll111llll_opy_(self):
    global bstack11l11llll_opy_
    global bstack1l111llll_opy_
    global bstack1ll1lll1ll_opy_
    try:
        if bstack111ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᝉ") in bstack11l11llll_opy_ and self.session_id != None and bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠬࡺࡥࡴࡶࡖࡸࡦࡺࡵࡴࠩᝊ"), bstack111ll11_opy_ (u"࠭ࠧᝋ")) != bstack111ll11_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᝌ"):
            bstack1l11lll1l1_opy_ = bstack111ll11_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᝍ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᝎ")
            bstack1l11l1l11l_opy_(logger, True)
            if self != None:
                bstack1l1lll11_opy_(self, bstack1l11lll1l1_opy_, bstack111ll11_opy_ (u"ࠪ࠰ࠥ࠭ᝏ").join(threading.current_thread().bstackTestErrorMessages))
        item = store.get(bstack111ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨᝐ"), None)
        if item is not None and bstack1lll1l1l1l1_opy_:
            bstack111111ll1_opy_.bstack1lllllll1_opy_(self, bstack1lll1l11ll_opy_, logger, item)
        threading.current_thread().testStatus = bstack111ll11_opy_ (u"ࠬ࠭ᝑ")
    except Exception as e:
        logger.debug(bstack111ll11_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠢᝒ") + str(e))
    bstack1ll1lll1ll_opy_(self)
    self.session_id = None
def bstack1llll11l1l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1l111llll_opy_
    global bstack1ll1l1l11_opy_
    global bstack111ll1l11_opy_
    global bstack11l11llll_opy_
    global bstack1l111ll1l_opy_
    global bstack1111llll_opy_
    global bstack1l1ll1l1l_opy_
    global bstack1lll1l1111_opy_
    global bstack1lll1l1l1l1_opy_
    global bstack1lll1l11ll_opy_
    CONFIG[bstack111ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩᝓ")] = str(bstack11l11llll_opy_) + str(__version__)
    command_executor = bstack1lll11l11_opy_(bstack1l1ll1l1l_opy_)
    logger.debug(bstack1llll1l11_opy_.format(command_executor))
    proxy = bstack1ll11111ll_opy_(CONFIG, proxy)
    bstack1lll1ll1l1_opy_ = 0
    try:
        if bstack111ll1l11_opy_ is True:
            bstack1lll1ll1l1_opy_ = int(os.environ.get(bstack111ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ᝔")))
    except:
        bstack1lll1ll1l1_opy_ = 0
    bstack11l1lll1l_opy_ = bstack111ll1ll1_opy_(CONFIG, bstack1lll1ll1l1_opy_)
    logger.debug(bstack1ll1ll1111_opy_.format(str(bstack11l1lll1l_opy_)))
    bstack1lll1l11ll_opy_ = CONFIG.get(bstack111ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ᝕"))[bstack1lll1ll1l1_opy_]
    if bstack111ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ᝖") in CONFIG and CONFIG[bstack111ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ᝗")]:
        bstack1l1lll1ll_opy_(bstack11l1lll1l_opy_, bstack1lll1l1111_opy_)
    if bstack1llll1lll1_opy_.bstack11l11ll1_opy_(CONFIG, bstack1lll1ll1l1_opy_) and bstack1llll1lll1_opy_.bstack11ll1l111_opy_(bstack11l1lll1l_opy_, options):
        bstack1lll1l1l1l1_opy_ = True
        bstack1llll1lll1_opy_.set_capabilities(bstack11l1lll1l_opy_, CONFIG)
    if desired_capabilities:
        bstack1111l1l11_opy_ = bstack1ll11l1111_opy_(desired_capabilities)
        bstack1111l1l11_opy_[bstack111ll11_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬ᝘")] = bstack1l11111l_opy_(CONFIG)
        bstack1l1l1ll1ll_opy_ = bstack111ll1ll1_opy_(bstack1111l1l11_opy_)
        if bstack1l1l1ll1ll_opy_:
            bstack11l1lll1l_opy_ = update(bstack1l1l1ll1ll_opy_, bstack11l1lll1l_opy_)
        desired_capabilities = None
    if options:
        bstack1l1l11llll_opy_(options, bstack11l1lll1l_opy_)
    if not options:
        options = bstack111lll11l_opy_(bstack11l1lll1l_opy_)
    if proxy and bstack1l111lll1_opy_() >= version.parse(bstack111ll11_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭᝙")):
        options.proxy(proxy)
    if options and bstack1l111lll1_opy_() >= version.parse(bstack111ll11_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭᝚")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1l111lll1_opy_() < version.parse(bstack111ll11_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ᝛")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack11l1lll1l_opy_)
    logger.info(bstack1ll11ll1ll_opy_)
    if bstack1l111lll1_opy_() >= version.parse(bstack111ll11_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩ᝜")):
        bstack1l111ll1l_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l111lll1_opy_() >= version.parse(bstack111ll11_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ᝝")):
        bstack1l111ll1l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l111lll1_opy_() >= version.parse(bstack111ll11_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫ᝞")):
        bstack1l111ll1l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack1l111ll1l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack1l1ll111l_opy_ = bstack111ll11_opy_ (u"ࠬ࠭᝟")
        if bstack1l111lll1_opy_() >= version.parse(bstack111ll11_opy_ (u"࠭࠴࠯࠲࠱࠴ࡧ࠷ࠧᝠ")):
            bstack1l1ll111l_opy_ = self.caps.get(bstack111ll11_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢᝡ"))
        else:
            bstack1l1ll111l_opy_ = self.capabilities.get(bstack111ll11_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣᝢ"))
        if bstack1l1ll111l_opy_:
            bstack1ll1llll1l_opy_(bstack1l1ll111l_opy_)
            if bstack1l111lll1_opy_() <= version.parse(bstack111ll11_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩᝣ")):
                self.command_executor._url = bstack111ll11_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᝤ") + bstack1l1ll1l1l_opy_ + bstack111ll11_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣᝥ")
            else:
                self.command_executor._url = bstack111ll11_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢᝦ") + bstack1l1ll111l_opy_ + bstack111ll11_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢᝧ")
            logger.debug(bstack1ll1lllll_opy_.format(bstack1l1ll111l_opy_))
        else:
            logger.debug(bstack1l11111l1_opy_.format(bstack111ll11_opy_ (u"ࠢࡐࡲࡷ࡭ࡲࡧ࡬ࠡࡊࡸࡦࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣᝨ")))
    except Exception as e:
        logger.debug(bstack1l11111l1_opy_.format(e))
    bstack1l111llll_opy_ = self.session_id
    if bstack111ll11_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᝩ") in bstack11l11llll_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack111ll11_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭ᝪ"), None)
        if item:
            bstack1lll11ll1ll_opy_ = getattr(item, bstack111ll11_opy_ (u"ࠪࡣࡹ࡫ࡳࡵࡡࡦࡥࡸ࡫࡟ࡴࡶࡤࡶࡹ࡫ࡤࠨᝫ"), False)
            if not getattr(item, bstack111ll11_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬᝬ"), None) and bstack1lll11ll1ll_opy_:
                setattr(store[bstack111ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩ᝭")], bstack111ll11_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᝮ"), self)
        bstack11l1ll1l_opy_.bstack111l1lll_opy_(self)
    bstack1111llll_opy_.append(self)
    if bstack111ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᝯ") in CONFIG and bstack111ll11_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ᝰ") in CONFIG[bstack111ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ᝱")][bstack1lll1ll1l1_opy_]:
        bstack1ll1l1l11_opy_ = CONFIG[bstack111ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᝲ")][bstack1lll1ll1l1_opy_][bstack111ll11_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᝳ")]
    logger.debug(bstack1l1ll11ll1_opy_.format(bstack1l111llll_opy_))
def bstack11llll1ll_opy_(self, url):
    global bstack11l1111ll_opy_
    global CONFIG
    try:
        bstack1111lllll_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1ll1ll11l1_opy_.format(str(err)))
    try:
        bstack11l1111ll_opy_(self, url)
    except Exception as e:
        try:
            bstack1lll11l111_opy_ = str(e)
            if any(err_msg in bstack1lll11l111_opy_ for err_msg in bstack1ll11lll11_opy_):
                bstack1111lllll_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1ll1ll11l1_opy_.format(str(err)))
        raise e
def bstack1111l11ll_opy_(item, when):
    global bstack1ll111111l_opy_
    try:
        bstack1ll111111l_opy_(item, when)
    except Exception as e:
        pass
def bstack111l11l1l_opy_(item, call, rep):
    global bstack1l11lll11l_opy_
    global bstack1111llll_opy_
    name = bstack111ll11_opy_ (u"ࠬ࠭᝴")
    try:
        if rep.when == bstack111ll11_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ᝵"):
            bstack1l111llll_opy_ = threading.current_thread().bstackSessionId
            bstack1lll11lll1l_opy_ = item.config.getoption(bstack111ll11_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ᝶"))
            try:
                if (str(bstack1lll11lll1l_opy_).lower() != bstack111ll11_opy_ (u"ࠨࡶࡵࡹࡪ࠭᝷")):
                    name = str(rep.nodeid)
                    bstack1111ll11_opy_ = bstack1llll11l_opy_(bstack111ll11_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ᝸"), name, bstack111ll11_opy_ (u"ࠪࠫ᝹"), bstack111ll11_opy_ (u"ࠫࠬ᝺"), bstack111ll11_opy_ (u"ࠬ࠭᝻"), bstack111ll11_opy_ (u"࠭ࠧ᝼"))
                    os.environ[bstack111ll11_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࡟ࡕࡇࡖࡘࡤࡔࡁࡎࡇࠪ᝽")] = name
                    for driver in bstack1111llll_opy_:
                        if bstack1l111llll_opy_ == driver.session_id:
                            driver.execute_script(bstack1111ll11_opy_)
            except Exception as e:
                logger.debug(bstack111ll11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨ᝾").format(str(e)))
            try:
                bstack11l1l1l11_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack111ll11_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ᝿"):
                    status = bstack111ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪក") if rep.outcome.lower() == bstack111ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫខ") else bstack111ll11_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬគ")
                    reason = bstack111ll11_opy_ (u"࠭ࠧឃ")
                    if status == bstack111ll11_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧង"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack111ll11_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭ច") if status == bstack111ll11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩឆ") else bstack111ll11_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩជ")
                    data = name + bstack111ll11_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭ឈ") if status == bstack111ll11_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬញ") else name + bstack111ll11_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠡࠡࠩដ") + reason
                    bstack111l11ll1_opy_ = bstack1llll11l_opy_(bstack111ll11_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩឋ"), bstack111ll11_opy_ (u"ࠨࠩឌ"), bstack111ll11_opy_ (u"ࠩࠪឍ"), bstack111ll11_opy_ (u"ࠪࠫណ"), level, data)
                    for driver in bstack1111llll_opy_:
                        if bstack1l111llll_opy_ == driver.session_id:
                            driver.execute_script(bstack111l11ll1_opy_)
            except Exception as e:
                logger.debug(bstack111ll11_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡥࡲࡲࡹ࡫ࡸࡵࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨត").format(str(e)))
    except Exception as e:
        logger.debug(bstack111ll11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡵࡷࡥࡹ࡫ࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࡻࡾࠩថ").format(str(e)))
    bstack1l11lll11l_opy_(item, call, rep)
notset = Notset()
def bstack1l1lll1l11_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1ll1l11lll_opy_
    if str(name).lower() == bstack111ll11_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷ࠭ទ"):
        return bstack111ll11_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨធ")
    else:
        return bstack1ll1l11lll_opy_(self, name, default, skip)
def bstack11111l11_opy_(self):
    global CONFIG
    global bstack1111111l_opy_
    try:
        proxy = bstack1llll1111l_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack111ll11_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭ន")):
                proxies = bstack1l1lll1l1_opy_(proxy, bstack1lll11l11_opy_())
                if len(proxies) > 0:
                    protocol, bstack1ll1l1l1l1_opy_ = proxies.popitem()
                    if bstack111ll11_opy_ (u"ࠤ࠽࠳࠴ࠨប") in bstack1ll1l1l1l1_opy_:
                        return bstack1ll1l1l1l1_opy_
                    else:
                        return bstack111ll11_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦផ") + bstack1ll1l1l1l1_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack111ll11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡱࡴࡲࡼࡾࠦࡵࡳ࡮ࠣ࠾ࠥࢁࡽࠣព").format(str(e)))
    return bstack1111111l_opy_(self)
def bstack11ll111l_opy_():
    return (bstack111ll11_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨភ") in CONFIG or bstack111ll11_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪម") in CONFIG) and bstack1ll11l1l1_opy_() and bstack1l111lll1_opy_() >= version.parse(
        bstack1ll11l11l1_opy_)
def bstack1lllll1l1_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1ll1l1l11_opy_
    global bstack111ll1l11_opy_
    global bstack11l11llll_opy_
    CONFIG[bstack111ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩយ")] = str(bstack11l11llll_opy_) + str(__version__)
    bstack1lll1ll1l1_opy_ = 0
    try:
        if bstack111ll1l11_opy_ is True:
            bstack1lll1ll1l1_opy_ = int(os.environ.get(bstack111ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨរ")))
    except:
        bstack1lll1ll1l1_opy_ = 0
    CONFIG[bstack111ll11_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣល")] = True
    bstack11l1lll1l_opy_ = bstack111ll1ll1_opy_(CONFIG, bstack1lll1ll1l1_opy_)
    logger.debug(bstack1ll1ll1111_opy_.format(str(bstack11l1lll1l_opy_)))
    if CONFIG.get(bstack111ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧវ")):
        bstack1l1lll1ll_opy_(bstack11l1lll1l_opy_, bstack1lll1l1111_opy_)
    if bstack111ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧឝ") in CONFIG and bstack111ll11_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪឞ") in CONFIG[bstack111ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩស")][bstack1lll1ll1l1_opy_]:
        bstack1ll1l1l11_opy_ = CONFIG[bstack111ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪហ")][bstack1lll1ll1l1_opy_][bstack111ll11_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ឡ")]
    import urllib
    import json
    bstack1ll1l111l1_opy_ = bstack111ll11_opy_ (u"ࠩࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠫអ") + urllib.parse.quote(json.dumps(bstack11l1lll1l_opy_))
    browser = self.connect(bstack1ll1l111l1_opy_)
    return browser
def bstack1l1ll1l1_opy_():
    global bstack1lll111l11_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1lllll1l1_opy_
        bstack1lll111l11_opy_ = True
    except Exception as e:
        pass
def bstack1lll1l11l11_opy_():
    global CONFIG
    global bstack1l1l111111_opy_
    global bstack1l1ll1l1l_opy_
    global bstack1lll1l1111_opy_
    global bstack111ll1l11_opy_
    global bstack1ll1111lll_opy_
    CONFIG = json.loads(os.environ.get(bstack111ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࠩឣ")))
    bstack1l1l111111_opy_ = eval(os.environ.get(bstack111ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬឤ")))
    bstack1l1ll1l1l_opy_ = os.environ.get(bstack111ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡍ࡛ࡂࡠࡗࡕࡐࠬឥ"))
    bstack1l1ll111_opy_(CONFIG, bstack1l1l111111_opy_)
    bstack1ll1111lll_opy_ = bstack1l11l111l_opy_.bstack11l1l1ll_opy_(CONFIG, bstack1ll1111lll_opy_)
    global bstack1l111ll1l_opy_
    global bstack1ll1lll1ll_opy_
    global bstack1l111l11_opy_
    global bstack1l111l1l1_opy_
    global bstack11l1111l1_opy_
    global bstack1ll1lll1l_opy_
    global bstack11lll111l_opy_
    global bstack11l1111ll_opy_
    global bstack1111111l_opy_
    global bstack1ll1l11lll_opy_
    global bstack1ll111111l_opy_
    global bstack1l11lll11l_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1l111ll1l_opy_ = webdriver.Remote.__init__
        bstack1ll1lll1ll_opy_ = WebDriver.quit
        bstack11lll111l_opy_ = WebDriver.close
        bstack11l1111ll_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack111ll11_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩឦ") in CONFIG or bstack111ll11_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫឧ") in CONFIG) and bstack1ll11l1l1_opy_():
        if bstack1l111lll1_opy_() < version.parse(bstack1ll11l11l1_opy_):
            logger.error(bstack1l11l1lll_opy_.format(bstack1l111lll1_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack1111111l_opy_ = RemoteConnection._get_proxy_url
            except Exception as e:
                logger.error(bstack11ll1l1l_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack1ll1l11lll_opy_ = Config.getoption
        from _pytest import runner
        bstack1ll111111l_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack1llllll1l_opy_)
    try:
        from pytest_bdd import reporting
        bstack1l11lll11l_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack111ll11_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩឨ"))
    bstack1lll1l1111_opy_ = CONFIG.get(bstack111ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ឩ"), {}).get(bstack111ll11_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬឪ"))
    bstack111ll1l11_opy_ = True
    bstack1ll1l1ll11_opy_(bstack1lllll1lll_opy_)
if (bstack111lll111l_opy_()):
    bstack1lll1l11l11_opy_()
@bstack11lllll111_opy_(class_method=False)
def bstack1lll1l111l1_opy_(hook_name, event, bstack1lll11l11l1_opy_=None):
    if hook_name not in [bstack111ll11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬឫ"), bstack111ll11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩឬ"), bstack111ll11_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬឭ"), bstack111ll11_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩឮ"), bstack111ll11_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ឯ"), bstack111ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪឰ"), bstack111ll11_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩឱ"), bstack111ll11_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ឲ")]:
        return
    node = store[bstack111ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣ࡮ࡺࡥ࡮ࠩឳ")]
    if hook_name in [bstack111ll11_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬ឴"), bstack111ll11_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩ឵")]:
        node = store[bstack111ll11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡰࡳࡩࡻ࡬ࡦࡡ࡬ࡸࡪࡳࠧា")]
    elif hook_name in [bstack111ll11_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧិ"), bstack111ll11_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫី")]:
        node = store[bstack111ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡩ࡬ࡢࡵࡶࡣ࡮ࡺࡥ࡮ࠩឹ")]
    if event == bstack111ll11_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬឺ"):
        hook_type = bstack1llllll1ll1_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack1l111lll1l_opy_ = {
            bstack111ll11_opy_ (u"࠭ࡵࡶ࡫ࡧࠫុ"): uuid,
            bstack111ll11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫូ"): bstack1lll1l1l11_opy_(),
            bstack111ll11_opy_ (u"ࠨࡶࡼࡴࡪ࠭ួ"): bstack111ll11_opy_ (u"ࠩ࡫ࡳࡴࡱࠧើ"),
            bstack111ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ឿ"): hook_type,
            bstack111ll11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠧៀ"): hook_name
        }
        store[bstack111ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩេ")].append(uuid)
        bstack1lll11llll1_opy_ = node.nodeid
        if hook_type == bstack111ll11_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫែ"):
            if not _11lll1l1l1_opy_.get(bstack1lll11llll1_opy_, None):
                _11lll1l1l1_opy_[bstack1lll11llll1_opy_] = {bstack111ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ៃ"): []}
            _11lll1l1l1_opy_[bstack1lll11llll1_opy_][bstack111ll11_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧោ")].append(bstack1l111lll1l_opy_[bstack111ll11_opy_ (u"ࠩࡸࡹ࡮ࡪࠧៅ")])
        _11lll1l1l1_opy_[bstack1lll11llll1_opy_ + bstack111ll11_opy_ (u"ࠪ࠱ࠬំ") + hook_name] = bstack1l111lll1l_opy_
        bstack1lll1l1llll_opy_(node, bstack1l111lll1l_opy_, bstack111ll11_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬះ"))
    elif event == bstack111ll11_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫៈ"):
        bstack1l11l111l1_opy_ = node.nodeid + bstack111ll11_opy_ (u"࠭࠭ࠨ៉") + hook_name
        _11lll1l1l1_opy_[bstack1l11l111l1_opy_][bstack111ll11_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ៊")] = bstack1lll1l1l11_opy_()
        bstack1lll1l1111l_opy_(_11lll1l1l1_opy_[bstack1l11l111l1_opy_][bstack111ll11_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭់")])
        bstack1lll1l1llll_opy_(node, _11lll1l1l1_opy_[bstack1l11l111l1_opy_], bstack111ll11_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ៌"), bstack1lll11l1lll_opy_=bstack1lll11l11l1_opy_)
def bstack1lll111lll1_opy_():
    global bstack1lll1l11l1l_opy_
    if bstack1l1llll1l1_opy_():
        bstack1lll1l11l1l_opy_ = bstack111ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧ៍")
    else:
        bstack1lll1l11l1l_opy_ = bstack111ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ៎")
@bstack11l1ll1l_opy_.bstack1lll1llll1l_opy_
def bstack1lll1l11lll_opy_():
    bstack1lll111lll1_opy_()
    if bstack1ll11l1l1_opy_():
        bstack1llll1l1_opy_(bstack1l11ll1ll_opy_)
    bstack111ll11l11_opy_ = bstack111l1ll1ll_opy_(bstack1lll1l111l1_opy_)
bstack1lll1l11lll_opy_()