# Bash dotfile

## Header

```bash
##      _______
##     /          /     /
##    --------   /_____/
##          /   /     /
##  --------   /     /
##
## Author: Sujith Sudarshan
```

## Alias

```bash
alias ll='ls -l'
alias la='ls -A'
alias l='ls -CF'
alias ~='cd ~'
alias ..='cd ..'
alias ...='cd ../..'
alias ..3='cd ../../..'
alias ..4='cd ../../..'
```

## Fix missing XDG_RUNTIME_DIR

```bash
if [ -z "$XDG_RUNTIME_DIR" ]; then
  # Try systemd created path
  XDG_RUNTIME_DIR=/run/user/$UID
  if [ ! -d "$XDG_RUNTIME_DIR" ]; then
    # systemd-created directory doesn't exist
    XDG_RUNTIME_DIR=/tmp/$USER-runtime
    if [ ! -d "$XDG_RUNTIME_DIR" ]; then
      mkdir -m 0700 "$XDG_RUNTIME_DIR"
    fi
  fi
fi

# Check dir has got the correct type, ownership, and permissions
if ! [[ -d "$XDG_RUNTIME_DIR" && -O "$XDG_RUNTIME_DIR" &&
    "$(stat -c '%a' "$XDG_RUNTIME_DIR")" = 700 ]]; then
  echo "\$XDG_RUNTIME_DIR: permissions problem with $XDG_RUNTIME_DIR:" >&2
  ls -ld "$XDG_RUNTIME_DIR" >&2
  XDG_RUNTIME_DIR=$(mktemp -d /tmp/"$USER"-runtime-XXXXXX)
  echo "Set \$XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR" >&2
fi
```

