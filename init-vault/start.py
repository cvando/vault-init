import requests
import json
import sys
import conf.default as cfg

headers = {
    'X-Vault-Token': cfg.vault_token,
}
r = requests.get(cfg.vault_url+cfg.vault_path, headers=headers)

if r.status_code == 200:
  jsondata = json.loads(r.text)
  secrets = jsondata['data']['data']
  open('/env/secret.env', 'w').close()
  f = open("/env/secret.env", "a")
  for i in secrets:
    f.write(i.upper()+'="'+secrets[i].replace("\n","")+'"'+"\n")
  f.close()
  print("Secrets ok")
else:
  print("Error status code =! 200, retrieving secret")
  sys.exit()