from gendiff.gendiff import generate_diff
import json
import yaml


flat_json_one = json.load(open('./tests/fixtures/flat_json1.json'))
flat_json_two = json.load(open('./tests/fixtures/flat_json2.json'))
json_one = json.load(open('./tests/fixtures/json_file1.json'))
json_two = json.load(open('./tests/fixtures/json_file2.json'))

flat_yaml_one = yaml.safe_load(open('./tests/fixtures/flat_yaml1.yml'))
flat_yaml_two = yaml.safe_load(open('./tests/fixtures/flat_yaml2.yml'))

flat_json_and_yaml_true = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}
'''

template = '''{
    common: {
      + follow: False
        setting1: Value 1
      - setting2: 200
      - setting3: True
      + setting3: None
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
'''

def test_flat_json():
    assert generate_diff(flat_json_one, flat_json_two) == flat_json_and_yaml_true


def test_flat_yaml():
    assert generate_diff(flat_yaml_one, flat_yaml_two) == flat_json_and_yaml_true


def test_json_files():
    assert generate_diff(json_one, json_two) == template
