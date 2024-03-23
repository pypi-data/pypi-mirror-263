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
import datetime
import threading
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack11lll11lll_opy_ import RobotHandler
from bstack_utils.capture import bstack11llll1l11_opy_
from bstack_utils.bstack1l11111l11_opy_ import bstack11lll1ll1l_opy_, bstack11llll11l1_opy_, bstack11lll1lll1_opy_
from bstack_utils.bstack1111111ll_opy_ import bstack11l1ll1l_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1ll1l1l1_opy_, bstack1lll1l1l11_opy_, Result, \
    bstack11lllll111_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    store = {
        bstack111ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧ഼ࠫ"): [],
        bstack111ll11_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡠࡪࡲࡳࡰࡹࠧഽ"): [],
        bstack111ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸ࠭ാ"): []
    }
    bstack11lll1l1ll_opy_ = []
    bstack11lll1l111_opy_ = []
    @staticmethod
    def bstack1l1111lll1_opy_(log):
        if not (log[bstack111ll11_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫി")] and log[bstack111ll11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬീ")].strip()):
            return
        active = bstack11l1ll1l_opy_.bstack1l111llll1_opy_()
        log = {
            bstack111ll11_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫു"): log[bstack111ll11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬൂ")],
            bstack111ll11_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪൃ"): datetime.datetime.utcnow().isoformat() + bstack111ll11_opy_ (u"ࠨ࡜ࠪൄ"),
            bstack111ll11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ൅"): log[bstack111ll11_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫെ")],
        }
        if active:
            if active[bstack111ll11_opy_ (u"ࠫࡹࡿࡰࡦࠩേ")] == bstack111ll11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪൈ"):
                log[bstack111ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭൉")] = active[bstack111ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧൊ")]
            elif active[bstack111ll11_opy_ (u"ࠨࡶࡼࡴࡪ࠭ോ")] == bstack111ll11_opy_ (u"ࠩࡷࡩࡸࡺࠧൌ"):
                log[bstack111ll11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦ്ࠪ")] = active[bstack111ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫൎ")]
        bstack11l1ll1l_opy_.bstack1l1lll11ll_opy_([log])
    def __init__(self):
        self.messages = Messages()
        self._1l11111111_opy_ = None
        self._1l1111l111_opy_ = None
        self._11lll1l1l1_opy_ = OrderedDict()
        self.bstack1l11l1111l_opy_ = bstack11llll1l11_opy_(self.bstack1l1111lll1_opy_)
    @bstack11lllll111_opy_(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack1l111l1l1l_opy_()
        if not self._11lll1l1l1_opy_.get(attrs.get(bstack111ll11_opy_ (u"ࠬ࡯ࡤࠨ൏")), None):
            self._11lll1l1l1_opy_[attrs.get(bstack111ll11_opy_ (u"࠭ࡩࡥࠩ൐"))] = {}
        bstack1l111111ll_opy_ = bstack11lll1lll1_opy_(
                bstack11lllll1ll_opy_=attrs.get(bstack111ll11_opy_ (u"ࠧࡪࡦࠪ൑")),
                name=name,
                bstack1l1111llll_opy_=bstack1lll1l1l11_opy_(),
                file_path=os.path.relpath(attrs[bstack111ll11_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ൒")], start=os.getcwd()) if attrs.get(bstack111ll11_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ൓")) != bstack111ll11_opy_ (u"ࠪࠫൔ") else bstack111ll11_opy_ (u"ࠫࠬൕ"),
                framework=bstack111ll11_opy_ (u"ࠬࡘ࡯ࡣࡱࡷࠫൖ")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack111ll11_opy_ (u"࠭ࡩࡥࠩൗ"), None)
        self._11lll1l1l1_opy_[attrs.get(bstack111ll11_opy_ (u"ࠧࡪࡦࠪ൘"))][bstack111ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ൙")] = bstack1l111111ll_opy_
    @bstack11lllll111_opy_(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack1l11l111ll_opy_()
        self._11llll1111_opy_(messages)
        for bstack1l11111lll_opy_ in self.bstack11lll1l1ll_opy_:
            bstack1l11111lll_opy_[bstack111ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ൚")][bstack111ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩ൛")].extend(self.store[bstack111ll11_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪ൜")])
            bstack11l1ll1l_opy_.bstack11llllll1l_opy_(bstack1l11111lll_opy_)
        self.bstack11lll1l1ll_opy_ = []
        self.store[bstack111ll11_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰࡤ࡮࡯ࡰ࡭ࡶࠫ൝")] = []
    @bstack11lllll111_opy_(class_method=True)
    def start_test(self, name, attrs):
        self.bstack1l11l1111l_opy_.start()
        if not self._11lll1l1l1_opy_.get(attrs.get(bstack111ll11_opy_ (u"࠭ࡩࡥࠩ൞")), None):
            self._11lll1l1l1_opy_[attrs.get(bstack111ll11_opy_ (u"ࠧࡪࡦࠪൟ"))] = {}
        driver = bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧൠ"), None)
        bstack1l11111l11_opy_ = bstack11lll1lll1_opy_(
            bstack11lllll1ll_opy_=attrs.get(bstack111ll11_opy_ (u"ࠩ࡬ࡨࠬൡ")),
            name=name,
            bstack1l1111llll_opy_=bstack1lll1l1l11_opy_(),
            file_path=os.path.relpath(attrs[bstack111ll11_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪൢ")], start=os.getcwd()),
            scope=RobotHandler.bstack11llll1l1l_opy_(attrs.get(bstack111ll11_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫൣ"), None)),
            framework=bstack111ll11_opy_ (u"ࠬࡘ࡯ࡣࡱࡷࠫ൤"),
            tags=attrs[bstack111ll11_opy_ (u"࠭ࡴࡢࡩࡶࠫ൥")],
            hooks=self.store[bstack111ll11_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࡟ࡩࡱࡲ࡯ࡸ࠭൦")],
            bstack1l1111ll11_opy_=bstack11l1ll1l_opy_.bstack1l11111ll1_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack111ll11_opy_ (u"ࠣࡽࢀࠤࡡࡴࠠࡼࡿࠥ൧").format(bstack111ll11_opy_ (u"ࠤࠣࠦ൨").join(attrs[bstack111ll11_opy_ (u"ࠪࡸࡦ࡭ࡳࠨ൩")]), name) if attrs[bstack111ll11_opy_ (u"ࠫࡹࡧࡧࡴࠩ൪")] else name
        )
        self._11lll1l1l1_opy_[attrs.get(bstack111ll11_opy_ (u"ࠬ࡯ࡤࠨ൫"))][bstack111ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ൬")] = bstack1l11111l11_opy_
        threading.current_thread().current_test_uuid = bstack1l11111l11_opy_.bstack1l1111l1l1_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack111ll11_opy_ (u"ࠧࡪࡦࠪ൭"), None)
        self.bstack11llll1lll_opy_(bstack111ll11_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ൮"), bstack1l11111l11_opy_)
    @bstack11lllll111_opy_(class_method=True)
    def end_test(self, name, attrs):
        self.bstack1l11l1111l_opy_.reset()
        bstack11lllll1l1_opy_ = bstack11lllll11l_opy_.get(attrs.get(bstack111ll11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ൯")), bstack111ll11_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ൰"))
        self._11lll1l1l1_opy_[attrs.get(bstack111ll11_opy_ (u"ࠫ࡮ࡪࠧ൱"))][bstack111ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ൲")].stop(time=bstack1lll1l1l11_opy_(), duration=int(attrs.get(bstack111ll11_opy_ (u"࠭ࡥ࡭ࡣࡳࡷࡪࡪࡴࡪ࡯ࡨࠫ൳"), bstack111ll11_opy_ (u"ࠧ࠱ࠩ൴"))), result=Result(result=bstack11lllll1l1_opy_, exception=attrs.get(bstack111ll11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ൵")), bstack1l11111l1l_opy_=[attrs.get(bstack111ll11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ൶"))]))
        self.bstack11llll1lll_opy_(bstack111ll11_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ൷"), self._11lll1l1l1_opy_[attrs.get(bstack111ll11_opy_ (u"ࠫ࡮ࡪࠧ൸"))][bstack111ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ൹")], True)
        self.store[bstack111ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪൺ")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @bstack11lllll111_opy_(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack1l111l1l1l_opy_()
        current_test_id = bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡥࠩൻ"), None)
        bstack11lll1llll_opy_ = current_test_id if bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡦࠪർ"), None) else bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡺ࡯ࡴࡦࡡ࡬ࡨࠬൽ"), None)
        if attrs.get(bstack111ll11_opy_ (u"ࠪࡸࡾࡶࡥࠨൾ"), bstack111ll11_opy_ (u"ࠫࠬൿ")).lower() in [bstack111ll11_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ඀"), bstack111ll11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨඁ")]:
            hook_type = bstack1l1111111l_opy_(attrs.get(bstack111ll11_opy_ (u"ࠧࡵࡻࡳࡩࠬං")), bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬඃ"), None))
            hook_name = bstack111ll11_opy_ (u"ࠩࡾࢁࠬ඄").format(attrs.get(bstack111ll11_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪඅ"), bstack111ll11_opy_ (u"ࠫࠬආ")))
            if hook_type in [bstack111ll11_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩඇ"), bstack111ll11_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩඈ")]:
                hook_name = bstack111ll11_opy_ (u"ࠧ࡜ࡽࢀࡡࠥࢁࡽࠨඉ").format(bstack1l111l1ll1_opy_.get(hook_type), attrs.get(bstack111ll11_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨඊ"), bstack111ll11_opy_ (u"ࠩࠪඋ")))
            bstack1l111lll1l_opy_ = bstack11llll11l1_opy_(
                bstack11lllll1ll_opy_=bstack11lll1llll_opy_ + bstack111ll11_opy_ (u"ࠪ࠱ࠬඌ") + attrs.get(bstack111ll11_opy_ (u"ࠫࡹࡿࡰࡦࠩඍ"), bstack111ll11_opy_ (u"ࠬ࠭ඎ")).lower(),
                name=hook_name,
                bstack1l1111llll_opy_=bstack1lll1l1l11_opy_(),
                file_path=os.path.relpath(attrs.get(bstack111ll11_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ඏ")), start=os.getcwd()),
                framework=bstack111ll11_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭ඐ"),
                tags=attrs[bstack111ll11_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭එ")],
                scope=RobotHandler.bstack11llll1l1l_opy_(attrs.get(bstack111ll11_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩඒ"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack1l111lll1l_opy_.bstack1l1111l1l1_opy_()
            threading.current_thread().current_hook_id = bstack11lll1llll_opy_ + bstack111ll11_opy_ (u"ࠪ࠱ࠬඓ") + attrs.get(bstack111ll11_opy_ (u"ࠫࡹࡿࡰࡦࠩඔ"), bstack111ll11_opy_ (u"ࠬ࠭ඕ")).lower()
            self.store[bstack111ll11_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪඖ")] = [bstack1l111lll1l_opy_.bstack1l1111l1l1_opy_()]
            if bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ඗"), None):
                self.store[bstack111ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬ඘")].append(bstack1l111lll1l_opy_.bstack1l1111l1l1_opy_())
            else:
                self.store[bstack111ll11_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡡ࡫ࡳࡴࡱࡳࠨ඙")].append(bstack1l111lll1l_opy_.bstack1l1111l1l1_opy_())
            if bstack11lll1llll_opy_:
                self._11lll1l1l1_opy_[bstack11lll1llll_opy_ + bstack111ll11_opy_ (u"ࠪ࠱ࠬක") + attrs.get(bstack111ll11_opy_ (u"ࠫࡹࡿࡰࡦࠩඛ"), bstack111ll11_opy_ (u"ࠬ࠭ග")).lower()] = { bstack111ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩඝ"): bstack1l111lll1l_opy_ }
            bstack11l1ll1l_opy_.bstack11llll1lll_opy_(bstack111ll11_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨඞ"), bstack1l111lll1l_opy_)
        else:
            bstack1l111l111l_opy_ = {
                bstack111ll11_opy_ (u"ࠨ࡫ࡧࠫඟ"): uuid4().__str__(),
                bstack111ll11_opy_ (u"ࠩࡷࡩࡽࡺࠧච"): bstack111ll11_opy_ (u"ࠪࡿࢂࠦࡻࡾࠩඡ").format(attrs.get(bstack111ll11_opy_ (u"ࠫࡰࡽ࡮ࡢ࡯ࡨࠫජ")), attrs.get(bstack111ll11_opy_ (u"ࠬࡧࡲࡨࡵࠪඣ"), bstack111ll11_opy_ (u"࠭ࠧඤ"))) if attrs.get(bstack111ll11_opy_ (u"ࠧࡢࡴࡪࡷࠬඥ"), []) else attrs.get(bstack111ll11_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨඦ")),
                bstack111ll11_opy_ (u"ࠩࡶࡸࡪࡶ࡟ࡢࡴࡪࡹࡲ࡫࡮ࡵࠩට"): attrs.get(bstack111ll11_opy_ (u"ࠪࡥࡷ࡭ࡳࠨඨ"), []),
                bstack111ll11_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨඩ"): bstack1lll1l1l11_opy_(),
                bstack111ll11_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬඪ"): bstack111ll11_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧණ"),
                bstack111ll11_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬඬ"): attrs.get(bstack111ll11_opy_ (u"ࠨࡦࡲࡧࠬත"), bstack111ll11_opy_ (u"ࠩࠪථ"))
            }
            if attrs.get(bstack111ll11_opy_ (u"ࠪࡰ࡮ࡨ࡮ࡢ࡯ࡨࠫද"), bstack111ll11_opy_ (u"ࠫࠬධ")) != bstack111ll11_opy_ (u"ࠬ࠭න"):
                bstack1l111l111l_opy_[bstack111ll11_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧ඲")] = attrs.get(bstack111ll11_opy_ (u"ࠧ࡭࡫ࡥࡲࡦࡳࡥࠨඳ"))
            if not self.bstack11lll1l111_opy_:
                self._11lll1l1l1_opy_[self._1l111l1111_opy_()][bstack111ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫප")].add_step(bstack1l111l111l_opy_)
                threading.current_thread().current_step_uuid = bstack1l111l111l_opy_[bstack111ll11_opy_ (u"ࠩ࡬ࡨࠬඵ")]
            self.bstack11lll1l111_opy_.append(bstack1l111l111l_opy_)
    @bstack11lllll111_opy_(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack1l11l111ll_opy_()
        self._11llll1111_opy_(messages)
        current_test_id = bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡨࠬබ"), None)
        bstack11lll1llll_opy_ = current_test_id if current_test_id else bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡹࡵࡪࡶࡨࡣ࡮ࡪࠧභ"), None)
        bstack11lll1ll11_opy_ = bstack11lllll11l_opy_.get(attrs.get(bstack111ll11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬම")), bstack111ll11_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧඹ"))
        bstack1l111lll11_opy_ = attrs.get(bstack111ll11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨය"))
        if bstack11lll1ll11_opy_ != bstack111ll11_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩර") and not attrs.get(bstack111ll11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ඼")) and self._1l11111111_opy_:
            bstack1l111lll11_opy_ = self._1l11111111_opy_
        bstack1l11l11l1l_opy_ = Result(result=bstack11lll1ll11_opy_, exception=bstack1l111lll11_opy_, bstack1l11111l1l_opy_=[bstack1l111lll11_opy_])
        if attrs.get(bstack111ll11_opy_ (u"ࠪࡸࡾࡶࡥࠨල"), bstack111ll11_opy_ (u"ࠫࠬ඾")).lower() in [bstack111ll11_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ඿"), bstack111ll11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨව")]:
            bstack11lll1llll_opy_ = current_test_id if current_test_id else bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡵࡸ࡭ࡹ࡫࡟ࡪࡦࠪශ"), None)
            if bstack11lll1llll_opy_:
                bstack1l11l111l1_opy_ = bstack11lll1llll_opy_ + bstack111ll11_opy_ (u"ࠣ࠯ࠥෂ") + attrs.get(bstack111ll11_opy_ (u"ࠩࡷࡽࡵ࡫ࠧස"), bstack111ll11_opy_ (u"ࠪࠫහ")).lower()
                self._11lll1l1l1_opy_[bstack1l11l111l1_opy_][bstack111ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧළ")].stop(time=bstack1lll1l1l11_opy_(), duration=int(attrs.get(bstack111ll11_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪෆ"), bstack111ll11_opy_ (u"࠭࠰ࠨ෇"))), result=bstack1l11l11l1l_opy_)
                bstack11l1ll1l_opy_.bstack11llll1lll_opy_(bstack111ll11_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ෈"), self._11lll1l1l1_opy_[bstack1l11l111l1_opy_][bstack111ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ෉")])
        else:
            bstack11lll1llll_opy_ = current_test_id if current_test_id else bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠ࡫ࡧ්ࠫ"), None)
            if bstack11lll1llll_opy_ and len(self.bstack11lll1l111_opy_) == 1:
                current_step_uuid = bstack1ll1l1l1_opy_(threading.current_thread(), bstack111ll11_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡺࡥࡱࡡࡸࡹ࡮ࡪࠧ෋"), None)
                self._11lll1l1l1_opy_[bstack11lll1llll_opy_][bstack111ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ෌")].bstack11llllll11_opy_(current_step_uuid, duration=int(attrs.get(bstack111ll11_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪ෍"), bstack111ll11_opy_ (u"࠭࠰ࠨ෎"))), result=bstack1l11l11l1l_opy_)
            else:
                self.bstack11llll111l_opy_(attrs)
            self.bstack11lll1l111_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack111ll11_opy_ (u"ࠧࡩࡶࡰࡰࠬා"), bstack111ll11_opy_ (u"ࠨࡰࡲࠫැ")) == bstack111ll11_opy_ (u"ࠩࡼࡩࡸ࠭ෑ"):
                return
            self.messages.push(message)
            bstack1l111l1l11_opy_ = []
            if bstack11l1ll1l_opy_.bstack1l111llll1_opy_():
                bstack1l111l1l11_opy_.append({
                    bstack111ll11_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ි"): bstack1lll1l1l11_opy_(),
                    bstack111ll11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬී"): message.get(bstack111ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ු")),
                    bstack111ll11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ෕"): message.get(bstack111ll11_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ූ")),
                    **bstack11l1ll1l_opy_.bstack1l111llll1_opy_()
                })
                if len(bstack1l111l1l11_opy_) > 0:
                    bstack11l1ll1l_opy_.bstack1l1lll11ll_opy_(bstack1l111l1l11_opy_)
        except Exception as err:
            pass
    def close(self):
        bstack11l1ll1l_opy_.bstack1l111ll1ll_opy_()
    def bstack11llll111l_opy_(self, bstack1l1111l11l_opy_):
        if not bstack11l1ll1l_opy_.bstack1l111llll1_opy_():
            return
        kwname = bstack111ll11_opy_ (u"ࠨࡽࢀࠤࢀࢃࠧ෗").format(bstack1l1111l11l_opy_.get(bstack111ll11_opy_ (u"ࠩ࡮ࡻࡳࡧ࡭ࡦࠩෘ")), bstack1l1111l11l_opy_.get(bstack111ll11_opy_ (u"ࠪࡥࡷ࡭ࡳࠨෙ"), bstack111ll11_opy_ (u"ࠫࠬේ"))) if bstack1l1111l11l_opy_.get(bstack111ll11_opy_ (u"ࠬࡧࡲࡨࡵࠪෛ"), []) else bstack1l1111l11l_opy_.get(bstack111ll11_opy_ (u"࠭࡫ࡸࡰࡤࡱࡪ࠭ො"))
        error_message = bstack111ll11_opy_ (u"ࠢ࡬ࡹࡱࡥࡲ࡫࠺ࠡ࡞ࠥࡿ࠵ࢃ࡜ࠣࠢࡿࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࡢࠢࡼ࠳ࢀࡠࠧࠦࡼࠡࡧࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࡢࠢࡼ࠴ࢀࡠࠧࠨෝ").format(kwname, bstack1l1111l11l_opy_.get(bstack111ll11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨෞ")), str(bstack1l1111l11l_opy_.get(bstack111ll11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪෟ"))))
        bstack1l111l11ll_opy_ = bstack111ll11_opy_ (u"ࠥ࡯ࡼࡴࡡ࡮ࡧ࠽ࠤࡡࠨࡻ࠱ࡿ࡟ࠦࠥࢂࠠࡴࡶࡤࡸࡺࡹ࠺ࠡ࡞ࠥࡿ࠶ࢃ࡜ࠣࠤ෠").format(kwname, bstack1l1111l11l_opy_.get(bstack111ll11_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ෡")))
        bstack11llll11ll_opy_ = error_message if bstack1l1111l11l_opy_.get(bstack111ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭෢")) else bstack1l111l11ll_opy_
        bstack1l111l1lll_opy_ = {
            bstack111ll11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ෣"): self.bstack11lll1l111_opy_[-1].get(bstack111ll11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ෤"), bstack1lll1l1l11_opy_()),
            bstack111ll11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ෥"): bstack11llll11ll_opy_,
            bstack111ll11_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ෦"): bstack111ll11_opy_ (u"ࠪࡉࡗࡘࡏࡓࠩ෧") if bstack1l1111l11l_opy_.get(bstack111ll11_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ෨")) == bstack111ll11_opy_ (u"ࠬࡌࡁࡊࡎࠪ෩") else bstack111ll11_opy_ (u"࠭ࡉࡏࡈࡒࠫ෪"),
            **bstack11l1ll1l_opy_.bstack1l111llll1_opy_()
        }
        bstack11l1ll1l_opy_.bstack1l1lll11ll_opy_([bstack1l111l1lll_opy_])
    def _1l111l1111_opy_(self):
        for bstack11lllll1ll_opy_ in reversed(self._11lll1l1l1_opy_):
            bstack1l11l11l11_opy_ = bstack11lllll1ll_opy_
            data = self._11lll1l1l1_opy_[bstack11lllll1ll_opy_][bstack111ll11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ෫")]
            if isinstance(data, bstack11llll11l1_opy_):
                if not bstack111ll11_opy_ (u"ࠨࡇࡄࡇࡍ࠭෬") in data.bstack1l111ll111_opy_():
                    return bstack1l11l11l11_opy_
            else:
                return bstack1l11l11l11_opy_
    def _11llll1111_opy_(self, messages):
        try:
            bstack11llll1ll1_opy_ = BuiltIn().get_variable_value(bstack111ll11_opy_ (u"ࠤࠧࡿࡑࡕࡇࠡࡎࡈ࡚ࡊࡒࡽࠣ෭")) in (bstack11lll1l11l_opy_.DEBUG, bstack11lll1l11l_opy_.TRACE)
            for message, bstack1l1111l1ll_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack111ll11_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ෮"))
                level = message.get(bstack111ll11_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ෯"))
                if level == bstack11lll1l11l_opy_.FAIL:
                    self._1l11111111_opy_ = name or self._1l11111111_opy_
                    self._1l1111l111_opy_ = bstack1l1111l1ll_opy_.get(bstack111ll11_opy_ (u"ࠧࡳࡥࡴࡵࡤ࡫ࡪࠨ෰")) if bstack11llll1ll1_opy_ and bstack1l1111l1ll_opy_ else self._1l1111l111_opy_
        except:
            pass
    @classmethod
    def bstack11llll1lll_opy_(self, event: str, bstack1l111l11l1_opy_: bstack11lll1ll1l_opy_, bstack11llllllll_opy_=False):
        if event == bstack111ll11_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ෱"):
            bstack1l111l11l1_opy_.set(hooks=self.store[bstack111ll11_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫෲ")])
        if event == bstack111ll11_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩෳ"):
            event = bstack111ll11_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ෴")
        if bstack11llllllll_opy_:
            bstack1l1111ll1l_opy_ = {
                bstack111ll11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ෵"): event,
                bstack1l111l11l1_opy_.bstack1l111lllll_opy_(): bstack1l111l11l1_opy_.bstack1l111ll11l_opy_(event)
            }
            self.bstack11lll1l1ll_opy_.append(bstack1l1111ll1l_opy_)
        else:
            bstack11l1ll1l_opy_.bstack11llll1lll_opy_(event, bstack1l111l11l1_opy_)
class Messages:
    def __init__(self):
        self._1l11l11111_opy_ = []
    def bstack1l111l1l1l_opy_(self):
        self._1l11l11111_opy_.append([])
    def bstack1l11l111ll_opy_(self):
        return self._1l11l11111_opy_.pop() if self._1l11l11111_opy_ else list()
    def push(self, message):
        self._1l11l11111_opy_[-1].append(message) if self._1l11l11111_opy_ else self._1l11l11111_opy_.append([message])
class bstack11lll1l11l_opy_:
    FAIL = bstack111ll11_opy_ (u"ࠫࡋࡇࡉࡍࠩ෶")
    ERROR = bstack111ll11_opy_ (u"ࠬࡋࡒࡓࡑࡕࠫ෷")
    WARNING = bstack111ll11_opy_ (u"࠭ࡗࡂࡔࡑࠫ෸")
    bstack1l111111l1_opy_ = bstack111ll11_opy_ (u"ࠧࡊࡐࡉࡓࠬ෹")
    DEBUG = bstack111ll11_opy_ (u"ࠨࡆࡈࡆ࡚ࡍࠧ෺")
    TRACE = bstack111ll11_opy_ (u"ࠩࡗࡖࡆࡉࡅࠨ෻")
    bstack1l111ll1l1_opy_ = [FAIL, ERROR]
def bstack11lll11ll1_opy_(bstack11lllllll1_opy_):
    if not bstack11lllllll1_opy_:
        return None
    if bstack11lllllll1_opy_.get(bstack111ll11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭෼"), None):
        return getattr(bstack11lllllll1_opy_[bstack111ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ෽")], bstack111ll11_opy_ (u"ࠬࡻࡵࡪࡦࠪ෾"), None)
    return bstack11lllllll1_opy_.get(bstack111ll11_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ෿"), None)
def bstack1l1111111l_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack111ll11_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭฀"), bstack111ll11_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪก")]:
        return
    if hook_type.lower() == bstack111ll11_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨข"):
        if current_test_uuid is None:
            return bstack111ll11_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡅࡑࡒࠧฃ")
        else:
            return bstack111ll11_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩค")
    elif hook_type.lower() == bstack111ll11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧฅ"):
        if current_test_uuid is None:
            return bstack111ll11_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩฆ")
        else:
            return bstack111ll11_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫง")