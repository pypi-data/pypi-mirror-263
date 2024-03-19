import jinja2
import yaml

def load(yml: str, environment: dict = {}) -> object:
  '''
  Loads a valid YAML-string. Runs the YAML-string through the Jinja2-templating engine,
  using the initial YAML and a supplied environment dictinary to mutate the environment.
  This allows self-referencing within the same YAML-file while using Jinja2 variables.
    
  Returns a python-object from the final rendered YAML.
  '''
  prej2yml  = yaml.safe_load(yml)
  j2env     = jinja2.Environment()
  j2temp    = j2env.from_string(str(prej2yml))
  postj2yml = j2temp.render(**prej2yml, **environment)

  return yaml.safe_load(postj2yml)
