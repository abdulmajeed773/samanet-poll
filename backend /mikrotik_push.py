from routeros_api import RouterOsApiPool
from config import MIKROTIK_HOST, MIKROTIK_USER, MIKROTIK_PASS

api_pool = RouterOsApiPool(
    host=MIKROTIK_HOST,
    username=MIKROTIK_USER,
    password=MIKROTIK_PASS,
    plaintext_login=True
)
api = api_pool.get_api()

active = api.get_resource('/ip/hotspot/active').get()
for user in active:
    print(f"💻 {user['mac-address']} - {user['address']}")
