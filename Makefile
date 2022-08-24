run:
	@echo "--> Running"
	@python3 main.py $(n)

install-dependencies:
	@echo "--> Installing Python dependencies"
	@pip install -r requirements.txt