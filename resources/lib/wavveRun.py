# -*- coding: utf-8 -*-
from wavveCore import *
__author__ = "NightRain"
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmc
import sys
import urlparse
import inputstreamhelper
import datetime
import time
reload(sys)
sys.setdefaultencoding('utf-8')
o0oO0 = [
    {'title': '홈', 'uicode': 'GN1', 'came': 'home'}, {'title': 'LIVE 채널', 'uicode': 'GN3', 'came': 'live'}, {
        'title': 'VOD 방송', 'uicode': 'GN2', 'came': 'broadcast'}    # i1IIi.I1Ii111 / IiII * OoooooooOO + I11i * oO0o
    # i11iIiiIii - II111iiii % I1Ii111 - iIii1I11I1II1.I1ii11iIi11i.II111iiii
    , {'title': '영화(Movie)', 'uicode': 'GN17', 'came': 'movie'}, {'title': '해외시리즈', 'uicode': 'GN12', 'came': 'global'}, {'title': '분류별 - 방송(VOD) - 인기순', 'uicode': 'GENRE', 'came': 'vodgenre', 'orderby': 'viewtime', 'ordernm': '인기순'}, {'title': '분류별 - 방송(VOD) - 최신순', 'uicode': 'GENRE', 'came': 'vodgenre', 'orderby': 'new', 'ordernm': '최신순'}, {'title': '분류별 - 영화(Movie) - 인기순', 'uicode': 'GENRE', 'came': 'moviegenre_svod', 'orderby': 'paid', 'ordernm': '인기순'}, {'title': '분류별 - 영화(Movie) - 업데이트순', 'uicode': 'GENRE', 'came': 'moviegenre_svod', 'orderby': 'displaystart', 'ordernm': '업데이트순'}, {'title': '검색', 'uicode': 'SEARCH', 'came': '-'}, {'title': 'Watched(시청목록)', 'uicode': 'WATCH', 'came': '-'}
]
OOoO = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
__addon__ = xbmcaddon.Addon()
__language__ = __addon__.getLocalizedString
__profile__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
__version__ = __addon__.getAddonInfo('version')
__addonid__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')


