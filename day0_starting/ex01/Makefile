# Small makefile to make the execution of 3.10 python code easier on 42 machines that run on 3.14 ATM
# DONT FORGET TO RUN FCLEAN WHEN FINNISHING CORRECTING THE DAY (clean the 3.10 python image)

PYTHON_VERSION := python:3.10
FILENAME := format_ft_time.py

all: run

run:
	docker run --rm -it -v "$$PWD":/app -w /app $(PYTHON_VERSION) python $(FILENAME)

fclean:
	-docker rmi $(PYTHON_VERSION)

re: fclean all

.PHONY: all run fclean re
