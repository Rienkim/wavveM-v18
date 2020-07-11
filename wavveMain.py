# -*- coding: utf-8 -*-
from wavveRun import *
__author__ = "NightRain"
import os
import sys
import xbmcaddon
reload(sys)
sys.setdefaultencoding('utf-8')
__cwd__ = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path'))
__lib__ = os.path.join(__cwd__, 'resources', 'lib')
sys.path.append(__lib__)


def Iiii111Ii11I1():
  ooO0oooOoO0 = urlparse.parse_qs(sys.argv[2][1:])
  for II11i in ooO0oooOoO0.keys():
    ooO0oooOoO0[II11i] = ooO0oooOoO0[II11i][0]
  return ooO0oooOoO0


i1111 = o000o0o00o0Oo(sys.argv[0], int(sys.argv[1]), Iiii111Ii11I1())
i1111.wavve_main()
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