class o000o0o00o0Oo (object):
  def __init__(self, in_addonurl, in_handle, in_params):
    self._addon_url = in_addonurl
    self._addon_handle = in_handle
    self.main_params = in_params
    self.WavveObj = iII111ii()

  def addon_noti(self, sting):
    try:
      oOOOO = xbmcgui.Dialog()
      oOOOO.notification(__addonname__, sting)
    except:
      None

  def addon_log(self, string, isDebug=False):
    try:
      I1Ii = string.encode('utf-8', 'ignore')
    except:
      I1Ii = 'addonException: addon_log'
    if isDebug:
      o0oOo0Ooo0O = xbmc.LOGDEBUG
    else:
      o0oOo0Ooo0O = xbmc.LOGNOTICE
    xbmc.log("[%s-%s]: %s" %
             (__addonid__, __version__, I1Ii), level=o0oOo0Ooo0O)

  def get_keyboard_input(self, title):
    OOoO000O0OO = None
    iiI1IiI = xbmc.Keyboard()
    iiI1IiI.setHeading(title)
    xbmc.sleep(1000)
    iiI1IiI.doModal()
    if (iiI1IiI.isConfirmed()):
      OOoO000O0OO = iiI1IiI.getText()
    return OOoO000O0OO

  def get_settings_login_info(self):
    ii1 = __addon__.getSetting('id')
    o0oO0o00oo = __addon__.getSetting('pw')
    II1i1Ii11Ii11 = __addon__.getSetting('selected_profile')
    return (ii1, o0oO0o00oo, II1i1Ii11Ii11)

  def get_selQuality(self):
    try:
      oOOo0oo = [1080, 720, 480, 360]
      I11II1i = int(__addon__.getSetting('selected_quality'))
      return oOOo0oo[I11II1i]
    except:
      None
    return 1080

  def get_settings_exclusion21(self):
    iI = __addon__.getSetting('exclusion21')
    if iI == 'false':
      return False
    else:
      return True

  def get_settings_direct_replay(self):
    o00oOO0 = int(__addon__.getSetting('direct_replay'))
    if o00oOO0 == 0:
      return False
    else:
      return True

  def get_settings_addinfo(self):
    O0OOO00oo = __addon__.getSetting('add_infoyn')
    if O0OOO00oo == 'false':
      return False
    else:
      return True

  def get_settings_thumbnail_landyn(self):
    Ii1i11IIii1I = int(__addon__.getSetting('thumbnail_way'))
    if Ii1i11IIii1I == 0:
      return True
    else:
      return False

  def set_winCredential(self, credential):
    OooO0OoOOOO = xbmcgui.Window(10000)
    OooO0OoOOOO.setProperty('WAVVE_M_CREDENTIAL', credential)
    OooO0OoOOOO.setProperty(
        'WAVVE_M_LOGINTIME', datetime.datetime.now().strftime('%Y-%m-%d'))

  def get_winCredential(self):
    OooO0OoOOOO = xbmcgui.Window(10000)
    return OooO0OoOOOO.getProperty('WAVVE_M_CREDENTIAL')

  def set_winEpisodeOrderby(self, orderby):
    OooO0OoOOOO = xbmcgui.Window(10000)
    OooO0OoOOOO.setProperty('WAVVE_M_ORDERBY', orderby)

  def get_winEpisodeOrderby(self):
    OooO0OoOOOO = xbmcgui.Window(10000)
    return OooO0OoOOOO.getProperty('WAVVE_M_ORDERBY')

  def add_dir(self, label, sublabel='', img='', infoLabels=None, isFolder=True, params=''):
    i11iIIIIIi1 = '%s?%s' % (self._addon_url, urllib.urlencode(params))
    if sublabel:
      IiI11iII1 = '%s < %s >' % (label, sublabel)
    else:
      IiI11iII1 = label
    if not img:
      img = 'DefaultFolder.png'
    i1I11i1I = xbmcgui.ListItem(IiI11iII1)
    i1I11i1I.setArt({'thumbnailImage': img, 'icon': img, 'poster': img})
    if infoLabels:
      i1I11i1I.setInfo(type="video", infoLabels=infoLabels)
    if not isFolder:
      i1I11i1I.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(
        self._addon_handle, i11iIIIIIi1, i1I11i1I, isFolder)

  def dp_Main_List(self):
    for i11i1I1 in o0oO0:
      IiI11iII1 = i11i1I1.get('title')
      if i11i1I1.get('uicode') == 'GENRE':
        O0ii1ii1ii = {'mode': 'GENRE', 'uicode': i11i1I1.get('came'), 'genre': '-', 'subgenre': '-', 'orderby': i11i1I1.get('orderby'), 'ordernm': i11i1I1.get('ordernm')
                      }
      elif i11i1I1.get('uicode') == 'WATCH':
        O0ii1ii1ii = {'mode': 'WATCH', 'genre': '-'
                      }
      elif i11i1I1.get('uicode') == 'SEARCH':
        O0ii1ii1ii = {'mode': 'SEARCH', 'genre': '-'
                      }
      else:
        O0ii1ii1ii = {'mode': 'GNB_LIST', 'uicode': i11i1I1.get('uicode'), 'came': i11i1I1.get('came')
                      }
      iiIii = True
      if i11i1I1.get('uicode') == 'XXX':
        O0ii1ii1ii['mode'] = 'XXX'
        iiIii = False
      self.add_dir(IiI11iII1, sublabel='', img='', infoLabels=None,
                   isFolder=iiIii, params=O0ii1ii1ii)
    if len(o0oO0) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle)

  def login_main(self):
    (IIIIii1I, IiI1i, o0O) = self.get_settings_login_info()
    if not (IIIIii1I and IiI1i):
      oOOOO = xbmcgui.Dialog()
      i1i = oOOOO.yesno(__name__, __language__(30101).encode(
          'utf8'), __language__(30102).encode('utf8'))
      if i1i == True:
        __addon__.openSettings()
        sys.exit()
    O00o0OO0 = datetime.datetime.now().strftime('%Y-%m-%d')
    if xbmcgui.Window(10000).getProperty('WAVVE_M_LOGINWAIT') == 'TRUE':
      oOOo0 = 0
      while True:
        oOOo0 += 1
        time.sleep(0.05)
        if xbmcgui.Window(10000).getProperty('WAVVE_M_LOGINTIME') == O00o0OO0:
          return
        if oOOo0 > 600:
          return
    else:
      xbmcgui.Window(10000).setProperty('WAVVE_M_LOGINWAIT', 'TRUE')
    if xbmcgui.Window(10000).getProperty('WAVVE_M_LOGINTIME') == O00o0OO0:
      xbmcgui.Window(10000).setProperty('WAVVE_M_LOGINWAIT', 'FALSE')
      return
    if not self.WavveObj.GetCredential(IIIIii1I, IiI1i, o0O):
      self.addon_noti(__language__(30103).encode('utf8'))
      xbmcgui.Window(10000).setProperty('WAVVE_M_LOGINWAIT', 'FALSE')
      sys.exit()
    self.set_winCredential(self.WavveObj.LoadCredential())
    self.set_winEpisodeOrderby('desc')
    xbmcgui.Window(10000).setProperty('WAVVE_M_LOGINWAIT', 'FALSE')

  def dp_setEpOrderby(self, args):
    iIIiIi1 = args.get('orderby')
    self.set_winEpisodeOrderby(iIIiIi1)
    xbmc.executebuiltin("Container.Refresh")

  def dp_Gnb_List(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    Oo0OO = self.WavveObj.GetGnList(args.get('uicode'))
    for O0OO in Oo0OO:
      IiI11iII1 = O0OO.get('title')
      O0ii1ii1ii = {'mode': 'GN_LIST' if O0OO.get('uicode') != 'CY1' else 'GN_MYVIEW', 'uicode': O0OO.get('uicode'), 'came': args.get('came'), 'page': '1'
                    }
      self.add_dir(IiI11iII1, sublabel='', img='',
                   infoLabels=None, isFolder=True, params=O0ii1ii1ii)
    if len(Oo0OO) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def dp_Myview_Group(self, args):
    IiI11iII1 = 'VOD 시청내역'
    O0ii1ii1ii = {'mode': 'MYVIEW_LIST', 'uicode': 'vod', 'page': '1'
                  }
    self.add_dir(IiI11iII1, sublabel='', img='', infoLabels=None,
                 isFolder=True, params=O0ii1ii1ii)
    IiI11iII1 = '영화 시청내역'
    O0ii1ii1ii['uicode'] = 'movie'
    self.add_dir(IiI11iII1, sublabel='', img='', infoLabels=None,
                 isFolder=True, params=O0ii1ii1ii)
    xbmcplugin.endOfDirectory(self._addon_handle)

  def dp_Myview_List(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    oo0 = self.get_settings_addinfo()
    IiI1iIiIIIii = args.get('uicode')
    oOoO = int(args.get('page'))
    oOoO00O0, OO = self.WavveObj.GetMyviewList(
        IiI1iIiIIIii, oOoO, addinfoyn=oo0)
    for II1IIIIiII1i in oOoO00O0:
      IiI11iII1 = II1IIIIiII1i.get('title')
      i1II1 = II1IIIIiII1i.get('subtitle')
      i11i1 = II1IIIIiII1i.get('thumbnail')
      i1iI = II1IIIIiII1i.get('info')
      if IiI1iIiIIIii == 'movie' and oo0 == True:
        IiI11iII1 = '%s (%s)' % (IiI11iII1, str(i1iI.get('year')))
      else:
        i1iI['plot'] = IiI11iII1
      if IiI1iIiIIIii == 'vod':
        O0ii1ii1ii = {'mode': 'DEEP_LIST', 'contentid': II1IIIIiII1i.get('programid'), 'contentidType': 'programid', 'uicode': 'vod', 'page': '1', 'title': IiI11iII1, 'subtitle': i1II1, 'thumbnail': i11i1, 'viewage': II1IIIIiII1i.get('viewage')
                      }
        iiIii = True
      else:
        O0ii1ii1ii = {'mode': 'MOVIE', 'contentid': II1IIIIiII1i.get('contentid'), 'contentidType': 'contentid', 'uicode': 'movie', 'page': '1', 'title': IiI11iII1, 'subtitle': i1II1, 'thumbnail': i11i1, 'viewage': II1IIIIiII1i.get('viewage')
                      }
        iiIii = False
      if II1IIIIiII1i.get('viewage') == '21':
        i1II1 += ' (%s)' % (II1IIIIiII1i.get('viewage'))
      self.add_dir(IiI11iII1, sublabel=i1II1, img=i11i1,
                   infoLabels=i1iI, isFolder=iiIii, params=O0ii1ii1ii)
    if OO:
      O0ii1ii1ii['mode'] = 'MYVIEW_LIST'
      O0ii1ii1ii['uicode'] = IiI1iIiIIIii
      O0ii1ii1ii['page'] = str(oOoO + 1)
      IiI11iII1 = '[B]%s >>[/B]' % '다음 페이지'
      i1II1 = str(oOoO + 1)
      self.add_dir(IiI11iII1, sublabel=i1II1, img='',
                   infoLabels=None, isFolder=True, params=O0ii1ii1ii)
    if len(oOoO00O0) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def dp_Genre_Group(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    I1 = args.get('mode')
    OooooO0oOOOO = args.get('uicode')
    o0O00oOOoo = args.get('genre')
    i1I1iIi = args.get('subgenre')
    iIIiIi1 = args.get('orderby')
    IIii11Ii1i1I = args.get('ordernm')
    if o0O00oOOoo == '-':
      II1iI1I11I = self.WavveObj.GetGenreGroup(
          OooooO0oOOOO, o0O00oOOoo, iIIiIi1, IIii11Ii1i1I, exclusion21=self.get_settings_exclusion21())
    else:
      o0OO0 = {'adult': args.get('adult'), 'broadcastid': args.get('broadcastid'), 'contenttype': args.get('contenttype'), 'genre': args.get('genre'), 'uiparent': args.get('uiparent'), 'uirank': args.get('uirank'), 'uitype': args.get('uitype'), 'orderby': iIIiIi1, 'ordernm': IIii11Ii1i1I
               }
      II1iI1I11I = self.WavveObj.GetGenreGroup_sub(o0OO0)
    for oO in II1iI1I11I:
      IiI11iII1 = oO.get('title') + '  (' + IIii11Ii1i1I + ')'
      O0ii1ii1ii = {'mode': I1, 'uicode': OooooO0oOOOO, 'genre': oO.get('genre'), 'subgenre': oO.get('subgenre'), 'adult': oO.get('adult'), 'page': '1', 'broadcastid': oO.get('broadcastid'), 'contenttype': oO.get('contenttype'), 'uiparent': oO.get('uiparent'), 'uirank': oO.get('uirank'), 'uitype': oO.get('uitype'), 'orderby': iIIiIi1, 'ordernm': IIii11Ii1i1I
                    }
      if OooooO0oOOOO == 'moviegenre' or OooooO0oOOOO == 'moviegenre_svod' or OooooO0oOOOO == 'moviegenre_ppv' or oO.get('subgenre') != '-':
        O0ii1ii1ii['mode'] = 'GENRE_LIST'
      else:
        None
      self.add_dir(IiI11iII1, sublabel='', img='',
                   infoLabels=None, isFolder=True, params=O0ii1ii1ii)
    if len(II1iI1I11I) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def dp_Genre_List(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    oo0 = self.get_settings_addinfo()
    OooooO0oOOOO = args.get('uicode')
    oOoO = int(args.get('page'))
    O0ii1ii1ii = {'adult': args.get('adult'), 'broadcastid': args.get('broadcastid'), 'contenttype': args.get('contenttype'), 'genre': args.get('genre'), 'subgenre': args.get('subgenre'), 'uiparent': args.get('uiparent'), 'uirank': args.get('uirank'), 'uitype': args.get('uitype'), 'orderby': args.get('orderby')
                  }
    if args.get('genre') == args.get('subgenre'):
      O0ii1ii1ii['subgenre'] = 'all'
    II1iI1I11I, OO = self.WavveObj.GetGenreList(
        OooooO0oOOOO, O0ii1ii1ii, oOoO, addinfoyn=oo0)
    for oO in II1iI1I11I:
      IiI11iII1 = oO.get('title')
      i11i1 = oO.get('thumbnail')
      i1iI = oO.get('info')
      if OooooO0oOOOO == 'moviegenre_svod' and oo0 == True:
        IiI11iII1 = '%s (%s)' % (IiI11iII1, str(i1iI.get('year')))
      else:
        i1iI['plot'] = IiI11iII1
      if OooooO0oOOOO == 'vodgenre':
        oooooo0OO = {'mode': 'DEEP_LIST', 'contentid': oO.get('uicode'), 'contentidType': 'contentid', 'uicode': 'vod', 'page': '1', 'title': IiI11iII1, 'subtitle': '', 'thumbnail': i11i1, 'viewage': oO.get('viewage')
                     }
        iiIii = True
      else:
        oooooo0OO = {'mode': 'MOVIE', 'contentid': oO.get('uicode'), 'contentidType': 'contentid', 'uicode': 'movie', 'page': '1', 'title': IiI11iII1, 'subtitle': '', 'thumbnail': i11i1, 'viewage': oO.get('viewage')
                     }
        iiIii = False
      if oooooo0OO.get('viewage') == '21':
        IiI11iII1 += ' (%s)' % (oooooo0OO.get('viewage'))
      self.add_dir(IiI11iII1, sublabel='', img=i11i1,
                   infoLabels=i1iI, isFolder=iiIii, params=oooooo0OO)
    if OO:
      O0ii1ii1ii['mode'] = 'GENRE_LIST'
      O0ii1ii1ii['uicode'] = OooooO0oOOOO
      O0ii1ii1ii['page'] = str(oOoO + 1)
      IiI11iII1 = '[B]%s >>[/B]' % '다음 페이지'
      i1II1 = str(oOoO + 1)
      self.add_dir(IiI11iII1, sublabel=i1II1, img='',
                   infoLabels=None, isFolder=True, params=O0ii1ii1ii)
    if len(II1iI1I11I) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def dp_Deeplink_List(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    oo0 = self.get_settings_addinfo()
    OooooO0oOOOO = args.get('uicode')
    I1ii11 = args.get('came')
    oOoO = int(args.get('page'))
    Ii1i1iI, OO = self.WavveObj.GetDeeplinkList(
        OooooO0oOOOO, I1ii11, oOoO, addinfoyn=oo0)
    for ooo0o00 in Ii1i1iI:
      IiI11iII1 = ooo0o00.get('title')
      i1II1 = ooo0o00.get('subtitle')
      i11i1 = ooo0o00.get('thumbnail')
      ooO = ooo0o00.get('uicode')
      o0o00 = ooo0o00.get('channelepg')
      O0ii1ii1ii = {'uicode': ooO, 'came': I1ii11, 'contentid': ooo0o00.get('contentid'), 'contentidType': ooo0o00.get('contentidType'), 'page': '1', 'title': IiI11iII1, 'subtitle': i1II1, 'thumbnail': i11i1, 'viewage': ooo0o00.get('viewage')
                    }
      if ooO == 'channel':
        O0ii1ii1ii['mode'] = 'LIVE'
      elif ooO == 'movie':
        O0ii1ii1ii['mode'] = 'MOVIE'
      else:
        O0ii1ii1ii['mode'] = 'DEEP_LIST'
      i1iI = ooo0o00.get('info')
      if o0o00:
        i1iI['plot'] = '%s\n\n%s' % (IiI11iII1, o0o00)
      elif ooO == 'movie' and oo0 == True:
        IiI11iII1 = '%s (%s)' % (IiI11iII1, str(i1iI.get('year')))
      else:
        i1iI['plot'] = '%s\n\n%s' % (IiI11iII1, i1II1)
      if ooo0o00.get('viewage') == '21':
        i1II1 += ' (%s)' % (ooo0o00.get('viewage'))
      if ooO in ['channel', 'movie']:
        iiIii = False
      elif O0ii1ii1ii['contentidType'] == 'direct':
        iiIii = False
        O0ii1ii1ii['mode'] = 'VOD'
      else:
        iiIii = True
      self.add_dir(IiI11iII1, sublabel=i1II1, img=i11i1,
                   infoLabels=i1iI, isFolder=iiIii, params=O0ii1ii1ii)
    if OO:
      O0ii1ii1ii['mode'] = 'GN_LIST'
      O0ii1ii1ii['uicode'] = OooooO0oOOOO
      O0ii1ii1ii['page'] = str(oOoO + 1)
      IiI11iII1 = '[B]%s >>[/B]' % '다음 페이지'
      i1II1 = str(oOoO + 1)
      self.add_dir(IiI11iII1, sublabel=i1II1, img='',
                   infoLabels=None, isFolder=True, params=O0ii1ii1ii)
    if len(Ii1i1iI) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def dp_Episodelink_List(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    OoO0ooO = args.get('contentid')
    O000 = args.get('contentidType')
    IiI1iIiIIIii = args.get('uicode')
    oOoO = int(args.get('page'))
    OoOo, OO = self.WavveObj.GetEpisodeList(
        OoO0ooO, IiI1iIiIIIii, O000, oOoO, orderby=self.get_winEpisodeOrderby())
    for O00 in OoOo:
      IiI11iII1 = O00.get('title')
      i1II1 = O00.get('subtitle')
      i11i1 = O00.get('thumbnail')
      O0ii1ii1ii = {'mode': 'VOD', 'uicode': O00.get('uicode'), 'contentid': O00.get('contentid'), 'programid': O00.get('programid'), 'title': IiI11iII1, 'subtitle': i1II1, 'thumbnail': i11i1, 'viewage': O00.get('viewage')
                    }
      if O00.get('viewage') == '21':
        i1II1 += ' (%s)' % (O00.get('viewage'))
      Oooo0 = O00.get('info')
      Oooo0['plot'] = O00.get('synopsis')
      self.add_dir(IiI11iII1, sublabel=i1II1, img=i11i1,
                   infoLabels=Oooo0, isFolder=False, params=O0ii1ii1ii)
    if oOoO == 1:
      i1iI = {'plot': '정렬순서를 변경합니다.'}
      O0ii1ii1ii = {}
      O0ii1ii1ii['mode'] = 'ORDER_BY'
      if self.get_winEpisodeOrderby() == 'desc':
        IiI11iII1 = '정렬순서변경 : 최신화부터 -> 1회부터'
        O0ii1ii1ii['orderby'] = 'asc'
      else:
        IiI11iII1 = '정렬순서변경 : 1회부터 -> 최신화부터'
        O0ii1ii1ii['orderby'] = 'desc'
      self.add_dir(IiI11iII1, sublabel='', img='', infoLabels=i1iI,
                   isFolder=False, params=O0ii1ii1ii)
    if OO:
      O0ii1ii1ii['mode'] = 'DEEP_LIST'
      O0ii1ii1ii['uicode'] = IiI1iIiIIIii
      O0ii1ii1ii['contentid'] = OoO0ooO
      O0ii1ii1ii['contentidType'] = O000
      O0ii1ii1ii['page'] = str(oOoO + 1)
      IiI11iII1 = '[B]%s >>[/B]' % '다음 페이지'
      i1II1 = str(oOoO + 1)
      self.add_dir(IiI11iII1, sublabel=i1II1, img='',
                   infoLabels=None, isFolder=True, params=O0ii1ii1ii)
    if len(OoOo) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def play_VIDEO(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    OoO0ooO = args.get('contentid')
    IiI1iIiIIIii = args.get('uicode')
    Oooo00 = self.get_selQuality()
    self.addon_log(OoO0ooO + ' - ' + IiI1iIiIIIii, False)
    II11iI111i1, Oo00OoOo, ii1ii111, i11111I1I = self.WavveObj.GetStreamingURL(
        OoO0ooO, IiI1iIiIIIii, Oooo00)
    I1I11iI11iI1i = '%s|Cookie=%s' % (II11iI111i1, Oo00OoOo)
    self.addon_log(I1I11iI11iI1i, False)
    if II11iI111i1 == '':
      self.addon_noti(__language__(30303).encode('utf8'))
      return
    I1IIIiI1I1ii1 = xbmcgui.ListItem(path=I1I11iI11iI1i)
    if ii1ii111:
      i11iiiiI1i = ii1ii111['customdata']
      iIIii = ii1ii111['drmhost']
      iiIi1IIiI = 'mpd'
      i1 = 'com.widevine.alpha'
      OO00OO0O0 = inputstreamhelper.Helper(iiIi1IIiI, drm=i1)
      if OO00OO0O0.check_inputstream():
        if IiI1iIiIIIii == 'movie':
          OoO0O0O0o00 = 'https://www.wavve.com/player/movie?movieid=%s' % OoO0ooO
        else:
          OoO0O0O0o00 = 'https://www.wavve.com/player/vod?programid=%s&page=1' % OoO0ooO
        OOOoO000 = {'content-type': 'application/octet-stream', 'origin': 'https://www.wavve.com', 'pallycon-customdata': i11iiiiI1i, 'referer': OoO0O0O0o00, 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': OOoO
                    }
        oOOOOIi = iIIii + '|' + urllib.urlencode(OOOoO000) + '|R{SSM}|'
        I1IIIiI1I1ii1.setProperty(
            'inputstreamaddon', OO00OO0O0.inputstream_addon)
        I1IIIiI1I1ii1.setProperty(
            'inputstream.adaptive.manifest_type', iiIi1IIiI)
        I1IIIiI1I1ii1.setProperty('inputstream.adaptive.license_type', i1)
        I1IIIiI1I1ii1.setProperty('inputstream.adaptive.license_key', oOOOOIi)
        I1IIIiI1I1ii1.setProperty(
            'inputstream.adaptive.stream_headers', 'Cookie=%s' % Oo00OoOo)
    xbmcplugin.setResolvedUrl(self._addon_handle, True, I1IIIiI1I1ii1)
    if i11111I1I:
      self.addon_noti(i11111I1I.encode('utf-8'))
    else:
      if '/preview.' in urlparse.urlsplit(II11iI111i1).path:
        self.addon_noti(__language__(30401).encode('utf8'))
    try:
      if args.get('mode') in ['VOD', 'MOVIE'] and args.get('title') and args.get('viewage') != '21':
        O0ii1ii1ii = {'code': args.get('programid') if args.get('mode') == 'VOD' else args.get('contentid'), 'img': args.get('thumbnail'), 'title': args.get('title'), 'subtitle': args.get('subtitle'), 'videoid': args.get('contentid')
                      }
        self.Save_Watched_List(args.get('mode').lower(), O0ii1ii1ii)
    except:
      None

  def dp_Watch_List(self, args):
    o0O00oOOoo = args.get('genre')
    o00oOO0 = self.get_settings_direct_replay()
    if o0O00oOOoo == '-':
      IiI11iII1 = 'VOD 시청내역'
      O0ii1ii1ii = {'mode': 'WATCH', 'genre': 'vod'
                    }
      self.add_dir(IiI11iII1, sublabel='', img='',
                   infoLabels=None, isFolder=True, params=O0ii1ii1ii)
      IiI11iII1 = '영화 시청내역'
      O0ii1ii1ii['genre'] = 'movie'
      self.add_dir(IiI11iII1, sublabel='', img='',
                   infoLabels=None, isFolder=True, params=O0ii1ii1ii)
      xbmcplugin.endOfDirectory(self._addon_handle)
    else:
      iI11I = self.Load_Watched_List(o0O00oOOoo)
      for I1i11ii11 in iI11I:
        OO00O0oOO = dict(urlparse.parse_qsl(I1i11ii11))
        IiI11iII1 = OO00O0oOO.get('title').strip()
        i1II1 = OO00O0oOO.get('subtitle').strip()
        if i1II1 == 'None':
          i1II1 = ''
        i11i1 = OO00O0oOO.get('img')
        Ooooo00o0OoO = OO00O0oOO.get('videoid')
        i1iI = {}
        if o0O00oOOoo == 'movie' and self.get_settings_addinfo() == True:
          oOO0 = self.WavveObj.GetMovieInfoList([OO00O0oOO.get('code')])
          i1iI = oOO0.get(OO00O0oOO.get('code'))
        else:
          i1iI['plot'] = '%s\n%s' % (IiI11iII1, i1II1)
        if o0O00oOOoo == 'vod':
          if o00oOO0 == False or Ooooo00o0OoO == None:
            O0ii1ii1ii = {'mode': 'DEEP_LIST', 'contentid': OO00O0oOO.get('code'), 'contentidType': 'programid', 'uicode': 'vod', 'page': '1'
                          }
            iiIii = True
          else:
            O0ii1ii1ii = {'mode': 'VOD', 'contentid': Ooooo00o0OoO, 'contentidType': 'contentid', 'programid': OO00O0oOO.get('code'), 'uicode': 'vod', 'title': IiI11iII1, 'subtitle': i1II1, 'thumbnail': i11i1
                          }
            iiIii = False
        else:
          O0ii1ii1ii = {'mode': 'MOVIE', 'contentid': OO00O0oOO.get('code'), 'contentidType': 'contentid', 'uicode': 'movie', 'title': IiI11iII1, 'thumbnail': i11i1
                        }
          iiIii = False
        self.add_dir(IiI11iII1, sublabel=i1II1, img=i11i1,
                     infoLabels=i1iI, isFolder=iiIii, params=O0ii1ii1ii)
      i1iI = {'plot': '시청목록을 삭제합니다.'}
      IiI11iII1 = '*** 시청목록 삭제 ***'
      O0ii1ii1ii = {'mode': 'MYVIEW_REMOVE', 'genre': o0O00oOOoo
                    }
      self.add_dir(IiI11iII1, sublabel='', img='', infoLabels=i1iI,
                   isFolder=False, params=O0ii1ii1ii)
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def dp_Search_Group(self, args):
    IiI11iII1 = 'VOD 검색'
    O0ii1ii1ii = {'mode': 'SEARCH_LIST', 'genre': 'vod', 'page': '1'
                  }
    self.add_dir(IiI11iII1, sublabel='', img='', infoLabels=None,
                 isFolder=True, params=O0ii1ii1ii)
    IiI11iII1 = '영화 검색'
    O0ii1ii1ii['genre'] = 'movie'
    self.add_dir(IiI11iII1, sublabel='', img='', infoLabels=None,
                 isFolder=True, params=O0ii1ii1ii)
    xbmcplugin.endOfDirectory(self._addon_handle)

  def dp_Search_List(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    oo0 = self.get_settings_addinfo()
    IiI1iIiIIIii = args.get('genre')
    oOoO = int(args.get('page'))
    if 'search_key' in args:
      iiI11I1i1i1iI = args.get('search_key')
    else:
      iiI11I1i1i1iI = self.get_keyboard_input(
          __language__(30003).encode('utf-8'))
      if not iiI11I1i1i1iI:
        return
    oooo00, OO = self.WavveObj.GetSearchList(
        iiI11I1i1i1iI, IiI1iIiIIIii, oOoO, exclusion21=self.get_settings_exclusion21(), addinfoyn=oo0)
    for o0O0O0 in oooo00:
      IiI11iII1 = o0O0O0.get('title')
      i11i1 = o0O0O0.get('thumbnail')
      i1iI = o0O0O0.get('info')
      if IiI1iIiIIIii == 'movie' and oo0 == True:
        IiI11iII1 = '%s (%s)' % (IiI11iII1, str(i1iI.get('year')))
      else:
        i1iI['plot'] = IiI11iII1
      if IiI1iIiIIIii == 'vod':
        O0ii1ii1ii = {'mode': 'DEEP_LIST', 'contentid': o0O0O0.get('programid'), 'contentidType': 'programid', 'uicode': 'vod', 'page': '1', 'title': IiI11iII1, 'subtitle': '', 'thumbnail': i11i1, 'viewage': o0O0O0.get('viewage')
                      }
        iiIii = True
      else:
        O0ii1ii1ii = {'mode': 'MOVIE', 'contentid': o0O0O0.get('contentid'), 'contentidType': 'contentid', 'uicode': 'movie', 'page': '1', 'title': IiI11iII1, 'subtitle': '', 'thumbnail': i11i1, 'viewage': o0O0O0.get('viewage')
                      }
        iiIii = False
      if O0ii1ii1ii.get('viewage') == '21':
        IiI11iII1 += ' (%s)' % (O0ii1ii1ii.get('viewage'))
      self.add_dir(IiI11iII1, sublabel='', img=i11i1,
                   infoLabels=i1iI, isFolder=iiIii, params=O0ii1ii1ii)
    if OO:
      O0ii1ii1ii['mode'] = 'SEARCH_LIST'
      O0ii1ii1ii['genre'] = IiI1iIiIIIii
      O0ii1ii1ii['page'] = str(oOoO + 1)
      O0ii1ii1ii['search_key'] = iiI11I1i1i1iI
      IiI11iII1 = '[B]%s >>[/B]' % '다음 페이지'
      i1II1 = str(oOoO + 1)
      self.add_dir(IiI11iII1, sublabel=i1II1, img='',
                   infoLabels=None, isFolder=True, params=O0ii1ii1ii)
    if len(oooo00) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle)

  def Load_Watched_List(self, genre):
    try:
      O0000 = xbmc.translatePath(os.path.join(
          __profile__, 'watchedlist_%s.txt' % genre))
      with open(O0000, 'r') as ooO00O0O0:
        iII1I1 = ooO00O0O0.readlines()
    except:
      iII1I1 = []
    return iII1I1

  def Save_Watched_List(self, genre, in_params):
    try:
      O0000 = xbmc.translatePath(os.path.join(
          __profile__, 'watchedlist_%s.txt' % genre))
      O00oo0ooO = self.Load_Watched_List(genre)
      with open(O0000, 'w') as ooO00O0O0:
        ooo = urllib.urlencode(in_params)
        ooo = ooo.encode('utf-8') + '\n'
        ooO00O0O0.write(ooo)
        iIIiiiiI = 0
        for I111i1I1 in O00oo0ooO:
          O0o00OOo00O0O = dict(urlparse.parse_qsl(I111i1I1))
          i111I11i = in_params.get('code')
          ii1OoOO = O0o00OOo00O0O.get('code')
          if genre == 'vod' and self.get_settings_direct_replay() == True:
            i111I11i = in_params.get('videoid')
            ii1OoOO = O0o00OOo00O0O.get('videoid') if ii1OoOO != None else '-'
          if i111I11i != ii1OoOO:
            ooO00O0O0.write(I111i1I1)
            iIIiiiiI += 1
            if iIIiiiiI >= 50:
              break
    except:
      None

  def Delete_Watched_List(self, genre):
    try:
      O0000 = xbmc.translatePath(os.path.join(
          __profile__, 'watchedlist_%s.txt' % genre))
      with open(O0000, 'w') as ooO00O0O0:
        ooO00O0O0.write('')
    except:
      None

  def dp_WatchList_Delete(self, args):
    o0O00oOOoo = args.get('genre')
    oOOOO = xbmcgui.Dialog()
    i1i = oOOOO.yesno(__name__, __language__(30201).encode(
        'utf8'), __language__(30202).encode('utf8'))
    if i1i == False:
      sys.exit()
    self.Delete_Watched_List(o0O00oOOoo)
    xbmc.executebuiltin("Container.Refresh")

  def wavve_main(self):
    I1 = self.main_params.get('mode', None)
    self.login_main()
    if I1 is None:
      self.dp_Main_List()
    elif I1 == 'GNB_LIST':
      self.dp_Gnb_List(self.main_params)
    elif I1 == 'GN_LIST':
      self.dp_Deeplink_List(self.main_params)
    elif I1 == 'DEEP_LIST':
      IiI1iIiIIIii = self.main_params.get('uicode', None)
      if IiI1iIiIIIii in ['quick', 'vod', 'program', 'x']:
        self.dp_Episodelink_List(self.main_params)
      else:
        None
    elif I1 in ['LIVE', 'VOD', 'MOVIE']:
      self.play_VIDEO(self.main_params)
      time.sleep(0.1)
    elif I1 == 'GN_MYVIEW':
      self.dp_Myview_Group(self.main_params)
    elif I1 == 'MYVIEW_LIST':
      self.dp_Myview_List(self.main_params)
    elif I1 == 'GENRE':
      self.dp_Genre_Group(self.main_params)
    elif I1 == 'GENRE_LIST':
      self.dp_Genre_List(self.main_params)
    elif I1 == 'WATCH':
      self.dp_Watch_List(self.main_params)
    elif I1 == 'MYVIEW_REMOVE':
      self.dp_WatchList_Delete(self.main_params)
    elif I1 == 'SEARCH':
      self.dp_Search_Group(self.main_params)
    elif I1 == 'SEARCH_LIST':
      self.dp_Search_List(self.main_params)
    elif I1 == 'ORDER_BY':
      self.dp_setEpOrderby(self.main_params)
    else:
      None
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
