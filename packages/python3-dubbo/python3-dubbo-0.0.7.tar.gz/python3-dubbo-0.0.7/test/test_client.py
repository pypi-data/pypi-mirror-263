# -*- coding: utf-8 -*-
from dubbo.client import DubboClient
from dubbo.client import ZkRegister
from dubbo.codec.encoder import Object
import logging
import json

logger = logging.getLogger('python-dubbo')
logging.basicConfig(level=logging.DEBUG)


def pretty_print(value):
    print(json.dumps(value, ensure_ascii=False, indent=4, sort_keys=True))


zk_client = ZkRegister('10.9.15.32:2181')

client = DubboClient('com.zto.titans.zim.api.contact.service.GroupService', zk_register=zk_client)

java_obj = Object('com.zto.titans.zim.api.contact.req.GetMemberInfoRequest')
java_obj['groupId'] = '1724309977011425339'
java_obj['userId'] = '10000044399'


result = client.call('getMemberInfo', java_obj)
pretty_print(result)