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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack1ll11l11l_opy_, bstack1ll11111l1_opy_
class bstack11ll1ll11_opy_:
  working_dir = os.getcwd()
  bstack1l11l1l1l_opy_ = False
  config = {}
  binary_path = bstack111ll11_opy_ (u"ࠨࠩᎱ")
  bstack11111ll11l_opy_ = bstack111ll11_opy_ (u"ࠩࠪᎲ")
  bstack1l1lllll1l_opy_ = False
  bstack1111l1llll_opy_ = None
  bstack1111ll1l11_opy_ = {}
  bstack1111l1111l_opy_ = 300
  bstack111111llll_opy_ = False
  logger = None
  bstack11111ll1l1_opy_ = False
  bstack1111lll1l1_opy_ = bstack111ll11_opy_ (u"ࠪࠫᎳ")
  bstack1111l11lll_opy_ = {
    bstack111ll11_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫᎴ") : 1,
    bstack111ll11_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭Ꮅ") : 2,
    bstack111ll11_opy_ (u"࠭ࡥࡥࡩࡨࠫᎶ") : 3,
    bstack111ll11_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧᎷ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1111lll111_opy_(self):
    bstack1111l11l11_opy_ = bstack111ll11_opy_ (u"ࠨࠩᎸ")
    bstack1111ll11ll_opy_ = sys.platform
    bstack11111l1111_opy_ = bstack111ll11_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨᎹ")
    if re.match(bstack111ll11_opy_ (u"ࠥࡨࡦࡸࡷࡪࡰࡿࡱࡦࡩࠠࡰࡵࠥᎺ"), bstack1111ll11ll_opy_) != None:
      bstack1111l11l11_opy_ = bstack11l1l11111_opy_ + bstack111ll11_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡴࡹࡸ࠯ࡼ࡬ࡴࠧᎻ")
      self.bstack1111lll1l1_opy_ = bstack111ll11_opy_ (u"ࠬࡳࡡࡤࠩᎼ")
    elif re.match(bstack111ll11_opy_ (u"ࠨ࡭ࡴࡹ࡬ࡲࢁࡳࡳࡺࡵࡿࡱ࡮ࡴࡧࡸࡾࡦࡽ࡬ࡽࡩ࡯ࡾࡥࡧࡨࡽࡩ࡯ࡾࡺ࡭ࡳࡩࡥࡽࡧࡰࡧࢁࡽࡩ࡯࠵࠵ࠦᎽ"), bstack1111ll11ll_opy_) != None:
      bstack1111l11l11_opy_ = bstack11l1l11111_opy_ + bstack111ll11_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡸ࡫ࡱ࠲ࡿ࡯ࡰࠣᎾ")
      bstack11111l1111_opy_ = bstack111ll11_opy_ (u"ࠣࡲࡨࡶࡨࡿ࠮ࡦࡺࡨࠦᎿ")
      self.bstack1111lll1l1_opy_ = bstack111ll11_opy_ (u"ࠩࡺ࡭ࡳ࠭Ꮐ")
    else:
      bstack1111l11l11_opy_ = bstack11l1l11111_opy_ + bstack111ll11_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡰ࡮ࡴࡵࡹ࠰ࡽ࡭ࡵࠨᏁ")
      self.bstack1111lll1l1_opy_ = bstack111ll11_opy_ (u"ࠫࡱ࡯࡮ࡶࡺࠪᏂ")
    return bstack1111l11l11_opy_, bstack11111l1111_opy_
  def bstack11111ll1ll_opy_(self):
    try:
      bstack1111llll1l_opy_ = [os.path.join(expanduser(bstack111ll11_opy_ (u"ࠧࢄࠢᏃ")), bstack111ll11_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭Ꮔ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1111llll1l_opy_:
        if(self.bstack11111l111l_opy_(path)):
          return path
      raise bstack111ll11_opy_ (u"ࠢࡖࡰࡤࡰࡧ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦᏅ")
    except Exception as e:
      self.logger.error(bstack111ll11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥࡶࡡࡵࡪࠣࡪࡴࡸࠠࡱࡧࡵࡧࡾࠦࡤࡰࡹࡱࡰࡴࡧࡤ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࠳ࠠࡼࡿࠥᏆ").format(e))
  def bstack11111l111l_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1111l111ll_opy_(self, bstack1111l11l11_opy_, bstack11111l1111_opy_):
    try:
      bstack11111l1ll1_opy_ = self.bstack11111ll1ll_opy_()
      bstack1111lll11l_opy_ = os.path.join(bstack11111l1ll1_opy_, bstack111ll11_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯ࡼ࡬ࡴࠬᏇ"))
      bstack11111l11ll_opy_ = os.path.join(bstack11111l1ll1_opy_, bstack11111l1111_opy_)
      if os.path.exists(bstack11111l11ll_opy_):
        self.logger.info(bstack111ll11_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡵ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧᏈ").format(bstack11111l11ll_opy_))
        return bstack11111l11ll_opy_
      if os.path.exists(bstack1111lll11l_opy_):
        self.logger.info(bstack111ll11_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡾ࡮ࡶࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡾࢁ࠱ࠦࡵ࡯ࡼ࡬ࡴࡵ࡯࡮ࡨࠤᏉ").format(bstack1111lll11l_opy_))
        return self.bstack1111ll1111_opy_(bstack1111lll11l_opy_, bstack11111l1111_opy_)
      self.logger.info(bstack111ll11_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳࠠࡼࡿࠥᏊ").format(bstack1111l11l11_opy_))
      response = bstack1ll11111l1_opy_(bstack111ll11_opy_ (u"࠭ࡇࡆࡖࠪᏋ"), bstack1111l11l11_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack1111lll11l_opy_, bstack111ll11_opy_ (u"ࠧࡸࡤࠪᏌ")) as file:
          file.write(response.content)
        self.logger.info(bstack111ll11_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦࡨࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡦࡴࡤࠡࡵࡤࡺࡪࡪࠠࡢࡶࠣࡿࢂࠨᏍ").format(bstack1111lll11l_opy_))
        return self.bstack1111ll1111_opy_(bstack1111lll11l_opy_, bstack11111l1111_opy_)
      else:
        raise(bstack111ll11_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡵࡪࡨࠤ࡫࡯࡬ࡦ࠰ࠣࡗࡹࡧࡴࡶࡵࠣࡧࡴࡪࡥ࠻ࠢࡾࢁࠧᏎ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack111ll11_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿ࠺ࠡࡽࢀࠦᏏ").format(e))
  def bstack1111lll1ll_opy_(self, bstack1111l11l11_opy_, bstack11111l1111_opy_):
    try:
      retry = 2
      bstack11111l11ll_opy_ = None
      bstack11111lll11_opy_ = False
      while retry > 0:
        bstack11111l11ll_opy_ = self.bstack1111l111ll_opy_(bstack1111l11l11_opy_, bstack11111l1111_opy_)
        bstack11111lll11_opy_ = self.bstack1111ll111l_opy_(bstack1111l11l11_opy_, bstack11111l1111_opy_, bstack11111l11ll_opy_)
        if bstack11111lll11_opy_:
          break
        retry -= 1
      return bstack11111l11ll_opy_, bstack11111lll11_opy_
    except Exception as e:
      self.logger.error(bstack111ll11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡨࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡴࡦࡺࡨࠣᏐ").format(e))
    return bstack11111l11ll_opy_, False
  def bstack1111ll111l_opy_(self, bstack1111l11l11_opy_, bstack11111l1111_opy_, bstack11111l11ll_opy_, bstack11111l11l1_opy_ = 0):
    if bstack11111l11l1_opy_ > 1:
      return False
    if bstack11111l11ll_opy_ == None or os.path.exists(bstack11111l11ll_opy_) == False:
      self.logger.warn(bstack111ll11_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡵࡧࡴࡩࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠱ࠦࡲࡦࡶࡵࡽ࡮ࡴࡧࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠥᏑ"))
      return False
    bstack1111l111l1_opy_ = bstack111ll11_opy_ (u"ࠨ࡞࠯ࠬࡃࡴࡪࡸࡣࡺ࡞࠲ࡧࡱ࡯ࠠ࡝ࡦ࠱ࡠࡩ࠱࠮࡝ࡦ࠮ࠦᏒ")
    command = bstack111ll11_opy_ (u"ࠧࡼࡿࠣ࠱࠲ࡼࡥࡳࡵ࡬ࡳࡳ࠭Ꮣ").format(bstack11111l11ll_opy_)
    bstack1111l1ll1l_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1111l111l1_opy_, bstack1111l1ll1l_opy_) != None:
      return True
    else:
      self.logger.error(bstack111ll11_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡥ࡫ࡩࡨࡱࠠࡧࡣ࡬ࡰࡪࡪࠢᏔ"))
      return False
  def bstack1111ll1111_opy_(self, bstack1111lll11l_opy_, bstack11111l1111_opy_):
    try:
      working_dir = os.path.dirname(bstack1111lll11l_opy_)
      shutil.unpack_archive(bstack1111lll11l_opy_, working_dir)
      bstack11111l11ll_opy_ = os.path.join(working_dir, bstack11111l1111_opy_)
      os.chmod(bstack11111l11ll_opy_, 0o755)
      return bstack11111l11ll_opy_
    except Exception as e:
      self.logger.error(bstack111ll11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡻ࡮ࡻ࡫ࡳࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠥᏕ"))
  def bstack1111ll1ll1_opy_(self):
    try:
      percy = str(self.config.get(bstack111ll11_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩᏖ"), bstack111ll11_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥᏗ"))).lower()
      if percy != bstack111ll11_opy_ (u"ࠧࡺࡲࡶࡧࠥᏘ"):
        return False
      self.bstack1l1lllll1l_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack111ll11_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡣࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᏙ").format(e))
  def bstack1111l11l1l_opy_(self):
    try:
      bstack1111l11l1l_opy_ = str(self.config.get(bstack111ll11_opy_ (u"ࠧࡱࡧࡵࡧࡾࡉࡡࡱࡶࡸࡶࡪࡓ࡯ࡥࡧࠪᏚ"), bstack111ll11_opy_ (u"ࠣࡣࡸࡸࡴࠨᏛ"))).lower()
      return bstack1111l11l1l_opy_
    except Exception as e:
      self.logger.error(bstack111ll11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼࠤࡨࡧࡰࡵࡷࡵࡩࠥࡳ࡯ࡥࡧ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᏜ").format(e))
  def init(self, bstack1l11l1l1l_opy_, config, logger):
    self.bstack1l11l1l1l_opy_ = bstack1l11l1l1l_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1111ll1ll1_opy_():
      return
    self.bstack1111ll1l11_opy_ = config.get(bstack111ll11_opy_ (u"ࠪࡴࡪࡸࡣࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᏝ"), {})
    self.bstack1111ll1l1l_opy_ = config.get(bstack111ll11_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧᏞ"), bstack111ll11_opy_ (u"ࠧࡧࡵࡵࡱࠥᏟ"))
    try:
      bstack1111l11l11_opy_, bstack11111l1111_opy_ = self.bstack1111lll111_opy_()
      bstack11111l11ll_opy_, bstack11111lll11_opy_ = self.bstack1111lll1ll_opy_(bstack1111l11l11_opy_, bstack11111l1111_opy_)
      if bstack11111lll11_opy_:
        self.binary_path = bstack11111l11ll_opy_
        thread = Thread(target=self.bstack11111l1lll_opy_)
        thread.start()
      else:
        self.bstack11111ll1l1_opy_ = True
        self.logger.error(bstack111ll11_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡱࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡕ࡫ࡲࡤࡻࠥᏠ").format(bstack11111l11ll_opy_))
    except Exception as e:
      self.logger.error(bstack111ll11_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᏡ").format(e))
  def bstack1111l11ll1_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack111ll11_opy_ (u"ࠨ࡮ࡲ࡫ࠬᏢ"), bstack111ll11_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯࡮ࡲ࡫ࠬᏣ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack111ll11_opy_ (u"ࠥࡔࡺࡹࡨࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࡳࠡࡣࡷࠤࢀࢃࠢᏤ").format(logfile))
      self.bstack11111ll11l_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack111ll11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࠠࡱࡣࡷ࡬࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᏥ").format(e))
  def bstack11111l1lll_opy_(self):
    bstack1111l1ll11_opy_ = self.bstack11111l1l1l_opy_()
    if bstack1111l1ll11_opy_ == None:
      self.bstack11111ll1l1_opy_ = True
      self.logger.error(bstack111ll11_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡹࡵ࡫ࡦࡰࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠣᏦ"))
      return False
    command_args = [bstack111ll11_opy_ (u"ࠨࡡࡱࡲ࠽ࡩࡽ࡫ࡣ࠻ࡵࡷࡥࡷࡺࠢᏧ") if self.bstack1l11l1l1l_opy_ else bstack111ll11_opy_ (u"ࠧࡦࡺࡨࡧ࠿ࡹࡴࡢࡴࡷࠫᏨ")]
    bstack1111l1l11l_opy_ = self.bstack1111l1l1ll_opy_()
    if bstack1111l1l11l_opy_ != None:
      command_args.append(bstack111ll11_opy_ (u"ࠣ࠯ࡦࠤࢀࢃࠢᏩ").format(bstack1111l1l11l_opy_))
    env = os.environ.copy()
    env[bstack111ll11_opy_ (u"ࠤࡓࡉࡗࡉ࡙ࡠࡖࡒࡏࡊࡔࠢᏪ")] = bstack1111l1ll11_opy_
    bstack11111ll111_opy_ = [self.binary_path]
    self.bstack1111l11ll1_opy_()
    self.bstack1111l1llll_opy_ = self.bstack111l11111l_opy_(bstack11111ll111_opy_ + command_args, env)
    self.logger.debug(bstack111ll11_opy_ (u"ࠥࡗࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠦᏫ"))
    bstack11111l11l1_opy_ = 0
    while self.bstack1111l1llll_opy_.poll() == None:
      bstack1111llll11_opy_ = self.bstack1111ll11l1_opy_()
      if bstack1111llll11_opy_:
        self.logger.debug(bstack111ll11_opy_ (u"ࠦࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲࠢᏬ"))
        self.bstack111111llll_opy_ = True
        return True
      bstack11111l11l1_opy_ += 1
      self.logger.debug(bstack111ll11_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡗ࡫ࡴࡳࡻࠣ࠱ࠥࢁࡽࠣᏭ").format(bstack11111l11l1_opy_))
      time.sleep(2)
    self.logger.error(bstack111ll11_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠬࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡇࡣ࡬ࡰࡪࡪࠠࡢࡨࡷࡩࡷࠦࡻࡾࠢࡤࡸࡹ࡫࡭ࡱࡶࡶࠦᏮ").format(bstack11111l11l1_opy_))
    self.bstack11111ll1l1_opy_ = True
    return False
  def bstack1111ll11l1_opy_(self, bstack11111l11l1_opy_ = 0):
    try:
      if bstack11111l11l1_opy_ > 10:
        return False
      bstack111l111111_opy_ = os.environ.get(bstack111ll11_opy_ (u"ࠧࡑࡇࡕࡇ࡞ࡥࡓࡆࡔ࡙ࡉࡗࡥࡁࡅࡆࡕࡉࡘ࡙ࠧᏯ"), bstack111ll11_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰࡮ࡲࡧࡦࡲࡨࡰࡵࡷ࠾࠺࠹࠳࠹ࠩᏰ"))
      bstack1111lllll1_opy_ = bstack111l111111_opy_ + bstack11l1l11l11_opy_
      response = requests.get(bstack1111lllll1_opy_)
      return True if response.json() else False
    except:
      return False
  def bstack11111l1l1l_opy_(self):
    bstack1111l11111_opy_ = bstack111ll11_opy_ (u"ࠩࡤࡴࡵ࠭Ᏹ") if self.bstack1l11l1l1l_opy_ else bstack111ll11_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᏲ")
    bstack111lll1111_opy_ = bstack111ll11_opy_ (u"ࠦࡦࡶࡩ࠰ࡣࡳࡴࡤࡶࡥࡳࡥࡼ࠳࡬࡫ࡴࡠࡲࡵࡳ࡯࡫ࡣࡵࡡࡷࡳࡰ࡫࡮ࡀࡰࡤࡱࡪࡃࡻࡾࠨࡷࡽࡵ࡫࠽ࡼࡿࠥᏳ").format(self.config[bstack111ll11_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᏴ")], bstack1111l11111_opy_)
    uri = bstack1ll11l11l_opy_(bstack111lll1111_opy_)
    try:
      response = bstack1ll11111l1_opy_(bstack111ll11_opy_ (u"࠭ࡇࡆࡖࠪᏵ"), uri, {}, {bstack111ll11_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ᏶"): (self.config[bstack111ll11_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ᏷")], self.config[bstack111ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬᏸ")])})
      if response.status_code == 200:
        bstack1111l1l1l1_opy_ = response.json()
        if bstack111ll11_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤᏹ") in bstack1111l1l1l1_opy_:
          return bstack1111l1l1l1_opy_[bstack111ll11_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥᏺ")]
        else:
          raise bstack111ll11_opy_ (u"࡚ࠬ࡯࡬ࡧࡱࠤࡓࡵࡴࠡࡈࡲࡹࡳࡪࠠ࠮ࠢࡾࢁࠬᏻ").format(bstack1111l1l1l1_opy_)
      else:
        raise bstack111ll11_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡲࡨࡶࡨࡿࠠࡵࡱ࡮ࡩࡳ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡶࡸࡦࡺࡵࡴࠢ࠰ࠤࢀࢃࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡆࡴࡪࡹࠡ࠯ࠣࡿࢂࠨᏼ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack111ll11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠࡱࡴࡲ࡮ࡪࡩࡴࠣᏽ").format(e))
  def bstack1111l1l1ll_opy_(self):
    bstack111l1111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack111ll11_opy_ (u"ࠣࡲࡨࡶࡨࡿࡃࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠦ᏾"))
    try:
      if bstack111ll11_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ᏿") not in self.bstack1111ll1l11_opy_:
        self.bstack1111ll1l11_opy_[bstack111ll11_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫ᐀")] = 2
      with open(bstack111l1111l1_opy_, bstack111ll11_opy_ (u"ࠫࡼ࠭ᐁ")) as fp:
        json.dump(self.bstack1111ll1l11_opy_, fp)
      return bstack111l1111l1_opy_
    except Exception as e:
      self.logger.error(bstack111ll11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡥࡵࡩࡦࡺࡥࠡࡲࡨࡶࡨࡿࠠࡤࡱࡱࡪ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᐂ").format(e))
  def bstack111l11111l_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1111lll1l1_opy_ == bstack111ll11_opy_ (u"࠭ࡷࡪࡰࠪᐃ"):
        bstack1111l1lll1_opy_ = [bstack111ll11_opy_ (u"ࠧࡤ࡯ࡧ࠲ࡪࡾࡥࠨᐄ"), bstack111ll11_opy_ (u"ࠨ࠱ࡦࠫᐅ")]
        cmd = bstack1111l1lll1_opy_ + cmd
      cmd = bstack111ll11_opy_ (u"ࠩࠣࠫᐆ").join(cmd)
      self.logger.debug(bstack111ll11_opy_ (u"ࠥࡖࡺࡴ࡮ࡪࡰࡪࠤࢀࢃࠢᐇ").format(cmd))
      with open(self.bstack11111ll11l_opy_, bstack111ll11_opy_ (u"ࠦࡦࠨᐈ")) as bstack11111l1l11_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack11111l1l11_opy_, text=True, stderr=bstack11111l1l11_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack11111ll1l1_opy_ = True
      self.logger.error(bstack111ll11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠦࡷࡪࡶ࡫ࠤࡨࡳࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢᐉ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack111111llll_opy_:
        self.logger.info(bstack111ll11_opy_ (u"ࠨࡓࡵࡱࡳࡴ࡮ࡴࡧࠡࡒࡨࡶࡨࡿࠢᐊ"))
        cmd = [self.binary_path, bstack111ll11_opy_ (u"ࠢࡦࡺࡨࡧ࠿ࡹࡴࡰࡲࠥᐋ")]
        self.bstack111l11111l_opy_(cmd)
        self.bstack111111llll_opy_ = False
    except Exception as e:
      self.logger.error(bstack111ll11_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺ࡯ࡱࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡥࡲࡱࡲࡧ࡮ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣᐌ").format(cmd, e))
  def bstack1l1lll1ll1_opy_(self):
    if not self.bstack1l1lllll1l_opy_:
      return
    try:
      bstack1111ll1lll_opy_ = 0
      while not self.bstack111111llll_opy_ and bstack1111ll1lll_opy_ < self.bstack1111l1111l_opy_:
        if self.bstack11111ll1l1_opy_:
          self.logger.info(bstack111ll11_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡵࡨࡸࡺࡶࠠࡧࡣ࡬ࡰࡪࡪࠢᐍ"))
          return
        time.sleep(1)
        bstack1111ll1lll_opy_ += 1
      os.environ[bstack111ll11_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡅࡉࡘ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࠩᐎ")] = str(self.bstack1111llllll_opy_())
      self.logger.info(bstack111ll11_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡷࡪࡺࡵࡱࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠧᐏ"))
    except Exception as e:
      self.logger.error(bstack111ll11_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᐐ").format(e))
  def bstack1111llllll_opy_(self):
    if self.bstack1l11l1l1l_opy_:
      return
    try:
      bstack11111lllll_opy_ = [platform[bstack111ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫᐑ")].lower() for platform in self.config.get(bstack111ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᐒ"), [])]
      bstack11111lll1l_opy_ = sys.maxsize
      bstack1111l1l111_opy_ = bstack111ll11_opy_ (u"ࠨࠩᐓ")
      for browser in bstack11111lllll_opy_:
        if browser in self.bstack1111l11lll_opy_:
          bstack11111llll1_opy_ = self.bstack1111l11lll_opy_[browser]
        if bstack11111llll1_opy_ < bstack11111lll1l_opy_:
          bstack11111lll1l_opy_ = bstack11111llll1_opy_
          bstack1111l1l111_opy_ = browser
      return bstack1111l1l111_opy_
    except Exception as e:
      self.logger.error(bstack111ll11_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡦࡪࡹࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᐔ").format(e))