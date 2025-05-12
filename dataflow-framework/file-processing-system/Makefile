.PHONY: run watch clean build-docker run-docker

run:
	python main.py --input sample.txt

watch:
	python main.py --watch

clean:
	rm -rf watch_dir/processed/* watch_dir/underprocess/*

build-docker:
	docker build -t file-processor .

run-docker:
	docker run -p 8000:8000 -v $(PWD)/watch_dir:/app/watch_dir file-processor
