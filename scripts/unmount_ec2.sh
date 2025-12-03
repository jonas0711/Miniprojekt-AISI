#!/bin/bash
# Script til at unmounte EC2-serveren

MOUNT_POINT="$HOME/ec2_mount"

if mountpoint -q "$MOUNT_POINT"; then
    echo "Unmounter serveren fra $MOUNT_POINT..."
    fusermount -u "$MOUNT_POINT"
    if [ $? -eq 0 ]; then
        echo "✅ Serveren er nu unmountet"
    else
        echo "❌ Fejl ved unmounting. Prøv: sudo fusermount -u $MOUNT_POINT"
    fi
else
    echo "Serveren er ikke mountet på $MOUNT_POINT"
fi

