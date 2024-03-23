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
import sys
import logging
import tarfile
import io
import os
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l11l1l_opy_
import tempfile
import json
bstack111l1l1111_opy_ = os.path.join(tempfile.gettempdir(), bstack111ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡥࡧࡥࡹ࡬࠴࡬ࡰࡩࠪጺ"))
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack111ll11_opy_ (u"ࠩ࡟ࡲࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧጻ"),
      datefmt=bstack111ll11_opy_ (u"ࠪࠩࡍࡀࠥࡎ࠼ࠨࡗࠬጼ"),
      stream=sys.stdout
    )
  return logger
def bstack111l11ll11_opy_():
  global bstack111l1l1111_opy_
  if os.path.exists(bstack111l1l1111_opy_):
    os.remove(bstack111l1l1111_opy_)
def bstack11l11l111_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack11l1l1ll_opy_(config, log_level):
  bstack111l11l1ll_opy_ = log_level
  if bstack111ll11_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ጽ") in config:
    bstack111l11l1ll_opy_ = bstack11l1l11l1l_opy_[config[bstack111ll11_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧጾ")]]
  if config.get(bstack111ll11_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨጿ"), False):
    logging.getLogger().setLevel(bstack111l11l1ll_opy_)
    return bstack111l11l1ll_opy_
  global bstack111l1l1111_opy_
  bstack11l11l111_opy_()
  bstack111l1l111l_opy_ = logging.Formatter(
    fmt=bstack111ll11_opy_ (u"ࠧ࡝ࡰࠨࠬࡦࡹࡣࡵ࡫ࡰࡩ࠮ࡹࠠ࡜ࠧࠫࡲࡦࡳࡥࠪࡵࡠ࡟ࠪ࠮࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠫࡶࡡࠥ࠳ࠠࠦࠪࡰࡩࡸࡹࡡࡨࡧࠬࡷࠬፀ"),
    datefmt=bstack111ll11_opy_ (u"ࠨࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪፁ")
  )
  bstack111l1l1ll1_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack111l1l1111_opy_)
  file_handler.setFormatter(bstack111l1l111l_opy_)
  bstack111l1l1ll1_opy_.setFormatter(bstack111l1l111l_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack111l1l1ll1_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack111ll11_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࠮ࡳࡧࡰࡳࡹ࡫࠮ࡳࡧࡰࡳࡹ࡫࡟ࡤࡱࡱࡲࡪࡩࡴࡪࡱࡱࠫፂ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack111l1l1ll1_opy_.setLevel(bstack111l11l1ll_opy_)
  logging.getLogger().addHandler(bstack111l1l1ll1_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack111l11l1ll_opy_
def bstack111l1l11ll_opy_(config):
  try:
    bstack111l11l1l1_opy_ = set([
      bstack111ll11_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬፃ"), bstack111ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧፄ"), bstack111ll11_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨፅ"), bstack111ll11_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪፆ"), bstack111ll11_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠩፇ"),
      bstack111ll11_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫፈ"), bstack111ll11_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬፉ"), bstack111ll11_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡒࡵࡳࡽࡿࡕࡴࡧࡵࠫፊ"), bstack111ll11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡓࡶࡴࡾࡹࡑࡣࡶࡷࠬፋ")
    ])
    bstack111l11lll1_opy_ = bstack111ll11_opy_ (u"ࠬ࠭ፌ")
    with open(bstack111ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩፍ")) as bstack111l11llll_opy_:
      bstack111l11ll1l_opy_ = bstack111l11llll_opy_.read()
      bstack111l11lll1_opy_ = re.sub(bstack111ll11_opy_ (u"ࡲࠨࡠࠫࡠࡸ࠱ࠩࡀࠥ࠱࠮ࠩࡢ࡮ࠨፎ"), bstack111ll11_opy_ (u"ࠨࠩፏ"), bstack111l11ll1l_opy_, flags=re.M)
      bstack111l11lll1_opy_ = re.sub(
        bstack111ll11_opy_ (u"ࡴࠪࡢ࠭ࡢࡳࠬࠫࡂࠬࠬፐ") + bstack111ll11_opy_ (u"ࠪࢀࠬፑ").join(bstack111l11l1l1_opy_) + bstack111ll11_opy_ (u"ࠫ࠮࠴ࠪࠥࠩፒ"),
        bstack111ll11_opy_ (u"ࡷ࠭࡜࠳࠼ࠣ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧፓ"),
        bstack111l11lll1_opy_, flags=re.M | re.I
      )
    def bstack111l1l1l1l_opy_(dic):
      bstack111l1l1l11_opy_ = {}
      for key, value in dic.items():
        if key in bstack111l11l1l1_opy_:
          bstack111l1l1l11_opy_[key] = bstack111ll11_opy_ (u"࡛࠭ࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪፔ")
        else:
          if isinstance(value, dict):
            bstack111l1l1l11_opy_[key] = bstack111l1l1l1l_opy_(value)
          else:
            bstack111l1l1l11_opy_[key] = value
      return bstack111l1l1l11_opy_
    bstack111l1l1l11_opy_ = bstack111l1l1l1l_opy_(config)
    return {
      bstack111ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪፕ"): bstack111l11lll1_opy_,
      bstack111ll11_opy_ (u"ࠨࡨ࡬ࡲࡦࡲࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫፖ"): json.dumps(bstack111l1l1l11_opy_)
    }
  except Exception as e:
    return {}
def bstack1l1lll11ll_opy_(config):
  global bstack111l1l1111_opy_
  try:
    if config.get(bstack111ll11_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫፗ"), False):
      return
    uuid = os.getenv(bstack111ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨፘ"))
    if not uuid or uuid == bstack111ll11_opy_ (u"ࠫࡳࡻ࡬࡭ࠩፙ"):
      return
    bstack111l1l11l1_opy_ = [bstack111ll11_opy_ (u"ࠬࡸࡥࡲࡷ࡬ࡶࡪࡳࡥ࡯ࡶࡶ࠲ࡹࡾࡴࠨፚ"), bstack111ll11_opy_ (u"࠭ࡐࡪࡲࡩ࡭ࡱ࡫ࠧ፛"), bstack111ll11_opy_ (u"ࠧࡱࡻࡳࡶࡴࡰࡥࡤࡶ࠱ࡸࡴࡳ࡬ࠨ፜"), bstack111l1l1111_opy_]
    bstack11l11l111_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack111ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠮࡮ࡲ࡫ࡸ࠳ࠧ፝") + uuid + bstack111ll11_opy_ (u"ࠩ࠱ࡸࡦࡸ࠮ࡨࡼࠪ፞"))
    with tarfile.open(output_file, bstack111ll11_opy_ (u"ࠥࡻ࠿࡭ࡺࠣ፟")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack111l1l11l1_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack111l1l11ll_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack111l11l11l_opy_ = data.encode()
        tarinfo.size = len(bstack111l11l11l_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack111l11l11l_opy_))
    bstack1lll111l1_opy_ = MultipartEncoder(
      fields= {
        bstack111ll11_opy_ (u"ࠫࡩࡧࡴࡢࠩ፠"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack111ll11_opy_ (u"ࠬࡸࡢࠨ፡")), bstack111ll11_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳ࡽ࠳ࡧࡻ࡫ࡳࠫ።")),
        bstack111ll11_opy_ (u"ࠧࡤ࡮࡬ࡩࡳࡺࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩ፣"): uuid
      }
    )
    response = requests.post(
      bstack111ll11_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡸࡴࡱࡵࡡࡥ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡩ࡬ࡪࡧࡱࡸ࠲ࡲ࡯ࡨࡵ࠲ࡹࡵࡲ࡯ࡢࡦࠥ፤"),
      data=bstack1lll111l1_opy_,
      headers={bstack111ll11_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ፥"): bstack1lll111l1_opy_.content_type},
      auth=(config[bstack111ll11_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ፦")], config[bstack111ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ፧")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack111ll11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡺࡶ࡬ࡰࡣࡧࠤࡱࡵࡧࡴ࠼ࠣࠫ፨") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack111ll11_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥ࡯ࡦ࡬ࡲ࡬ࠦ࡬ࡰࡩࡶ࠾ࠬ፩") + str(e))
  finally:
    try:
      bstack111l11ll11_opy_()
    except:
      pass