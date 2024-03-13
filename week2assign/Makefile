initializedb:
	flask db init
	
migrate:
	flask db migrate -m "$(message)"

dbupgrade:
	flask db upgrade

run:
	flask run

.PHONY: initializedb migrate dbupgrade run