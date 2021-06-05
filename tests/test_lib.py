from mippae_libs.auth import gen_token
from datetime import datetime, timedelta

def test_main():
    exp = datetime.now() + timedelta(days=2)
    token  = gen_token("Renato Martins", exp)
    print(token)
    assert False 
    