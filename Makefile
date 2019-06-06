.PHONY: test
test: python2 python3

.PHONY: python3
python3:
	docker build -t fountain-python3 --target python3 .
	docker run -ti --rm fountain-python3 python spec.py

.PHONY: python2
python2:
	docker build -t fountain-python2 --target python2 .
	docker run -ti --rm fountain-python2 python spec.py
