APPNAME=bridgepilot
TYPE=python
PYTHONVERSION="3.11.3"
EXTRAS="none"

help:
	@echo "usage: make [command]"

define kickoff
	@sudo bash .tmp/wget/bash-environment-manager-master/plugins/default/configuration/basis/core/assemble.sh $(APPNAME) $(SUDO_USER) $(CONFIGURATION) $(TYPE) $(PYTHONVERSION) $(HOSTTYPE)
endef

download_bash_environment_manager:
	@if test ! -d ".tmp/bash-environment-manager-master";then \
		sudo su -m $(SUDO_USER) -c "mkdir -p .tmp"; \
		sudo su -m $(SUDO_USER) -c "mkdir -p .tmp/wget"; \
		sudo su -m $(SUDO_USER) -c "cd .tmp/wget; wget -O bash-environment-manager.zip https://github.com/terminal-labs/bash-environment-manager/archive/master.zip"; \
		sudo su -m $(SUDO_USER) -c "cd .tmp/wget; unzip bash-environment-manager.zip"; \
	fi

conda: CONFIGURATION="default"
conda: HOSTTYPE="host"
conda: download_bash_environment_manager
	$(call kickoff)

vagrant.conda: CONFIGURATION="default"
vagrant.conda: HOSTTYPE="vagrant"
vagrant.conda: download_bash_environment_manager
	@if test ! -f "Vagrantfile";then \
		wget https://raw.githubusercontent.com/terminal-labs/bash-environment-shelf/master/vagrantfiles/Vagrantfile; \
		chown $(SUDO_USER) Vagrantfile; \
	fi
	$(call kickoff)