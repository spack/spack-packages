#!/usr/bin/env bash
# Run from any directory: bash .ci/gitlab/scripts/common/test_local_workspace.sh
set -eu
helper="$(cd "$(dirname "$0")" && pwd)/local_workspace.sh"
mkdir -p /tmp/pi-agent/gitlab-local-workspace
root=$(mktemp -d /tmp/pi-agent/gitlab-local-workspace/test.XXXXXXXXXX)
trap 'rm -rf "$root"' EXIT

run_job() {
    local job=$1 status=$2
    mkdir -p "$root/$job/local" "$root/$job/shared"
    CI_PROJECT_DIR="$root/$job/local" \
    SPACK_CI_SHARED_PROJECT_DIR="$root/$job/shared" \
    SPACK_CI_GENERATE="$3" SPACK_CI_STACK_NAME=smoke \
    bash -eu -c '
        cd "$CI_PROJECT_DIR"
        . "$1"
        test "$SPACK_USER_CACHE_PATH" = "$CI_PROJECT_DIR/tmp/_user_cache"
        test "$TMPDIR" = "$CI_PROJECT_DIR/tmp"
        output=jobs_scratch_dir/smoke
        if [ -z "$SPACK_CI_GENERATE" ]; then
            test -f "$output/concrete_environment/spack.lock"
            echo build-only > "$output/concrete_environment/build-only"
            for cache in patches providers tags; do
                test -f "$SPACK_USER_CACHE_PATH/cache/$cache/entry"
            done
        fi
        for cache in patches providers tags; do
            mkdir -p "$SPACK_USER_CACHE_PATH/cache/$cache"
            echo cached > "$SPACK_USER_CACHE_PATH/cache/$cache/entry"
        done
        # These heavy directories must never be copied back.
        mkdir -p .git opt/spack "$SPACK_USER_CACHE_PATH/bootstrap" "$TMPDIR/stage"
        mkdir -p "$output/concrete_environment" "$output/logs"
        echo environment > "$output/concrete_environment/spack.yaml"
        echo lock > "$output/concrete_environment/spack.lock"
        echo pipeline > "$output/cloud-ci-pipeline.yml"
        echo log > "$output/logs/build.log"
        exit "$2"
    ' bash "$helper" "$status"
}

run_job generate 0 generate
output="$root/generate/shared/jobs_scratch_dir/smoke"
test -f "$output/concrete_environment/spack.yaml"
test -f "$output/concrete_environment/spack.lock"
test -f "$output/cloud-ci-pipeline.yml"
test -f "$output/logs/build.log"
for cache in patches providers tags; do
    test -f "$root/generate/shared/tmp/_user_cache/cache/$cache/entry"
done
test ! -e "$root/generate/shared/.git"
test ! -e "$root/generate/shared/opt"
test ! -e "$root/generate/shared/tmp/_user_cache/bootstrap"
test ! -e "$root/generate/shared/tmp/stage"
test ! -e "$root/generate/local"

# A different node/workspace restores the environment, including relative includes.
mkdir -p "$root/build/shared"
cp -Rp "$root/generate/shared/." "$root/build/shared/"
run_job build 0 ""
test -f "$root/build/shared/jobs_scratch_dir/smoke/logs/build.log"
test -f "$root/build/shared/jobs_scratch_dir/smoke/concrete_environment/build-only"
test ! -e "$root/build/local"

# Preserve the failure status while still publishing available generation output.
status=0
run_job failed 7 generate || status=$?
test "$status" -eq 7
test -f "$root/failed/shared/jobs_scratch_dir/smoke/cloud-ci-pipeline.yml"
test -d "$root/failed/local"

# Missing output (e.g. early failure) must not replace the original exit status.
mkdir -p "$root/early/local" "$root/early/shared"
status=0
CI_PROJECT_DIR="$root/early/local" SPACK_CI_SHARED_PROJECT_DIR="$root/early/shared" \
SPACK_CI_GENERATE=generate SPACK_CI_STACK_NAME=smoke \
bash -eu -c '. "$1"; exit 9' bash "$helper" || status=$?
test "$status" -eq 9

# A failed copy-back must fail a successful job and retain its local files.
mkdir -p "$root/copy-failed/local/jobs_scratch_dir" "$root/copy-failed/shared"
touch "$root/copy-failed/shared/jobs_scratch_dir"
status=0
CI_PROJECT_DIR="$root/copy-failed/local" \
SPACK_CI_SHARED_PROJECT_DIR="$root/copy-failed/shared" \
bash -eu -c '. "$1"' bash "$helper" 2>/dev/null || status=$?
test "$status" -ne 0
test -d "$root/copy-failed/local"

echo 'Local workspace checks passed'
