APPNAME=bridge
TYPE=python
PYTHONVERSION="3.6.9"
EXTRAS="none"

help:
	@echo "usage: make [command]"

define kickoff
	@sudo bash .tmp/bash-environment-manager-master/groups/namespaces/types/$(TYPE)/assemble.sh $(APPNAME) $(SUDO_USER) $(CONFIGURATION) $(TYPE) $(PYTHONVERSION) $(HOSTTYPE)
endef

download_bash_environment_manager:
	@if test ! -d ".tmp/bash-environment-manager-master";then \
		sudo su -m $(SUDO_USER) -c "mkdir -p .tmp"; \
		sudo su -m $(SUDO_USER) -c "cd .tmp; wget -O bash-environment-manager.zip https://github.com/terminal-labs/bash-environment-manager/archive/master.zip"; \
		sudo su -m $(SUDO_USER) -c "cd .tmp; unzip bash-environment-manager.zip"; \
		sudo su -m $(SUDO_USER) -c "cd .tmp; mkdir -p download; mv bash-environment-manager.zip download/bash-environment-manager.zip"; \
	fi

conda: CONFIGURATION="python-conda_full"
conda: HOSTTYPE="host"
conda: download_bash_environment_manager
	$(call kickoff)

vagrant.conda: CONFIGURATION="vagrant-conda"
conda: HOSTTYPE="vagrant"
vagrant.conda: download_bash_environment_manager
	@if test ! -f "Vagrantfile";then \
		wget https://raw.githubusercontent.com/terminal-labs/bash-environment-shelf/master/vagrantfiles/Vagrantfile; \
		chown $(SUDO_USER) Vagrantfile; \
	fi
	$(call kickoff)
