from __future__ import annotations
# ^ this thing should fix problem for python3.9 and lower(?)

from os import urandom
from time import timezone
from binascii import hexlify
from base64 import b64encode
from uuid import UUID, uuid4
from json import loads, dumps
from typing import BinaryIO, Union
from time import time as timestamp

from .client import Client
from .lib import exceptions, headers, objects
from .lib.helpers import gen_deviceId, json_minify

class VCHeaders:
    def __init__(self, data = None):
        vc_headers = {
            "Accept-Language": "en-US",
            "Content-Type": "application/json",
            "User-Agent": "Amino/45725 CFNetwork/1126 Darwin/19.5.0",  # Closest server (this one for me)
            "Host": "rt.applovin.com",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "Keep-Alive",
            "Accept": "*/*"
        }

        if data: vc_headers["Content-Length"] = str(len(data))
        self.vc_headers = vc_headers


class SubClient(Client):
    def __init__(
        self, mainClient: Client,
        comId: str = None, aminoId: str = None, *,
        deviceId: str = None, autoDevice: bool | None = None, proxies: dict = None
    ):
        Client.__init__(
            self, deviceId=deviceId, proxies=proxies,
            autoDevice=autoDevice or mainClient.autoDevice, userAgent=mainClient.user_agent,
            http2_enabled=mainClient.http2_enabled,
            own_timeout=mainClient.timeout_settings,
            socket_enabled=False
        )
        self.vc_connect = False
        self.sid = mainClient.sid
        self.device_id = mainClient.device_id
        self.user_agent = mainClient.user_agent
        self.profile = mainClient.profile
        self.userId = mainClient.userId

        if comId is not None:
            self.comId = comId
            self.community: objects.Community = self.get_community_info(comId)

        if aminoId is not None:
            link = "http://aminoapps.com/c/"
            self.comId = self.get_from_code(link + aminoId).comId
            self.community: objects.Community = self.get_community_info(self.comId)

        if comId is None and aminoId is None: raise exceptions.NoCommunity()

        try: self.profile: objects.UserProfile = self.get_user_info(userId=self.profile.userId)
        except AttributeError: raise exceptions.FailedLogin()
        except exceptions.UserUnavailable: pass

    def additional_headers(self, data: str = None, content_type: str = None):
        return headers.additionals(
            data=data,
            content_type=content_type,
            user_agent=self.user_agent,
            sid=self.sid,
            auid=self.userId,
            deviceId=gen_deviceId() if self.autoDevice else self.device_id
        )

    def get_invite_codes(self, status: str = "normal", start: int = 0, size: int = 25) -> objects.InviteCodeList:
        response = self.session.get(f"/g/s-x{self.comId}/community/invitation?status={status}&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.InviteCodeList(response.json()["communityInvitationList"]).InviteCodeList

    def generate_invite_code(self, duration: int = 0, force: bool = True) -> objects.InviteCode:
        data = dumps({
            "duration": duration,
            "force": force,
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/g/s-x{self.comId}/community/invitation", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.InviteCode(response.json()["communityInvitation"]).InviteCode

    def get_vip_users(self) -> objects.UserProfileList:
        response = self.session.get(f"/{self.comId}/s/influencer", headers=self.additional_headers())
        if response.status_code != 200:
            return exceptions.CheckException(response)
        else: return objects.UserProfileList(response.json()["userProfileList"]).UserProfileList

    def delete_invite_code(self, inviteId: str) -> int:
        response = self.session.delete(f"/g/s-x{self.comId}/community/invitation/{inviteId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def post_blog(self, title: str, content: str, imageList: list = None, captionList: list = None, categoriesList: list = None, backgroundColor: str = None, fansOnly: bool = False, extensions: dict = None, crash: bool = False) -> int:
        mediaList = []

        if captionList is not None:
            for image, caption in zip(imageList, captionList):
                mediaList.append([100, self.upload_media(image, "image"), caption])

        else:
            if imageList is not None:
                for image in imageList:
                    mediaList.append([100, self.upload_media(image, "image"), None])

        data = {
            "address": None,
            "content": content,
            "title": title,
            "mediaList": mediaList,
            "extensions": extensions,
            "latitude": 0,
            "longitude": 0,
            "eventSource": "GlobalComposeMenu",
            "timestamp": int(timestamp() * 1000)
        }

        if fansOnly: data["extensions"] = {"fansOnly": fansOnly}
        if backgroundColor: data["extensions"] = {"style": {"backgroundColor": backgroundColor}}
        if categoriesList: data["taggedBlogCategoryIdList"] = categoriesList

        data = dumps(data)
        
        response = self.session.post(f"/x{self.comId}/s/blog", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def post_wiki(self, title: str, content: str, icon: str = None, imageList: list = None, keywords: str = None, backgroundColor: str = None, fansOnly: bool = False) -> int:
        mediaList = []

        for image in imageList:
            mediaList.append([100, self.upload_media(image, "image"), None])

        data = {
            "label": title,
            "content": content,
            "mediaList": mediaList,
            "eventSource": "GlobalComposeMenu",
            "timestamp": int(timestamp() * 1000)
        }

        if icon: data["icon"] = icon
        if keywords: data["keywords"] = keywords
        if fansOnly: data["extensions"] = {"fansOnly": fansOnly}
        if backgroundColor: data["extensions"] = {"style": {"backgroundColor": backgroundColor}}
        data = dumps(data)
        
        response = self.session.post(f"/x{self.comId}/s/item", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def edit_blog(self, blogId: str, title: str = None, content: str = None, imageList: list = None, categoriesList: list = None, backgroundColor: str = None, fansOnly: bool = False) -> int:
        mediaList = []

        for image in imageList:
            mediaList.append([100, self.upload_media(image, "image"), None])

        data = {
            "address": None,
            "mediaList": mediaList,
            "latitude": 0,
            "longitude": 0,
            "eventSource": "PostDetailView",
            "timestamp": int(timestamp() * 1000)
        }

        if title: data["title"] = title
        if content: data["content"] = content
        if fansOnly: data["extensions"] = {"fansOnly": fansOnly}
        if backgroundColor: data["extensions"] = {"style": {"backgroundColor": backgroundColor}}
        if categoriesList: data["taggedBlogCategoryIdList"] = categoriesList
        data = dumps(data)
        
        response = self.session.post(f"/x{self.comId}/s/blog/{blogId}", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def delete_blog(self, blogId: str) -> int:
        response = self.session.delete(f"/x{self.comId}/s/blog/{blogId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def delete_wiki(self, wikiId: str) -> int:
        response = self.session.delete(f"/x{self.comId}/s/item/{wikiId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def repost_blog(self, content: str = None, blogId: str = None, wikiId: str = None) -> int:
        if blogId is not None: refObjectId, refObjectType = blogId, 1
        elif wikiId is not None: refObjectId, refObjectType = wikiId, 2
        else: raise exceptions.SpecifyType()

        data = dumps({
            "content": content,
            "refObjectId": refObjectId,
            "refObjectType": refObjectType,
            "type": 2,
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/blog", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def check_in(self, tz: int = -timezone // 1000) -> int:
        data = dumps({
            "timezone": tz,
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/check-in", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def repair_check_in(self, method: int = 0) -> int:
        data = {"timestamp": int(timestamp() * 1000)}
        if method == 0: data["repairMethod"] = "1"  # Coins
        if method == 1: data["repairMethod"] = "2"  # Amino+

        data = dumps(data)
        
        response = self.session.post(f"/x{self.comId}/s/check-in/repair", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def lottery(self, tz: int = -timezone // 1000) -> objects.LotteryLog:
        data = dumps({
            "timezone": tz,
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/check-in/lottery", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.LotteryLog(response.json()["lotteryLog"]).LotteryLog

    def edit_profile(self, nickname: str = None, content: str = None, icon: BinaryIO = None, chatRequestPrivilege: str = None, imageList: list = None, captionList: list = None, backgroundImage: str = None, backgroundColor: str = None, titles: list = None, colors: list = None, defaultBubbleId: str = None) -> int:
        mediaList = []

        data = {"timestamp": int(timestamp() * 1000)}

        if captionList is not None:
            for image, caption in zip(imageList, captionList):
                mediaList.append([100, self.upload_media(image, "image"), caption])

        else:
            if imageList is not None:
                for image in imageList:
                    mediaList.append([100, self.upload_media(image, "image"), None])

        if imageList is not None or captionList is not None:
            data["mediaList"] = mediaList

        if nickname: data["nickname"] = nickname
        if icon: data["icon"] = self.upload_media(icon, "image")
        if content: data["content"] = content

        if chatRequestPrivilege: data["extensions"] = {"privilegeOfChatInviteRequest": chatRequestPrivilege}
        if backgroundImage: data["extensions"] = {"style": {"backgroundMediaList": [[100, backgroundImage, None, None, None]]}}
        if backgroundColor: data["extensions"] = {"style": {"backgroundColor": backgroundColor}}
        if defaultBubbleId: data["extensions"] = {"defaultBubbleId": defaultBubbleId}

        if titles or colors:
            tlt = []
            for titles, colors in zip(titles, colors):
                tlt.append({"title": titles, "color": colors})

            data["extensions"] = {"customTitles": tlt}

        data = dumps(data)
        
        response = self.session.post(f"/x{self.comId}/s/user-profile/{self.profile.userId}", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def vote_poll(self, blogId: str, optionId: str) -> int:
        data = dumps({
            "value": 1,
            "eventSource": "PostDetailView",
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/blog/{blogId}/poll/option/{optionId}/vote", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def comment(self, message: str, userId: str = None, blogId: str = None, wikiId: str = None, replyTo: str = None, isGuest: bool = False) -> int:
        data = {
            "content": message,
            "stickerId": None,
            "type": 0,
            "timestamp": int(timestamp() * 1000)
        }

        if replyTo: data["respondTo"] = replyTo

        if isGuest: comType = "g-comment"
        else: comType = "comment"

        if userId:
            data["eventSource"] = "UserProfileView"
            data = dumps(data)
            
            response = self.session.post(f"/x{self.comId}/s/user-profile/{userId}/{comType}", headers=self.additional_headers(data=data), data=data)

        elif blogId:
            data["eventSource"] = "PostDetailView"
            data = dumps(data)
            
            response = self.session.post(f"/x{self.comId}/s/blog/{blogId}/{comType}", headers=self.additional_headers(data=data), data=data)

        elif wikiId:
            data["eventSource"] = "PostDetailView"
            data = dumps(data)
            
            response = self.session.post(f"/x{self.comId}/s/item/{wikiId}/{comType}", headers=self.additional_headers(data=data), data=data)

        else: raise exceptions.SpecifyType()
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def delete_comment(self, commentId: str, userId: str = None, blogId: str = None, wikiId: str = None) -> int:
        if userId: response = self.session.delete(f"/x{self.comId}/s/user-profile/{userId}/comment/{commentId}", headers=self.additional_headers())
        elif blogId: response = self.session.delete(f"/x{self.comId}/s/blog/{blogId}/comment/{commentId}", headers=self.additional_headers())
        elif wikiId: response = self.session.delete(f"/x{self.comId}/s/item/{wikiId}/comment/{commentId}", headers=self.additional_headers())
        else: raise exceptions.SpecifyType()

        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def like_blog(self, blogId: Union[str, list] = None, wikiId: str = None) -> int:
        """
        Like a Blog, Multiple Blogs or a Wiki.

        **Parameters**
            - **blogId** : ID of the Blog or List of IDs of the Blogs. (for Blogs)
            - **wikiId** : ID of the Wiki. (for Wikis)

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        data = {
            "value": 4,
            "timestamp": int(timestamp() * 1000)
        }

        if blogId:
            if isinstance(blogId, str):
                data["eventSource"] = "UserProfileView"
                data = dumps(data)
                
                response = self.session.post(f"/x{self.comId}/s/blog/{blogId}/vote?cv=1.2", headers=self.additional_headers(data=data), data=data)

            elif isinstance(blogId, list):
                data["targetIdList"] = blogId
                data = dumps(data)
                
                response = self.session.post(f"/x{self.comId}/s/feed/vote", headers=self.additional_headers(data=data), data=data)

            else: raise exceptions.WrongType

        elif wikiId:
            data["eventSource"] = "PostDetailView"
            data = dumps(data)
            
            response = self.session.post(f"/x{self. comId}/s/item/{wikiId}/vote?cv=1.2", headers=self.additional_headers(data=data), data=data)

        else: raise exceptions.SpecifyType()
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def unlike_blog(self, blogId: str = None, wikiId: str = None) -> int:
        if blogId: response = self.session.delete(f"/x{self.comId}/s/blog/{blogId}/vote?eventSource=UserProfileView", headers=self.additional_headers())
        elif wikiId: response = self.session.delete(f"/x{self.comId}/s/item/{wikiId}/vote?eventSource=PostDetailView", headers=self.additional_headers())
        else: raise exceptions.SpecifyType()

        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def like_comment(self, commentId: str, userId: str = None, blogId: str = None, wikiId: str = None) -> int:
        data = {
            "value": 1,
            "timestamp": int(timestamp() * 1000)
        }

        if userId:
            data["eventSource"] = "UserProfileView"
            data = dumps(data)
            
            response = self.session.post(f"/x{self.comId}/s/user-profile/{userId}/comment/{commentId}/vote?cv=1.2&value=1", headers=self.additional_headers(data=data), data=data)

        elif blogId:
            data["eventSource"] = "PostDetailView"
            data = dumps(data)
            
            response = self.session.post(f"/x{self.comId}/s/blog/{blogId}/comment/{commentId}/vote?cv=1.2&value=1", headers=self.additional_headers(data=data), data=data)

        elif wikiId:
            data["eventSource"] = "PostDetailView"
            data = dumps(data)
            
            response = self.session.post(f"/x{self.comId}/s/item/{wikiId}/comment/{commentId}/g-vote?cv=1.2&value=1", headers=self.additional_headers(data=data), data=data)

        else: raise exceptions.SpecifyType()
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def unlike_comment(self, commentId: str, userId: str = None, blogId: str = None, wikiId: str = None) -> int:
        if userId: response = self.session.delete(f"/x{self.comId}/s/user-profile/{userId}/comment/{commentId}/g-vote?eventSource=UserProfileView", headers=self.additional_headers())
        elif blogId: response = self.session.delete(f"/x{self.comId}/s/blog/{blogId}/comment/{commentId}/g-vote?eventSource=PostDetailView", headers=self.additional_headers())
        elif wikiId: response = self.session.delete(f"/x{self.comId}/s/item/{wikiId}/comment/{commentId}/g-vote?eventSource=PostDetailView", headers=self.additional_headers())
        else: raise exceptions.SpecifyType()

        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def upvote_comment(self, blogId: str, commentId: str):
        data = dumps({
            "value": 1,
            "eventSource": "PostDetailView",
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/blog/{blogId}/comment/{commentId}/vote?cv=1.2&value=1", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def downvote_comment(self, blogId: str, commentId: str):
        data = dumps({
            "value": -1,
            "eventSource": "PostDetailView",
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/blog/{blogId}/comment/{commentId}/vote?cv=1.2&value=-1", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def unvote_comment(self, blogId: str, commentId: str):
        response = self.session.delete(f"/x{self.comId}/s/blog/{blogId}/comment/{commentId}/vote?eventSource=PostDetailView", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def reply_wall(self, userId: str, commentId: str, message: str):
        data = dumps({
            "content": message,
            "stackedId": None,
            "respondTo": commentId,
            "type": 0,
            "eventSource": "UserProfileView",
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/user-profile/{userId}/comment", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def send_active_obj(self, startTime: int = None, endTime: int = None, optInAdsFlags: int = 2147483647, tz: int = -timezone // 1000, timers: list = None, timestamp: int = int(timestamp() * 1000)): 
        data = {"userActiveTimeChunkList": [{"start": startTime, "end": endTime}], "timestamp": timestamp, "optInAdsFlags": optInAdsFlags, "timezone": tz} 
        if timers: data["userActiveTimeChunkList"] = timers 
        data = json_minify(dumps(data))  
        
        response = self.session.post(f"/x{self.comId}/s/community/stats/user-active-time", headers=self.additional_headers(data=data), data=data) 
        if response.status_code != 200: 
            return exceptions.CheckException(response) 
        else: return response.status_code

    def activity_status(self, status: str):
        if "on" in status.lower(): status = 1
        elif "off" in status.lower(): status = 2
        else: raise exceptions.WrongType(status)

        data = dumps({
            "onlineStatus": status,
            "duration": 86400,
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/user-profile/{self.profile.userId}/online-status", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    # TODO : Finish this
    def watch_ad(self):
        response = self.session.post(f"/g/s/wallet/ads/video/start", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def check_notifications(self):
        response = self.session.post(f"/x{self.comId}/s/notification/checked", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def delete_notification(self, notificationId: str):
        response = self.session.delete(f"/x{self.comId}/s/notification/{notificationId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def clear_notifications(self):
        response = self.session.delete(f"/x{self.comId}/s/notification", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def start_chat(self, userId: Union[str, list], message: str, title: str = None, content: str = None, isGlobal: bool = False, publishToGlobal: bool = False):
        if isinstance(userId, str): userIds = [userId]
        elif isinstance(userId, list): userIds = userId
        else: raise exceptions.WrongType(type(userId))

        data = {
            "title": title,
            "inviteeUids": userIds,
            "initialMessageContent": message,
            "content": content,
            "timestamp": int(timestamp() * 1000)
        }

        if isGlobal is True: data["type"] = 2; data["eventSource"] = "GlobalComposeMenu"
        else: data["type"] = 0

        if publishToGlobal is True: data["publishToGlobal"] = 1
        else: data["publishToGlobal"] = 0

        data = dumps(data)
        
        response = self.session.post(f"/x{self.comId}/s/chat/thread", data=data, headers=self.additional_headers(data=data))
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.Thread(response.json()["thread"]).Thread

    def invite_to_chat(self, userId: Union[str, list], chatId: str):
        if isinstance(userId, str): userIds = [userId]
        elif isinstance(userId, list): userIds = userId
        else: raise exceptions.WrongType(type(userId))

        data = dumps({
            "uids": userIds,
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/member/invite", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def add_to_favorites(self, userId: str):
        response = self.session.post(f"/x{self.comId}/s/user-group/quick-access/{userId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def send_coins(self, coins: int, blogId: str = None, chatId: str = None, objectId: str = None, transactionId: str = None):
        url = None
        if transactionId is None: transactionId = str(UUID(hexlify(urandom(16)).decode('ascii')))

        data = {
            "coins": coins,
            "tippingContext": {"transactionId": transactionId},
            "timestamp": int(timestamp() * 1000)
        }

        if blogId is not None: url = f"/x{self.comId}/s/blog/{blogId}/tipping"
        if chatId is not None: url = f"/x{self.comId}/s/chat/thread/{chatId}/tipping"
        if objectId is not None:
            data["objectId"] = objectId
            data["objectType"] = 2
            url = f"/x{self.comId}/s/tipping"

        if url is None: raise exceptions.SpecifyType()

        data = dumps(data)
        
        response = self.session.post(url, headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def thank_tip(self, chatId: str, userId: str):
        response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/tipping/tipped-users/{userId}/thank", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def follow(self, userId: Union[str, list]):
        """
        Follow an User or Multiple Users.

        **Parameters**
            - **userId** : ID of the User or List of IDs of the Users.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        if isinstance(userId, str):
            response = self.session.post(f"/x{self.comId}/s/user-profile/{userId}/member", headers=self.additional_headers())

        elif isinstance(userId, list):
            data = dumps({"targetUidList": userId, "timestamp": int(timestamp() * 1000)})
            
            response = self.session.post(f"/x{self.comId}/s/user-profile/{self.profile.userId}/joined", headers=self.additional_headers(data=data), data=data)

        else: raise exceptions.WrongType(type(userId))

        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def unfollow(self, userId: str):
        """
        Unfollow an User.

        **Parameters**
            - **userId** : ID of the User.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.delete(f"/x{self.comId}/s/user-profile/{self.profile.userId}/joined/{userId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def block(self, userId: str):
        """
        Block an User.

        **Parameters**
            - **userId** : ID of the User.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.post(f"/x{self.comId}/s/block/{userId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def unblock(self, userId: str):
        """
        Unblock an User.

        **Parameters**
            - **userId** : ID of the User.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.delete(f"/x{self.comId}/s/block/{userId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def visit(self, userId: str):
        """
        Visit an User.

        **Parameters**
            - **userId** : ID of the User.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.get(f"/x{self.comId}/s/user-profile/{userId}?action=visit", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def flag(self, reason: str, flagType: int, userId: str = None, blogId: str = None, wikiId: str = None, asGuest: bool = False):
        """
        Flag a User, Blog or Wiki.

        **Parameters**
            - **reason** : Reason of the Flag.
            - **flagType** : Type of the Flag.
            - **userId** : ID of the User.
            - **blogId** : ID of the Blog.
            - **wikiId** : ID of the Wiki.
            - *asGuest* : Execute as a Guest.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        if reason is None: raise exceptions.ReasonNeeded()
        if flagType is None: raise exceptions.FlagTypeNeeded()

        data = {
            "flagType": flagType,
            "message": reason,
            "timestamp": int(timestamp() * 1000)
        }

        if userId:
            data["objectId"] = userId
            data["objectType"] = 0

        elif blogId:
            data["objectId"] = blogId
            data["objectType"] = 1

        elif wikiId:
            data["objectId"] = wikiId
            data["objectType"] = 2

        else: raise exceptions.SpecifyType()

        if asGuest: flg = "g-flag"
        else: flg = "flag"

        data = dumps(data)
        
        response = self.session.post(f"/x{self.comId}/s/{flg}", data=data, headers=self.additional_headers(data=data))
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def send_message(
            self,
            chatId: str, message: str = None, messageType: int = 0,
            file: BinaryIO = None, fileType: str = None,
            replyTo: str = None, mentionUserIds: list = None,
            stickerId: str = None,
        
            embedId: str = None, embedObjectType: int = None, embedLink: str = None, embedTitle: str = None, embedContent: str = None, embedImage: BinaryIO = None,
            embedType: objects.EmbedTypes = objects.EmbedTypes.LINK_SNIPPET
        ):
        """
        Send a Message to a Chat.

        **Parameters**
            - **message** : Message to be sent
            - **chatId** : ID of the Chat.
            - **file** : File to be sent.
            - **fileType** : Type of the file.
                - ``audio``, ``image``, ``gif``
            - **messageType** : Type of the Message.
            - **mentionUserIds** : List of User IDS to mention. '@' needed in the Message.
            - **replyTo** : Message ID to reply to.
            - **stickerId** : Sticker ID to be sent.
            - **embedType** : Type of the Embed. Can be aminofixfix.lib.objects.EmbedTypes only. By default it's LinkSnippet one.
            - **embedLink** : Link of the Embed.
            - **embedImage** : Image of the Embed. Required to send Embed.
            - **embedId** : ID of the Embed. Works only in AttachedObject Embeds.
            - **embedType** : Type of the AttachedObject Embed. Works only in AttachedObject Embeds.
            - **embedTitle** : Title of the Embed. Works only in AttachedObject Embeds.
            - **embedContent** : Content of the Embed. Works only in AttachedObject Embeds.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """

        if message is not None and file is None:
            message = message.replace("<$", "‎‏").replace("$>", "‬‭")

        mentions = []
        if mentionUserIds:
            mentions = [{"uid": mention_uid} for mention_uid in mentionUserIds]

        if not isinstance(embedImage, BinaryIO):
            embedType = None

        if embedType == objects.EmbedTypes.LINK_SNIPPET:
            data = {
                "type": messageType,
                "content": message,
                "clientRefId": int(timestamp() / 10 % 1000000000),
                "extensions": {
                    "linkSnippetList": [{
                        "link": embedLink,
                        "mediaType": 100,
                        "mediaUploadValue": b64encode(embedImage.read()).decode(),
                        "mediaUploadValueContentType": "image/png"
                    }],
                    "mentionedArray": mentions
                },
                "timestamp": int(timestamp() * 1000)
            }
        elif embedType == objects.EmbedTypes.ATTACHED_OBJECT:
            data = {
                "type": messageType,
                "content": message,
                "clientRefId": int(timestamp() / 10 % 1000000000),
                "attachedObject": {
                    "objectId": embedId,
                    "objectType": embedObjectType,
                    "link": embedLink,
                    "title": embedTitle,
                    "content": embedContent,
                    "mediaList": [[100, self.upload_media(embedImage, "image"), None]]
                },
                "extensions": {"mentionedArray": mentions},
                "timestamp": int(timestamp() * 1000)
            }
        else:
            data = {
                "type": messageType,
                "content": message,
                "clientRefId": int(timestamp() / 10 % 1000000000),
                "extensions": {"mentionedArray": mentions},
                "timestamp": int(timestamp() * 1000)
            }

        if replyTo: data["replyMessageId"] = replyTo

        if stickerId:
            data["content"] = None
            data["stickerId"] = stickerId
            data["type"] = 3

        if file:
            data["content"] = None
            if fileType == "audio":
                data["type"] = 2
                data["mediaType"] = 110

            elif fileType == "image":
                data["mediaType"] = 100
                data["mediaUploadValueContentType"] = "image/jpg"
                data["mediaUhqEnabled"] = True

            elif fileType == "gif":
                data["mediaType"] = 100
                data["mediaUploadValueContentType"] = "image/gif"
                data["mediaUhqEnabled"] = True

            else: raise exceptions.SpecifyType(fileType)

            data["mediaUploadValue"] = b64encode(file.read()).decode()

        data = dumps(data)

        response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/message", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def delete_message(self, chatId: str, messageId: str, asStaff: bool = False, reason: str = None):
        """
        Delete a Message from a Chat.

        **Parameters**
            - **messageId** : ID of the Message.
            - **chatId** : ID of the Chat.
            - **asStaff** : If execute as a Staff member (Leader or Curator).
            - **reason** : Reason of the action to show on the Moderation History.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        data = {
            "adminOpName": 102,
            # "adminOpNote": {"content": reason},
            "timestamp": int(timestamp() * 1000)
        }
        if asStaff and reason:
            data["adminOpNote"] = {"content": reason}

        data = dumps(data)
        
        if not asStaff: response = self.session.delete(f"/x{self.comId}/s/chat/thread/{chatId}/message/{messageId}", headers=self.additional_headers())
        else: response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/message/{messageId}/admin", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def mark_as_read(self, chatId: str, messageId: str):
        """
        Mark a Message from a Chat as Read.

        **Parameters**
            - **messageId** : ID of the Message.
            - **chatId** : ID of the Chat.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        data = dumps({
            "messageId": messageId,
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/mark-as-read", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def edit_chat(self, chatId: str, doNotDisturb: bool = None, pinChat: bool = None, title: str = None, icon: str = None, backgroundImage: str = None, content: str = None, announcement: str = None, coHosts: list = None, keywords: list = None, pinAnnouncement: bool = None, publishToGlobal: bool = None, canTip: bool = None, viewOnly: bool = None, canInvite: bool = None, fansOnly: bool = None):
        """
        Send a Message to a Chat.

        **Parameters**
            - **chatId** : ID of the Chat.
            - **title** : Title of the Chat.
            - **content** : Content of the Chat.
            - **icon** : Icon of the Chat.
            - **backgroundImage** : Url of the Background Image of the Chat.
            - **announcement** : Announcement of the Chat.
            - **pinAnnouncement** : If the Chat Announcement should Pinned or not.
            - **coHosts** : List of User IDS to be Co-Host.
            - **keywords** : List of Keywords of the Chat.
            - **viewOnly** : If the Chat should be on View Only or not.
            - **canTip** : If the Chat should be Tippable or not.
            - **canInvite** : If the Chat should be Invitable or not.
            - **fansOnly** : If the Chat should be Fans Only or not.
            - **publishToGlobal** : If the Chat should show on Public Chats or not.
            - **doNotDisturb** : If the Chat should Do Not Disturb or not.
            - **pinChat** : If the Chat should Pinned or not.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        data = {"timestamp": int(timestamp() * 1000)}

        if title: data["title"] = title
        if content: data["content"] = content
        if icon: data["icon"] = icon
        if keywords: data["keywords"] = keywords
        if announcement: data["extensions"] = {"announcement": announcement}
        if pinAnnouncement: data["extensions"] = {"pinAnnouncement": pinAnnouncement}
        if fansOnly: data["extensions"] = {"fansOnly": fansOnly}

        if publishToGlobal: data["publishToGlobal"] = 0
        if not publishToGlobal: data["publishToGlobal"] = 1

        res = []

        if doNotDisturb is not None:
            if doNotDisturb:
                data = dumps({"alertOption": 2, "timestamp": int(timestamp() * 1000)})
                
                response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/member/{self.profile.userId}/alert", data=data, headers=self.additional_headers(data=data))
                if response.status_code != 200: res.append(exceptions.CheckException(response))
                else: res.append(response.status_code)

            if not doNotDisturb:
                data = dumps({"alertOption": 1, "timestamp": int(timestamp() * 1000)})
                
                response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/member/{self.profile.userId}/alert", data=data, headers=self.additional_headers(data=data))
                if response.status_code != 200: res.append(exceptions.CheckException(response))
                else: res.append(response.status_code)

        if pinChat is not None:
            if pinChat:
                response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/pin", data=data, headers=self.additional_headers())
                if response.status_code != 200: res.append(exceptions.CheckException(response))
                else: res.append(response.status_code)

            if not pinChat:
                response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/unpin", data=data, headers=self.additional_headers())
                if response.status_code != 200: res.append(exceptions.CheckException(response))
                else: res.append(response.status_code)

        if backgroundImage is not None:
            data = dumps({"media": [100, backgroundImage, None], "timestamp": int(timestamp() * 1000)})
            
            response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/member/{self.profile.userId}/background", data=data, headers=self.additional_headers(data=data))
            if response.status_code != 200: res.append(exceptions.CheckException(response))
            else: res.append(response.status_code)

        if coHosts is not None:
            data = dumps({"uidList": coHosts, "timestamp": int(timestamp() * 1000)})
            
            response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/co-host", data=data, headers=self.additional_headers(data=data))
            if response.status_code != 200: res.append(exceptions.CheckException(response))
            else: res.append(response.status_code)

        if viewOnly is not None:
            if viewOnly:
                response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/view-only/enable", headers=self.additional_headers())
                if response.status_code != 200: res.append(exceptions.CheckException(response))
                else: res.append(response.status_code)

            if not viewOnly:
                response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/view-only/disable", headers=self.additional_headers())
                if response.status_code != 200: res.append(exceptions.CheckException(response))
                else: res.append(response.status_code)

        if canInvite is not None:
            if canInvite:
                response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/members-can-invite/enable", data=data, headers=self.additional_headers(data=data))
                if response.status_code != 200: res.append(exceptions.CheckException(response))
                else: res.append(response.status_code)

            if not canInvite:
                response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/members-can-invite/disable", data=data, headers=self.additional_headers(data=data))
                if response.status_code != 200: res.append(exceptions.CheckException(response))
                else: res.append(response.status_code)

        if canTip is not None:
            if canTip:
                response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/tipping-perm-status/enable", data=data, headers=self.additional_headers(data=data))
                if response.status_code != 200: res.append(exceptions.CheckException(response))
                else: res.append(response.status_code)

            if not canTip:
                response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/tipping-perm-status/disable", data=data, headers=self.additional_headers(data=data))
                if response.status_code != 200: res.append(exceptions.CheckException(response))
                else: res.append(response.status_code)

        data = dumps(data)
        
        response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: res.append(exceptions.CheckException(response))
        else: res.append(response.status_code)

        return res

    def transfer_host(self, chatId: str, userIds: list):
        data = dumps({
            "uidList": userIds,
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/transfer-organizer", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def transfer_organizer(self, chatId: str, userIds: list):
        self.transfer_host(chatId, userIds)

    def accept_host(self, chatId: str, requestId: str):
        data = dumps({})
        
        response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/transfer-organizer/{requestId}/accept", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def accept_organizer(self, chatId: str, requestId: str):
        self.accept_host(chatId, requestId)

    def kick(self, userId: str, chatId: str, allowRejoin: bool = True):
        if allowRejoin: allowRejoin = 1
        if not allowRejoin: allowRejoin = 0
        response = self.session.delete(f"/x{self.comId}/s/chat/thread/{chatId}/member/{userId}?allowRejoin={allowRejoin}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def join_chat(self, chatId: str):
        """
        Join an Chat.

        **Parameters**
            - **chatId** : ID of the Chat.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/member/{self.profile.userId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def leave_chat(self, chatId: str):
        """
        Leave an Chat.

        **Parameters**
            - **chatId** : ID of the Chat.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.delete(f"/x{self.comId}/s/chat/thread/{chatId}/member/{self.profile.userId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code
        
    def delete_chat(self, chatId: str):
        """
        Delete a Chat.

        **Parameters**
            - **chatId** : ID of the Chat.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.delete(f"/x{self.comId}/s/chat/thread/{chatId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code
        
    def subscribe(self, userId: str, autoRenew: str = False, transactionId: str = None):
        if transactionId is None: transactionId = str(UUID(hexlify(urandom(16)).decode('ascii')))

        data = dumps({
            "paymentContext": {
                "transactionId": transactionId,
                "isAutoRenew": autoRenew
            },
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/influencer/{userId}/subscribe", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def promotion(self, noticeId: str, type: str = "accept"):
        response = self.session.post(f"/x{self.comId}/s/notice/{noticeId}/{type}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def play_quiz_raw(self, quizId: str, quizAnswerList: list, quizMode: int = 0):
        data = dumps({
            "mode": quizMode,
            "quizAnswerList": quizAnswerList,
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/blog/{quizId}/quiz/result", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def play_quiz(self, quizId: str, questionIdsList: list, answerIdsList: list, quizMode: int = 0):
        quizAnswerList = []

        for question, answer in zip(questionIdsList, answerIdsList):
            part = dumps({
                "optIdList": [answer],
                "quizQuestionId": question,
                "timeSpent": 0.0
            })

            quizAnswerList.append(loads(part))

        data = dumps({
            "mode": quizMode,
            "quizAnswerList": quizAnswerList,
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/blog/{quizId}/quiz/result", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def vc_permission(self, chatId: str, permission: int):
        """Voice Chat Join Permissions
        1 - Open to Everyone
        2 - Approval Required
        3 - Invite Only
        """
        data = dumps({
            "vvChatJoinType": permission,
            "timestamp": int(timestamp() * 1000)
        })
        
        response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/vvchat-permission", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def get_vc_reputation_info(self, chatId: str):
        response = self.session.get(f"/x{self.comId}/s/chat/thread/{chatId}/avchat-reputation", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.VcReputation(response.json()).VcReputation

    def claim_vc_reputation(self, chatId: str):
        response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/avchat-reputation", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.VcReputation(response.json()).VcReputation

    def get_all_users(self, type: str = "recent", start: int = 0, size: int = 25):
        if type == "recent": response = self.session.get(f"/x{self.comId}/s/user-profile?type=recent&start={start}&size={size}", headers=self.additional_headers())
        elif type == "banned": response = self.session.get(f"/x{self.comId}/s/user-profile?type=banned&start={start}&size={size}", headers=self.additional_headers())
        elif type == "featured": response = self.session.get(f"/x{self.comId}/s/user-profile?type=featured&start={start}&size={size}", headers=self.additional_headers())
        elif type == "leaders": response = self.session.get(f"/x{self.comId}/s/user-profile?type=leaders&start={start}&size={size}", headers=self.additional_headers())
        elif type == "curators": response = self.session.get(f"/x{self.comId}/s/user-profile?type=curators&start={start}&size={size}", headers=self.additional_headers())
        else: raise exceptions.WrongType(type)

        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserProfileCountList(response.json()).UserProfileCountList

    def get_online_users(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/live-layer?topic=ndtopic:x{self.comId}:online-members&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserProfileCountList(response.json()).UserProfileCountList

    def get_online_favorite_users(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/user-group/quick-access?type=online&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserProfileCountList(response.json()).UserProfileCountList

    def get_user_info(self, userId: str):
        """
        Information of an User.

        **Parameters**
            - **userId** : ID of the User.

        **Returns**
            - **Success** : :meth:`User Object <amino.lib.util.objects.UserProfile>`

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.get(f"/x{self.comId}/s/user-profile/{userId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserProfile(response.json()["userProfile"]).UserProfile

    def get_user_following(self, userId: str, start: int = 0, size: int = 25):
        """
        List of Users that the User is Following.

        **Parameters**
            - **userId** : ID of the User.
            - *start* : Where to start the list.
            - *size* : Size of the list.

        **Returns**
            - **Success** : :meth:`User List <amino.lib.util.objects.UserProfileList>`

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.get(f"/x{self.comId}/s/user-profile/{userId}/joined?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserProfileList(response.json()["userProfileList"]).UserProfileList

    def get_user_followers(self, userId: str, start: int = 0, size: int = 25):
        """
        List of Users that are Following the User.

        **Parameters**
            - **userId** : ID of the User.
            - *start* : Where to start the list.
            - *size* : Size of the list.

        **Returns**
            - **Success** : :meth:`User List <amino.lib.util.objects.UserProfileList>`

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.get(f"/x{self.comId}/s/user-profile/{userId}/member?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserProfileList(response.json()["userProfileList"]).UserProfileList

    def get_user_visitors(self, userId: str, start: int = 0, size: int = 25):
        """
        List of Users that Visited the User.

        **Parameters**
            - **userId** : ID of the User.
            - *start* : Where to start the list.
            - *size* : Size of the list.

        **Returns**
            - **Success** : :meth:`Visitors List <amino.lib.util.objects.visitorsList>`

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.get(f"/x{self.comId}/s/user-profile/{userId}/visitors?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.VisitorsList(response.json()).VisitorsList

    def get_user_checkins(self, userId: str):
        response = self.session.get(f"/x{self.comId}/s/check-in/stats/{userId}?timezone={-timezone // 1000}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserCheckIns(response.json()).UserCheckIns

    def get_user_blogs(self, userId: str, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/blog?type=user&q={userId}&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.BlogList(response.json()["blogList"]).BlogList

    def get_user_wikis(self, userId: str, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/item?type=user-all&start={start}&size={size}&cv=1.2&uid={userId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.WikiList(response.json()["itemList"]).WikiList

    def get_user_achievements(self, userId: str):
        response = self.session.get(f"/x{self.comId}/s/user-profile/{userId}/achievements", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserAchievements(response.json()["achievements"]).UserAchievements

    def get_influencer_fans(self, userId: str, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/influencer/{userId}/fans?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.InfluencerFans(response.json()).InfluencerFans

    def get_blocked_users(self, start: int = 0, size: int = 25):
        """
        List of Users that the User Blocked.

        **Parameters**
            - *start* : Where to start the list.
            - *size* : Size of the list.

        **Returns**
            - **Success** : :meth:`Users List <amino.lib.util.objects.UserProfileList>`

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.get(f"/x{self.comId}/s/block?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserProfileList(response.json()["userProfileList"]).UserProfileList

    def get_blocker_users(self, start: int = 0, size: int = 25):
        """
        List of Users that are Blocking the User.

        **Parameters**
            - *start* : Where to start the list.
            - *size* : Size of the list.

        **Returns**
            - **Success** : :meth:`List of User IDs <List>`

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """

        response = self.session.get(f"/x{self.comId}/s/block?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.json()["blockerUidList"]

    def search_users(self, nickname: str, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/user-profile?type=name&q={nickname}&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserProfileList(response.json()["userProfileList"]).UserProfileList

    def get_saved_blogs(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/bookmark?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserSavedBlogs(response.json()["bookmarkList"]).UserSavedBlogs

    def get_leaderboard_info(self, type: str, start: int = 0, size: int = 25):
        if "24" in type or "hour" in type: response = self.session.get(f"/g/s-x{self.comId}/community/leaderboard?rankingType=1&start={start}&size={size}", headers=self.additional_headers())
        elif "7" in type or "day" in type: response = self.session.get(f"/g/s-x{self.comId}/community/leaderboard?rankingType=2&start={start}&size={size}", headers=self.additional_headers())
        elif "rep" in type: response = self.session.get(f"/g/s-x{self.comId}/community/leaderboard?rankingType=3&start={start}&size={size}", headers=self.additional_headers())
        elif "check" in type: response = self.session.get(f"/g/s-x{self.comId}/community/leaderboard?rankingType=4", headers=self.additional_headers())
        elif "quiz" in type: response = self.session.get(f"/g/s-x{self.comId}/community/leaderboard?rankingType=5&start={start}&size={size}", headers=self.additional_headers())
        else: raise exceptions.WrongType(type)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserProfileList(response.json()["userProfileList"]).UserProfileList

    def get_wiki_info(self, wikiId: str):
        response = self.session.get(f"/x{self.comId}/s/item/{wikiId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.GetWikiInfo(response.json()).GetWikiInfo

    def get_recent_wiki_items(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/item?type=catalog-all&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.WikiList(response.json()["itemList"]).WikiList

    def get_wiki_categories(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/item-category?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.WikiCategoryList(response.json()["itemCategoryList"]).WikiCategoryList

    def get_wiki_category(self, categoryId: str, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/item-category/{categoryId}?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.WikiCategory(response.json()).WikiCategory

    def get_tipped_users(self, blogId: str = None, wikiId: str = None, quizId: str = None, fileId: str = None, chatId: str = None, start: int = 0, size: int = 25):
        if blogId or quizId:
            if quizId is not None: blogId = quizId
            response = self.session.get(f"/x{self.comId}/s/blog/{blogId}/tipping/tipped-users-summary?start={start}&size={size}", headers=self.additional_headers())
        elif wikiId: response = self.session.get(f"/x{self.comId}/s/item/{wikiId}/tipping/tipped-users-summary?start={start}&size={size}", headers=self.additional_headers())
        elif chatId: response = self.session.get(f"/x{self.comId}/s/chat/thread/{chatId}/tipping/tipped-users-summary?start={start}&size={size}", headers=self.additional_headers())
        elif fileId: response = self.session.get(f"/x{self.comId}/s/shared-folder/files/{fileId}/tipping/tipped-users-summary?start={start}&size={size}", headers=self.additional_headers())
        else: raise exceptions.SpecifyType()
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.TippedUsersSummary(response.json()).TippedUsersSummary

    def get_chat_threads(self, start: int = 0, size: int = 25):
        """
        List of Chats the account is in.

        **Parameters**
            - *start* : Where to start the list.
            - *size* : Size of the list.

        **Returns**
            - **Success** : :meth:`Chat List <amino.lib.util.objects.ThreadList>`

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.get(f"/x{self.comId}/s/chat/thread?type=joined-me&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.ThreadList(response.json()["threadList"]).ThreadList

    def get_public_chat_threads(self, type: str = "recommended", start: int = 0, size: int = 25):
        """
        List of Public Chats of the Community.

        **Parameters**
            - *start* : Where to start the list.
            - *size* : Size of the list.

        **Returns**
            - **Success** : :meth:`Chat List <amino.lib.util.objects.ThreadList>`

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.get(f"/x{self.comId}/s/chat/thread?type=public-all&filterType={type}&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.ThreadList(response.json()["threadList"]).ThreadList

    def get_chat_thread(self, chatId: str):
        """
        Get the Chat Object from an Chat ID.

        **Parameters**
            - **chatId** : ID of the Chat.

        **Returns**
            - **Success** : :meth:`Chat Object <amino.lib.util.objects.Thread>`

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.get(f"/x{self.comId}/s/chat/thread/{chatId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.Thread(response.json()["thread"]).Thread

    def get_chat_messages(self, chatId: str, size: int = 25, pageToken: str = None):
        """
        List of Messages from an Chat.

        **Parameters**
            - **chatId** : ID of the Chat.
            - *size* : Size of the list.
            - *pageToken* : Next Page Token.

        **Returns**
            - **Success** : :meth:`Message List <amino.lib.util.objects.MessageList>`

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """

        if pageToken is not None: url = f"/x{self.comId}/s/chat/thread/{chatId}/message?v=2&pagingType=t&pageToken={pageToken}&size={size}"
        else: url = f"/x{self.comId}/s/chat/thread/{chatId}/message?v=2&pagingType=t&size={size}"

        response = self.session.get(url, headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.GetMessages(response.json()).GetMessages

    def get_message_info(self, chatId: str, messageId: str):
        """
        Information of an Message from an Chat.

        **Parameters**
            - **chatId** : ID of the Chat.
            - **message** : ID of the Message.

        **Returns**
            - **Success** : :meth:`Message Object <amino.lib.util.objects.Message>`

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        response = self.session.get(f"/x{self.comId}/s/chat/thread/{chatId}/message/{messageId}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.Message(response.json()["message"]).Message

    def get_blog_info(self, blogId: str = None, wikiId: str = None, quizId: str = None, fileId: str = None):
        if blogId or quizId:
            if quizId is not None: blogId = quizId
            response = self.session.get(f"/x{self.comId}/s/blog/{blogId}", headers=self.additional_headers())
            if response.status_code != 200: 
                return exceptions.CheckException(response)
            else: return objects.GetBlogInfo(response.json()).GetBlogInfo

        elif wikiId:
            response = self.session.get(f"/x{self.comId}/s/item/{wikiId}", headers=self.additional_headers())
            if response.status_code != 200: 
                return exceptions.CheckException(response)
            else: return objects.GetWikiInfo(response.json()).GetWikiInfo

        elif fileId:
            response = self.session.get(f"/x{self.comId}/s/shared-folder/files/{fileId}", headers=self.additional_headers())
            if response.status_code != 200: 
                return exceptions.CheckException(response)
            else: return objects.SharedFolderFile(response.json()["file"]).SharedFolderFile

        else: raise exceptions.SpecifyType()

    def get_blog_comments(self, blogId: str = None, wikiId: str = None, quizId: str = None, fileId: str = None, sorting: str = "newest", start: int = 0, size: int = 25):
        if sorting == "newest": sorting = "newest"
        elif sorting == "oldest": sorting = "oldest"
        elif sorting == "top": sorting = "vote"

        if blogId or quizId:
            if quizId is not None: blogId = quizId
            response = self.session.get(f"/x{self.comId}/s/blog/{blogId}/comment?sort={sorting}&start={start}&size={size}", headers=self.additional_headers())
        elif wikiId: response = self.session.get(f"/x{self.comId}/s/item/{wikiId}/comment?sort={sorting}&start={start}&size={size}", headers=self.additional_headers())
        elif fileId: response = self.session.get(f"/x{self.comId}/s/shared-folder/files/{fileId}/comment?sort={sorting}&start={start}&size={size}", headers=self.additional_headers())
        else: raise exceptions.SpecifyType()

        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.CommentList(response.json()["commentList"]).CommentList

    def get_blog_categories(self, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/blog-category?size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.BlogCategoryList(response.json()["blogCategoryList"]).BlogCategoryList

    def get_blogs_by_category(self, categoryId: str,start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/blog-category/{categoryId}/blog-list?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.BlogList(response.json()["blogList"]).BlogList

    def get_quiz_rankings(self, quizId: str, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/blog/{quizId}/quiz/result?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.QuizRankings(response.json()).QuizRankings

    def get_wall_comments(self, userId: str, sorting: str, start: int = 0, size: int = 25):
        """
        List of Wall Comments of an User.

        **Parameters**
            - **userId** : ID of the User.
            - **sorting** : Order of the Comments.
                - ``newest``, ``oldest``, ``top``
            - *start* : Where to start the list.
            - *size* : Size of the list.

        **Returns**
            - **Success** : :meth:`Comments List <amino.lib.util.objects.CommentList>`

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """
        if sorting == "newest": sorting = "newest"
        elif sorting == "oldest": sorting = "oldest"
        elif sorting == "top": sorting = "vote"
        else: raise exceptions.WrongType(sorting)

        response = self.session.get(f"/x{self.comId}/s/user-profile/{userId}/comment?sort={sorting}&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.CommentList(response.json()["commentList"]).CommentList

    def get_recent_blogs(self, pageToken: str = None, start: int = 0, size: int = 25):
        if pageToken is not None: url = f"/x{self.comId}/s/feed/blog-all?pagingType=t&pageToken={pageToken}&size={size}"
        else: url = f"/x{self.comId}/s/feed/blog-all?pagingType=t&start={start}&size={size}"

        response = self.session.get(url, headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.RecentBlogs(response.json()).RecentBlogs

    def get_chat_users(self, chatId: str, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/chat/thread/{chatId}/member?start={start}&size={size}&type=default&cv=1.2", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserProfileList(response.json()["memberList"]).UserProfileList

    def get_notifications(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/notification?pagingType=t&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.NotificationList(response.json()["notificationList"]).NotificationList

    def get_notices(self, start: int = 0, size: int = 25):
        """
        :param start: Start of the List (Start: 0)
        :param size: Amount of Notices to Show
        :return: Notices List
        """
        response = self.session.get(f"/x{self.comId}/s/notice?type=usersV2&status=1&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.NoticeList(response.json()["noticeList"]).NoticeList

    def get_sticker_pack_info(self, sticker_pack_id: str):
        response = self.session.get(f"/x{self.comId}/s/sticker-collection/{sticker_pack_id}?includeStickers=true", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.StickerCollection(response.json()["stickerCollection"]).StickerCollection

    def get_sticker_packs(self):
        response = self.session.get(f"/x{self.comId}/s/sticker-collection?includeStickers=false&type=my-active-collection", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        return objects.StickerCollection(response.json()["stickerCollection"]).StickerCollection

    # TODO : Finish this
    def get_store_chat_bubbles(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/store/items?sectionGroupId=chat-bubble&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else:
            response = response.json()
            del response["api:message"], response["api:statuscode"], response["api:duration"], response["api:timestamp"]
            return response

    # TODO : Finish this
    def get_store_stickers(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/store/items?sectionGroupId=sticker&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else:
            response = response.json()
            del response["api:message"], response["api:statuscode"], response["api:duration"], response["api:timestamp"]
            return response

    def get_community_stickers(self):
        response = self.session.get(f"/x{self.comId}/s/sticker-collection?type=community-shared", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.CommunityStickerCollection(response.json()).CommunityStickerCollection

    def get_sticker_collection(self, collectionId: str):
        response = self.session.get(f"/x{self.comId}/s/sticker-collection/{collectionId}?includeStickers=true", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.StickerCollection(response.json()["stickerCollection"]).StickerCollection

    def get_shared_folder_info(self):
        response = self.session.get(f"/x{self.comId}/s/shared-folder/stats", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.GetSharedFolderInfo(response.json()["stats"]).GetSharedFolderInfo

    def get_shared_folder_files(self, type: str = "latest", start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/shared-folder/files?type={type}&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.SharedFolderFileList(response.json()["fileList"]).SharedFolderFileList

    #
    # MODERATION MENU
    #

    def moderation_history(self, userId: str = None, blogId: str = None, wikiId: str = None, quizId: str = None, fileId: str = None, size: int = 25):
        if userId: response = self.session.get(f"/x{self.comId}/s/admin/operation?objectId={userId}&objectType=0&pagingType=t&size={size}", headers=self.additional_headers())
        elif blogId: response = self.session.get(f"/x{self.comId}/s/admin/operation?objectId={blogId}&objectType=1&pagingType=t&size={size}", headers=self.additional_headers())
        elif quizId: response = self.session.get(f"/x{self.comId}/s/admin/operation?objectId={quizId}&objectType=1&pagingType=t&size={size}", headers=self.additional_headers())
        elif wikiId: response = self.session.get(f"/x{self.comId}/s/admin/operation?objectId={wikiId}&objectType=2&pagingType=t&size={size}", headers=self.additional_headers())
        elif fileId: response = self.session.get(f"/x{self.comId}/s/admin/operation?objectId={fileId}&objectType=109&pagingType=t&size={size}", headers=self.additional_headers())
        else: response = self.session.get(f"/x{self.comId}/s/admin/operation?pagingType=t&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.AdminLogList(response.json()["adminLogList"]).AdminLogList

    def feature(self, time: int, userId: str = None, chatId: str = None, blogId: str = None, wikiId: str = None):
        if chatId:
            if time == 1: time = 3600
            if time == 1: time = 7200
            if time == 1: time = 10800

        else:
            if time == 1: time = 86400
            elif time == 2: time = 172800
            elif time == 3: time = 259200
            else: raise exceptions.WrongType(time)

        data = {
            "adminOpName": 114,
            "adminOpValue": {
                "featuredDuration": time
            },
            "timestamp": int(timestamp() * 1000)
        }

        if userId:
            data["adminOpValue"] = {"featuredType": 4}
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/user-profile/{userId}/admin", headers=self.additional_headers(data=data), data=data)

        elif blogId:
            data["adminOpValue"] = {"featuredType": 1}
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/blog/{blogId}/admin", headers=self.additional_headers(data=data), data=data)

        elif wikiId:
            data["adminOpValue"] = {"featuredType": 1}
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/item/{wikiId}/admin", headers=self.additional_headers(data=data), data=data)

        elif chatId:
            data["adminOpValue"] = {"featuredType": 5}
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/admin", headers=self.additional_headers(data=data), data=data)

        else: raise exceptions.SpecifyType()
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.json()

    def unfeature(self, userId: str = None, chatId: str = None, blogId: str = None, wikiId: str = None):
        data = {
            "adminOpName": 114,
            "adminOpValue": {},
            "timestamp": int(timestamp() * 1000)
        }

        if userId:
            data["adminOpValue"] = {"featuredType": 0}
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/user-profile/{userId}/admin", headers=self.additional_headers(data=data), data=data)

        elif blogId:
            data["adminOpValue"] = {"featuredType": 0}
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/blog/{blogId}/admin", headers=self.additional_headers(data=data), data=data)

        elif wikiId:
            data["adminOpValue"] = {"featuredType": 0}
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/item/{wikiId}/admin", headers=self.additional_headers(data=data), data=data)

        elif chatId:
            data["adminOpValue"] = {"featuredType": 0}
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/admin", headers=self.additional_headers(data=data), data=data)

        else: raise exceptions.SpecifyType()
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.json()

    def hide(self, userId: str = None, chatId: str = None, blogId: str = None, wikiId: str = None, quizId: str = None, fileId: str = None, reason: str = None):
        data = {
            "adminOpNote": {
                "content": reason
            },
            "timestamp": int(timestamp() * 1000)
        }

        if userId:
            data["adminOpName"] = 18
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/user-profile/{userId}/admin", headers=self.additional_headers(data=data), data=data)

        elif blogId:
            data["adminOpName"] = 110
            data["adminOpValue"] = 9
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/blog/{blogId}/admin", headers=self.additional_headers(data=data), data=data)

        elif quizId:
            data["adminOpName"] = 110
            data["adminOpValue"] = 9
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/blog/{quizId}/admin", headers=self.additional_headers(data=data), data=data)

        elif wikiId:
            data["adminOpName"] = 110
            data["adminOpValue"] = 9
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/item/{wikiId}/admin", headers=self.additional_headers(data=data), data=data)

        elif chatId:
            data["adminOpName"] = 110
            data["adminOpValue"] = 9
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/admin", headers=self.additional_headers(data=data), data=data)

        elif fileId:
            data["adminOpName"] = 110
            data["adminOpValue"] = 9
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/shared-folder/files/{fileId}/admin", headers=self.additional_headers(data=data), data=data)

        else: raise exceptions.SpecifyType()
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.json()

    def unhide(self, userId: str = None, chatId: str = None, blogId: str = None, wikiId: str = None, quizId: str = None, fileId: str = None, reason: str = None):
        data = {
            "adminOpNote": {
                "content": reason
            },
            "timestamp": int(timestamp() * 1000)
        }

        if userId:
            data["adminOpName"] = 19
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/user-profile/{userId}/admin", headers=self.additional_headers(data=data), data=data)

        elif blogId:
            data["adminOpName"] = 110
            data["adminOpValue"] = 0
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/blog/{blogId}/admin", headers=self.additional_headers(data=data), data=data)

        elif quizId:
            data["adminOpName"] = 110
            data["adminOpValue"] = 0
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/blog/{quizId}/admin", headers=self.additional_headers(data=data), data=data)

        elif wikiId:
            data["adminOpName"] = 110
            data["adminOpValue"] = 0
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/item/{wikiId}/admin", headers=self.additional_headers(data=data), data=data)

        elif chatId:
            data["adminOpName"] = 110
            data["adminOpValue"] = 0
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/admin", headers=self.additional_headers(data=data), data=data)

        elif fileId:
            data["adminOpName"] = 110
            data["adminOpValue"] = 0
            data = dumps(data)
            response = self.session.post(f"/x{self.comId}/s/shared-folder/files/{fileId}/admin", headers=self.additional_headers(data=data), data=data)

        else: raise exceptions.SpecifyType()
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.json()

    def edit_titles(self, userId: str, titles: list, colors: list):
        tlt = []
        for titles, colors in zip(titles, colors):
            tlt.append({"title": titles, "color": colors})

        data = dumps({
            "adminOpName": 207,
            "adminOpValue": {
                "titles": tlt
            },
            "timestamp": int(timestamp() * 1000)
        })

        response = self.session.post(f"/x{self.comId}/s/user-profile/{userId}/admin", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.json()

    # TODO : List all warning texts
    def warn(self, userId: str, reason: str = None):
        data = dumps({
            "uid": userId,
            "title": "Custom",
            "content": reason,
            "attachedObject": {
                "objectId": userId,
                "objectType": 0
            },
            "penaltyType": 0,
            "adminOpNote": {},
            "noticeType": 7,
            "timestamp": int(timestamp() * 1000)
        })

        response = self.session.post(f"/x{self.comId}/s/notice", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.json()

    # TODO : List all strike texts
    def strike(self, userId: str, time: int, title: str = None, reason: str = None):
        if time == 1: time = 86400
        elif time == 2: time = 10800
        elif time == 3: time = 21600
        elif time == 4: time = 43200
        elif time == 5: time = 86400
        else: raise exceptions.WrongType(time)

        data = dumps({
            "uid": userId,
            "title": title,
            "content": reason,
            "attachedObject": {
                "objectId": userId,
                "objectType": 0
            },
            "penaltyType": 1,
            "penaltyValue": time,
            "adminOpNote": {},
            "noticeType": 4,
            "timestamp": int(timestamp() * 1000)
        })

        response = self.session.post(f"/x{self.comId}/s/notice", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.json()

    def ban(self, userId: str, reason: str, banType: int = None):
        data = dumps({
            "reasonType": banType,
            "note": {
                "content": reason
            },
            "timestamp": int(timestamp() * 1000)
        })

        response = self.session.post(f"/x{self.comId}/s/user-profile/{userId}/ban", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.json()

    def unban(self, userId: str, reason: str):
        data = dumps({
            "note": {
                "content": reason
            },
            "timestamp": int(timestamp() * 1000)
        })

        response = self.session.post(f"/x{self.comId}/s/user-profile/{userId}/unban", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.json()

    def reorder_featured_users(self, userIds: list):
        data = dumps({
            "uidList": userIds,
            "timestamp": int(timestamp() * 1000)
        })

        response = self.session.post(f"/x{self.comId}/s/user-profile/featured/reorder", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.json()

    def get_hidden_blogs(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/feed/blog-disabled?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.BlogList(response.json()["blogList"]).BlogList

    def get_featured_users(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/user-profile?type=featured&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.UserProfileCountList(response.json()).UserProfileCountList

    def review_quiz_questions(self, quizId: str):
        response = self.session.get(f"/x{self.comId}/s/blog/{quizId}?action=review", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.QuizQuestionList(response.json()["blog"]["quizQuestionList"]).QuizQuestionList

    def get_recent_quiz(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/blog?type=quizzes-recent&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.BlogList(response.json()["blogList"]).BlogList

    def get_trending_quiz(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/feed/quiz-trending?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.BlogList(response.json()["blogList"]).BlogList

    def get_best_quiz(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/feed/quiz-best-quizzes?start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.BlogList(response.json()["blogList"]).BlogList

    def send_action(self, actions: list, blogId: str = None, quizId: str = None, lastAction: bool = False):
        # Action List
        # Browsing

        if lastAction is True: t = 306
        else: t = 304

        data = {
            "o": {
                "actions": actions,
                "target": f"ndc://x{self.comId}/",
                "ndcId": int(self.comId),
                "params": {"topicIds": [45841, 17254, 26542, 42031, 22542, 16371, 6059, 41542, 15852]},
                "id": "831046"
            },
            "t": t
        }

        if blogId is not None or quizId is not None:
            data["target"] = f"ndc://x{self.comId}/blog/{blogId}"
            if blogId is not None: data["params"]["blogType"] = 0
            if quizId is not None: data["params"]["blogType"] = 6

        return self.send(dumps(data))

    # Provided by "spectrum#4691"
    def purchase(self, objectId: str, objectType: int, aminoPlus: bool = True, autoRenew: bool = False):
        data = {'objectId': objectId,
                'objectType': objectType,
                'v': 1,
                "timestamp": int(timestamp() * 1000)}

        if aminoPlus: data['paymentContext'] = {'discountStatus': 1, 'discountValue': 1, 'isAutoRenew': autoRenew}
        else: data['paymentContext'] = {'discountStatus': 0, 'discountValue': 1, 'isAutoRenew': autoRenew}

        data = dumps(data)
        response = self.session.post(f"/x{self.comId}/s/store/purchase", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    # Provided by "spectrum#4691"
    def apply_avatar_frame(self, avatarId: str, applyToAll: bool = True):
        """
        Apply avatar frame.

        **Parameters**
            - **avatarId** : ID of the avatar frame.
            - **applyToAll** : Apply to all.

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`

        """

        data = {"frameId": avatarId,
                "applyToAll": 0,
                "timestamp": int(timestamp() * 1000)}

        if applyToAll: data["applyToAll"] = 1

        data = dumps(data)
        response = self.session.post(f"/x{self.comId}/s/avatar-frame/apply", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def invite_to_vc(self, chatId: str, userId: str):
        """
        Invite a User to a Voice Chat

        **Parameters**
            - **chatId** - ID of the Chat
            - **userId** - ID of the User

        **Returns**
            - **Success** : 200 (int)

            - **Fail** : :meth:`Exceptions <aminofix.lib.util.exceptions>`
        """

        data = dumps({
            "uid": userId
        })

        response = self.session.post(f"/x{self.comId}/s/chat/thread/{chatId}/vvchat-presenter/invite/", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def add_poll_option(self, blogId: str, question: str):
        data = dumps({
            "mediaList": None,
            "title": question,
            "type": 0,
            "timestamp": int(timestamp() * 1000)
        })

        response = self.session.post(f"/x{self.comId}/s/blog/{blogId}/poll/option", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def create_wiki_category(self, title: str, parentCategoryId: str, content: str = None):
        data = dumps({
            "content": content,
            "icon": None,
            "label": title,
            "mediaList": None,
            "parentCategoryId": parentCategoryId,
            "timestamp": int(timestamp() * 1000)
        })

        response = self.session.post(f"/x{self.comId}/s/item-category", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def create_shared_folder(self,title: str):
        data = dumps({
                "title":title,
                "timestamp":int(timestamp() * 1000)
            })
        response = self.session.post(f"/x{self.comId}/s/shared-folder/folders", headers=self.additional_headers(data=data),data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def submit_to_wiki(self, wikiId: str, message: str):
        data = dumps({
            "message": message,
            "itemId": wikiId,
            "timestamp": int(timestamp() * 1000)
        })

        response = self.session.post(f"/x{self.comId}/s/knowledge-base-request", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def accept_wiki_request(self, requestId: str, destinationCategoryIdList: list):
        data = dumps({
            "destinationCategoryIdList": destinationCategoryIdList,
            "actionType": "create",
            "timestamp": int(timestamp() * 1000)
        })

        response = self.session.post(f"/x{self.comId}/s/knowledge-base-request/{requestId}/approve", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def reject_wiki_request(self, requestId: str):
        data = dumps({})

        response = self.session.post(f"/x{self.comId}/s/knowledge-base-request/{requestId}/reject", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def get_wiki_submissions(self, start: int = 0, size: int = 25):
        response = self.session.get(f"/x{self.comId}/s/knowledge-base-request?type=all&start={start}&size={size}", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.WikiRequestList(response.json()["knowledgeBaseRequestList"]).WikiRequestList

    def get_live_layer(self):
        response = self.session.get(f"/x{self.comId}/s/live-layer/homepage?v=2", headers=self.additional_headers())
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return objects.LiveLayer(response.json()["liveLayerList"]).LiveLayer

    def apply_bubble(self, bubbleId: str, chatId: str, applyToAll: bool = False):
        data = {
            "applyToAll": 0,
            "bubbleId": bubbleId,
            "threadId": chatId,
            "timestamp": int(timestamp() * 1000)
        }

        if applyToAll is True:
            data["applyToAll"] = 1

        data = dumps(data)
        response = self.session.post(f"/x{self.comId}/s/chat/thread/apply-bubble", headers=self.additional_headers(data=data), data=data)
        if response.status_code != 200: 
            return exceptions.CheckException(response)
        else: return response.status_code

    def send_video(self, chatId: str, videoFile: BinaryIO, imageFile: BinaryIO, message: str = None, mediaUhqEnabled: bool = False):
        """
            Sending video.

            chatId: str
            message: str
            videoFile: BinaryIO [open(file, "rb")]
            imageFile: BinaryIO [open(file, "rb")]
            mediaUhqEnabled: bool = False
        """
        i = str(uuid4()).upper()
        cover = f"{i}_thumb.jpg"
        video = f"{i}.mp4"
        
        data = dumps({
            "clientRefId": int(timestamp() / 10 % 1000000000),
            "content": message,
            "mediaType": 123,
            "videoUpload":
            {
                "contentType": "video/mp4",
                "cover": cover,
                "video": video
            },
            "type": 4,
            "timestamp": int(timestamp() * 1000),
            "mediaUhqEnabled": mediaUhqEnabled,
            "extensions": {}    
        })

        files = {
            video: (video, videoFile.read(), 'video/mp4'),
            cover: (cover, imageFile.read(), 'application/octet-stream'),
            'payload': (None, data, 'application/octet-stream')
        }
        
        response = self.session.post(
            f"/x{self.comId}/s/chat/thread/{chatId}/message",
            headers=self.additional_headers(data=data, content_type="default"),
            files=files
        )
        
        if response.status_code != 200: return exceptions.CheckException(response)
        else: return response.status_code