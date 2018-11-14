npm install
python copy_clientside_libraries.py
docker-compose -f local.yml build
echo "bringing up container as daemon"
docker-compose -f local.yml up -d
