![vkbee](https://raw.githubusercontent.com/asyncvk/vkbee/master/bg.png)
# vkbee
Simple Async VKLibrary faster than vk_api
```python
import aiohttp
import asyncio
import longpoll
import api
import time



import aiohttp
import asyncio
import vkbee
import time
import datetime

async def main(loop):
    token = "tokenhere"
    vk = vkbee.VkApi(token, loop=loop)
    delta = datetime.timedelta(hours=8, minutes=0)  # ������� �� UTC. ������ ������� ����� �������� ������ 3
    t = (datetime.datetime.now(datetime.timezone.utc) + delta)  # ����������� ���� � ����� ���������� �t�
    nowtime = t.strftime("%H:%M")  # ������� �����
    nowdate = t.strftime("%d.%m.%Y")  # ������� ����
    none={}
    on = await vkbee.VkApi.call(vk,"friends.getOnline",none)
    counted = len(on)  # ������� ���-�� ��������� � ������

    data = {
        'text':'VKBee: '+nowtime + " ? " + nowdate + " ? " + "������ ������: " + str(counted)
    }
    while True:
        a=await vkbee.VkApi.call(vk,'status.set',data)
        print(a)
        time.sleep(1)
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))

```
