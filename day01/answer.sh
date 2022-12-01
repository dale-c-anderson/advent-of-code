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
ANSWER_part1=$(sort -V "$SUMS" |tail -1)


echo "part 1: $ANSWER_part1"

ANSWER_par2=$(sort -V "$SUMS" |tail -3 | /usr/bin/awk '{s+=$1} END {print s}')
echo "part 2: $ANSWER_par2"
