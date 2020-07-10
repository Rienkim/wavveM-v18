# -*- coding: utf-8 -*-
__author__ = "NightRain"
import urllib
import urllib2
import cookielib
import re
import json
import sys
import urlparse
reload ( sys )
sys . setdefaultencoding ( 'utf-8' )
IiiIII111iI = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
class oo00 ( object ) :
 def __init__ ( self ) :
  self . MyCookie = cookielib . LWPCookieJar ( )
  self . Opener = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( self . MyCookie ) )
  self . Opener . addheaders = [ ( 'User-Agent' , IiiIII111iI ) ]
  urllib2 . install_opener ( self . Opener )
 def Request ( self , url , postdata = None ) :
  if postdata :
   II1Iiii1111i = self . Opener . open ( url , postdata )
  else :
   II1Iiii1111i = self . Opener . open ( url )
  oo00000o0 = II1Iiii1111i . read ( )
  II1Iiii1111i . close ( )
  return oo00000o0
 def Request2 ( self , url , params = None , postdata = None ) :
  import requests
  Oo0o0ooO0oOOO = { 'User-Agent' : IiiIII111iI }
  if postdata :
   II1Iiii1111i = requests . post ( url , headers = Oo0o0ooO0oOOO , params = params , data = postdata )
  else :
   II1Iiii1111i = requests . get ( url , headers = Oo0o0ooO0oOOO , params = params )
  oo00000o0 = II1Iiii1111i . json ( )
  return oo00000o0
