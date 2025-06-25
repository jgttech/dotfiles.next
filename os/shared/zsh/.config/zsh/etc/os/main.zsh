#!/usr/bin/env zsh
if [[ $(uname) == "Darwin" ]]; then
  darwin="${DOTFILES_ZSH_DIR}/etc/os/darwin.zsh"
  [[ -f "$darwin" ]] && source "$darwin"
elif command -v pacman &> /dev/null; then
  archlinux="$DOTFILES_ZSH_DIR/etc/os/archlinux.zsh"
  [[ -f "$archlinux" ]] && source "$archlinux";
fi
