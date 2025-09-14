# create folder if not exists
mkdir -p data
mkdir -p utils
mkdir -p src
mkdir -p config
mkdir -p app
mkdir -p chroma_db
mkdir -p pipeline


# create empty files if not exists
touch utils/__init__.py
touch utils/custom_exception.py
touch utils/logger.py
touch src/__init__.py
touch src/data_loader.py
touch src/prompt_template.py
touch src/vector_store.py
touch src/recommender.py
touch config/__init__.py
touch app/__init__.py
touch app/app.py
touch pipeline/__init__.py
touch pipeline/pipeline.py
touch pipeline/build_pipeline.py
touch .env
touch requirements.txt
touch setup.py
touch README.md
touch .gitignore