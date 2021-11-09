import os
import pathlib
import yaml
import pytest

def test_yamls():
  files = [x for os.listdir(".") if pathlib.Path(x).suffix == "yaml"]
  for file in files:
    with open(file, 'r') as stream:
      try:
        return yaml.load(stream)
      except yaml.YAMLError as exception:
        raise exception
        
        
