# Fetch and checkout the latest passing develop
release_ref=${1-:snapshots/develop-latest}
git fetch origin "$release_ref"
git checkout "$release_ref"

# Create and push the branch
branch="releases/v$(date +%Y.%m)"
git checkout -b "$branch"
git push origin "$branch"
