#!/bin/bash

# Variables
DEVICE="PARTUUID=1a5dcbc1-e65c-422a-b841-8266e3c3e42a" # blkid /dev/sdb2
MOUNT_POINT="/mnt/harddisk"
DEST_DIR="/root/media"
SOURCE_DIR="$MOUNT_POINT"

# Check argument
if [ -z "$1" ]; then
  echo "Usage: sync {movies|tvshows|all}"
  exit 1
fi

# Create mount point if it doesn't exist
mkdir -p "$MOUNT_POINT"

# Mount the external hard disk
mount "$DEVICE" "$MOUNT_POINT"
if [ $? -ne 0 ]; then
  echo "Failed to mount $DEVICE"
  exit 1
fi

# Sync based on argument
case "$1" in
  movies)
    mkdir -p "$DEST_DIR/movies"
    rsync -avh --progress --delete "$SOURCE_DIR/movies/" "$DEST_DIR/movies/"
    ;;
  tvshows)
    mkdir -p "$DEST_DIR/tvshows"
    rsync -avh --progress --delete "$SOURCE_DIR/tvshows/" "$DEST_DIR/tvshows/"
    ;;
  all)
    rsync -avh --progress --delete "$SOURCE_DIR/" "$DEST_DIR/"
    ;;
  *)
    echo "Invalid option: $1"
    echo "Usage: sync {movies|tvshows|all}"
    umount "$DEVICE"
    exit 1
    ;;
esac

# Unmount the disk
umount "$DEVICE"