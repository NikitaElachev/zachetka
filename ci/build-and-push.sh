#!/usr/bin/env bash
set -euo pipefail

branch="${1:-${TEAMCITY_BUILD_BRANCH:-main}}"
image_repo="${IMAGE_REPO:-antonnest/zachetka}"
build_number="${2:-${TEAMCITY_BUILD_NUMBER:-local}}"
safe_branch="$(printf '%s' "$branch" | tr '/_' '--' | tr -cd '[:alnum:].-')"
image="${image_repo}:ci-${safe_branch}-${build_number}"

echo "Building ${image} from branch ${branch}"
docker build -t "$image" .
docker run --rm "$image" python -c 'from main import health; assert health()["status"] == "ok"'

case "$branch" in
  dev|prod)
    release="${image_repo}:${branch}"
    docker tag "$image" "$release"
    docker push "$release"
    echo "Published ${release}"
    ;;
  *)
    echo "Build checked; no publishing rule for branch ${branch}"
    ;;
esac
