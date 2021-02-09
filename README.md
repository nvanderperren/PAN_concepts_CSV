# PAN for MEDEA

## Getting started

Clone this repository

```bash
git clone https://github.com/nvanderperren/PAN_concepts_CSV.git && cd PAN_concepts_CSV
```

Export all PAN concepts from https://data.cultureelerfgoed.nl/term/id/pan/PAN.html and save it as `response.json` in the `PAN_concepts_CSV` folder.

```
https://data.cultureelerfgoed.nl/PoolParty/api/7.0/projects/1E267A03-76FD-0001-F681-567064301637/export?format=rdf/json&exportModules=concepts
```

Use an API tool like Postman, or `curl` if you prefer the command line. You need a username and password.

Execute `script.py`.

```
python3 script.py
```

You get an `pan_data.csv` in the folder with all concepts for MEDEA.
