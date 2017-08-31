# -*- coding: utf-8 -*-
# filename: handle.py
import reply
import receive
import web

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #��̨����־
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content = "test"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
            if isinstance(recMsg, receive.EventMsg):
                if recMsg.Event == 'CLICK':
                    if recMsg.Eventkey == 'mpGuide':
                        content = "��д�У���δ���".encode('utf-8')
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
            print "���Ҳ�����"
            return reply.Msg().send()
        except Exception, Argment:
            return Argment