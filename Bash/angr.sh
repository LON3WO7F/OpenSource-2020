#!/bin/bash
cmd="bash"
if [ "$1" != "bash" ]; then
  cmd="source /usr/share/virtualenvwrapper/virtualenvwrapper.sh && workon angr && python3 $@"
fi
#echo $cmd
mkdir -p output
docker run -it --rm -v "$PWD":/data:ro -v "$PWD/output":/data/output -w "/data" -u angr angr/angr bash -c "$cmd"
