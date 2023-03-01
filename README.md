بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ

# bless

Qur'an for Desktop using [Qur'an Server](https://github.com/bal-sm/quran_server) API (WORK IN PROGRESS)

## How-to run

This project is still in early stages of development, but here's how to install the latest build:

### Install Python

[Download](https://www.python.org/downloads/)

> Make sure to install the 3.11 version.

### Install pipx (Optional)

Run this command:

```bash
python3 -m pip install --user pipx
```

### Ensure path (after installing pipx)

Don't forget to run this command after installing pipx:

```bash
python3 -m pipx ensurepath
```

### Install bless

```bash
pipx install git+https://github.com/bal-sm/bless.git
```

### Load fixture

[Download An-Nas fixture](https://raw.githubusercontent.com/bal-sm/bless_server/master/dquran/fixtures/dquran.An-Nas.yaml), then _Save Page as..._, and put it on somewhere.

Run this command on the folder which you put the fixture in:

```sh
bless-server-manage loaddata dquran.An-Nas.yaml
```

### Start bless

```sh
bless-start
```
