build:
	@docker-compose -f local.yml build
	@npm install
	@python ./copy_clientside_libraries.py

up:
	@docker-compose -f local.yml up -d

stop:
	@docker-compose -f local.yml stop

down:
	@docker-compose -f local.yml down

restart:
	@docker-compose -f local.yml restart

makemigrations:
	@docker-compose -f local.yml run --rm django poetry run ./manage.py makemigrations

migrate:
	@docker-compose -f local.yml run --rm django poetry run ./manage.py migrate

logs:
	@docker-compose -f local.yml logs -tf django
