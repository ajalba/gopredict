MODULE := gopredict
run:
	@streamlit run ./src/$(MODULE)/__main__.py
test:
	@pytest
clean:
	rm -rf .pytest_cache .coverage coverage.xml
install:
	pip install -r requirements.txt
.PHONY: clean test