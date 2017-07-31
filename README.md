Scripts for update data

Wiki Fr

```
graber/france/wiki.py [-f] [-s /path/to/insee/file.csv] [-r 'insee+12345'] [-l 'https://fr.wikipedia.org/wiki/Paris']

-f force update
-s source of insee data
-r request to wiki with search
-l link to wiki page
```


Run tests in docker

```
docker exec -it docker_wiki_parser_python_1 sh -c 'export PYTHONPATH="$PYTHONPATH:/app/" && export PYTHONIOENCODING="utf-8" && python /app/tests/wiki_fr_parser.py'
```

