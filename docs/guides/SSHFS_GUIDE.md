# Guide til at mounte EC2-serveren som en lokal mappe

## Hvad er SSHFS?

SSHFS (SSH File System) gør det muligt at mounte en remote mappe via SSH, så du kan se og redigere filer på EC2-serveren direkte i dit lokale filsystem - ligesom en normal mappe!

## Installation

Første gang skal du installere SSHFS:

```bash
sudo apt update
sudo apt install -y sshfs
```

## Brug

### Mounte serveren

Kør dette script for at mounte EC2-serveren:

```bash
./mount_ec2.sh
```

Dette vil:
- Installere SSHFS hvis det ikke er installeret
- Oprette en mappe `~/ec2_mount` (hvis den ikke findes)
- Mounte EC2-serverens `/home/ubuntu` mappe til `~/ec2_mount`

Efter mounting kan du:
- Se filer: `ls ~/ec2_mount`
- Redigere filer: `nano ~/ec2_mount/fil.txt`
- Kopiere filer: `cp ~/ec2_mount/fil.txt ~/lokalt/`
- Oprette mapper: `mkdir ~/ec2_mount/ny_mappe`

### Unmounte serveren

Når du er færdig, unmount serveren:

```bash
./unmount_ec2.sh
```

Eller manuelt:

```bash
fusermount -u ~/ec2_mount
```

## Vigtigt

- **Husk at unmounte** før du lukker terminalen eller slukker computeren
- Filerne er stadig på serveren - du ser dem bare lokalt
- Ændringer gemmes direkte på serveren
- Hvis forbindelsen bryder, skal du unmounte og mounte igen

## Fejlfinding

Hvis mounting fejler:
1. Tjek at SSH-forbindelsen virker: `ssh ec2`
2. Tjek at mount point mappen findes: `ls -la ~/ec2_mount`
3. Prøv at unmounte først: `fusermount -u ~/ec2_mount`

