from gendiff.gendiff import generate_diff
import json
import yaml


flat_json_one = json.load(open('./tests/fixtures/file_one.json'))
flat_json_two = json.load(open('./tests/fixtures/file_two.json'))
flat_yaml_one = yaml.safe_load(open('./tests/fixtures/flat_yaml1.yml'))
flat_yaml_two = yaml.safe_load(open('./tests/fixtures/flat_yaml2.yml'))

def test_flat_json():
    assert generate_diff(flat_json_one, flat_json_two) == '{\n  - follow: False\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: True\n}'


def test_flat_yaml():
    assert generate_diff(flat_yaml_one, flat_yaml_two) == '{\n  - follow: False\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: True\n}'
