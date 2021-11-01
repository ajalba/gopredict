MODULE := gopredict
run:
	@streamlit run ./src/$(MODULE)/__main__.py
test:
	@pytest
clean:

.PHONY: clean test