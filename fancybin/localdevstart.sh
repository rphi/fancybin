#!/bin/bash

# make sure we stop all background tasks when the server is shut down
trap_with_arg() { # from https://stackoverflow.com/a/2183063/804678
  local func="$1"; shift
  for sig in "$@"; do
    trap "$func $sig" "$sig"
  done
}

stop() {
  trap - SIGINT EXIT
  printf '\n%s\n' "recieved $1, killing children"
  kill -s SIGINT 0
}

trap_with_arg 'stop' EXIT SIGINT SIGTERM SIGHUP

# Now, let's get things started...
echo "Getting local dev server for FancyBin ready to go..."
echo "----------------------------------------------------"

echo ">>> Installing yarn dependencies"
yarn install
if [ $? -ne 0 ]; then
    echo "Error running yarn install. Exiting"
    exit $?
fi

echo ">>> Building Monaco workers"
ROOT=$PWD/node_modules/monaco-editor/esm/vs
OPTS="--no-source-maps --log-level 1 --out-dir ./static/dist --public-url ./"        # Parcel options - See: https://parceljs.org/cli.html

echo " - JSON worker..."
npx parcel build $ROOT/language/json/json.worker.js $OPTS
echo " - CSS worker..."
npx parcel build $ROOT/language/css/css.worker.js $OPTS
echo " - HTML worker..."
npx parcel build $ROOT/language/html/html.worker.js $OPTS
echo " - TypeScript worker..."
npx parcel build $ROOT/language/typescript/ts.worker.js $OPTS
echo " - Editor worker..."
npx parcel build $ROOT/editor/editor.worker.js $OPTS

echo ">>> Starting parcel for static/vendor assets"
npx parcel watch ./static/src/*.js --out-dir ./static/dist --public-url ./ &

echo ">>> Checking we have a virtual env for Django"
ROOTDIR=$(dirname "$0")
if [ ! -d "$ROOTDIR/.venv" ]; then
  echo "No .venv found."
  bash ./localdevbootstrap.sh
fi

echo ">>> Activating virtualenv"
source ./localdevvenv.sh

# echo ">>> Setting environment variables"
# if [ ! -f ./envfile.sh ]; then
#     echo "Can't find envfile.sh, create this from the template first."
#     exit 1
# fi
# source ./envfile.sh

echo ">>> Running any pending Django migrations"
python3 manage.py migrate

echo ">>> Starting Django development server"
python3 manage.py runserver 0.0.0.0:8008
