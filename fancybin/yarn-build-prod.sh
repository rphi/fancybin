#!/bin/bash

yarn clean

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

echo ">>> Building static/vendor assets with Parcel.js"
npx parcel build ./static/src/*.js --out-dir ./static/dist --public-url ./
