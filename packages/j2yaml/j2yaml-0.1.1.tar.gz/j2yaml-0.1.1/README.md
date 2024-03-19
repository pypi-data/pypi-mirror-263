# j2yaml
Jinja2-templates inside YAML-files. 
Simply trying to mimic cookiecutter or Ansible in how Jinja is parsed within YAML-files.

## Install

```bash
pip install j2yaml
```

## Usage Example

```yaml
---
# test.yaml
foo: Demo
bar: "{{ testvar }}"
fez: "{{ foo }}"
```

```python
# test.py
import j2yaml

with open('test.yaml') as file:
  yml = file.read()
  data = j2yaml.load(yml, {'testvar':'asd'})

print(data)
```

```bash
python test.py
{'foo': 'Demo', 'bar': 'asd', 'fez': 'Demo'}
```
