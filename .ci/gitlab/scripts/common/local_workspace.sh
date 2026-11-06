# Sourced after both checkouts, with CI_PROJECT_DIR pointing at the local workspace.
export SPACK_USER_CACHE_PATH="${CI_PROJECT_DIR}/tmp/_user_cache"
export TMPDIR="${CI_PROJECT_DIR}/tmp"
mkdir -p "${TMPDIR}" "${SPACK_USER_CACHE_PATH}/cache"

# Keep the same relative layout so generated environment includes remain valid.
# Only these paths are transferred; checkouts, bootstrap installs and build stages stay local.
SPACK_CI_TRANSFER_PATHS="jobs_scratch_dir tmp/_user_cache/cache/patches tmp/_user_cache/cache/providers tmp/_user_cache/cache/tags"
for path in $SPACK_CI_TRANSFER_PATHS; do
    if [ -d "${SPACK_CI_SHARED_PROJECT_DIR}/${path}" ]; then
        mkdir -p "${CI_PROJECT_DIR}/${path}"
        cp -Rp "${SPACK_CI_SHARED_PROJECT_DIR}/${path}/." "${CI_PROJECT_DIR}/${path}/"
    fi
done

finish_local_workspace() {
    status=$?
    trap - EXIT
    # GitLab after_script runs in a new shell, so aggregate before removing the local install tree.
    if [ -n "${SPACK_JOB_SPEC_DAG_HASH:-}" ]; then
        "${SPACK_CI_SPACK_ROOT}/bin/spack" python \
            "${SPACK_CI_PACKAGES_ROOT}/.ci/gitlab/scripts/common/aggregate_package_logs.spack.py" \
            --prefix "${SPACK_CI_SPACK_ROOT}/opt/spack" --log install_times.json \
            "${SPACK_ARTIFACTS_ROOT}/user_data/install_times.json" || true
    fi
    for path in $SPACK_CI_TRANSFER_PATHS; do
        if [ -d "${CI_PROJECT_DIR}/${path}" ]; then
            mkdir -p "${SPACK_CI_SHARED_PROJECT_DIR}/${path}" && \
                cp -Rp "${CI_PROJECT_DIR}/${path}/." "${SPACK_CI_SHARED_PROJECT_DIR}/${path}/" || {
                    # Preserve the original job failure if there was one.
                    if [ "$status" -eq 0 ]; then status=1; fi
                }
        fi
    done
    # Do not remove the workspace if persistence failed or the job needs debugging.
    if [ "$status" -eq 0 ]; then
        cd "${SPACK_CI_SHARED_PROJECT_DIR}" || exit 1
        rm -rf "${CI_PROJECT_DIR}"
    fi
    exit "$status"
}
trap finish_local_workspace EXIT
