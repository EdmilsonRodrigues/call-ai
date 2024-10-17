import subprocess
import os
import shutil
import venv


cwd = os.getcwd()

current = cwd.split(os.path.sep)[-1]

print(f"O atual diretório é {current}")

possible_venvs = (".venv", "venv")

if current != "call_ai":
    os.chdir("..")
    os.rename(current, "call_ai")
    print("Diretório renomeado para call_ai")
    os.chdir("call_ai")
    old_venv = None
    for env in possible_venvs:
        if os.path.exists(env):
            old_venv = env
            break
    if old_venv:
        shutil.rmtree(old_venv)
        print("Antigo ambiente virtual deletado")

for env in possible_venvs:
    if os.path.exists(env):
        existing_venv = env
        break
else:
    venv.create(".venv", with_pip=True)
    existing_venv = ".venv"
    print("Novo ambiente virtual criado em .venv")

if os.name == "nt":
    bin = "Scripts"
else:
    bin = "bin"

pip = os.path.join(existing_venv, bin, "pip")

requirements = ("requirements.txt", "requirements.dev.txt", "requirements.test.txt")

for requirement in requirements:
    if os.path.exists(requirement):
        subprocess.run([pip, "install", "-r", requirement])
        print(f"Os módulos requeridos no arquivo {requirement} foram instalados")
    else:
        print(f"Erro: Não foi encontrado arquivo {requirement}")
