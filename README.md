# rpi_felica_poweroff_with_nfcpy

## How to use

- `rpi_config/90-rc-s380.rules` to Raspberry Pi's `/etc/udev/rules.d/90-rc-s380.rules`
- `rpi_config/rc-s380.service` to Raspberry Pi's `/etc/systemd/system/rc-s380.service`
- deploy `src` directory to Raspberry Pi's `/home/pi/projects/rpi_felica_poweroff_with_nfcpy/`
  - rename `.env.template` to `.env`, set values for your environment
  
## Tested Environment

- Raspberry Pi 2 Model B
- Raspberry Pi OS 32-bit
  - Released 2022-01-28
- Python 3.9.2
- nfcpy 1.0.4 
- slack_sdk 3.15.2
- PaSoRi RC-S380

## Related Blog (Written in Japanese)

- [Raspberry Pi 2 + PaSoRi RC-S380 + nfcpyにて、FeliCa読み取り時にPowerOffし、Slackへ通知してみた - メモ的な思考的な](https://thinkami.hatenablog.com/entry/2022/03/28/234902)
