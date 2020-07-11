# -*- coding: utf-8 -*-
__author__ = "NightRain"
import urllib
import urllib2
import cookielib
import re
import json
import sys
import urlparse
reload(sys)
sys.setdefaultencoding('utf-8')
userAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'


class Session (object):
  def __init__(self):
    self.MyCookie = cookielib.LWPCookieJar()
    self.Opener = urllib2.build_opener(
        urllib2.HTTPCookieProcessor(self.MyCookie))
    self.Opener.addheaders = [('User-Agent', userAgent)]
    urllib2.install_opener(self.Opener)

  def Request(self, url, postdata=None):
    if postdata:
      request = self.Opener.open(url, postdata)
    else:
      request = self.Opener.open(url)
    readData = request.read()
    request.close()
    return readData

  def Request2(self, url, params=None, postdata=None):
    import requests
    headers = {'User-Agent': userAgent}
    if postdata:
      request = requests.post(
          url, headers=headers, params=params, data=postdata)
    else:
      request = requests.get(url, headers=headers, params=params)
    json = request.json()
    return json


class iII111ii (object):
  def __init__(self):
    self.SESSION = Session()
    self.API_DOMAIN = 'https://apis.pooq.co.kr'
    self.APIKEY = 'E5F3E0D30947AA5440556471321BB6D9'
    self.CREDENTIAL = 'none'
    self.DEVICE = 'pc'
    self.DRM = 'wm'
    self.PARTNER = 'pooq'
    self.POOQZONE = 'none'
    self.REGION = 'kor'
    self.TARGETAGE = 'all'
    self.CREDENTIAL = 'none'
    self.HTTPTAG = 'https://'
    self.LIST_LIMIT = 30
    self.EP_LIMIT = 30
    self.MV_LIMIT = 24
    self.guid = 'none'
    self.guidtimestamp = 'none'

  def SaveCredential(self, credential):
    self.CREDENTIAL = credential

  def LoadCredential(self):
    return self.CREDENTIAL

  def GetDefaultParams(self):
    defaultParams = {'apikey': self.APIKEY,
                     'credential': self.CREDENTIAL,
                     'device': self.DEVICE,
                     'drm': self.DRM,
                     'partner': self.PARTNER,
                     'pooqzone': self.POOQZONE,
                     'region': self.REGION,
                     'targetage': self.TARGETAGE
                     }
    return defaultParams

  def makeurl(self, domain, path, query=None):
    url = ''
    if domain:
      if re.search(r'http[s]*://', domain):
        url += domain
      else:
        url += 'http://%s' % domain
      if path:
        url += path
        if query:
          url += '?%s' % query
    return url

  def MakeServiceUrl(self, path, params):
    url = self.makeurl(self.API_DOMAIN, path, urllib.urlencode(params))
    return url

  def GetGUID(self, guid_str='POOQ', guidType=1):
    def getRandStr(media):
      from datetime import datetime
      strTime = datetime.now().strftime('%Y%m%d%H%M%S')
      randomNumStr = getRandomNumStr(5)
      return randomNumStr + media + strTime

    def getRandomNumStr(num):
      from random import randint
      randomNumStr = ""
      for _ in range(0, num):
        randomNum = str(randint(1, 5))
        randomNumStr += randomNum
      return randomNumStr
    randStr = getRandStr(guid_str)
    hashStr = self.GetHash(randStr)
    if guidType == 2:
      hashStr = '%s-%s-%s-%s-%s' % (hashStr[: 8], hashStr[8: 12],
                                    hashStr[12: 16], hashStr[16: 20], hashStr[20:])
    return hashStr

  def GetHash(self, hash_str):
    import hashlib
    md5sum = hashlib.md5()
    md5sum.update(hash_str)
    return str(md5sum.hexdigest())

  def CheckQuality(self, sel_qt, qt_list):
    result = 0
    for qt in qt_list:
      if sel_qt >= qt:
        return qt
      result = qt
    return result

  def GetCredential(self, user_id, user_pw, user_pf):
    result = False
    try:
      postData = {'id': user_id, 'password': user_pw, 'profile': '0', 'pushid': '', 'type': 'general'
                  }
      url = self.MakeServiceUrl('/login', self.GetDefaultParams())
      req = self.SESSION.Request(
          url, postdata=urllib.urlencode(postData))
      jsonData = json.loads(req)
      credential = jsonData['credential']
      if user_pf != 0:
        postData = {'id': credential, 'password': '', 'profile': str(user_pf), 'pushid': '', 'type': 'credential'
                    }
        req = self.SESSION.Request(
            url, postdata=urllib.urlencode(postData))
        jsonData = json.loads(req)
        credential = jsonData['credential']
      if credential:
        result = True
    except Exception as e:
      print(e)
      credential = 'none'
    self.SaveCredential(credential)
    return result

  def GetIssue(self):
    result = False
    try:
      url = self.MakeServiceUrl('/guid/issue', self.GetDefaultParams())
      req = self.SESSION.Request(url)
      jsonData = json.loads(req)
      guid = jsonData['guid']
      guidTimeStamp = jsonData['guidtimestamp']
      if guid:
        result = True
    except Exception as e:
      print(e)
      guid = 'none'
      guidTimeStamp = 'none'
    self.guid = guid
    self.guidtimestamp = guidTimeStamp
    return result

  def GetGnList(self, gn_str):
    result = []
    try:
      path = '/cf/supermultisections/' + gn_str
      url = self.MakeServiceUrl(path, self.GetDefaultParams())
      req = self.SESSION.Request(url)
      jsonData = json.loads(req)
      if not ('multisectionlist' in jsonData):
        return None
      multiSectionList = jsonData['multisectionlist']
      for multiSection in multiSectionList:
        title = multiSection['title']
        if len(title) == 0:
          continue
        if title == 'minor':
          continue
        if re.search(u'베너', title):
          continue
        title = re.sub('\n|\!|\~|(@0@)|(@\^0@)', '', title)
        title = title.lstrip('#')
        for bodylist in multiSection['eventlist'][0]['bodylist']:
          if re.search(r'uicode:', bodylist):
            elem = {'title': unicode(title), 'uicode': re.sub(r'uicode:', '', bodylist)
                    }
            result.append(elem)
            break
    except Exception as e:
      print(e)
    return result

  def GetDeeplinkList(self, gn_str, came_str, page_int, addinfoyn=False):
    result = []
    pageCount = count = 1
    contentType = 'quick'
    contentId = contentIdType = channelEpg = ''
    compareCount = False
    epgList = {}
    try:
      url = self.MakeServiceUrl(
          '/cf/deeplink/' + gn_str, self.GetDefaultParams())
      req = self.SESSION.Request(url)
      jsonData = json.loads(req)
      if not ('url' in jsonData):
        return None
      jsonUrl = jsonData['url']
      print jsonUrl
      jsonUrlDict = dict(urlparse.parse_qsl(urlparse.urlsplit(jsonUrl).query))
      jsonUrlDict['came'] = came_str
      jsonUrlDict['limit'] = str(self.LIST_LIMIT)
      if 'contenttype' in jsonUrlDict:
        contentType = jsonUrlDict['contenttype']
      if came_str == 'movie':
        jsonUrlDict['mtype'] = 'svod'
      if page_int != 1:
        jsonUrlDict['offset'] = str((page_int - 1) * self.LIST_LIMIT)
        jsonUrlDict['page'] = str(page_int)
      url = self.HTTPTAG + urlparse.urlsplit(jsonUrl).path + '?' + \
          urllib.urlencode(jsonUrlDict) + '&' + \
          urllib.urlencode(self.GetDefaultParams())
      req = self.SESSION.Request(url)
      jsonData = json.loads(req)
      if not ('celllist' in jsonData['cell_toplist']):
        return result, compareCount
      cellList = jsonData['cell_toplist']['celllist']
      if (contentType == 'channel' and came_str == 'live'):
        if ('genre' in jsonUrlDict):
          genre = jsonUrlDict['genre']
        else:
          genre = 'all'
        print "*epgcall*"
        epgList = self.GetEPGList(genre)
      for cell in cellList:
        title = subtitle = thumbnail = ''
        title = cell.get('title_list')[0].get('text')
        if (len(cell.get('title_list')) > 1):
          if (cell.get('title_list')[1].get('text').startswith('@')):
            for OO in cell.get('bottom_taglist'):
              if OO == 'playy' or OO == 'won':
                subtitle = OO
          else:
            subtitle = cell.get('title_list')[1].get('text')
            subtitle = re.sub(r'(\$O\$)|(\&[a-z]{2}\;)', '', subtitle)
        if (cell.get('thumbnail') != ''):
          thumbnail = 'https://%s' % cell.get('thumbnail')
        eventListUrl = cell['event_list'][1].get('url')
        eventListUrlDict = dict(urlparse.parse_qsl(
            urlparse.urlsplit(eventListUrl).query))
        if re.search(u'programid=\&', eventListUrl) and ('contentid' in eventListUrlDict):
          contentId = eventListUrlDict['contentid']
          contentIdType = 'direct'
        elif ('contentid' in eventListUrlDict):
          contentId = eventListUrlDict['contentid']
          contentIdType = 'contentid'
        elif ('programid' in eventListUrlDict):
          contentId = eventListUrlDict['programid']
          contentIdType = 'programid'
          contentType = 'program'
        elif ('channelid' in eventListUrlDict):
          contentId = eventListUrlDict['channelid']
          contentIdType = 'channelid'
          if contentId in epgList:
            channelEpg = epgList[contentId]
          else:
            channelEpg = ''
        elif ('movieid' in eventListUrlDict):
          contentId = eventListUrlDict['movieid']
          contentIdType = 'movieid'
          contentType = 'movie'
        else:
          contentId = '-'
          contentIdType = '-'
        info = {}
        info['mpaa'] = cell.get('age')
        try:
          if ('channelid' in eventListUrlDict):
            info['mediatype'] = 'video'
            info['title'] = '%s < %s >' % (
                unicode(title), unicode(subtitle))
            info['tvshowtitle'] = unicode(subtitle)
            info['studio'] = unicode(title)
          elif ('movieid' in eventListUrlDict):
            info['mediatype'] = 'movie'
            info['title'] = unicode(title_list)
          else:
            info['mediatype'] = 'episode'
            info['title'] = unicode(title_list)
        except:
          None
        elem = {'title': unicode(title), 'subtitle': unicode(subtitle), 'thumbnail': thumbnail, 'uicode': i1I1ii, 'contentid': contentId, 'contentidType': contentIdType, 'viewage': O0oOO0.get('age'), 'channelepg': channelEpg, 'info': info
                }
        result.append(elem)
      pageCount = int(jsonData['cell_toplist']['pagecount'])
      if jsonData['cell_toplist']['count']:
        count = int(jsonData['cell_toplist']['count'])
      else:
        count = self.LIST_LIMIT
      compareCount = pageCount > count
    except Exception as e:
      print(e)
    try:
      if result[0].get('contentidType') == 'movieid' and addinfoyn == True:
        movieList = []
        movieInfoList = {}
        for elem in result:
          movieList.append(elem.get('contentid'))
        movieInfoList = self.GetMovieInfoList(movieList)
        for i in range(len(result)):
          result[i]['info'] = movieInfoList.get(result[i]['contentid'])
    except:
      None
    return (result, compareCount)

  def GetEpisodeList(self, contentid, contenttype, contentidType, page_int, orderby='desc'):
    resultList = []
    pageCount = count = 1
    compareCount = False
    if orderby == 'desc':
      orderby = 'new'
    else:
      orderby = 'old'
    try:
      parameters = self.GetDefaultParams()
      if contentidType == 'contentid':
        url = self.MakeServiceUrl('/cf/vod/contents/' + contentid, parameters)
        req = self.SESSION.Request(url)
        jsonData = json.loads(req)
        if not ('programid' in jsonData):
          return None
        programId = jsonData['programid']
      else:
        programId = contentid
      uri = {'limit': self.EP_LIMIT, 'offset': str((page_int - 1) * self.EP_LIMIT), 'orderby': orderby
             }
      url = self.API_DOMAIN + '/vod/programs-contents/' + programId + '?' + \
          urllib.urlencode(uri) + '&' + urllib.urlencode(parameters)
      req = self.SESSION.Request(url)
      jsonData = json.loads(req)
      if not ('list' in jsonData):
        return None
      for listElem in jsonData['list']:
        title = listElem.get('programtitle')
        subtitle = '%s회, %s(%s)' % (listElem.get('episodenumber'), listElem.get(
            'releasedate'), listElem.get('releaseweekday'))
        if (listElem.get('image') != ''):
          thumbnail = 'https://%s' % listElem.get('image')
        synopsis = re.sub(
            u'(\<[a-zA-Z]{1,2}\>)|(\<\/[a-zA-Z]{1,2}\>)', '', unicode(listElem.get('synopsis')))
        info = {}
        info['title'] = unicode(title)
        info['mediatype'] = 'episode'
        info['mpaa'] = listElem.get('targetage')
        try:
          if 'episodenumber' in listElem:
            info['episode'] = listElem.get('episodenumber')
          if 'releasedate' in listElem:
            info['year'] = int(listElem.get('releasedate')[: 4])
          if 'releasedate' in listElem:
            info['aired'] = listElem.get('releasedate')
          if 'playtime' in listElem:
            info['duration'] = listElem.get('playtime')
          if 'episodeactors' in listElem:
            if listElem.get('episodeactors') != '':
              info['cast'] = listElem.get('episodeactors').split(',')
        except:
          None
        result = {'title': unicode(title), 'subtitle': unicode(subtitle), 'thumbnail': thumbnail, 'uicode': contenttype, 'contentid': listElem.get('contentid'), 'programid': listElem.get('programid'), 'synopsis': synopsis, 'viewage': listElem.get('targetage'), 'info': info
                  }
        resultList.append(result)
      pageCount = int(jsonData['pagecount'])
      if jsonData['count']:
        count = int(jsonData['count'])
      else:
        count = self.EP_LIMIT
      compareCount = pageCount > count
    except Exception as e:
      print(e)
    return (resultList, compareCount)

  def GetMyviewList(self, contenttype, page_int, addinfoyn=False):
    resultList = []
    pageCount = count = 1
    compareCount = False
    try:
      uri = {'contenttype': contenttype, 'limit': self.MV_LIMIT, 'offset': str((page_int - 1) * self.MV_LIMIT), 'orderby': 'new'
             }
      url = self.API_DOMAIN + '/myview/contents' + '?' + \
          urllib.urlencode(uri) + '&' + \
          urllib.urlencode(self.GetDefaultParams())
      req = self.SESSION.Request(url)
      jsonData = json.loads(req)
      if not ('list' in jsonData[0]):
        return None
      jsonDataList = jsonData[0]['list']
      for elem in jsonDataList:
        info = {}
        if contenttype == 'vod':
          title = elem.get('programtitle')
          subtitle = '%s회, %s' % (elem.get(
              'episodenumber'), elem.get('releasedate'))
          contentId = elem.get('contentid')
          programId = elem.get('programid')
          info['title'] = unicode(title)
          info['mediatype'] = 'episode'
          info['mpaa'] = elem.get('targetage')
          try:
            info['studio'] = elem.get('channelname')
          except:
            None
          try:
            if 'releasedate' in elem:
              info['year'] = int(elem.get('releasedate')[: 4])
            if 'releasedate' in elem:
              info['aired'] = elem.get('releasedate')
          except:
            None
        else:
          title = elem.get('title')
          subtitle = ''
          contentId = programId = elem.get('movieid')
          info['title'] = unicode(title)
          info['mediatype'] = 'movie'
          info['mpaa'] = elem.get('targetage')
          try:
            if 'releasedate' in elem:
              info['year'] = int(elem.get('releasedate')[: 4])
            if 'releasedate' in elem:
              info['aired'] = elem.get('releasedate')
          except:
            None
        if (elem.get('image') != ''):
          thumbnail = 'https://%s' % elem.get('image')
        result = {'title': unicode(title), 'subtitle': unicode(subtitle), 'thumbnail': thumbnail, 'uicode': contenttype,
                  'contentid': contentId, 'programid': programId, 'viewage': O0oOO0.get('targetage'), 'info': info}
        resultList.append(result)
      pageCount = int(jsonData[0]['pagecount'])
      if jsonData[0]['count']:
        count = int(jsonData[0]['count'])
      else:
        count = self.MV_LIMIT
      compareCount = pageCount > count
    except Exception as e:
      print(e)
    try:
      if contenttype == 'movie' and addinfoyn == True:
        movieList = []
        movieInfoList = {}
        for result in resultList:
          movieList.append(result.get('contentid'))
        movieInfoList = self.GetMovieInfoList(movieList)
        for i in range(len(resultList)):
          resultList[i]['info'] = movieInfoList.get(
              resultList[i]['contentid'])
    except:
      None
    return resultList, compareCount

  def GetSearchList(self, search_key, genre, page_int, exclusion21=False, addinfoyn=False):
    resultList = []
    pageCount = count = 1
    compareCount = False
    try:
      uri = {'type': 'program' if genre == 'vod' else 'movie', 'keyword': search_key, 'offset': str((page_int - 1) * self.LIST_LIMIT), 'limit': self.LIST_LIMIT, 'orderby': 'score', 'isplayymovie': 'y'
             }
      url = self.API_DOMAIN + '/cf/search/list.js' + '?' + \
          urllib.urlencode(uri) + '&' + \
          urllib.urlencode(self.GetDefaultParams())
      req = self.SESSION.Request(url)
      jsonData = json.loads(req)
      if not ('celllist' in jsonData['cell_toplist']):
        return resultList, compareCount
      cellList = jsonData['cell_toplist']['celllist']
      for cell in cellList:
        info = {}
        title = cell['title_list'][0]['text']
        if (cell.get('thumbnail') != ''):
          I1i = 'https://%s' % cell.get('thumbnail')
        for body in cell['event_list'][0]['bodylist']:
          if re.search(r'uicode:', body):
            if genre == 'vod':
              contentId = ''
              programId = re.sub(r'uicode:', '', body)
              info['mediatype'] = 'episode'
            else:
              contentId = re.sub(r'uicode:', '', body)
              programId = ''
              if cell.get('bottom_taglist')[0] == 'playy':
                title += ' [playy]'
              info['mediatype'] = 'movie'
            info['title'] = unicode(cell['title_list'][0]['text'])
            info['mpaa'] = cell.get('age')
            IiIi1I1 = {'title': unicode(title), 'thumbnail': I1i, 'uicode': genre, 'contentid': contentId, 'programid': programId, 'viewage': cell.get('age'), 'info': info
                       }
        if exclusion21 == False or cell.get('age') != '21':
          resultList.append(IiIi1I1)
      pageCount = int(jsonData['cell_toplist']['pagecount'])
      if jsonData['cell_toplist']['count']:
        count = int(jsonData['cell_toplist']['count'])
      else:
        count = self.LIST_LIMIT
      compareCount = pageCount > count
    except Exception as e:
      print(e)
    try:
      if genre == 'movie' and addinfoyn == True:
        movieList = []
        movieInfoList = {}
        for result in resultList:
          movieList.append(result.get('contentid'))
        movieInfoList = self.GetMovieInfoList(movieList)
        for i in range(len(resultList)):
          resultList[i]['info'] = movieInfoList.get(
              resultList[i]['contentid'])
    except:
      None
    return resultList, compareCount

  def GetGenreGroup(self, maintype, subtype, orderby, ordernm, exclusion21=False):
    resultList = []
    try:
      uri = {'type': maintype}
      url = self.API_DOMAIN + '/cf/filters' + '?' + \
          urllib.urlencode(uri) + '&' + \
          urllib.urlencode(self.GetDefaultParams())
      req = self.SESSION.Request(url)
      jsonData = json.loads(req)
      if not (maintype in jsonData):
        return None
      jsonMainType = jsonData[maintype]
      if subtype == '-':
        for elem in jsonMainType:
          urlDict = dict(urlparse.parse_qsl(
              urlparse.urlsplit(elem.get('url')).query))
          result = {'title': elem.get('text'), 'genre': elem.get('id'), 'subgenre': '-', 'adult': elem.get('adult'), 'broadcastid': urlDict.get('broadcastid'), 'contenttype': urlDict.get('contenttype'), 'uiparent': urlDict.get('uiparent'), 'uirank': urlDict.get('uirank'), 'uitype': urlDict.get('uitype'), 'orderby': orderby, 'ordernm': ordernm
                    }
          if exclusion21 == False or result.get('adult') == 'n':
            resultList.append(result)
      else:
        for elem in jsonMainType:
          if elem.get('id') == subtype:
            for II in elem['sublist']:
              urlDict = dict(urlparse.parse_qsl(
                  urlparse.urlsplit(II.get('url')).query))
              result = {'title': II.get('text'), 'genre': subtype, 'subgenre': II.get('id'), 'adult': II.get('adult'), 'broadcastid': urlDict.get('broadcastid'), 'contenttype': urlDict.get('contenttype'), 'uiparent': urlDict.get('uiparent'), 'uirank': urlDict.get('uirank'), 'uitype': urlDict.get('uitype'), 'orderby': orderby, 'ordernm': ordernm
                        }
              resultList.append(result)
            break
    except Exception as e:
      print(e)
    return resultList

  def GetGenreGroup_sub(self, in_params):
    resultList = []
    try:
      uri = {'WeekDay': 'all', 'limit': '20', 'offset': '0', 'orderby': in_params.get('orderby'), 'adult': in_params.get('adult'), 'broadcastid': in_params.get('broadcastid'), 'contenttype': in_params.get('contenttype'), 'genre': in_params.get('genre'), 'uiparent': in_params.get('uiparent'), 'uirank': in_params.get('uirank'), 'uitype': in_params.get('uitype')
             }
      url = self.API_DOMAIN + '/cf/vod/newcontents' + '?' + \
          urllib.urlencode(uri) + '&' + \
          urllib.urlencode(self.GetDefaultParams())
      req = self.SESSION.Request(url)
      jsonData = json.loads(req)
      if not ('filter_item_list' in jsonData['filter']['filterlist'][1]):
        return None
      filterItemList = jsonData['filter']['filterlist'][1]['filter_item_list']
      for filterItem in filterItemList:
        result = {'broadcastid': in_params.get('broadcastid'), 'contenttype': in_params.get('contenttype'), 'genre': in_params.get('genre'), 'uiparent': in_params.get('uiparent'), 'uirank': in_params.get('uirank'), 'uitype': in_params.get('uitype'), 'adult': filterItem.get('adult'), 'title': filterItem.get('title'), 'subgenre': filterItem.get('api_parameters')[filterItem.get('api_parameters').find('=') + 1:], 'orderby': in_params.get('orderby')
                  }
        resultList.append(result)
    except Exception as e:
      print(e)
    return resultList

  def GetGenreList(self, genre, in_params, page_int, addinfoyn=False):
    resultList = []
    pageCount = count = 1
    compareCount = False
    try:
      uri = {'WeekDay': 'all', 'adult': in_params.get('adult'), 'broadcastid': in_params.get('broadcastid'), 'contenttype': in_params.get('contenttype'), 'genre': in_params.get(
          'genre'), 'orderby': in_params.get('orderby'), 'uiparent': in_params.get('uiparent'), 'uirank': in_params.get('uirank'), 'uitype': in_params.get('uitype')}
      if genre == 'vodgenre':
        path = '/cf/vod/newcontents'
        if in_params.get('subgenre') != '-':
          uri['subgenre'] = in_params.get('subgenre')
      else:
        path = '/cf/movie/contents'
        uri['price'] = 'all'
        uri['sptheme'] = 'svod'
      uri['limit'] = self.LIST_LIMIT
      uri['offset'] = str((page_int - 1) * self.LIST_LIMIT)
      uri['page'] = str(page_int)
      url = self.API_DOMAIN + path + '?' + \
          urllib.urlencode(uri) + '&' + \
          urllib.urlencode(self.GetDefaultParams())
      req = self.SESSION.Request(url)
      jsonData = json.loads(req)
      if not ('celllist' in jsonData['cell_toplist']):
        return None
      for cell in jsonData['cell_toplist']['celllist']:
        info = {}
        title = I1i = ''
        title = cell['title_list'][0]['text']
        if (cell.get('thumbnail') != ''):
          I1i = 'https://%s' % cell.get('thumbnail')
        for uicode in cell['event_list'][0]['bodylist']:
          if re.search(r'uicode:', uicode):
            info['title'] = unicode(title)
            info['mpaa'] = cell.get('age')
            if genre == 'moviegenre_svod':
              info['mediatype'] = 'movie'
            else:
              info['mediatype'] = 'episode'
            result = {'title': unicode(title), 'uicode': re.sub(r'uicode:', '', uicode), 'thumbnail': I1i, 'viewage': cell.get('age'), 'info': info
                      }
        resultList.append(result)
      pageCount = int(jsonData['cell_toplist']['pagecount'])
      if jsonData['cell_toplist']['count']:
        count = int(jsonData['cell_toplist']['count'])
      else:
        count = self.LIST_LIMIT
      compareCount = pageCount > count
    except Exception as e:
      print(e)
    try:
      if genre == 'moviegenre_svod' and addinfoyn == True:
        movieList = []
        movieInfoList = {}
        for result in resultList:
          movieList.append(result.get('uicode'))
        movieInfoList = self.GetMovieInfoList(movieList)
        for i in range(len(resultList)):
          resultList[i]['info'] = movieInfoList.get(resultList[i]['uicode'])
    except:
      None
    return resultList, compareCount

  def GetEPGList(self, genre):
    resultDict = {}
    try:
      import datetime
      currentTime = datetime.datetime.now()
      if genre == 'all':
        endDateTime = currentTime + datetime.timedelta(hours=2)
      else:
        endDateTime = currentTime + datetime.timedelta(hours=3)
      uri = {'limit': '100', 'offset': '0', 'genre': genre, 'startdatetime': currentTime.strftime('%Y-%m-%d %H:%M'), 'enddatetime': endDateTime.strftime('%Y-%m-%d %H:%M')
                  }
      url = self.API_DOMAIN + '/live/epgs' + '?' + \
          urllib.urlencode(uri) + '&' + urllib.urlencode(self.GetDefaultParams())
      req = self.SESSION.Request(url)
      jsonData = json.loads(req)
      jsonDataList = jsonData['list']
      for elem in jsonDataList:
        channelId = ''
        for e in elem['list']:
          if channelId:
            channelId += '\n'
          channelId += e['title'] + '\n'
          channelId += ' [%s ~ %s]' % (e['starttime']
                                  [- 5:], e['endtime'][- 5:]) + '\n'
        resultDict[elem['channelid']] = unicode(channelId)
    except Exception as e:
      print(e)
    return resultDict

  def GetMovieInfoList(self, movie_list):
    resultDict = {}
    try:
      for movie in movie_list:
        url = self.API_DOMAIN + '/movie/contents/' + movie
        req = self.SESSION.Request(url)
        jsonData = json.loads(req)
        resultMovie = {}
        resultMovie['mediatype'] = 'movie'
        cast = []
        for actor in jsonData['actors']['list']:
          cast.append(actor.get('text'))
        if cast[0] != '':
          resultMovie['cast'] = cast
        directorList = []
        for director in jsonData['directors']['list']:
          directorList.append(director.get('text'))
        if directorList[0] != '':
          resultMovie['director'] = directorList
        genreList = []
        for genre in jsonData['genre']['list']:
          genreList.append(genre.get('text'))
        if genreList[0] != '':
          resultMovie['genre'] = genreList
        if jsonData.get('releasedate') != '':
          resultMovie['year'] = jsonData['releasedate'][: 4]
          resultMovie['aired'] = jsonData['releasedate']
        resultMovie['country'] = jsonData['country']
        resultMovie['duration'] = jsonData['playtime']
        resultMovie['title'] = jsonData['title']
        resultMovie['mpaa'] = jsonData['targetage']
        resultMovie['plot'] = jsonData['synopsis']
        resultDict[movie] = resultMovie
    except Exception as e:
      return {}
    return resultDict

  def GetStreamingURL(self, contentid, contenttype, quality_int):
    playurl = awscookie = drm = previewmsg = ''
    qualityList = []
    try:
      if contenttype == 'channel':
        path = '/live/channels/' + contentid
        contentType = 'live'
      elif contenttype == 'movie':
        path = '/cf/movie/contents/' + contentid
        contentType = 'movie'
      else:
        path = '/cf/vod/contents/' + contentid
        contentType = 'vod'
      defaultParams = self.GetDefaultParams()
      url = self.MakeServiceUrl(path, defaultParams)
      reqJson = self.SESSION.Request2(self.API_DOMAIN + path, params=defaultParams)
      jsonQualityList = reqJson['qualities']['list']
      if jsonQualityList == None:
        return (playurl, awscookie, drm, previewmsg)
      IioO0O = 'hls'
      if 'drms' in reqJson:
        if reqJson['drms']:
          IioO0O = 'dash'
      if 'type' in reqJson:
        if reqJson['type'] == 'onair':
          contentType = 'onairvod'
      for jsonQuality in jsonQualityList:
        qualityList.append(int(jsonQuality.get('id').rstrip('p')))
    except Exception as e:
      return (playurl, awscookie, drm, previewmsg)
    try:
      quality = self.CheckQuality(quality_int, qualityList)
      path = '/streaming'
      parameters = {'contentid': contentid, 'contenttype': contentType, 'action': IioO0O, 'quality': str(quality) + 'p', 'deviceModelId': 'Windows 10', 'guid': self.GetGUID(guidType=2), 'lastplayid': self.guid, 'authtype': 'cookie', 'isabr': 'y', 'ishevc': 'n'
                  }
      url = self.API_DOMAIN + path + '?' + \
          urllib.urlencode(defaultParams) + '&' + urllib.urlencode(parameters)
      parameters.update(defaultParams)
      reqJson = self.SESSION.Request2(self.API_DOMAIN + path, params=parameters)
      playurl = reqJson['playurl']
      if playurl == None:
        return None
      awscookie = reqJson['awscookie']
      drm = reqJson['drm']
      if 'previewmsg' in reqJson['preview']:
        previewmsg = reqJson['preview']['previewmsg']
    except Exception as e:
      print(e)
    playurl = playurl.replace('pooq.co.kr', 'wavve.com')
    return (playurl, awscookie, drm, previewmsg)
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
