import docker
import datetime
import requests

client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')
webhook_url = "https://discordapp.com/api/webhooks/1207362276756291584/nw1LhshqgRNApODyZRbVJFXNfjXVp7wgDGdlXTaAqqCznjI050NlLs-c_Jl7c3gYBgBe"

for event in client.events(decode=True,filters={"event":"die"}):
    container_id = event["id"]
    container_name = event["Actor"]["Attributes"]["name"]
    epoch_time = datetime.datetime.fromtimestamp(event["time"])

    payload = {"content": f"O container {container_name} ({container_id}) foi finalizado {epoch_time}"}

    print(payload)
    requests.post(webhook_url,data=payload)