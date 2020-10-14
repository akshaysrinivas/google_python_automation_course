#!/bin/bash

for file in *.pdf; do
    name=$(basename "$file" .pdf)
    mv "$file" "$name.docx"
done
