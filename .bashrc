# REF: https://docs.python-guide.org/dev/virtualenvs/

# One-time create a "virtualenv" that uses Python 3 for this project
if [ ! -d .virtualenv ]; then
  virtualenv -p python3 .virtualenv
fi
# NOTE: Python 3 has "venv" built-in that can do the same thing!
# python3 -m venv .virtualenv
# virtualenv .virtualenv
# source .virtualenv/bin/activate

# Activate this virtualenv
source .virtualenv/bin/activate

# Should now safely see this project is indeed using Python 3
python --version

# The example script should run correctly
#pip install requests
#vi example.py
#import requests
#response = requests.get('https://httpbin.org/ip')
#print('Your IP is {0}'.format(response.json()['origin']))
#:wq!
#python example.py


# Freeze this project's requirements to a file for source control
#pip freeze > requirements.txt

# Install this project's requirements
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

echo " "
echo "####################"
echo "# See .env file"
echo "# Launch Flask:"
echo "python -m flask run"
echo " "
