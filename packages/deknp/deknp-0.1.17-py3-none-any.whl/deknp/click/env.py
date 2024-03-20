import os
import json
import typer
from dynaconf.loaders.env_loader import load_from_env
from dektools.file import read_text
from ..core.base.env_vars import EnvVars
from ..core import run_plugin_dv3_env_vars, PluginDv3EnvVars

app = typer.Typer(add_completion=False)


@app.command()
def to(env, path=None):  # dev, stage, prod
    run_plugin_dv3_env_vars()
    path_project = path or os.getcwd()
    data = json.loads(read_text(os.path.join(path_project, PluginDv3EnvVars.env_path_data)))
    ev = EnvVars(os.path.join(path_project, PluginDv3EnvVars.env_path_src))
    ev.update('envBase', data.get('base'))
    ev.update('envEnv', data.get(env))


@app.command()
def final(path=None, prefix='DEKNP_ENV'):
    path_project = path or os.getcwd()
    data = {}
    load_from_env(
        key=None,
        prefix=prefix,
        obj=data,
        silent=True,
    )
    data = {k: v for k, v in data.items() if k.isupper()}
    EnvVars(os.path.join(path_project, PluginDv3EnvVars.env_path_src)).update('env', data)
