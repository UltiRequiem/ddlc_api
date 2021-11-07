all: pre-run

pre-run: 
	poetry shell

dev:
	ENV=dev uvicorn ddlc:app --reload

start:
	uvicorn ddlc:app

fmt:
	black .
