build:
	@docker-compose -f local.yml build --build-arg BUILD=DEV
	@npm install
	@python ./copy_clientside_libraries.py
	@rm -rf node_modules

up:
	@docker-compose -f local.yml up

dup:
	@docker-compose -f local.yml up -d

stop:
	@docker-compose -f local.yml stop

down:
	@docker-compose -f local.yml down

restart:
	@docker-compose -f local.yml restart

makemigrations:
	@docker-compose -f local.yml run --rm django ./manage.py makemigrations

migrate:
	@docker-compose -f local.yml run --rm django ./manage.py migrate

logs:
	@docker-compose -f local.yml logs -tf $(service)

shell:
	@docker-compose -f local.yml run --rm django ./manage.py shell

notebook:
	@docker-compose -f local.yml run -p 8888:8888 --rm django ./manage.py shell_plus --notebook
