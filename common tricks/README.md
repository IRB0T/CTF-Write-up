# Common-Tricks

1. Recursively unzip zip files command
======		
Command : while [ "`find . -type f -name '*.zip' | wc -l`" -gt 0 ]; do find -type f -name "*.zip" -exec unzip -- '{}' \; -exec rm -- '{}' \;; done
or 
command : find . -name "*.zip" -exec unzip {} \;

