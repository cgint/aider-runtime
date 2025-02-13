#! /bin/bash

SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Checking for new versions ..."
cd $SOURCE_DIR
poetry update