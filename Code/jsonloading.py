# these two functions are very straightforward, they just make reading and writing to json files simple
# by opening and closing the file in a single function, corruption of these important data files is avoided
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
