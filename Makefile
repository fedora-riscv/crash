# Makefile for source rpm: crash
# $Id$
NAME := crash
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
