set -e
git add -u . || true
git commit -mcommit || true
git pull --rebase
./venv/bin/pelican content -s pelicanconf.py
cp keybase.txt docs/
cp CNAME docs/CNAME
git add docs
git commit -mdocs
git push
