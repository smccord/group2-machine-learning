#!/usr/bin/env bash

set -e

# Tag the latest build with the short git sha as well as version of key runtimes
# and packages.
GIT_SHA_TAG=${SOURCE_COMMIT:0:12}
docker tag $IMAGE_NAME "$DOCKER_REPO:$GIT_SHA_TAG"
PY_VERSION_TAG="python-$(docker run --rm ${IMAGE_NAME} python --version 2>&1 | awk '{print $2}')"
docker tag $IMAGE_NAME "$DOCKER_REPO:$PY_VERSION_TAG"
