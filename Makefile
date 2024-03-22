default: run

run:
	python3 main.py

test:
	python3 -m pytest tests/*

curl:
	curl http://127.0.0.1:5000/play?choice=paper

black:
	black --check .
