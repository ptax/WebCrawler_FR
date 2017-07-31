#Scripts for update data

##Wiki France parser command

```
graber/france/wiki.py [-f] [-s /path/to/insee/file.csv] [-r 'insee+12345'] [-l 'https://fr.wikipedia.org/wiki/Paris']

-f force update
-s source of insee data
-r request to wiki with search
-l link to wiki page
```

#Environment

install docker with docker-compose


##Run commands
```
cd /path/to/project/root
docker-compose -f docker/docker-compose.yml up
```


#Run tests in docker

```
docker exec -it docker_wiki_parser_python_1 sh -c 'export PYTHONPATH="$PYTHONPATH:/app/" && export PYTHONIOENCODING="utf-8" && python /app/tests/wiki_fr_parser.py'
```

