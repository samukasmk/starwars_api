#!/usr/bin/env bash

GIT_DIR=$(git rev-parse --git-dir)

echo "Installing hooks..."
ln -s scripts/git-hooks/hooks/pre-commit $GIT_DIR/hooks/pre-commit
ln -s scripts/git-hooks/hooks/commit-msg $GIT_DIR/hooks/commit-msg
echo "Done"!