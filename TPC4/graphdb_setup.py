import subprocess
import argparse

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e.stderr}")

parser = argparse.ArgumentParser()
parser.add_argument("-i", action="store_true", help="Executar os passos para inicializar o container")
parser.add_argument("-f", action="store_true", help="Executar os passos para finalizar o container")
parser.add_argument("-p", action="store_true", help="Executar os passos para finalizar o container")

args = parser.parse_args()
cmds = []

if args.i:
    cmds = [
        "sudo docker volume create graphdb_data",
        "sudo docker volume ls",
        "sudo docker run -d -p 7200:7200 -v graphdb_data:/opt/graphdb/home --name gdb 1919d5a74509"
    ]

elif args.f:
    container_id = subprocess.getoutput("sudo docker ps --filter 'publish=7200' --format '{{.ID}}'").strip()
    
    if container_id:
        cmds = [
            f"sudo docker stop {container_id}",
            f"sudo docker rm {container_id}",
            "sudo docker volume rm graphdb_data"
        ]
    else:
        print("Nenhum container encontrado com a porta 7200.")
        cmds = []  # Não executa mais nenhum comando se não encontrar o container

elif args.p:
    cmds = [
        "sudo docker volume prune",
    ]
    
if cmds:
    for cmd in cmds:
        run_command(cmd)
else:
    print("Nenhum comando a ser executado.")
