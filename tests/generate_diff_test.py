from gendiff.gendiff import generate_diff
import json


file1 = json.load(open('./tests/fixtures/file_one.json'))
file2 = json.load(open('./tests/fixtures/file_two.json'))

def test_answer():
    assert generate_diff(file1, file2) == '{\n  - follow: False\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: True\n}'
