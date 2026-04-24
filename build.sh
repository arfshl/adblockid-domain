#!/bin/sh

# fetch from upstream
curl -o ubl_gambling_raw.txt -L https://github.com/realodix/AdBlockID-src/raw/refs/heads/main/src/addons/ubl_gambling.txt
curl -o badware_raw.adfl -L https://github.com/realodix/AdBlockID-src/raw/refs/heads/main/src/addons/badware.adfl
curl -o ubl_porn_int_raw.txt -L https://github.com/realodix/AdBlockID-src/raw/refs/heads/main/src/addons/ubl_porn_int.txt
curl -o ubl_porn_id_raw.txt -L https://github.com/realodix/AdBlockID-src/raw/refs/heads/main/src/addons/ubl_porn_id.txt
curl -o ubl_badware_raw.txt -L https://github.com/realodix/AdBlockID-src/raw/refs/heads/main/src/addons/ubl_badware.txt

# convert to domain-only format
# depends: python
rm -r filters
mkdir -p filters
python3 scripts/cleanup.py ubl_gambling_raw.txt -o filters/ubl_gambling.txt
python3 scripts/cleanup.py badware_raw.adfl -o filters/badware.txt
python3 scripts/cleanup.py ubl_porn_int_raw.txt -o filters/ubl_porn_int.txt
python3 scripts/cleanup.py ubl_porn_id_raw.txt -o filters/ubl_porn_id.txt
python3 scripts/cleanup.py ubl_badware_raw.txt -o filters/ubl_badware.txt

# delete original files
rm *_raw.*