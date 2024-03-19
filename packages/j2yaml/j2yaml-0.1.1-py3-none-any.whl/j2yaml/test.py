import main as j2yaml
import unittest

yml = """---
var: testing
foo: "{{ testvar }}"
bar:
  - str1
  - str2
mutated: "{{ var }}"
..."""


class Test(unittest.TestCase):
  def setUp(self):
    self.testvar = 'asdqwe'
    self.data = j2yaml.load(yml, {'testvar':self.testvar})
  
  def test_var(self):
    self.assertEqual(self.data["var"], 'testing', 'The loaded YAML-variable "var" is wrong.')
  def test_env(self):
    self.assertEqual(self.data["foo"], self.testvar, 'The injected variable to the template-environment is wrong.')
  def test_mut(self):
    self.assertEqual(self.data["mutated"], 'testing', 'The mutated variable is wrong.')

if __name__ == '__main__':
  unittest.main()
