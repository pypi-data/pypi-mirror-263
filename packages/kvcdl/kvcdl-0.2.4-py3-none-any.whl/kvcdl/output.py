from os import listdir, path
from os.path import isfile, join
from .config import config
from .models import LocalSecret
from .certificate import pkcs12_to_pem
import xattr

class Output:
  def __init__(self, dir):
    self._dir = dir
    self._version_xattr = 'user.kvcdl_version'

  @property
  def _secrets(self):
    __secrets = []

    for _filename in listdir(self._dir):
      _fullpath = join(self._dir, _filename)
      if isfile(_fullpath):
        __secrets.append(LocalSecret(
          _filename,
          xattr.getxattr(_fullpath, self._version_xattr).decode('utf-8'))
        )

    return __secrets

  def _output_files(self, secret_name, version, value_pkcs12):
    _file_name = secret_name + '.' + config['output']['ext']
    _fullpath = path.join(self._dir, _file_name)
    _value_pem = pkcs12_to_pem(value_pkcs12)

    with open(_fullpath, 'wb') as writer:
      writer.write(_value_pem)
      xattr.setxattr(
        writer,
        self._version_xattr,
        bytes(version, encoding='utf-8')
      )
    
    _file_name_base = Path(_fullpath).stem

    _secret_content = open(_fullpath, 'r').read()
    _ca_cert_content = ''
    _cert_content = ''
    _key_content = ''
    _mode = 'ca'
    if config['output']['ext'] == 'pem':
      for _line in _secret_content.splitlines():
        match _mode:
          case 'ca':
            _ca_cert_content += _line
            if '-END CERTIFICATE-' in _line:
              _mode = 'key'
            else:
              _ca_cert_content += '\n'
          case 'key':
            _key_content += _line
            if '-END PRIVATE KEY-' in _line:
              _mode = 'cert'
            else:
              _key_content += '\n'
          case 'cert':
            _cert_content += _line
            if '-END CERTIFICATE-' in _line:
              _mode = 'done'
            else:
              _cert_content += '\n'
          case 'done':
            break
          case _:
            raise ValueError('Invalid mode: {}'.format(_mode))

    with open(_file_name_base + '-ca.pem', 'w') as f:
      f.write(_ca_cert_content)

    with open(_file_name_base + '-cert.pem', 'w') as f:
      f.write(_cert_content)

    with open(_file_name_base + '-key.pem', 'w') as f:
      f.write(_key_content)

  @property
  def _secret_names(self):
    return list(map(lambda s: s.name, self._secrets))

  def sync(self, kv_secrets):
    _output_secrets = []

    for s in kv_secrets:
      if s.name in self._secret_names:
        local_secret = self._secrets[self._secret_names.index(s.name)]
        if s.properties.version == local_secret.version:
          print('debug: Skipping {}'.format(s.name))
          continue
      self._output_files(s.name, s.properties.version, s.value)
      _output_secrets.append(s)
      print('debug: Output secret {}'.format(s.name))

    return _output_secrets
