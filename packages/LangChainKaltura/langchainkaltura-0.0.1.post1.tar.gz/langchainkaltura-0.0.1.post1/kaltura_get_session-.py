# https://teamdynamix.umich.edu/TDClient/30/Portal/KB/ArticleDet?ID=7132

secret = "********************************"
user_id = "YOUR_USER_ID"
k_type = KalturaSessionType.ADMIN
partner_id = 1038472
expiry = 8640000
privileges = "disableentitlement"

result = client.session.start(secret, user_id, k_type, partner_id, expiry, privileges)
print(result)

# MDk2NmZkZjkyNWNjYzNmZDg3MjIxNDAwODMyZjIyY2VmYjQ0YWYyZnwxMDM4NDcyOzEwMzg0NzI7MTcxODI5NzAyNzsyOzE3MDk2NTcwMjcuMjk4Mzs7ZGlzYWJsZWVudGl0bGVtZW50Ozs=
