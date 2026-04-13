run:
	python manage.py runserver 0.0.0.0:8000

migrate:
	python manage.py migrate

make:
	python manage.py makemigrations

redis:
	docker start my-redis
show:
	python manage.py showmigrations
	
plus:
	python manage.py shell_plus --ipython

shell:
	python manage.py shell

createsuperuser:
	python manage.py createsuperuser

collectstatic:
	python manage.py collectstatic --no-input

test:
	python manage.py test

venv:
	source venv/bin/activate

requirements:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

# Combined commands
migrate-all: makemigrations migrate

resetdb: makemigrations migrate createsuperuser

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

# Format code
format:
	@echo "🎯 Форматируем весь Django проект..."
	
	# Autoflake
	@find . -type f -name "*.py" \
	  -not -path "*/venv/*" \
	  -not -path "*/fitenv/*" \
	  -not -path "*/env/*" \
	  -not -path "*/.venv/*" \
	  -not -path "*/__pycache__/*" \
	  -not -path "*/migrations/*" \
	  -not -path "*/apps*" \
	  -not -path "*/node_modules/*" \
	  -not -path "*/.git/*" \
	  -not -path "*/app/*" | \
	xargs autoflake --in-place --remove-all-unused-imports --remove-unused-variables
	
	# ISort
	@find . -type f -name "*.py" \
	  -not -path "*/venv/*" \
	  -not -path "*/env/*" \
	  -not -path "*/fitenv/*" \
	  -not -path "*/.venv/*" \
	  -not -path "*/__pycache__/*" \
	  -not -path "*/migrations/*" \
	  -not -path "*/node_modules/*" \
	  -not -path "*/.git/*" \
	  -not -path "*/app/*" | \
	xargs isort --profile black --line-length 88
	
	# Black
	@find . -type f -name "*.py" \
	  -not -path "*/venv/*" \
	  -not -path "*/fitenv/*" \
	  -not -path "*/env/*" \
	  -not -path "*/.venv/*" \
	  -not -path "*/__pycache__/*" \
	  -not -path "*/migrations/*" \
	  -not -path "*/node_modules/*" \
	  -not -path "*/.git/*" \
	  -not -path "*/app/*" | \
	xargs black --line-length 88 --target-version py310
	
	@echo "✅ Форматирование завершено!"


lint:
	@echo "🔍 Проверяем качество кода..."
	@find . -type f -name "*.py" \
	  -not -path "*/venv/*" \
	  -not -path "*/fitenv/*" \
	  -not -path "*/env/*" \
	  -not -path "*/.venv/*" \
	  -not -path "*/__pycache__/*" \
	  -not -path "*/migrations/*" \
	  -not -path "*/node_modules/*" \
	  -not -path "*/.git/*" \
	  -not -path "*/app/*" | \
	xargs flake8 --max-line-length=88 --extend-ignore=E203,W503

# Полный цикл: форматирование + проверка
quality: format lint
	@echo "🎉 Код идеален!"

# Резервная копия БД
backup:
	@echo "💾 Создаем бэкап базы..."
	python manage.py dumpdata > backup_$(shell date +%Y%m%d_%H%M%S).json