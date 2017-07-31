Run tests in docker

```
docker exec -it docker_wiki_parser_python_1 sh -c 'export PYTHONPATH="$PYTHONPATH:/app/" && export PYTHONIOENCODING="utf-8" && python /app/tests/wiki_fr_parser.py'
```