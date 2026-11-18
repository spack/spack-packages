#!/bin/zsh

prev_release=$1
current_release="v$(date +%Y.%m)"

extract_package_names() {
  sed 's/^.*packages\/\([^\/]\+\)\/package\.py$/*  \1/g' $1 > .tmp$1
  sed 's/_/-/g' .tmp$1 >> CHANGELOG.$current_release
}

format_header() {
  current_version="$current_release"
  prev_version="$prev_release"
  spack_min_version="1.0.0" # TODO denote this for the build cache and the Package API seperately
  package_api="2.2" # TODO Extract from repo.yaml
  bc_layout_version="3"
  spack_cur_version="1.2.0"
  spack_cur_version_major="1"
  spack_cur_version_minor="2"
  spack_cur_version_patch="0"
  spack_cur_commit="63943396d634faa92cb59474df3558ec9b9b2425"
  count_packages=$(find ./repos -name package.py | wc -l)
  count_packages_prev="8752" # TODO compute this


  cp CHANGELOG.header.template CHANGELOG.header.$current_release
  sed -i "s/{{count_packages_prev}}/$count_packages_prev/g" CHANGELOG.header.$current_release
  sed -i "s/{{current_version}}/$current_version/g" CHANGELOG.header.$current_release
  sed -i "s/{{prev_version}}/$prev_version/g" CHANGELOG.header.$current_release
  sed -i "s/{{spack_min_version}}/$spack_min_version/g" CHANGELOG.header.$current_release
  sed -i "s/{{package_api}}/$package_api/g" CHANGELOG.header.$current_release
  sed -i "s/{{bc_layout_version}}/$bc_layout_version/g" CHANGELOG.header.$current_release
  sed -i "s/{{spack_cur_version}}/$spack_cur_version/g" CHANGELOG.header.$current_release
  sed -i "s/{{spack_cur_version_major}}/$spack_cur_version_major/g" CHANGELOG.header.$current_release
  sed -i "s/{{spack_cur_version_minor}}/$spack_cur_version_minor/g" CHANGELOG.header.$current_release
  sed -i "s/{{spack_cur_version_patch}}/$spack_cur_version_patch/g" CHANGELOG.header.$current_release
  sed -i "s/{{spack_cur_commit}}/$spack_cur_commit/g" CHANGELOG.header.$current_release
  sed -i "s/{{count_packages}}/$count_packages/g" CHANGELOG.header.$current_release
  sed -i "s/{{count_packages_prev}}/$count_packages_prev/g" CHANGELOG.header.$current_release
}

format_header
cat CHANGELOG.header.$current_release > CHANGELOG.$current_release

git diff --name-status "releases/$prev_release".."releases/$current_release" | grep "package.py" > .rel-files.txt

grep "^A" .rel-files.txt > .rel-new-packages.txt
echo "
### New packages
" >> CHANGELOG.$current_release
extract_package_names .rel-new-packages.txt >> CHANGELOG.$current_release

grep "^D" .rel-files.txt > .rel-del-packages.txt
echo "
### Removed packages
" >> CHANGELOG.$current_release
extract_package_names .rel-del-packages.txt >> CHANGELOG.$current_release

git log --name-only -S "\+.*deprecated=True" "releases/$prev_release".."releases/$current_release" | grep "package.py" > .rel-deprecated.txt
extract_package_names .rel-deprecated.txt >> CHANGELOG.$current_release

# Add a newline to the end of the changelog
echo >> CHANGELOG.$current_release

cat CHANGELOG.$current_release

if read -q "choice?Commit? [Yn] "; then
  cat CHANGELOG.$current_release CHANGELOG.md > CHANGELOG.md.tmp
  mv CHANGELOG.md.tmp CHANGELOG.md
else
  echo
  echo "goodbye"
fi
