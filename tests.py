import os
import pathlib
import yaml
import pytest

def test_yamls():
  files = [x for x in os.listdir(".") if x.endswith(("yaml","yml",))]
  print(files)
  for file in files:
    with open(file, 'r') as stream:
      try:
        return yaml.safe_load(stream)
      except yaml.YAMLError as exception:
        raise exception
        
        
