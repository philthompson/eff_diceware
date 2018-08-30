#!/bin/bash

FILE1="${1}"
FILE2="${2}"

FILE1_WORDS="$(awk '{print $2}' "${FILE1}")"
FILE2_WORDS="$(awk '{print $2}' "${FILE2}")"

echo "words removed:"
echo "${FILE1_WORDS}" | while read WORD; do
  if [ -z "$(echo "${FILE2_WORDS}" | grep -m 1 "^${WORD}$")" ]; then
    echo $WORD
  fi
done | sort | paste -d '|' - - - - - - | sed 's/^/|/' | sed 's/$/|/'

echo
echo "words added:"
echo "${FILE2_WORDS}" | while read WORD; do
  if [ -z "$(echo "${FILE1_WORDS}" | grep -m 1 "^${WORD}$")" ]; then
    echo $WORD
  fi
done | sort | paste -d '|' - - - - - - | sed 's/^/|/' | sed 's/$/|/'