class iII111ii ( object ) :
 def __init__ ( self ) :
  self . SESSION = oo00 ( )
  self . API_DOMAIN = 'https://apis.pooq.co.kr'
  self . APIKEY = 'E5F3E0D30947AA5440556471321BB6D9'
  self . CREDENTIAL = 'none'
  self . DEVICE = 'pc'
  self . DRM = 'wm'
  self . PARTNER = 'pooq'
  self . POOQZONE = 'none'
  self . REGION = 'kor'
  if 3 - 3: iii1I1I + O0
  self . TARGETAGE = 'all'
  self . CREDENTIAL = 'none'
  self . HTTPTAG = 'https://'
  self . LIST_LIMIT = 30
  self . EP_LIMIT = 30
  self . MV_LIMIT = 24
  self . guid = 'none'
  self . guidtimestamp = 'none'
 def SaveCredential ( self , credential ) :
  self . CREDENTIAL = credential
 def LoadCredential ( self ) :
  return self . CREDENTIAL
 def GetDefaultParams ( self ) :
  O0O00Ooo = { 'apikey' : self . APIKEY ,
 'credential' : self . CREDENTIAL ,
 'device' : self . DEVICE ,
 'drm' : self . DRM ,
 'partner' : self . PARTNER ,
 'pooqzone' : self . POOQZONE ,
 'region' : self . REGION ,
 'targetage' : self . TARGETAGE
 }
  return O0O00Ooo
  if 64 - 64: oO0o - O0 / II111iiii / o0oOOo0O0Ooo / iIii1I11I1II1
 def makeurl ( self , domain , path , query = None ) :
  IiIIIiI1I1 = ''
  if domain :
   if re . search ( r'http[s]*://' , domain ) :
    IiIIIiI1I1 += domain
   else :
    IiIIIiI1I1 += 'http://%s' % domain
   if path :
    IiIIIiI1I1 += path
    if query : IiIIIiI1I1 += '?%s' % query
  return IiIIIiI1I1
 def MakeServiceUrl ( self , path , params ) :
  IiIIIiI1I1 = self . makeurl ( self . API_DOMAIN , path , urllib . urlencode ( params ) )
  return IiIIIiI1I1
 def GetGUID ( self , guid_str = 'POOQ' , guidType = 1 ) :
  def ii1I ( media ) :
   from datetime import datetime
   OooO0 = datetime . now ( ) . strftime ( '%Y%m%d%H%M%S' )
   II11iiii1Ii = OO0o ( 5 )
   Ooo = II11iiii1Ii + media + OooO0
   return Ooo
  def OO0o ( num ) :
   from random import randint
   oOOO00o = ""
   for O0O00o0OOO0 in range ( 0 , num ) :
    Ii1iIIIi1ii = str ( randint ( 1 , 5 ) )
    oOOO00o += Ii1iIIIi1ii
   return oOOO00o
  Ooo = ii1I ( guid_str )
  III1i1i = self . GetHash ( Ooo )
  if guidType == 2 :
   III1i1i = '%s-%s-%s-%s-%s' % ( III1i1i [ : 8 ] , III1i1i [ 8 : 12 ] , III1i1i [ 12 : 16 ] , III1i1i [ 16 : 20 ] , III1i1i [ 20 : ] )
  return III1i1i
 def GetHash ( self , hash_str ) :
  import hashlib
  iiii = hashlib . md5 ( )
  if 54 - 54: I1ii11iIi11i * OOooOOo
  iiii . update ( hash_str )
  return str ( iiii . hexdigest ( ) )
  if 13 - 13: O00oOoOoO0o0O + OoOoOO00 - OoooooooOO + O0oo0OO0 . iii1I1I + OoO0O00
 def CheckQuality ( self , sel_qt , qt_list ) :
  Ii = 0
  for oo0O0oOOO00oO in qt_list :
   if sel_qt >= oo0O0oOOO00oO : return oo0O0oOOO00oO
   Ii = oo0O0oOOO00oO
  return Ii
 def GetCredential ( self , user_id , user_pw , user_pf ) :
  I1II1III11iii = False
  try :
   Oo000 = '/login'
   O0O00Ooo = self . GetDefaultParams ( )
   oo = { 'id' : user_id
 , 'password' : user_pw
 , 'profile' : '0'
 , 'pushid' : ''
 , 'type' : 'general'
 }
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 , postdata = urllib . urlencode ( oo ) )
   OOOO = json . loads ( II1Iiii1111i )
   i11i1 = OOOO [ 'credential' ]
   if user_pf != 0 :
    oo = { 'id' : i11i1
 , 'password' : ''
 , 'profile' : str ( user_pf )
 , 'pushid' : ''
 , 'type' : 'credential'
 }
    II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 , postdata = urllib . urlencode ( oo ) )
    OOOO = json . loads ( II1Iiii1111i )
    i11i1 = OOOO [ 'credential' ]
   if i11i1 : I1II1III11iii = True
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   i11i1 = 'none'
  self . SaveCredential ( i11i1 )
  return I1II1III11iii
 def GetIssue ( self ) :
  I11III1II = False
  try :
   Oo000 = '/guid/issue'
   O0O00Ooo = self . GetDefaultParams ( )
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   i1I11i1iI = OOOO [ 'guid' ]
   I1ii1Ii1 = OOOO [ 'guidtimestamp' ]
   if i1I11i1iI : I11III1II = True
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
   i1I11i1iI = 'none'
   I1ii1Ii1 = 'none'
  self . guid = i1I11i1iI
  self . guidtimestamp = I1ii1Ii1
  return I11III1II
 def GetGnList ( self , gn_str ) :
  I1i1IiI1 = [ ]
  try :
   Oo000 = '/cf/supermultisections/' + gn_str
   O0O00Ooo = self . GetDefaultParams ( )
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if not ( 'multisectionlist' in OOOO ) : return None
   OOO0o = OOOO [ 'multisectionlist' ]
   for O0oOO0 in OOO0o :
    O0ooo0O0oo0 = O0oOO0 [ 'title' ]
    if len ( O0ooo0O0oo0 ) == 0 : continue
    if O0ooo0O0oo0 == 'minor' : continue
    if re . search ( u'베너' , O0ooo0O0oo0 ) : continue
    O0ooo0O0oo0 = re . sub ( '\n|\!|\~|(@0@)|(@\^0@)' , '' , O0ooo0O0oo0 )
    O0ooo0O0oo0 = O0ooo0O0oo0 . lstrip ( '#' )
    for O0O in O0oOO0 [ 'eventlist' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , O0O ) :
      ooo0OO = { 'title' : unicode ( O0ooo0O0oo0 )
 , 'uicode' : re . sub ( r'uicode:' , '' , O0O )
 }
      I1i1IiI1 . append ( ooo0OO )
      break
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
  return I1i1IiI1
 def GetDeeplinkList ( self , gn_str , came_str , page_int , addinfoyn = False ) :
  iiIii = [ ]
  ooo0O = oOoO0o00OO0 = 1
  i1I1ii = 'quick'
  oOOo0 = oo00O00oO = iIiIIIi = ''
  ooo00OOOooO = False
  O00OOOoOoo0O = { }
  try :
   Oo000 = '/cf/deeplink/' + gn_str
   O0O00Ooo = self . GetDefaultParams ( )
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if not ( 'url' in OOOO ) : return None
   OooOOOOo = OOOO [ 'url' ]
   print OooOOOOo
   Oo000 = urlparse . urlsplit ( OooOOOOo ) . path
   I11i1ii1 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( OooOOOOo ) . query ) )
   I11i1ii1 [ 'came' ] = came_str
   I11i1ii1 [ 'limit' ] = str ( self . LIST_LIMIT )
   if 'contenttype' in I11i1ii1 : i1I1ii = I11i1ii1 [ 'contenttype' ]
   if came_str == 'movie' : I11i1ii1 [ 'mtype' ] = 'svod'
   if page_int != 1 :
    I11i1ii1 [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
    I11i1ii1 [ 'page' ] = str ( page_int )
   IiIIIiI1I1 = self . HTTPTAG + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if not ( 'celllist' in OOOO [ 'cell_toplist' ] ) : return iiIii , ooo00OOOooO
   oO00OOoO00 = OOOO [ 'cell_toplist' ] [ 'celllist' ]
   if ( i1I1ii == 'channel' and came_str == 'live' ) :
    if ( 'genre' in I11i1ii1 ) :
     o00oO0oOo00 = I11i1ii1 [ 'genre' ]
    else :
     o00oO0oOo00 = 'all'
    print "*epgcall*"
    O00OOOoOoo0O = self . GetEPGList ( o00oO0oOo00 )
   for O0oOO0 in oO00OOoO00 :
    O0ooO0Oo00o = ooO0oOOooOo0 = i1I1ii11i1Iii = ''
    O0ooO0Oo00o = O0oOO0 . get ( 'title_list' ) [ 0 ] . get ( 'text' )
    if ( len ( O0oOO0 . get ( 'title_list' ) ) > 1 ) :
     if ( O0oOO0 . get ( 'title_list' ) [ 1 ] . get ( 'text' ) . startswith ( '@' ) ) :
      for OO in O0oOO0 . get ( 'bottom_taglist' ) :
       if OO == 'playy' or OO == 'won' : ooO0oOOooOo0 = OO
     else :
      ooO0oOOooOo0 = O0oOO0 . get ( 'title_list' ) [ 1 ] . get ( 'text' )
      ooO0oOOooOo0 = re . sub ( r'(\$O\$)|(\&[a-z]{2}\;)' , '' , ooO0oOOooOo0 )
    if ( O0oOO0 . get ( 'thumbnail' ) != '' ) : i1I1ii11i1Iii = 'https://%s' % O0oOO0 . get ( 'thumbnail' )
    oOo0oO = O0oOO0 [ 'event_list' ] [ 1 ] . get ( 'url' )
    OOOO0oo0 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( oOo0oO ) . query ) )
    if re . search ( u'programid=\&' , oOo0oO ) and ( 'contentid' in OOOO0oo0 ) :
     oOOo0 = OOOO0oo0 [ 'contentid' ]
     oo00O00oO = 'direct'
    elif ( 'contentid' in OOOO0oo0 ) :
     oOOo0 = OOOO0oo0 [ 'contentid' ]
     oo00O00oO = 'contentid'
    elif ( 'programid' in OOOO0oo0 ) :
     oOOo0 = OOOO0oo0 [ 'programid' ]
     oo00O00oO = 'programid'
     i1I1ii = 'program'
    elif ( 'channelid' in OOOO0oo0 ) :
     oOOo0 = OOOO0oo0 [ 'channelid' ]
     oo00O00oO = 'channelid'
     if oOOo0 in O00OOOoOoo0O :
      iIiIIIi = O00OOOoOoo0O [ oOOo0 ]
     else :
      iIiIIIi = ''
    elif ( 'movieid' in OOOO0oo0 ) :
     oOOo0 = OOOO0oo0 [ 'movieid' ]
     oo00O00oO = 'movieid'
     i1I1ii = 'movie'
    else :
     oOOo0 = '-'
     oo00O00oO = '-'
    oO = { }
    oO [ 'mpaa' ] = O0oOO0 . get ( 'age' )
    try :
     if ( 'channelid' in OOOO0oo0 ) :
      oO [ 'mediatype' ] = 'video'
      oO [ 'title' ] = '%s < %s >' % ( unicode ( O0ooO0Oo00o ) , unicode ( ooO0oOOooOo0 ) )
      oO [ 'tvshowtitle' ] = unicode ( ooO0oOOooOo0 )
      oO [ 'studio' ] = unicode ( O0ooO0Oo00o )
     elif ( 'movieid' in OOOO0oo0 ) :
      oO [ 'mediatype' ] = 'movie'
      oO [ 'title' ] = unicode ( title_list )
     else :
      oO [ 'mediatype' ] = 'episode'
      oO [ 'title' ] = unicode ( title_list )
    except :
     None
    ooo0OO = { 'title' : unicode ( O0ooO0Oo00o )
 , 'subtitle' : unicode ( ooO0oOOooOo0 )
 , 'thumbnail' : i1I1ii11i1Iii
 , 'uicode' : i1I1ii
 , 'contentid' : oOOo0
 , 'contentidType' : oo00O00oO
 , 'viewage' : O0oOO0 . get ( 'age' )
 , 'channelepg' : iIiIIIi
 , 'info' : oO
 }
    iiIii . append ( ooo0OO )
   ooo0O = int ( OOOO [ 'cell_toplist' ] [ 'pagecount' ] )
   if OOOO [ 'cell_toplist' ] [ 'count' ] : oOoO0o00OO0 = int ( OOOO [ 'cell_toplist' ] [ 'count' ] )
   else : oOoO0o00OO0 = self . LIST_LIMIT
   ooo00OOOooO = ooo0O > oOoO0o00OO0
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
  try :
   if iiIii [ 0 ] . get ( 'contentidType' ) == 'movieid' and addinfoyn == True :
    Oo0O0oooo = [ ]
    I111iI = { }
    for O0oO in iiIii : Oo0O0oooo . append ( O0oO . get ( 'contentid' ) )
    I111iI = self . GetMovieInfoList ( Oo0O0oooo )
    for O0O00o0OOO0 in range ( len ( iiIii ) ) :
     iiIii [ O0O00o0OOO0 ] [ 'info' ] = I111iI . get ( iiIii [ O0O00o0OOO0 ] [ 'contentid' ] )
  except :
   None
  return ( iiIii , ooo00OOOooO )
 def GetEpisodeList ( self , contentid , contenttype , contentidType , page_int , orderby = 'desc' ) :
  OOOoOo = [ ]
  ooo0O = oOoO0o00OO0 = 1
  ooo00OOOooO = False
  if orderby == 'desc' :
   orderby = 'new'
  else :
   orderby = 'old'
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   if contentidType == 'contentid' :
    Oo000 = '/cf/vod/contents/' + contentid
    IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
    II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
    OOOO = json . loads ( II1Iiii1111i )
    if not ( 'programid' in OOOO ) : return None
    O00oO000O0O = OOOO [ 'programid' ]
   else :
    O00oO000O0O = contentid
   Oo000 = '/vod/programs-contents/' + O00oO000O0O
   I11i1ii1 = { 'limit' : self . EP_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . EP_LIMIT )
 , 'orderby' : orderby
   }
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if not ( 'list' in OOOO ) : return None
   ooOoO00 = OOOO [ 'list' ]
   for O0oOO0 in ooOoO00 :
    II11Ii1iI1iII = O0oOO0 . get ( 'programtitle' )
    Oo0o00OO0000 = '%s회, %s(%s)' % ( O0oOO0 . get ( 'episodenumber' ) , O0oOO0 . get ( 'releasedate' ) , O0oOO0 . get ( 'releaseweekday' ) )
    if ( O0oOO0 . get ( 'image' ) != '' ) : I1i = 'https://%s' % O0oOO0 . get ( 'image' )
    i11I = unicode ( O0oOO0 . get ( 'synopsis' ) )
    i11I = re . sub ( u'(\<[a-zA-Z]{1,2}\>)|(\<\/[a-zA-Z]{1,2}\>)' , '' , i11I )
    oO = { }
    oO [ 'title' ] = unicode ( II11Ii1iI1iII )
    oO [ 'mediatype' ] = 'episode'
    oO [ 'mpaa' ] = O0oOO0 . get ( 'targetage' )
    try :
     if 'episodenumber' in O0oOO0 : oO [ 'episode' ] = O0oOO0 . get ( 'episodenumber' )
     if 'releasedate' in O0oOO0 : oO [ 'year' ] = int ( O0oOO0 . get ( 'releasedate' ) [ : 4 ] )
     if 'releasedate' in O0oOO0 : oO [ 'aired' ] = O0oOO0 . get ( 'releasedate' )
     if 'playtime' in O0oOO0 : oO [ 'duration' ] = O0oOO0 . get ( 'playtime' )
     if 'episodeactors' in O0oOO0 :
      if O0oOO0 . get ( 'episodeactors' ) != '' : oO [ 'cast' ] = O0oOO0 . get ( 'episodeactors' ) . split ( ',' )
    except :
     None
    iiii1 = { 'title' : unicode ( II11Ii1iI1iII )
 , 'subtitle' : unicode ( Oo0o00OO0000 )
 , 'thumbnail' : I1i
 , 'uicode' : contenttype
 , 'contentid' : O0oOO0 . get ( 'contentid' )
 , 'programid' : O0oOO0 . get ( 'programid' )
 , 'synopsis' : i11I
 , 'viewage' : O0oOO0 . get ( 'targetage' )
 , 'info' : oO
    }
    OOOoOo . append ( iiii1 )
   ooo0O = int ( OOOO [ 'pagecount' ] )
   if OOOO [ 'count' ] : oOoO0o00OO0 = int ( OOOO [ 'count' ] )
   else : oOoO0o00OO0 = self . EP_LIMIT
   ooo00OOOooO = ooo0O > oOoO0o00OO0
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
  return ( OOOoOo , ooo00OOOooO )
 def GetMyviewList ( self , contenttype , page_int , addinfoyn = False ) :
  ooOOOooO = [ ]
  ooo0O = oOoO0o00OO0 = 1
  ooo00OOOooO = False
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   Oo000 = '/myview/contents'
   I11i1ii1 = { 'contenttype' : contenttype
 , 'limit' : self . MV_LIMIT
 , 'offset' : str ( ( page_int - 1 ) * self . MV_LIMIT )
 , 'orderby' : 'new'
 }
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if not ( 'list' in OOOO [ 0 ] ) : return None
   ii = OOOO [ 0 ] [ 'list' ]
   for O0oOO0 in ii :
    oO = { }
    if contenttype == 'vod' :
     II11Ii1iI1iII = O0oOO0 . get ( 'programtitle' )
     Oo0o00OO0000 = '%s회, %s' % ( O0oOO0 . get ( 'episodenumber' ) , O0oOO0 . get ( 'releasedate' ) )
     oOOo0 = O0oOO0 . get ( 'contentid' )
     O00oO000O0O = O0oOO0 . get ( 'programid' )
     oO [ 'title' ] = unicode ( II11Ii1iI1iII )
     oO [ 'mediatype' ] = 'episode'
     oO [ 'mpaa' ] = O0oOO0 . get ( 'targetage' )
     try :
      oO [ 'studio' ] = O0oOO0 . get ( 'channelname' )
     except :
      None
     try :
      if 'releasedate' in O0oOO0 : oO [ 'year' ] = int ( O0oOO0 . get ( 'releasedate' ) [ : 4 ] )
      if 'releasedate' in O0oOO0 : oO [ 'aired' ] = O0oOO0 . get ( 'releasedate' )
     except :
      None
    else :
     II11Ii1iI1iII = O0oOO0 . get ( 'title' )
     Oo0o00OO0000 = ''
     oOOo0 = O00oO000O0O = O0oOO0 . get ( 'movieid' )
     oO [ 'title' ] = unicode ( II11Ii1iI1iII )
     oO [ 'mediatype' ] = 'movie'
     oO [ 'mpaa' ] = O0oOO0 . get ( 'targetage' )
     try :
      if 'releasedate' in O0oOO0 : oO [ 'year' ] = int ( O0oOO0 . get ( 'releasedate' ) [ : 4 ] )
      if 'releasedate' in O0oOO0 : oO [ 'aired' ] = O0oOO0 . get ( 'releasedate' )
     except :
      None
    if ( O0oOO0 . get ( 'image' ) != '' ) : I1i = 'https://%s' % O0oOO0 . get ( 'image' )
    IiIi1I1 = { 'title' : unicode ( II11Ii1iI1iII )
 , 'subtitle' : unicode ( Oo0o00OO0000 )
 , 'thumbnail' : I1i
 , 'uicode' : contenttype
 , 'contentid' : oOOo0
 , 'programid' : O00oO000O0O
 , 'viewage' : O0oOO0 . get ( 'targetage' )
 , 'info' : oO
 }
    ooOOOooO . append ( IiIi1I1 )
   ooo0O = int ( OOOO [ 0 ] [ 'pagecount' ] )
   if OOOO [ 0 ] [ 'count' ] : oOoO0o00OO0 = int ( OOOO [ 0 ] [ 'count' ] )
   else : oOoO0o00OO0 = self . MV_LIMIT
   ooo00OOOooO = ooo0O > oOoO0o00OO0
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
  try :
   if contenttype == 'movie' and addinfoyn == True :
    Oo0O0oooo = [ ]
    I111iI = { }
    for O0oO in ooOOOooO : Oo0O0oooo . append ( O0oO . get ( 'contentid' ) )
    I111iI = self . GetMovieInfoList ( Oo0O0oooo )
    for O0O00o0OOO0 in range ( len ( ooOOOooO ) ) :
     ooOOOooO [ O0O00o0OOO0 ] [ 'info' ] = I111iI . get ( ooOOOooO [ O0O00o0OOO0 ] [ 'contentid' ] )
  except :
   None
  return ooOOOooO , ooo00OOOooO
 def GetSearchList ( self , search_key , genre , page_int , exclusion21 = False , addinfoyn = False ) :
  iIiIiIiI = [ ]
  ooo0O = oOoO0o00OO0 = 1
  ooo00OOOooO = False
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   Oo000 = '/cf/search/list.js'
   I11i1ii1 = { 'type' : 'program' if genre == 'vod' else 'movie'
 , 'keyword' : search_key
 , 'offset' : str ( ( page_int - 1 ) * self . LIST_LIMIT )
 , 'limit' : self . LIST_LIMIT
   , 'orderby' : 'score'
 , 'isplayymovie' : 'y'
 }
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if not ( 'celllist' in OOOO [ 'cell_toplist' ] ) : return iIiIiIiI , ooo00OOOooO
   IIiI1Ii = OOOO [ 'cell_toplist' ] [ 'celllist' ]
   for O0oOO0 in IIiI1Ii :
    oO = { }
    II11Ii1iI1iII = O0oOO0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if ( O0oOO0 . get ( 'thumbnail' ) != '' ) : I1i = 'https://%s' % O0oOO0 . get ( 'thumbnail' )
    for O0O in O0oOO0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , O0O ) :
      if genre == 'vod' :
       oOOo0 = ''
       O00oO000O0O = re . sub ( r'uicode:' , '' , O0O )
       oO [ 'mediatype' ] = 'episode'
      else :
       oOOo0 = re . sub ( r'uicode:' , '' , O0O )
       O00oO000O0O = ''
       if O0oOO0 . get ( 'bottom_taglist' ) [ 0 ] == 'playy' :
        II11Ii1iI1iII += ' [playy]'
       oO [ 'mediatype' ] = 'movie'
      oO [ 'title' ] = unicode ( O0oOO0 [ 'title_list' ] [ 0 ] [ 'text' ] )
      oO [ 'mpaa' ] = O0oOO0 . get ( 'age' )
      IiIi1I1 = { 'title' : unicode ( II11Ii1iI1iII )
 , 'thumbnail' : I1i
 , 'uicode' : genre
 , 'contentid' : oOOo0
 , 'programid' : O00oO000O0O
 , 'viewage' : O0oOO0 . get ( 'age' )
 , 'info' : oO
 }
    if exclusion21 == False or O0oOO0 . get ( 'age' ) != '21' :
     iIiIiIiI . append ( IiIi1I1 )
   ooo0O = int ( OOOO [ 'cell_toplist' ] [ 'pagecount' ] )
   if OOOO [ 'cell_toplist' ] [ 'count' ] : oOoO0o00OO0 = int ( OOOO [ 'cell_toplist' ] [ 'count' ] )
   else : oOoO0o00OO0 = self . LIST_LIMIT
   ooo00OOOooO = ooo0O > oOoO0o00OO0
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
  try :
   if genre == 'movie' and addinfoyn == True :
    Oo0O0oooo = [ ]
    I111iI = { }
    for O0oO in iIiIiIiI : Oo0O0oooo . append ( O0oO . get ( 'contentid' ) )
    I111iI = self . GetMovieInfoList ( Oo0O0oooo )
    for O0O00o0OOO0 in range ( len ( iIiIiIiI ) ) :
     iIiIiIiI [ O0O00o0OOO0 ] [ 'info' ] = I111iI . get ( iIiIiIiI [ O0O00o0OOO0 ] [ 'contentid' ] )
  except :
   None
  return iIiIiIiI , ooo00OOOooO
 def GetGenreGroup ( self , maintype , subtype , orderby , ordernm , exclusion21 = False ) :
  iiIi1i = [ ]
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   Oo000 = '/cf/filters'
   I11i1ii1 = { 'type' : maintype }
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if not ( maintype in OOOO ) : return None
   iIi1Ii1i1iI = OOOO [ maintype ]
   if subtype == '-' :
    for O0oOO0 in iIi1Ii1i1iI :
     ii111IiiI1 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( O0oOO0 . get ( 'url' ) ) . query ) )
     IiIi1I1 = { 'title' : O0oOO0 . get ( 'text' )
 , 'genre' : O0oOO0 . get ( 'id' )
 , 'subgenre' : '-'
 , 'adult' : O0oOO0 . get ( 'adult' )
 , 'broadcastid' : ii111IiiI1 . get ( 'broadcastid' )
 , 'contenttype' : ii111IiiI1 . get ( 'contenttype' )
 , 'uiparent' : ii111IiiI1 . get ( 'uiparent' )
 , 'uirank' : ii111IiiI1 . get ( 'uirank' )
 , 'uitype' : ii111IiiI1 . get ( 'uitype' )
 , 'orderby' : orderby
 , 'ordernm' : ordernm
 }
     if exclusion21 == False or IiIi1I1 . get ( 'adult' ) == 'n' :
      iiIi1i . append ( IiIi1I1 )
   else :
    for O0oOO0 in iIi1Ii1i1iI :
     if O0oOO0 . get ( 'id' ) == subtype :
      for II in O0oOO0 [ 'sublist' ] :
       ii111IiiI1 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( II . get ( 'url' ) ) . query ) )
       IiIi1I1 = { 'title' : II . get ( 'text' )
 , 'genre' : subtype
 , 'subgenre' : II . get ( 'id' )
 , 'adult' : II . get ( 'adult' )
 , 'broadcastid' : ii111IiiI1 . get ( 'broadcastid' )
 , 'contenttype' : ii111IiiI1 . get ( 'contenttype' )
 , 'uiparent' : ii111IiiI1 . get ( 'uiparent' )
 , 'uirank' : ii111IiiI1 . get ( 'uirank' )
 , 'uitype' : ii111IiiI1 . get ( 'uitype' )
 , 'orderby' : orderby
 , 'ordernm' : ordernm
 }
       iiIi1i . append ( IiIi1I1 )
      break
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
  return iiIi1i
 def GetGenreGroup_sub ( self , in_params ) :
  iiIi1i = [ ]
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   Oo000 = '/cf/vod/newcontents'
   I11i1ii1 = { 'WeekDay' : 'all'
 , 'limit' : '20'
 , 'offset' : '0'

   , 'orderby' : in_params . get ( 'orderby' )
 , 'adult' : in_params . get ( 'adult' )
 , 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )
 }
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if not ( 'filter_item_list' in OOOO [ 'filter' ] [ 'filterlist' ] [ 1 ] ) : return None
   iIi1Ii1i1iI = OOOO [ 'filter' ] [ 'filterlist' ] [ 1 ] [ 'filter_item_list' ]
   for O0oOO0 in iIi1Ii1i1iI :
    IiIi1I1 = { 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )

 , 'adult' : O0oOO0 . get ( 'adult' )
 , 'title' : O0oOO0 . get ( 'title' )
 , 'subgenre' : O0oOO0 . get ( 'api_parameters' ) [ O0oOO0 . get ( 'api_parameters' ) . find ( '=' ) + 1 : ]
 , 'orderby' : in_params . get ( 'orderby' )
 }
    iiIi1i . append ( IiIi1I1 )
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
  return iiIi1i
 def GetGenreList ( self , genre , in_params , page_int , addinfoyn = False ) :
  iiIi1i = [ ]
  ooo0O = oOoO0o00OO0 = 1
  ooo00OOOooO = False
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   I11i1ii1 = { 'WeekDay' : 'all'
 , 'adult' : in_params . get ( 'adult' )
 , 'broadcastid' : in_params . get ( 'broadcastid' )
 , 'contenttype' : in_params . get ( 'contenttype' )
 , 'genre' : in_params . get ( 'genre' )

   , 'orderby' : in_params . get ( 'orderby' )
 , 'uiparent' : in_params . get ( 'uiparent' )
 , 'uirank' : in_params . get ( 'uirank' )
 , 'uitype' : in_params . get ( 'uitype' )
 }
   if genre == 'vodgenre' :
    Oo000 = '/cf/vod/newcontents'
    if in_params . get ( 'subgenre' ) != '-' :
     I11i1ii1 [ 'subgenre' ] = in_params . get ( 'subgenre' )
   else :
    Oo000 = '/cf/movie/contents'
    I11i1ii1 [ 'price' ] = 'all'
    I11i1ii1 [ 'sptheme' ] = 'svod'
   I11i1ii1 [ 'limit' ] = self . LIST_LIMIT
   I11i1ii1 [ 'offset' ] = str ( ( page_int - 1 ) * self . LIST_LIMIT )
   I11i1ii1 [ 'page' ] = str ( page_int )
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   if not ( 'celllist' in OOOO [ 'cell_toplist' ] ) : return None
   iIi1Ii1i1iI = OOOO [ 'cell_toplist' ] [ 'celllist' ]
   for O0oOO0 in iIi1Ii1i1iI :
    oO = { }
    II11Ii1iI1iII = I1i = ''
    II11Ii1iI1iII = O0oOO0 [ 'title_list' ] [ 0 ] [ 'text' ]
    if ( O0oOO0 . get ( 'thumbnail' ) != '' ) : I1i = 'https://%s' % O0oOO0 . get ( 'thumbnail' )
    for O0O in O0oOO0 [ 'event_list' ] [ 0 ] [ 'bodylist' ] :
     if re . search ( r'uicode:' , O0O ) :
      oO [ 'title' ] = unicode ( II11Ii1iI1iII )
      oO [ 'mpaa' ] = O0oOO0 . get ( 'age' )
      if genre == 'moviegenre_svod' :
       oO [ 'mediatype' ] = 'movie'
      else :
       oO [ 'mediatype' ] = 'episode'
      IiIi1I1 = { 'title' : unicode ( II11Ii1iI1iII )
 , 'uicode' : re . sub ( r'uicode:' , '' , O0O )
 , 'thumbnail' : I1i
 , 'viewage' : O0oOO0 . get ( 'age' )
 , 'info' : oO
 }
    iiIi1i . append ( IiIi1I1 )
   ooo0O = int ( OOOO [ 'cell_toplist' ] [ 'pagecount' ] )
   if OOOO [ 'cell_toplist' ] [ 'count' ] : oOoO0o00OO0 = int ( OOOO [ 'cell_toplist' ] [ 'count' ] )
   else : oOoO0o00OO0 = self . LIST_LIMIT
   ooo00OOOooO = ooo0O > oOoO0o00OO0
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
  try :
   if genre == 'moviegenre_svod' and addinfoyn == True :
    Oo0O0oooo = [ ]
    I111iI = { }
    for O0oO in iiIi1i : Oo0O0oooo . append ( O0oO . get ( 'uicode' ) )
    I111iI = self . GetMovieInfoList ( Oo0O0oooo )
    for O0O00o0OOO0 in range ( len ( iiIi1i ) ) :
     iiIi1i [ O0O00o0OOO0 ] [ 'info' ] = I111iI . get ( iiIi1i [ O0O00o0OOO0 ] [ 'uicode' ] )
  except :
   None
  return iiIi1i , ooo00OOOooO
 def GetEPGList ( self , genre ) :
  o0 = { }
  try :
   import datetime
   I1iIIIi1 = datetime . datetime . now ( )
   if genre == 'all' :
    Iii = I1iIIIi1 + datetime . timedelta ( hours = 2 )
   else :
    Iii = I1iIIIi1 + datetime . timedelta ( hours = 3 )
   O0O00Ooo = self . GetDefaultParams ( )
   I11i1ii1 = { 'limit' : '100'
 , 'offset' : '0'
 , 'genre' : genre
 , 'startdatetime' : I1iIIIi1 . strftime ( '%Y-%m-%d %H:%M' )
 , 'enddatetime' : Iii . strftime ( '%Y-%m-%d %H:%M' )
 }
   Oo000 = '/live/epgs'
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( I11i1ii1 ) + '&' + urllib . urlencode ( O0O00Ooo )
   II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
   OOOO = json . loads ( II1Iiii1111i )
   iIiii = OOOO [ 'list' ]
   for O0oOO0 in iIiii :
    I111 = ''
    for IiIIiiI11III in O0oOO0 [ 'list' ] :
     if I111 : I111 += '\n'
     I111 += IiIIiiI11III [ 'title' ] + '\n'
     I111 += ' [%s ~ %s]' % ( IiIIiiI11III [ 'starttime' ] [ - 5 : ] , IiIIiiI11III [ 'endtime' ] [ - 5 : ] ) + '\n'
    o0 [ O0oOO0 [ 'channelid' ] ] = unicode ( I111 )
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
  return o0
 def GetMovieInfoList ( self , movie_list ) :
  oOoOOo000oOoO0 = { }
  try :
   O0O00Ooo = self . GetDefaultParams ( )
   Oo000 = self . API_DOMAIN + '/movie/contents/'
   for O0oO in movie_list :
    IiIIIiI1I1 = Oo000 + O0oO
    II1Iiii1111i = self . SESSION . Request ( IiIIIiI1I1 )
    OOOO = json . loads ( II1Iiii1111i )
    oO = { }
    oO [ 'mediatype' ] = 'movie'
    o00 = [ ]
    for OO00O0oOO in OOOO [ 'actors' ] [ 'list' ] : o00 . append ( OO00O0oOO . get ( 'text' ) )
    if o00 [ 0 ] != '' : oO [ 'cast' ] = o00
    Ooooo00o0OoO = [ ]
    for oooo0O0O0o0 in OOOO [ 'directors' ] [ 'list' ] : Ooooo00o0OoO . append ( oooo0O0O0o0 . get ( 'text' ) )
    if Ooooo00o0OoO [ 0 ] != '' : oO [ 'director' ] = Ooooo00o0OoO
    iiIi1i = [ ]
    for OOoOoo0 in OOOO [ 'genre' ] [ 'list' ] : iiIi1i . append ( OOoOoo0 . get ( 'text' ) )
    if iiIi1i [ 0 ] != '' : oO [ 'genre' ] = iiIi1i
    if OOOO . get ( 'releasedate' ) != '' :
     oO [ 'year' ] = OOOO [ 'releasedate' ] [ : 4 ]
     oO [ 'aired' ] = OOOO [ 'releasedate' ]
    oO [ 'country' ] = OOOO [ 'country' ]
    oO [ 'duration' ] = OOOO [ 'playtime' ]
    oO [ 'title' ] = OOOO [ 'title' ]
    oO [ 'mpaa' ] = OOOO [ 'targetage' ]
    oO [ 'plot' ] = OOOO [ 'synopsis' ]
    oOoOOo000oOoO0 [ O0oO ] = oO
  except Exception as oO0ooO0OoOOOO :
   return { }
  return oOoOOo000oOoO0
 def GetStreamingURL ( self , contentid , contenttype , quality_int ) :
  O0iIi1IiII = I1iooo = ii1iiIi1 = i111iiI1ii = ''
  IIiii = [ ]
  try :
   if contenttype == 'channel' :
    Oo000 = '/live/channels/' + contentid
    II1i1i1iII1 = 'live'
   elif contenttype == 'movie' :
    Oo000 = '/cf/movie/contents/' + contentid
    II1i1i1iII1 = 'movie'
   else :
    Oo000 = '/cf/vod/contents/' + contentid
    II1i1i1iII1 = 'vod'
   O0O00Ooo = self . GetDefaultParams ( )
   IiIIIiI1I1 = self . MakeServiceUrl ( Oo000 , O0O00Ooo )
   OOOO = self . SESSION . Request2 ( self . API_DOMAIN + Oo000 , params = O0O00Ooo )
   I11 = OOOO [ 'qualities' ] [ 'list' ]
   if I11 == None : return ( O0iIi1IiII , I1iooo , ii1iiIi1 , i111iiI1ii )
   IioO0O = 'hls'
   if 'drms' in OOOO :
    if OOOO [ 'drms' ] :
     IioO0O = 'dash'
   if 'type' in OOOO :
    if OOOO [ 'type' ] == 'onair' :
     II1i1i1iII1 = 'onairvod'
   for IiIi1II11i in I11 :
    IIiii . append ( int ( IiIi1II11i . get ( 'id' ) . rstrip ( 'p' ) ) )
  except Exception as oO0ooO0OoOOOO :
   return ( O0iIi1IiII , I1iooo , ii1iiIi1 , i111iiI1ii )
  try :
   O0OoOoO00O = self . CheckQuality ( quality_int , IIiii )
   Oo000 = '/streaming'
   I11i1ii1 = { 'contentid' : contentid
 , 'contenttype' : II1i1i1iII1
 , 'action' : IioO0O
 , 'quality' : str ( O0OoOoO00O ) + 'p'
 , 'deviceModelId' : 'Windows 10'
 , 'guid' : self . GetGUID ( guidType = 2 )
 , 'lastplayid' : self . guid
 , 'authtype' : 'cookie'
 , 'isabr' : 'y'
 , 'ishevc' : 'n'
 }
   IiIIIiI1I1 = self . API_DOMAIN + Oo000 + '?' + urllib . urlencode ( O0O00Ooo ) + '&' + urllib . urlencode ( I11i1ii1 )
   I11i1ii1 . update ( O0O00Ooo )
   OOOO = self . SESSION . Request2 ( self . API_DOMAIN + Oo000 , params = I11i1ii1 )
   O0iIi1IiII = OOOO [ 'playurl' ]
   if O0iIi1IiII == None : return None
   I1iooo = OOOO [ 'awscookie' ]
   ii1iiIi1 = OOOO [ 'drm' ]
   if 'previewmsg' in OOOO [ 'preview' ] : i111iiI1ii = OOOO [ 'preview' ] [ 'previewmsg' ]
  except Exception as oO0ooO0OoOOOO :
   print ( oO0ooO0OoOOOO )
  O0iIi1IiII = O0iIi1IiII . replace ( 'pooq.co.kr' , 'wavve.com' )
  return ( O0iIi1IiII , I1iooo , ii1iiIi1 , i111iiI1ii )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
