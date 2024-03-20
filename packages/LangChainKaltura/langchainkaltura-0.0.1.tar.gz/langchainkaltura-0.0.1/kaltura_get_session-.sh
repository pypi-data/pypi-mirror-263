#!/bin/sh --

# https://teamdynamix.umich.edu/TDClient/30/Portal/KB/ArticleDet?ID=7132

curl -X POST https://www.kaltura.com/api_v3/service/session/action/start \
    -d "secret=********" \
    -d "userId=YOUR_USER_ID" \
    -d "type=2" \
    -d "partnerId=1038472" \
    -d "expiry=8640000" \
    -d "privileges=disableentitlement"

# MDk2NmZkZjkyNWNjYzNmZDg3MjIxNDAwODMyZjIyY2VmYjQ0YWYyZnwxMDM4NDcyOzEwMzg0NzI7MTcxODI5NzAyNzsyOzE3MDk2NTcwMjcuMjk4Mzs7ZGlzYWJsZWVudGl0bGVtZW50Ozs=
