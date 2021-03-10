def make_inner(json):
    if isinstance(json, dict):
        items = {}
        for item in json:
            items[item] = make_inner(json[item])
        return {'type': 'dict', 'items': items}
    return {'type': 'value', 'value': json}


def merge(json1, json2):
    if json1 is None:
        return {
            'type': 'add',
            'value': json2
        }
    if json2 is None:
        return {
            'type': 'del',
            'value': json1
        }

    if json1['type'] == 'dict' and json2['type'] == 'dict':
        items = {}
        for key in {*json1['items'], *json2['items']}:
            items[key] = merge(json1['items'].get(key), json2['items'].get(key))
        return {'type': 'dict',
                'items': items}

    if json1 == json2:
        return json1

    return {
        'type': 'diff',
        'old': json1,
        'new': json2
    }


def render(tree):
    return render_ts(tree, 0)


def necessary_action(item):
    actions = {
        'value': render_val,
        'del': render_del,
        'add': render_add,
        'diff': render_diff
    }
    return actions[item['type']]


def render_dict(tree, ts=0):
    res = ''
    for key in sorted(tree['items'].keys()):
        item = tree['items'][key]
        if item['type'] == 'dict':
            res += ' ' * ts + '    ' + str(key) + ': '
            res += render_ts(item, ts + 4)
        else:
            action = necessary_action(item)
            res += action(key, item, ts)
    return res


def render_ts(tree, ts=0):
    res = ''
    if tree['type'] == 'dict':
        res += '{\n'
        res += render_dict(tree, ts)
        res += ' ' * ts + '}\n'
        return res

    if tree['type'] in ['value', 'add', 'del']:
        res += str(tree['value'])
        res += '\n'
        return res

    return res


def render_val(key, val, ts):
    res = ' ' * ts + '    ' + str(key) + ': '
    res += render_ts(val, ts + 4)
    return res


def render_del(key, val, ts):
    res = ' ' * ts + '  - ' + str(key) + ': '
    res += render_ts(val['value'], ts + 4)
    return res


def render_add(key, val, ts):
    res = ' ' * ts + '  + ' + str(key) + ': '
    res += render_ts(val['value'], ts + 4)
    return res


def render_diff(key, val, ts):
    res = ' ' * ts + '  - ' + str(key) + ': '
    res += render_ts(val['old'], ts + 4)
    res += ' ' * ts + '  + ' + str(key) + ': '
    res += render_ts(val['new'], ts + 4)
    return res


def generate_diff(file1, file2):
    i1 = make_inner(file1)
    i2 = make_inner(file2)
    merged = merge(i1, i2)
    return render(merged)
