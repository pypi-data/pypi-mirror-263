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
class bstack11l1ll111l_opy_(object):
  bstack11l1l1lll_opy_ = os.path.join(os.path.expanduser(bstack111ll11_opy_ (u"ࠧࡿ໋ࠩ")), bstack111ll11_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ໌"))
  bstack11l1ll1l11_opy_ = os.path.join(bstack11l1l1lll_opy_, bstack111ll11_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶ࠲࡯ࡹ࡯࡯ࠩໍ"))
  bstack11l1ll11l1_opy_ = None
  perform_scan = None
  bstack1ll11llll_opy_ = None
  bstack1111ll1l1_opy_ = None
  bstack11ll11111l_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack111ll11_opy_ (u"ࠪ࡭ࡳࡹࡴࡢࡰࡦࡩࠬ໎")):
      cls.instance = super(bstack11l1ll111l_opy_, cls).__new__(cls)
      cls.instance.bstack11l1ll1l1l_opy_()
    return cls.instance
  def bstack11l1ll1l1l_opy_(self):
    try:
      with open(self.bstack11l1ll1l11_opy_, bstack111ll11_opy_ (u"ࠫࡷ࠭໏")) as bstack1ll1l1ll_opy_:
        bstack11l1ll1111_opy_ = bstack1ll1l1ll_opy_.read()
        data = json.loads(bstack11l1ll1111_opy_)
        if bstack111ll11_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧ໐") in data:
          self.bstack11ll11l1ll_opy_(data[bstack111ll11_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨ໑")])
        if bstack111ll11_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨ໒") in data:
          self.bstack11ll11ll11_opy_(data[bstack111ll11_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩ໓")])
    except:
      pass
  def bstack11ll11ll11_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts[bstack111ll11_opy_ (u"ࠩࡶࡧࡦࡴࠧ໔")]
      self.bstack1ll11llll_opy_ = scripts[bstack111ll11_opy_ (u"ࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠧ໕")]
      self.bstack1111ll1l1_opy_ = scripts[bstack111ll11_opy_ (u"ࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠨ໖")]
      self.bstack11ll11111l_opy_ = scripts[bstack111ll11_opy_ (u"ࠬࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠪ໗")]
  def bstack11ll11l1ll_opy_(self, bstack11l1ll11l1_opy_):
    if bstack11l1ll11l1_opy_ != None and len(bstack11l1ll11l1_opy_) != 0:
      self.bstack11l1ll11l1_opy_ = bstack11l1ll11l1_opy_
  def store(self):
    try:
      with open(self.bstack11l1ll1l11_opy_, bstack111ll11_opy_ (u"࠭ࡷࠨ໘")) as file:
        json.dump({
          bstack111ll11_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࠤ໙"): self.bstack11l1ll11l1_opy_,
          bstack111ll11_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࡴࠤ໚"): {
            bstack111ll11_opy_ (u"ࠤࡶࡧࡦࡴࠢ໛"): self.perform_scan,
            bstack111ll11_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠢໜ"): self.bstack1ll11llll_opy_,
            bstack111ll11_opy_ (u"ࠦ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࡔࡷࡰࡱࡦࡸࡹࠣໝ"): self.bstack1111ll1l1_opy_,
            bstack111ll11_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥໞ"): self.bstack11ll11111l_opy_
          }
        }, file)
    except:
      pass
  def bstack11l1l11l1_opy_(self, bstack11l1ll11ll_opy_):
    try:
      return any(command.get(bstack111ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫໟ")) == bstack11l1ll11ll_opy_ for command in self.bstack11l1ll11l1_opy_)
    except:
      return False
bstack1lll11ll1_opy_ = bstack11l1ll111l_opy_()