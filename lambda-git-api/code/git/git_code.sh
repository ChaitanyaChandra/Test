#!/bin/bash

rm -rf /tmp/repo || true

# Set the repository URL and target directory
REPO_URL="https://chaitanya-chandra:$1@github.com/chaitu-org/test.git"
TARGET_DIR="/tmp/repo"

# Set your Git username and email
GIT_USERNAME="chaitanyachandra"
GIT_EMAIL="chay@outlook.in"

# Clone the repository
git clone $REPO_URL $TARGET_DIR


# Change into the cloned repository directory
cd $TARGET_DIR

# Set the Git configuration for the script
git config user.name "$GIT_USERNAME"
git config user.email "$GIT_EMAIL"

# Make changes to the repository
# Example: Create a new file
IST=$(TZ='Asia/Kolkata' date +'%T %Z')
echo "time is $IST" > new_file.txt

# Stage the changes
git add new_file.txt

# Commit the changes
git commit -m "Added at $IST"

# Push the changes to the remote repository
git push origin main
