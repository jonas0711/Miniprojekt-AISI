# Guide til Jonas — sådan logger du ind på EC2-serveren

## 1. Lav en SSH-nøgle på din egen computer

Åbn Terminal og kør:

```bash
ssh-keygen -t rsa -b 4096 -C "jonas"
```

Tryk Enter tre gange.

Dette laver to filer:

* *id_rsa* (privat nøgle — DEL IKKE DENNE)
* *id_rsa.pub* (offentlig nøgle — DEL DENNE)

Nøglerne ligger typisk i:

```
~/.ssh/
```

## 2. Send mig (Peter) din *id_rsa.pub*

Kør:

```bash
cat ~/.ssh/id_rsa.pub
```

Kopiér hele linjen og send den til mig.

Den starter sådan her:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQ...
```

## 3. Når Peter har lagt din nøgle ind på serveren

Du kan så logge ind med:

```bash
ssh -i ~/.ssh/id_rsa ubuntu@ec2-51-21-200-191.eu-north-1.compute.amazonaws.com
```

Hvis din nøgle ligger et andet sted, brug den korrekte sti.

## 4. Første gang — acceptere fingerprint

Skriv:

```
yes
```

Så er du inde på serveren.

---

# Det er alt Jonas skal gøre.

