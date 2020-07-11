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
elemList = [
    {'title': '홈', 'uicode': 'GN1', 'came': 'home'}, {'title': 'LIVE 채널', 'uicode': 'GN3', 'came': 'live'}, {'title': 'VOD 방송', 'uicode': 'GN2', 'came': 'broadcast'}, {'title': '영화(Movie)', 'uicode': 'GN17', 'came': 'movie'}, {'title': '해외시리즈', 'uicode': 'GN12', 'came': 'global'}, {'title': '분류별 - 방송(VOD) - 인기순', 'uicode': 'GENRE', 'came': 'vodgenre', 'orderby': 'viewtime', 'ordernm': '인기순'}, {'title': '분류별 - 방송(VOD) - 최신순', 'uicode': 'GENRE', 'came': 'vodgenre', 'orderby': 'new', 'ordernm': '최신순'}, {
        'title': '분류별 - 영화(Movie) - 인기순', 'uicode': 'GENRE', 'came': 'moviegenre_svod', 'orderby': 'paid', 'ordernm': '인기순'}, {'title': '분류별 - 영화(Movie) - 업데이트순', 'uicode': 'GENRE', 'came': 'moviegenre_svod', 'orderby': 'displaystart', 'ordernm': '업데이트순'}, {'title': '검색', 'uicode': 'SEARCH', 'came': '-'}, {'title': 'Watched(시청목록)', 'uicode': 'WATCH', 'came': '-'}
]
userAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
__addon__ = xbmcaddon.Addon()
__language__ = __addon__.getLocalizedString
__profile__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
__version__ = __addon__.getAddonInfo('version')
__addonid__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')


