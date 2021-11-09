import os
import pathlib
import yaml
import pytest

def test_yamls():
  files = [x for x in os.listdir(".") if x.endswith(("yaml","yml",))]
  print(files)
  assert False
  for file in files:
    print(file)
    with open(file, 'r') as stream:
      try:
        return yaml.load(stream)
      except yaml.YAMLError as exception:
        raise exception
        
        
