from kvcdl.config import config
from kvcdl.keyvault import Keyvault
from kvcdl.output import Output
from kvcdl.hook import Hook

def main():
  vault = Keyvault(list(config['keyvaults'].keys())[0])
  local_storage = Output(config['output']['dir'])

  output = local_storage.sync(vault.secrets)

  if len(output) > 0:
    if config['hook']:
      hook = Hook(config['hook']['action'], config['hook']['service'])
      hook.run()
      print('debug: Hook ran')