class WavveRun (object):
  def __init__(self, in_addonurl, in_handle, in_params):
    self._addon_url = in_addonurl
    self._addon_handle = in_handle
    self.main_params = in_params
    self.WavveObj = iII111ii()

  def addon_noti(self, sting):
    try:
      dialog = xbmcgui.Dialog()
      dialog.notification(__addonname__, sting)
    except:
      None

  def addon_log(self, string, isDebug=False):
    try:
      logStr = string.encode('utf-8', 'ignore')
    except:
      logStr = 'addonException: addon_log'
    if isDebug:
      logLevel = xbmc.LOGDEBUG
    else:
      logLevel = xbmc.LOGNOTICE
    xbmc.log("[%s-%s]: %s" %
             (__addonid__, __version__, logStr), level=logLevel)

  def get_keyboard_input(self, title):
    text = None
    keyboard = xbmc.Keyboard()
    keyboard.setHeading(title)
    xbmc.sleep(1000)
    keyboard.doModal()
    if (keyboard.isConfirmed()):
      text = keyboard.getText()
    return text

  def get_settings_login_info(self):
    loginId = __addon__.getSetting('id')
    loginPw = __addon__.getSetting('pw')
    selectedProfile = __addon__.getSetting('selected_profile')
    return (loginId, loginPw, selectedProfile)

  def get_selQuality(self):
    try:
      qualityList = [1080, 720, 480, 360]
      selectedQuality = int(__addon__.getSetting('selected_quality'))
      return qualityList[selectedQuality]
    except:
      None
    return 1080

  def get_settings_exclusion21(self):
    isExclusion21 = __addon__.getSetting('exclusion21')
    if isExclusion21 == 'false':
      return False
    else:
      return True

  def get_settings_direct_replay(self):
    directPlay = int(__addon__.getSetting('direct_replay'))
    if directPlay == 0:
      return False
    else:
      return True

  def get_settings_addinfo(self):
    addInfoyn = __addon__.getSetting('add_infoyn')
    if addInfoyn == 'false':
      return False
    else:
      return True

  def get_settings_thumbnail_landyn(self):
    thumbnailWay = int(__addon__.getSetting('thumbnail_way'))
    if thumbnailWay == 0:
      return True
    else:
      return False

  def set_winCredential(self, credential):
    window = xbmcgui.Window(10000)
    window.setProperty('WAVVE_M_CREDENTIAL', credential)
    window.setProperty(
        'WAVVE_M_LOGINTIME', datetime.datetime.now().strftime('%Y-%m-%d'))

  def get_winCredential(self):
    window = xbmcgui.Window(10000)
    return window.getProperty('WAVVE_M_CREDENTIAL')

  def set_winEpisodeOrderby(self, orderby):
    window = xbmcgui.Window(10000)
    window.setProperty('WAVVE_M_ORDERBY', orderby)

  def get_winEpisodeOrderby(self):
    window = xbmcgui.Window(10000)
    return window.getProperty('WAVVE_M_ORDERBY')

  def add_dir(self, label, sublabel='', img='', infoLabels=None, isFolder=True, params=''):
    url = '%s?%s' % (self._addon_url, urllib.urlencode(params))
    if sublabel:
      itemLabel = '%s < %s >' % (label, sublabel)
    else:
      itemLabel = label
    if not img:
      img = 'DefaultFolder.png'
    listItem = xbmcgui.ListItem(itemLabel)
    listItem.setArt({'thumbnailImage': img, 'icon': img, 'poster': img})
    if infoLabels:
      listItem.setInfo(type="video", infoLabels=infoLabels)
    if not isFolder:
      listItem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(
        self._addon_handle, url, listItem, isFolder)

  def dp_Main_List(self):
    for elem in elemList:
      title = elem.get('title')
      if elem.get('uicode') == 'GENRE':
        parameters = {'mode': 'GENRE', 'uicode': elem.get('came'), 'genre': '-', 'subgenre': '-', 'orderby': elem.get('orderby'), 'ordernm': elem.get('ordernm')
                      }
      elif elem.get('uicode') == 'WATCH':
        parameters = {'mode': 'WATCH', 'genre': '-'
                      }
      elif elem.get('uicode') == 'SEARCH':
        parameters = {'mode': 'SEARCH', 'genre': '-'
                      }
      else:
        parameters = {'mode': 'GNB_LIST', 'uicode': elem.get('uicode'), 'came': elem.get('came')
                      }
      iiIii = True
      if elem.get('uicode') == 'XXX':
        parameters['mode'] = 'XXX'
        iiIii = False
      self.add_dir(title, sublabel='', img='', infoLabels=None,
                   isFolder=iiIii, params=parameters)
    if len(elemList) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle)

  def login_main(self):
    (loginId, loginPw, selectedProfile) = self.get_settings_login_info()
    if not (loginId and loginPw):
      dialog = xbmcgui.Dialog()
      isYes = dialog.yesno(__name__, __language__(30101).encode(
          'utf8'), __language__(30102).encode('utf8'))
      if isYes == True:
        __addon__.openSettings()
        sys.exit()
    strtime = datetime.datetime.now().strftime('%Y-%m-%d')
    if xbmcgui.Window(10000).getProperty('WAVVE_M_LOGINWAIT') == 'TRUE':
      count = 0
      while True:
        count += 1
        time.sleep(0.05)
        if xbmcgui.Window(10000).getProperty('WAVVE_M_LOGINTIME') == strtime:
          return
        if count > 600:
          return
    else:
      xbmcgui.Window(10000).setProperty('WAVVE_M_LOGINWAIT', 'TRUE')
    if xbmcgui.Window(10000).getProperty('WAVVE_M_LOGINTIME') == strtime:
      xbmcgui.Window(10000).setProperty('WAVVE_M_LOGINWAIT', 'FALSE')
      return
    if not self.WavveObj.GetCredential(loginId, loginPw, selectedProfile):
      self.addon_noti(__language__(30103).encode('utf8'))
      xbmcgui.Window(10000).setProperty('WAVVE_M_LOGINWAIT', 'FALSE')
      sys.exit()
    self.set_winCredential(self.WavveObj.LoadCredential())
    self.set_winEpisodeOrderby('desc')
    xbmcgui.Window(10000).setProperty('WAVVE_M_LOGINWAIT', 'FALSE')

  def dp_setEpOrderby(self, args):
    orderby = args.get('orderby')
    self.set_winEpisodeOrderby(orderby)
    xbmc.executebuiltin("Container.Refresh")

  def dp_Gnb_List(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    gnList = self.WavveObj.GetGnList(args.get('uicode'))
    for gn in gnList:
      title = gn.get('title')
      parameters = {'mode': 'GN_LIST' if gn.get('uicode') != 'CY1' else 'GN_MYVIEW', 'uicode': gn.get('uicode'), 'came': args.get('came'), 'page': '1'
                    }
      self.add_dir(title, sublabel='', img='',
                   infoLabels=None, isFolder=True, params=parameters)
    if len(gnList) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def dp_Myview_Group(self, args):
    self.add_dir('VOD 시청내역', sublabel='', img='', infoLabels=None,
                 isFolder=True, params={'mode': 'MYVIEW_LIST', 'uicode': 'vod', 'page': '1'})
    self.add_dir('영화 시청내역', sublabel='', img='', infoLabels=None,
                 isFolder=True, params={'mode': 'MYVIEW_LIST', 'uicode': 'movie', 'page': '1'})
    xbmcplugin.endOfDirectory(self._addon_handle)

  def dp_Myview_List(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    IsAddInfo = self.get_settings_addinfo()
    uicode = args.get('uicode')
    pageNum = int(args.get('page'))
    viewList, OO = self.WavveObj.GetMyviewList(
        uicode, pageNum, addinfoyn=IsAddInfo)
    for view in viewList:
      title = view.get('title')
      subtitle = view.get('subtitle')
      thumbnail = view.get('thumbnail')
      info = view.get('info')
      if uicode == 'movie' and IsAddInfo == True:
        title = '%s (%s)' % (title, str(info.get('year')))
      else:
        info['plot'] = title
      if uicode == 'vod':
        paramters = {'mode': 'DEEP_LIST', 'contentid': view.get('programid'), 'contentidType': 'programid', 'uicode': 'vod', 'page': '1', 'title': title, 'subtitle': subtitle, 'thumbnail': thumbnail, 'viewage': view.get('viewage')
                     }
        isFolder = True
      else:
        paramters = {'mode': 'MOVIE', 'contentid': view.get('contentid'), 'contentidType': 'contentid', 'uicode': 'movie', 'page': '1', 'title': title, 'subtitle': subtitle, 'thumbnail': thumbnail, 'viewage': view.get('viewage')
                     }
        isFolder = False
      if view.get('viewage') == '21':
        subtitle += ' (%s)' % (view.get('viewage'))
      self.add_dir(title, sublabel=subtitle, img=thumbnail,
                   infoLabels=info, isFolder=isFolder, params=paramters)
    if OO:
      paramters['mode'] = 'MYVIEW_LIST'
      paramters['uicode'] = uicode
      paramters['page'] = str(pageNum + 1)
      label = '[B]%s >>[/B]' % '다음 페이지'
      sublabel = str(pageNum + 1)
      self.add_dir(label, sublabel=sublabel, img='',
                   infoLabels=None, isFolder=True, params=paramters)
    if len(viewList) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def dp_Genre_Group(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    mode = args.get('mode')
    uicode = args.get('uicode')
    genre = args.get('genre')
    # subgenre = args.get('subgenre')
    orderby = args.get('orderby')
    ordernm = args.get('ordernm')
    if genre == '-':
      genreGroup = self.WavveObj.GetGenreGroup(
          uicode, genre, orderby, ordernm, exclusion21=self.get_settings_exclusion21())
    else:
      parameters = {'adult': args.get('adult'), 'broadcastid': args.get('broadcastid'), 'contenttype': args.get('contenttype'), 'genre': args.get('genre'), 'uiparent': args.get('uiparent'), 'uirank': args.get('uirank'), 'uitype': args.get('uitype'), 'orderby': orderby, 'ordernm': ordernm
                    }
      genreGroup = self.WavveObj.GetGenreGroup_sub(parameters)
    for elem in genreGroup:
      label = elem.get('title') + '  (' + ordernm + ')'
      parameters = {'mode': mode, 'uicode': uicode, 'genre': elem.get('genre'), 'subgenre': elem.get('subgenre'), 'adult': elem.get('adult'), 'page': '1', 'broadcastid': elem.get('broadcastid'), 'contenttype': elem.get('contenttype'), 'uiparent': elem.get('uiparent'), 'uirank': elem.get('uirank'), 'uitype': elem.get('uitype'), 'orderby': orderby, 'ordernm': ordernm
                    }
      if uicode == 'moviegenre' or uicode == 'moviegenre_svod' or uicode == 'moviegenre_ppv' or elem.get('subgenre') != '-':
        parameters['mode'] = 'GENRE_LIST'
      else:
        None
      self.add_dir(label, sublabel='', img='',
                   infoLabels=None, isFolder=True, params=parameters)
    if len(genreGroup) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def dp_Genre_List(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    isAddInfo = self.get_settings_addinfo()
    uicode = args.get('uicode')
    pageNum = int(args.get('page'))
    parameters = {'adult': args.get('adult'), 'broadcastid': args.get('broadcastid'), 'contenttype': args.get('contenttype'), 'genre': args.get('genre'), 'subgenre': args.get('subgenre'), 'uiparent': args.get('uiparent'), 'uirank': args.get('uirank'), 'uitype': args.get('uitype'), 'orderby': args.get('orderby')
                  }
    if args.get('genre') == args.get('subgenre'):
      parameters['subgenre'] = 'all'
    genreList, compareCount = self.WavveObj.GetGenreList(
        uicode, parameters, pageNum, addinfoyn=isAddInfo)
    for genre in genreList:
      title = genre.get('title')
      thumbnail = genre.get('thumbnail')
      info = genre.get('info')
      if uicode == 'moviegenre_svod' and isAddInfo == True:
        title = '%s (%s)' % (title, str(info.get('year')))
      else:
        info['plot'] = title
      if uicode == 'vodgenre':
        params = {'mode': 'DEEP_LIST', 'contentid': genre.get('uicode'), 'contentidType': 'contentid', 'uicode': 'vod', 'page': '1', 'title': title, 'subtitle': '', 'thumbnail': thumbnail, 'viewage': genre.get('viewage')
                  }
        isFolder = True
      else:
        params = {'mode': 'MOVIE', 'contentid': genre.get('uicode'), 'contentidType': 'contentid', 'uicode': 'movie', 'page': '1', 'title': title, 'subtitle': '', 'thumbnail': thumbnail, 'viewage': genre.get('viewage')
                  }
        isFolder = False
      if params.get('viewage') == '21':
        title += ' (%s)' % (params.get('viewage'))
      self.add_dir(title, sublabel='', img=thumbnail,
                   infoLabels=info, isFolder=isFolder, params=params)
    if compareCount:
      parameters['mode'] = 'GENRE_LIST'
      parameters['uicode'] = uicode
      parameters['page'] = str(pageNum + 1)
      label = '[B]%s >>[/B]' % '다음 페이지'
      sublabel = str(pageNum + 1)
      self.add_dir(label, sublabel=sublabel, img='',
                   infoLabels=None, isFolder=True, params=parameters)
    if len(genreList) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def dp_Deeplink_List(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    isAddInfo = self.get_settings_addinfo()
    uicode = args.get('uicode')
    came = args.get('came')
    pageNum = int(args.get('page'))
    deepLinkList, compareCount = self.WavveObj.GetDeeplinkList(
        uicode, came, pageNum, addinfoyn=isAddInfo)
    for deepLink in deepLinkList:
      title = deepLink.get('title')
      subtitle = deepLink.get('subtitle')
      thumbnail = deepLink.get('thumbnail')
      uicode = deepLink.get('uicode')
      channelEpg = deepLink.get('channelepg')
      parameters = {'uicode': uicode, 'came': came, 'contentid': deepLink.get('contentid'), 'contentidType': deepLink.get('contentidType'), 'page': '1', 'title': title, 'subtitle': subtitle, 'thumbnail': thumbnail, 'viewage': deepLink.get('viewage')
                    }
      if uicode == 'channel':
        parameters['mode'] = 'LIVE'
      elif uicode == 'movie':
        parameters['mode'] = 'MOVIE'
      else:
        parameters['mode'] = 'DEEP_LIST'
      info = deepLink.get('info')
      if channelEpg:
        info['plot'] = '%s\n\n%s' % (title, channelEpg)
      elif uicode == 'movie' and oo0 == True:
        title = '%s (%s)' % (title, str(info.get('year')))
      else:
        info['plot'] = '%s\n\n%s' % (title, subtitle)
      if deepLink.get('viewage') == '21':
        subtitle += ' (%s)' % (deepLink.get('viewage'))
      if uicode in ['channel', 'movie']:
        isFolder = False
      elif parameters['contentidType'] == 'direct':
        isFolder = False
        parameters['mode'] = 'VOD'
      else:
        isFolder = True
      self.add_dir(title, sublabel=subtitle, img=thumbnail,
                   infoLabels=info, isFolder=isFolder, params=parameters)
    if compareCount:
      parameters['mode'] = 'GN_LIST'
      parameters['uicode'] = uicode
      parameters['page'] = str(pageNum + 1)
      label = '[B]%s >>[/B]' % '다음 페이지'
      sublabel = str(pageNum + 1)
      self.add_dir(label, sublabel=sublabel, img='',
                   infoLabels=None, isFolder=True, params=parameters)
    if len(deepLinkList) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def dp_Episodelink_List(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    contentId = args.get('contentid')
    contentIdType = args.get('contentidType')
    uicode = args.get('uicode')
    pageNum = int(args.get('page'))
    episodeList, compareCount = self.WavveObj.GetEpisodeList(
        contentId, uicode, contentIdType, pageNum, orderby=self.get_winEpisodeOrderby())
    for episode in episodeList:
      title = episode.get('title')
      subtitle = episode.get('subtitle')
      thumbnail = episode.get('thumbnail')
      parameters = {'mode': 'VOD', 'uicode': episode.get('uicode'), 'contentid': episode.get('contentid'), 'programid': episode.get(
          'programid'), 'title': title, 'subtitle': subtitle, 'thumbnail': thumbnail, 'viewage': episode.get('viewage')}
      if episode.get('viewage') == '21':
        subtitle += ' (%s)' % (episode.get('viewage'))
      info = episode.get('info')
      info['plot'] = episode.get('synopsis')
      self.add_dir(title, sublabel=subtitle, img=thumbnail,
                   infoLabels=info, isFolder=False, params=parameters)
    if pageNum == 1:
      info = {'plot': '정렬순서를 변경합니다.'}
      parameters = {}
      parameters['mode'] = 'ORDER_BY'
      if self.get_winEpisodeOrderby() == 'desc':
        label = '정렬순서변경 : 최신화부터 -> 1회부터'
        parameters['orderby'] = 'asc'
      else:
        label = '정렬순서변경 : 1회부터 -> 최신화부터'
        parameters['orderby'] = 'desc'
      self.add_dir(label, sublabel='', img='', infoLabels=info,
                   isFolder=False, params=parameters)
    if compareCount:
      parameters['mode'] = 'DEEP_LIST'
      parameters['uicode'] = uicode
      parameters['contentid'] = contentId
      parameters['contentidType'] = contentIdType
      parameters['page'] = str(pageNum + 1)
      label = '[B]%s >>[/B]' % '다음 페이지'
      sublabel = str(pageNum + 1)
      self.add_dir(label, sublabel=sublabel, img='',
                   infoLabels=None, isFolder=True, params=parameters)
    if len(episodeList) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def play_VIDEO(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    contentId = args.get('contentid')
    uicode = args.get('uicode')
    quality = self.get_selQuality()
    self.addon_log(contentId + ' - ' + uicode, False)
    playurl, awscookie, drm, previewmsg = self.WavveObj.GetStreamingURL(
        contentId, uicode, quality)
    path = '%s|Cookie=%s' % (playurl, awscookie)
    self.addon_log(path, False)
    if playurl == '':
      self.addon_noti(__language__(30303).encode('utf8'))
      return
    listItem = xbmcgui.ListItem(path=path)
    if drm:
      customdata = drm['customdata']
      drmhost = drm['drmhost']
      menifestType = 'mpd'
      helper = inputstreamhelper.Helper(menifestType, drm='com.widevine.alpha')
      if helper.check_inputstream():
        if uicode == 'movie':
          referer = 'https://www.wavve.com/player/movie?movieid=%s' % contentId
        else:
          referer = 'https://www.wavve.com/player/vod?programid=%s&page=1' % contentId
        uri = {'content-type': 'application/octet-stream', 'origin': 'https://www.wavve.com', 'pallycon-customdata': customdata, 'referer': referer, 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': userAgent
               }
        licenseKey = drmhost + '|' + urllib.urlencode(uri) + '|R{SSM}|'
        listItem.setProperty(
            'inputstreamaddon', helper.inputstream_addon)
        listItem.setProperty(
            'inputstream.adaptive.manifest_type', menifestType)
        listItem.setProperty('inputstream.adaptive.license_type', i1)
        listItem.setProperty('inputstream.adaptive.license_key', licenseKey)
        listItem.setProperty(
            'inputstream.adaptive.stream_headers', 'Cookie=%s' % awscookie)
    xbmcplugin.setResolvedUrl(self._addon_handle, True, listItem)
    if previewmsg:
      self.addon_noti(previewmsg.encode('utf-8'))
    else:
      if '/preview.' in urlparse.urlsplit(playurl).path:
        self.addon_noti(__language__(30401).encode('utf8'))
    try:
      if args.get('mode') in ['VOD', 'MOVIE'] and args.get('title') and args.get('viewage') != '21':
        parameters = {'code': args.get('programid') if args.get('mode') == 'VOD' else args.get('contentid'), 'img': args.get('thumbnail'), 'title': args.get('title'), 'subtitle': args.get('subtitle'), 'videoid': args.get('contentid')
                      }
        self.Save_Watched_List(args.get('mode').lower(), parameters)
    except:
      None

  def dp_Watch_List(self, args):
    genre = args.get('genre')
    directReplay = self.get_settings_direct_replay()
    if genre == '-':
      self.add_dir('VOD 시청내역', sublabel='', img='',
                   infoLabels=None, isFolder=True, params={'mode': 'WATCH', 'genre': 'vod'})
      self.add_dir('영화 시청내역', sublabel='', img='',
                   infoLabels=None, isFolder=True, params={'mode': 'WATCH', 'genre': 'movie'})
      xbmcplugin.endOfDirectory(self._addon_handle)
    else:
      watchedList = self.Load_Watched_List(genre)
      for watched in watchedList:
        watchedDict = dict(urlparse.parse_qsl(watched))
        title = watchedDict.get('title').strip()
        subtitle = watchedDict.get('subtitle').strip()
        if subtitle == 'None':
          subtitle = ''
        img = watchedDict.get('img')
        videoId = watchedDict.get('videoid')
        info = {}
        if genre == 'movie' and self.get_settings_addinfo() == True:
          movieInfoList = self.WavveObj.GetMovieInfoList(
              [watchedDict.get('code')])
          info = movieInfoList.get(watchedDict.get('code'))
        else:
          info['plot'] = '%s\n%s' % (title, subtitle)
        if genre == 'vod':
          if directReplay == False or videoId == None:
            parameters = {'mode': 'DEEP_LIST', 'contentid': watchedDict.get('code'), 'contentidType': 'programid', 'uicode': 'vod', 'page': '1'
                          }
            isFolder = True
          else:
            parameters = {'mode': 'VOD', 'contentid': videoId, 'contentidType': 'contentid', 'programid': watchedDict.get('code'), 'uicode': 'vod', 'title': title, 'subtitle': subtitle, 'thumbnail': img
                          }
            isFolder = False
        else:
          parameters = {'mode': 'MOVIE', 'contentid': watchedDict.get('code'), 'contentidType': 'contentid', 'uicode': 'movie', 'title': title, 'thumbnail': img
                        }
          isFolder = False
        self.add_dir(title, sublabel=subtitle, img=img,
                     infoLabels=info, isFolder=isFolder, params=parameters)
      info = {'plot': '시청목록을 삭제합니다.'}
      label = '*** 시청목록 삭제 ***'
      parameters = {'mode': 'MYVIEW_REMOVE', 'genre': genre
                    }
      self.add_dir(label, sublabel='', img='', infoLabels=info,
                   isFolder=False, params=parameters)
      xbmcplugin.endOfDirectory(self._addon_handle, cacheToDisc=False)

  def dp_Search_Group(self, args):
    self.add_dir('VOD 검색', sublabel='', img='', infoLabels=None,
                 isFolder=True, params={'mode': 'SEARCH_LIST', 'genre': 'vod', 'page': '1'})
    self.add_dir('영화 검색', sublabel='', img='', infoLabels=None,
                 isFolder=True, params={'mode': 'SEARCH_LIST', 'genre': 'movie', 'page': '1'})
    xbmcplugin.endOfDirectory(self._addon_handle)

  def dp_Search_List(self, args):
    self.WavveObj.SaveCredential(self.get_winCredential())
    isAddInfo = self.get_settings_addinfo()
    genre = args.get('genre')
    pageNum = int(args.get('page'))
    if 'search_key' in args:
      searchKey = args.get('search_key')
    else:
      searchKey = self.get_keyboard_input(
          __language__(30003).encode('utf-8'))
      if not searchKey:
        return
    searchList, compareCount = self.WavveObj.GetSearchList(
        searchKey, genre, pageNum, exclusion21=self.get_settings_exclusion21(), addinfoyn=isAddInfo)
    for search in searchList:
      title = search.get('title')
      thumbnail = search.get('thumbnail')
      info = search.get('info')
      if genre == 'movie' and isAddInfo == True:
        title = '%s (%s)' % (title, str(info.get('year')))
      else:
        info['plot'] = title
      if genre == 'vod':
        parameters = {'mode': 'DEEP_LIST', 'contentid': search.get('programid'), 'contentidType': 'programid', 'uicode': 'vod', 'page': '1', 'title': title, 'subtitle': '', 'thumbnail': thumbnail, 'viewage': search.get('viewage')
                      }
        isFolder = True
      else:
        parameters = {'mode': 'MOVIE', 'contentid': search.get('contentid'), 'contentidType': 'contentid', 'uicode': 'movie', 'page': '1', 'title': title, 'subtitle': '', 'thumbnail': thumbnail, 'viewage': search.get('viewage')
                      }
        isFolder = False
      if parameters.get('viewage') == '21':
        title += ' (%s)' % (parameters.get('viewage'))
      self.add_dir(title, sublabel='', img=thumbnail,
                   infoLabels=info, isFolder=isFolder, params=parameters)
    if compareCount:
      parameters['mode'] = 'SEARCH_LIST'
      parameters['genre'] = genre
      parameters['page'] = str(pageNum + 1)
      parameters['search_key'] = searchKey
      label = '[B]%s >>[/B]' % '다음 페이지'
      sublabel = str(pageNum + 1)
      self.add_dir(label, sublabel=sublabel, img='',
                   infoLabels=None, isFolder=True, params=parameters)
    if len(searchList) > 0:
      xbmcplugin.endOfDirectory(self._addon_handle)

  def Load_Watched_List(self, genre):
    try:
      watchedListFilePath = xbmc.translatePath(os.path.join(
          __profile__, 'watchedlist_%s.txt' % genre))
      with open(watchedListFilePath, 'r') as f:
        watchedList = f.readlines()
    except:
      watchedList = []
    return watchedList

  def Save_Watched_List(self, genre, in_params):
    try:
      watchedListFilePath = xbmc.translatePath(os.path.join(
          __profile__, 'watchedlist_%s.txt' % genre))
      watchedList = self.Load_Watched_List(genre)
      with open(watchedListFilePath, 'w') as f:
        ooo = urllib.urlencode(in_params)
        ooo = ooo.encode('utf-8') + '\n'
        f.write(ooo)
        i = 0
        for watched in watchedList:
          watchedDict = dict(urlparse.parse_qsl(watched))
          paramsCode = in_params.get('code')
          watchedDictCode = watchedDict.get('code')
          if genre == 'vod' and self.get_settings_direct_replay() == True:
            paramsCode = in_params.get('videoid')
            watchedDictCode = watchedDict.get(
                'videoid') if watchedDictCode != None else '-'
          if paramsCode != watchedDictCode:
            f.write(watched)
            i += 1
            if i >= 50:
              break
    except:
      None

  def Delete_Watched_List(self, genre):
    try:
      watchedListFilePath = xbmc.translatePath(os.path.join(
          __profile__, 'watchedlist_%s.txt' % genre))
      with open(watchedListFilePath, 'w') as f:
        f.write('')
    except:
      None

  def dp_WatchList_Delete(self, args):
    genre = args.get('genre')
    dialog = xbmcgui.Dialog()
    isYes = dialog.yesno(__name__, __language__(30201).encode(
        'utf8'), __language__(30202).encode('utf8'))
    if isYes == False:
      sys.exit()
    self.Delete_Watched_List(genre)
    xbmc.executebuiltin("Container.Refresh")

  def wavve_main(self):
    mode = self.main_params.get('mode', None)
    self.login_main()
    if mode is None:
      self.dp_Main_List()
    elif mode == 'GNB_LIST':
      self.dp_Gnb_List(self.main_params)
    elif mode == 'GN_LIST':
      self.dp_Deeplink_List(self.main_params)
    elif mode == 'DEEP_LIST':
      uicode = self.main_params.get('uicode', None)
      if uicode in ['quick', 'vod', 'program', 'x']:
        self.dp_Episodelink_List(self.main_params)
      else:
        None
    elif mode in ['LIVE', 'VOD', 'MOVIE']:
      self.play_VIDEO(self.main_params)
      time.sleep(0.1)
    elif mode == 'GN_MYVIEW':
      self.dp_Myview_Group(self.main_params)
    elif mode == 'MYVIEW_LIST':
      self.dp_Myview_List(self.main_params)
    elif mode == 'GENRE':
      self.dp_Genre_Group(self.main_params)
    elif mode == 'GENRE_LIST':
      self.dp_Genre_List(self.main_params)
    elif mode == 'WATCH':
      self.dp_Watch_List(self.main_params)
    elif mode == 'MYVIEW_REMOVE':
      self.dp_WatchList_Delete(self.main_params)
    elif mode == 'SEARCH':
      self.dp_Search_Group(self.main_params)
    elif mode == 'SEARCH_LIST':
      self.dp_Search_List(self.main_params)
    elif mode == 'ORDER_BY':
      self.dp_setEpOrderby(self.main_params)
    else:
      None
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
