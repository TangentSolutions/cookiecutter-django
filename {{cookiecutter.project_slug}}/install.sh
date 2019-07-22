#! /bin/bash

pip install --upgrade pip pipenv

if [ ! -f Pipfile.lock ]; then
    echo "Pipfile.lock not found! Creating one."
    pipenv lock
fi

if [ "$BUILD" == "DEV" ];
    then
    	echo "Installing development dependencies";
    	pipenv install --dev --system --deploy --ignore-pipfile;
    else
    	echo "Installing production dependencies";
    	pipenv install --system --deploy --ignore-pipfile;
fi
