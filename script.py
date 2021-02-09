import json
import csv

# concepts
HAS_LABEL="http://www.w3.org/2004/02/skos/core#prefLabel"
HAS_START="https://data.cultureelerfgoed.nl/vocab/id/pan#hasInitialDate"
HAS_END="https://data.cultureelerfgoed.nl/vocab/id/pan#hasFinalDate"
HAS_NOTE="http://www.w3.org/2004/02/skos/core#scopeNote"
HAS_IMAGE="https://data.cultureelerfgoed.nl/vocab/id/pan#hasImage"
HAS_BROADER = "http://www.w3.org/2004/02/skos/core#broader"

# CSV header met URI, name, description, start_date, end_date, image, broader_term,

def get_value(record, concept, multilangual = False):
    value = ''
    if concept in record:
        items = record[concept]
        for item in items:
            if multilangual:
                if item['lang'] == 'nl':
                    value = item['value'].encode('utf-8')
            else: 
                value = item['value'].encode('utf-8')
    return value

def is_middelages(begin_date, end_date):
    try: 
        if int(end_date) < 950:
            return False
        elif int(begin_date) > 1500:
            return False
    except:
        return True
    return True

def get_line(record):
    line = []
    label = get_value(record, HAS_LABEL, True).rstrip()
    scope_note = get_value(record, HAS_NOTE, True).rstrip()
    initial_date = get_value(record, HAS_START).rstrip()
    end_date = get_value(record, HAS_END).rstrip()
    image = get_value(record, HAS_IMAGE).rstrip()
    broader = get_value(record, HAS_BROADER).rstrip()
    if is_middelages(initial_date, end_date):
        line = [label, scope_note, initial_date, end_date, image, broader]
    return line

def get_items():
    lines = []
    json_file = open("response.json", 'r')
    content = json.load(json_file)
    keys = content.keys()
    keys.sort()
    for key in keys:
        if len(key) < 54 and len(key) > 45 and not (key.encode('utf-8').endswith('ABR') 
        or key.encode('utf-8').endswith('PAN') or key.encode('utf-8').endswith('adms/0.1')
        or key.encode('utf-8').endswith('brooch') or key.encode('utf-8').endswith('period')):
            record = content[key]
            line = get_line(record)
            if len(line) > 0:
                line.insert(0,key.encode('utf-8'))
                lines.append(line)
    json_file.close()
    return lines

def create_csv(lines):
    csv_file = open("pan_data.csv", 'w')
    writer = csv.writer(csv_file)
    header = ["URI", "name", "description", "start_date", "end_date", "image", "parent"]
    rows = [header]
    rows.extend(lines)
    writer.writerows(rows)
    csv_file.close()

items = get_items()
create_csv(items)
