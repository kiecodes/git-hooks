#!/bin/bash

###################################################################
#title         :install_hooks.sh
#description   :Installs a commit-msg hook for git
#author        :Various
#date          :20200604
#version       :1.0.0
#usage         :bash install_hooks.sh
#notes         :
#bash_version  :4.4.19(1)-release
###################################################################

LIB_DIR=submodules

rm -f .git/hooks/commit-msg
ln -s -f ../../src/commit-msg.py .git/hooks/commit-msg

rm -rf .git/hooks/${LIB_DIR}
ln -s -f ../../src/${LIB_DIR} .git/hooks/${LIB_DIR}