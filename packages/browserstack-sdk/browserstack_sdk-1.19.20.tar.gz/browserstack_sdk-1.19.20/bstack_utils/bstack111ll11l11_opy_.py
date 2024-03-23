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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result
def _111ll1l11l_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack111l1ll1ll_opy_:
    def __init__(self, handler):
        self._111l1lll1l_opy_ = {}
        self._111ll11111_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        self._111l1lll1l_opy_[bstack111ll11_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬጘ")] = Module._111l1ll11l_opy_
        self._111l1lll1l_opy_[bstack111ll11_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫጙ")] = Module._111l1ll111_opy_
        self._111l1lll1l_opy_[bstack111ll11_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫጚ")] = Class._111l1llll1_opy_
        self._111l1lll1l_opy_[bstack111ll11_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ጛ")] = Class._111ll1l111_opy_
        Module._111l1ll11l_opy_ = self.bstack111ll111ll_opy_(bstack111ll11_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩጜ"))
        Module._111l1ll111_opy_ = self.bstack111ll111ll_opy_(bstack111ll11_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨጝ"))
        Class._111l1llll1_opy_ = self.bstack111ll111ll_opy_(bstack111ll11_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨጞ"))
        Class._111ll1l111_opy_ = self.bstack111ll111ll_opy_(bstack111ll11_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪጟ"))
    def bstack111l1lllll_opy_(self, bstack111l1lll11_opy_, hook_type):
        meth = getattr(bstack111l1lll11_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._111ll11111_opy_[hook_type] = meth
            setattr(bstack111l1lll11_opy_, hook_type, self.bstack111ll1111l_opy_(hook_type))
    def bstack111ll11lll_opy_(self, instance, bstack111l1ll1l1_opy_):
        if bstack111l1ll1l1_opy_ == bstack111ll11_opy_ (u"ࠥࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪࠨጠ"):
            self.bstack111l1lllll_opy_(instance.obj, bstack111ll11_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠧጡ"))
            self.bstack111l1lllll_opy_(instance.obj, bstack111ll11_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠤጢ"))
        if bstack111l1ll1l1_opy_ == bstack111ll11_opy_ (u"ࠨ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠢጣ"):
            self.bstack111l1lllll_opy_(instance.obj, bstack111ll11_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࠨጤ"))
            self.bstack111l1lllll_opy_(instance.obj, bstack111ll11_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠥጥ"))
        if bstack111l1ll1l1_opy_ == bstack111ll11_opy_ (u"ࠤࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠤጦ"):
            self.bstack111l1lllll_opy_(instance.obj, bstack111ll11_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠣጧ"))
            self.bstack111l1lllll_opy_(instance.obj, bstack111ll11_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠧጨ"))
        if bstack111l1ll1l1_opy_ == bstack111ll11_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࠨጩ"):
            self.bstack111l1lllll_opy_(instance.obj, bstack111ll11_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠧጪ"))
            self.bstack111l1lllll_opy_(instance.obj, bstack111ll11_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠤጫ"))
    @staticmethod
    def bstack111l1l1lll_opy_(hook_type, func, args):
        if hook_type in [bstack111ll11_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧጬ"), bstack111ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫጭ")]:
            _111ll1l11l_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack111ll1111l_opy_(self, hook_type):
        def bstack111ll111l1_opy_(arg=None):
            self.handler(hook_type, bstack111ll11_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪጮ"))
            result = None
            exception = None
            try:
                self.bstack111l1l1lll_opy_(hook_type, self._111ll11111_opy_[hook_type], (arg,))
                result = Result(result=bstack111ll11_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫጯ"))
            except Exception as e:
                result = Result(result=bstack111ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬጰ"), exception=e)
                self.handler(hook_type, bstack111ll11_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬጱ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111ll11_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ጲ"), result)
        def bstack111ll11l1l_opy_(this, arg=None):
            self.handler(hook_type, bstack111ll11_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨጳ"))
            result = None
            exception = None
            try:
                self.bstack111l1l1lll_opy_(hook_type, self._111ll11111_opy_[hook_type], (this, arg))
                result = Result(result=bstack111ll11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩጴ"))
            except Exception as e:
                result = Result(result=bstack111ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪጵ"), exception=e)
                self.handler(hook_type, bstack111ll11_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪጶ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111ll11_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫጷ"), result)
        if hook_type in [bstack111ll11_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬጸ"), bstack111ll11_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩጹ")]:
            return bstack111ll11l1l_opy_
        return bstack111ll111l1_opy_
    def bstack111ll111ll_opy_(self, bstack111l1ll1l1_opy_):
        def bstack111ll11ll1_opy_(this, *args, **kwargs):
            self.bstack111ll11lll_opy_(this, bstack111l1ll1l1_opy_)
            self._111l1lll1l_opy_[bstack111l1ll1l1_opy_](this, *args, **kwargs)
        return bstack111ll11ll1_opy_