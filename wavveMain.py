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


def dropMultiArgv():
  argvDict = urlparse.parse_qs(sys.argv[2][1:])
  for key in argvDict.keys():
    argvDict[key] = argvDict[key][0]
  return argvDict


obj = WavveRun(sys.argv[0], int(sys.argv[1]), dropMultiArgv())
obj.wavve_main()
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
