import requests
import json
import sys
import conf.default as cfg

headers = {
    'X-Vault-Token': cfg.vault_token,
}
r = requests.get(cfg.vault_url+cfg.vault_path, headers=headers)

envfile = "/env/secret"+cfg.vault_path.replace('/','-')+".env"

if r.status_code == 200:
  jsondata = json.loads(r.text)
  secrets = jsondata['data']['data']
  open(envfile, 'w').close()
  f = open(envfile, "a")
  for i in secrets:
    f.write(i.upper()+'="'+secrets[i].replace("\n","")+'"'+"\n")
  f.close()
  print("Secrets ok")
else:
  print("Error status code =! 200, retrieving secret")
  sys.exit()
