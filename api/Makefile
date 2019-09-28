.DEFAULT_GOAL := help

install: server.install
daemon: server.daemon ## Start
stop: server.stop

include makefiles/server.mk
include makefiles/test.mk
include makefiles/database.mk
include makefiles/format.mk
include makefiles/help.mk
