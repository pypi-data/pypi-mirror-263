import os
from dynaconf.loaders.env_loader import load_from_env

settings ={}# {'AAA':'2222222'}

os.environ['TEST_aaa'] = "WERWR"

load_from_env(
    key=None,
    prefix="TEST",
    obj=settings,
    silent=True,
)

print( settings)