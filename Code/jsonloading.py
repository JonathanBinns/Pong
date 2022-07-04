def loadjson(filename):
    import os, json
    file = f"Json/{filename}.json"
    with open(file, 'r') as f:
        data = json.load(f)
    return data

def writejson(filename, data):
    import os, json
    file = f"Json/{filename}.json"
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, separators=(',', ': '))
