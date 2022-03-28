import binascii
import os
import shlex
import subprocess

import asyncio
import nfc
from dotenv import load_dotenv
from slack_sdk.web.async_client import AsyncWebClient


async def post():
    client = AsyncWebClient(os.environ['SLACK_BOT_TOKEN'])
    response = await client.chat_postMessage(
        channel=os.environ['DESTINATION'],
        text=':zzz:',
    )
    print(response)

def on_connect(tag):
    idm = binascii.hexlify(tag._nfcid).decode('utf-8')
    print(idm)

    # ラズパイのACT LEDをheartbeatにする
    cmd = shlex.split("echo heartbeat")
    cmd_redirect = shlex.split("sudo tee /sys/class/leds/led0/trigger")

    p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd_redirect, stdin=p1.stdout)
    p1.stdout.close()
    p2.communicate()[0]

    # Slackにポストする
    asyncio.run(post())

    # シャットダウン
    cmd_power_off = shlex.split("sudo systemctl poweroff")
    subprocess.Popen(cmd_power_off)


if __name__ == "__main__":
    load_dotenv()

    print('読み取りを開始します')
    with nfc.ContactlessFrontend('usb:054c:06c3') as cf:
        cf.connect(rdwr={'on-connect': on_connect})
