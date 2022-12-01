#!/bin/bash
set -eu -o pipefail

TEMPDIR=$(mktemp -d)
SUMS=$(mktemp)
INPUT="$(pwd)/input.txt"

cd "$TEMPDIR";
/usr/bin/csplit  "$INPUT" '/^$/' --elide-empty-files '{*}' --quiet
for FILE in "$TEMPDIR/"*; do
  /usr/bin/awk '{s+=$1} END {print s}' "$FILE" >> "$SUMS"
done
ANSWER=$(sort -V "$SUMS" |tail -1)


echo "$ANSWER"
