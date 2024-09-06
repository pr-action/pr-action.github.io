#!/bin/sh
apt install build-essential
pip install -r requirements.txt
pip install .
python setup.py build
STATICPR_LIB_PATH=$(find build/ -maxdepth 1 -type d -name 'lib.*' -print -quit | xargs -I {} sh -c "find {} -type f -name 'staticpr*' -print -quit | sed 's|^./||'")
pip install pyinstaller
pyinstaller --add-binary ${STATICPR_LIB_PATH}:. --copy-metadata codecov-cli --hidden-import staticpr_languages -F pr_action/main.py
cp ./dist/main ./dist/praction_$1
