```
 7153  find . -type f \( -name "*.md" -o -name "*.c" -o -name "Makefile" -o -name "*.py" \) -print
 7154  find . -type f \( -name "*.md" -o -name "*.c" -o -name "Makefile" -o -name "*.py" \) -exec rm {} +
7158  mkdir ../drill
 7159  find . -type f -exec cp {} ../drill/ \;
 python3 mk_docker.py
 ./upload.sh
 ```
