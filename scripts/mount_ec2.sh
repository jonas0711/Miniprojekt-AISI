#!/bin/bash
# Script til at mounte EC2-serveren som en lokal mappe via SSHFS
# Dette gør det muligt at se og redigere filer på serveren direkte i filsystemet

# Opret mount point hvis det ikke findes
MOUNT_POINT="$HOME/ec2_mount"

# Tjek om SSHFS er installeret
if ! command -v sshfs &> /dev/null; then
    echo "❌ SSHFS er ikke installeret lokalt!"
    echo ""
    echo "Installér det med:"
    echo "  sudo apt update"
    echo "  sudo apt install -y sshfs"
    echo ""
    exit 1
fi

# Opret mount point mappe hvis den ikke findes
if [ ! -d "$MOUNT_POINT" ]; then
    echo "Opretter mount point: $MOUNT_POINT"
    mkdir -p "$MOUNT_POINT"
fi

# Tjek om mappen allerede er mountet
if mountpoint -q "$MOUNT_POINT"; then
    echo "Serveren er allerede mountet på $MOUNT_POINT"
    echo "For at unmounte, kør: fusermount -u $MOUNT_POINT"
    exit 0
fi

# Mount serveren
echo "Monterer EC2-serveren på $MOUNT_POINT..."
sshfs ec2:/home/ubuntu "$MOUNT_POINT" -o default_permissions

if [ $? -eq 0 ]; then
    echo "✅ Serveren er nu mountet på $MOUNT_POINT"
    echo "Du kan nu se filerne i: $MOUNT_POINT"
    echo ""
    echo "For at unmounte, kør: fusermount -u $MOUNT_POINT"
else
    echo "❌ Fejl ved mounting. Tjek at SSH-forbindelsen virker med: ssh ec2"
fi

