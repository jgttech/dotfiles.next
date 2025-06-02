# Where, within the container, the dotfiles
# are at.
SETUP := .dotfiles/bin/setup

# Builds all the images used to test the
# dotfiles against.
.PHONY: install
install:
	@docker compose build

# Only for archlinux, at the moment, but
# is designed to support more OS's later.
.PHONY: archlinux
archlinux:
	@clear
	@docker compose down archlinux
	@docker compose up archlinux -d
	@docker compose exec archlinux bash -c 'cat $$HOME/$(SETUP) | bash'

.PHONY: ssh-archlinux
ssh-archlinux:
	@docker compose exec archlinux bash
