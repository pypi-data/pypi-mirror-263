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
from uuid import uuid4
from bstack_utils.helper import bstack1lll1l1l11_opy_, bstack11l111l1l1_opy_
from bstack_utils.bstack1111l111l_opy_ import bstack1llllll111l_opy_
class bstack11lll1ll1l_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack1l1111llll_opy_=None, framework=None, tags=[], scope=[], bstack1llll11llll_opy_=None, bstack1llll111l1l_opy_=True, bstack1llll11l11l_opy_=None, bstack11ll11l11_opy_=None, result=None, duration=None, bstack11lllll1ll_opy_=None, meta={}):
        self.bstack11lllll1ll_opy_ = bstack11lllll1ll_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack1llll111l1l_opy_:
            self.uuid = uuid4().__str__()
        self.bstack1l1111llll_opy_ = bstack1l1111llll_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1llll11llll_opy_ = bstack1llll11llll_opy_
        self.bstack1llll11l11l_opy_ = bstack1llll11l11l_opy_
        self.bstack11ll11l11_opy_ = bstack11ll11l11_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
    def bstack1l1111l1l1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack1llll1l1111_opy_(self):
        bstack1llll11l111_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack111ll11_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩᒤ"): bstack1llll11l111_opy_,
            bstack111ll11_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠩᒥ"): bstack1llll11l111_opy_,
            bstack111ll11_opy_ (u"ࠨࡸࡦࡣ࡫࡯࡬ࡦࡲࡤࡸ࡭࠭ᒦ"): bstack1llll11l111_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack111ll11_opy_ (u"ࠤࡘࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡸࡱࡪࡴࡴ࠻ࠢࠥᒧ") + key)
            setattr(self, key, val)
    def bstack1llll1l11ll_opy_(self):
        return {
            bstack111ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨᒨ"): self.name,
            bstack111ll11_opy_ (u"ࠫࡧࡵࡤࡺࠩᒩ"): {
                bstack111ll11_opy_ (u"ࠬࡲࡡ࡯ࡩࠪᒪ"): bstack111ll11_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ᒫ"),
                bstack111ll11_opy_ (u"ࠧࡤࡱࡧࡩࠬᒬ"): self.code
            },
            bstack111ll11_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࡳࠨᒭ"): self.scope,
            bstack111ll11_opy_ (u"ࠩࡷࡥ࡬ࡹࠧᒮ"): self.tags,
            bstack111ll11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᒯ"): self.framework,
            bstack111ll11_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᒰ"): self.bstack1l1111llll_opy_
        }
    def bstack1llll111ll1_opy_(self):
        return {
         bstack111ll11_opy_ (u"ࠬࡳࡥࡵࡣࠪᒱ"): self.meta
        }
    def bstack1llll1l11l1_opy_(self):
        return {
            bstack111ll11_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡘࡥࡳࡷࡱࡔࡦࡸࡡ࡮ࠩᒲ"): {
                bstack111ll11_opy_ (u"ࠧࡳࡧࡵࡹࡳࡥ࡮ࡢ࡯ࡨࠫᒳ"): self.bstack1llll11llll_opy_
            }
        }
    def bstack1llll1l1ll1_opy_(self, bstack1llll11ll1l_opy_, details):
        step = next(filter(lambda st: st[bstack111ll11_opy_ (u"ࠨ࡫ࡧࠫᒴ")] == bstack1llll11ll1l_opy_, self.meta[bstack111ll11_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᒵ")]), None)
        step.update(details)
    def bstack1llll11ll11_opy_(self, bstack1llll11ll1l_opy_):
        step = next(filter(lambda st: st[bstack111ll11_opy_ (u"ࠪ࡭ࡩ࠭ᒶ")] == bstack1llll11ll1l_opy_, self.meta[bstack111ll11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᒷ")]), None)
        step.update({
            bstack111ll11_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᒸ"): bstack1lll1l1l11_opy_()
        })
    def bstack11llllll11_opy_(self, bstack1llll11ll1l_opy_, result, duration=None):
        bstack1llll11l11l_opy_ = bstack1lll1l1l11_opy_()
        if bstack1llll11ll1l_opy_ is not None and self.meta.get(bstack111ll11_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬᒹ")):
            step = next(filter(lambda st: st[bstack111ll11_opy_ (u"ࠧࡪࡦࠪᒺ")] == bstack1llll11ll1l_opy_, self.meta[bstack111ll11_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᒻ")]), None)
            step.update({
                bstack111ll11_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᒼ"): bstack1llll11l11l_opy_,
                bstack111ll11_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬᒽ"): duration if duration else bstack11l111l1l1_opy_(step[bstack111ll11_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᒾ")], bstack1llll11l11l_opy_),
                bstack111ll11_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᒿ"): result.result,
                bstack111ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧᓀ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1llll11l1ll_opy_):
        if self.meta.get(bstack111ll11_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᓁ")):
            self.meta[bstack111ll11_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᓂ")].append(bstack1llll11l1ll_opy_)
        else:
            self.meta[bstack111ll11_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᓃ")] = [ bstack1llll11l1ll_opy_ ]
    def bstack1llll11lll1_opy_(self):
        return {
            bstack111ll11_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᓄ"): self.bstack1l1111l1l1_opy_(),
            **self.bstack1llll1l11ll_opy_(),
            **self.bstack1llll1l1111_opy_(),
            **self.bstack1llll111ll1_opy_()
        }
    def bstack1llll111lll_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack111ll11_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᓅ"): self.bstack1llll11l11l_opy_,
            bstack111ll11_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ᓆ"): self.duration,
            bstack111ll11_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᓇ"): self.result.result
        }
        if data[bstack111ll11_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᓈ")] == bstack111ll11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᓉ"):
            data[bstack111ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᓊ")] = self.result.bstack11ll1l11l1_opy_()
            data[bstack111ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᓋ")] = [{bstack111ll11_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᓌ"): self.result.bstack11l11ll111_opy_()}]
        return data
    def bstack1llll1l111l_opy_(self):
        return {
            bstack111ll11_opy_ (u"ࠬࡻࡵࡪࡦࠪᓍ"): self.bstack1l1111l1l1_opy_(),
            **self.bstack1llll1l11ll_opy_(),
            **self.bstack1llll1l1111_opy_(),
            **self.bstack1llll111lll_opy_(),
            **self.bstack1llll111ll1_opy_()
        }
    def bstack1l111ll11l_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack111ll11_opy_ (u"࠭ࡓࡵࡣࡵࡸࡪࡪࠧᓎ") in event:
            return self.bstack1llll11lll1_opy_()
        elif bstack111ll11_opy_ (u"ࠧࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᓏ") in event:
            return self.bstack1llll1l111l_opy_()
    def bstack1l111lllll_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1llll11l11l_opy_ = time if time else bstack1lll1l1l11_opy_()
        self.duration = duration if duration else bstack11l111l1l1_opy_(self.bstack1l1111llll_opy_, self.bstack1llll11l11l_opy_)
        if result:
            self.result = result
class bstack11lll1lll1_opy_(bstack11lll1ll1l_opy_):
    def __init__(self, hooks=[], bstack1l1111ll11_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l1111ll11_opy_ = bstack1l1111ll11_opy_
        super().__init__(*args, **kwargs, bstack11ll11l11_opy_=bstack111ll11_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᓐ"))
    @classmethod
    def bstack1llll111l11_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack111ll11_opy_ (u"ࠩ࡬ࡨࠬᓑ"): id(step),
                bstack111ll11_opy_ (u"ࠪࡸࡪࡾࡴࠨᓒ"): step.name,
                bstack111ll11_opy_ (u"ࠫࡰ࡫ࡹࡸࡱࡵࡨࠬᓓ"): step.keyword,
            })
        return bstack11lll1lll1_opy_(
            **kwargs,
            meta={
                bstack111ll11_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪ࠭ᓔ"): {
                    bstack111ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᓕ"): feature.name,
                    bstack111ll11_opy_ (u"ࠧࡱࡣࡷ࡬ࠬᓖ"): feature.filename,
                    bstack111ll11_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ᓗ"): feature.description
                },
                bstack111ll11_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫᓘ"): {
                    bstack111ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨᓙ"): scenario.name
                },
                bstack111ll11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᓚ"): steps,
                bstack111ll11_opy_ (u"ࠬ࡫ࡸࡢ࡯ࡳࡰࡪࡹࠧᓛ"): bstack1llllll111l_opy_(test)
            }
        )
    def bstack1llll11l1l1_opy_(self):
        return {
            bstack111ll11_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᓜ"): self.hooks
        }
    def bstack1llll1l1l11_opy_(self):
        if self.bstack1l1111ll11_opy_:
            return {
                bstack111ll11_opy_ (u"ࠧࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸ࠭ᓝ"): self.bstack1l1111ll11_opy_
            }
        return {}
    def bstack1llll1l111l_opy_(self):
        return {
            **super().bstack1llll1l111l_opy_(),
            **self.bstack1llll11l1l1_opy_()
        }
    def bstack1llll11lll1_opy_(self):
        return {
            **super().bstack1llll11lll1_opy_(),
            **self.bstack1llll1l1l11_opy_()
        }
    def bstack1l111lllll_opy_(self):
        return bstack111ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪᓞ")
class bstack11llll11l1_opy_(bstack11lll1ll1l_opy_):
    def __init__(self, hook_type, *args, **kwargs):
        self.hook_type = hook_type
        super().__init__(*args, **kwargs, bstack11ll11l11_opy_=bstack111ll11_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᓟ"))
    def bstack1l111ll111_opy_(self):
        return self.hook_type
    def bstack1llll1l1l1l_opy_(self):
        return {
            bstack111ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ᓠ"): self.hook_type
        }
    def bstack1llll1l111l_opy_(self):
        return {
            **super().bstack1llll1l111l_opy_(),
            **self.bstack1llll1l1l1l_opy_()
        }
    def bstack1llll11lll1_opy_(self):
        return {
            **super().bstack1llll11lll1_opy_(),
            **self.bstack1llll1l1l1l_opy_()
        }
    def bstack1l111lllll_opy_(self):
        return bstack111ll11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳ࠭ᓡ")