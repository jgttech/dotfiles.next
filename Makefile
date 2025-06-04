INSTALL := .dotfiles/install

.PHONY: archlinux
archlinux:
	@clear
	@docker compose down archlinux
	@docker compose up archlinux -d
	@docker compose exec archlinux bash -c 'cat $$HOME/$(INSTALL) | bash'

.PHONY: ssh-archlinux
ssh-archlinux:
	@docker compose exec archlinux bash
