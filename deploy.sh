set -e
git add -u . || true
git commit -mcommit || true
git pull --rebase
uv run pelican content -s pelicanconf.py
cp CNAME docs/CNAME
git add docs
git commit -mdocs
git push
