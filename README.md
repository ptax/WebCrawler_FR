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


##Run dev environment
```bash
cd /path/to/project/root
docker-compose -f docker/docker-compose-dev.yml up
```

##Update project in prod
```bash
cd /project/gwparser/batch
git pull
/project/gwparser/batch/update
```

#Run tests in docker

```bash
docker exec -it docker_wiki_parser_python_1 python /app/tests/wiki_fr_parser.py
```

