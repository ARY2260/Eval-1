## [Eval](https://foobar.com)

Fork and clone the repository from GitHub.
```bash
git clone https://github.com/<your-username-here>/Eval.git
```

Traverse to the directory where the repository is cloned.
```bash
cd WikiExtractor
```

<br>

### Website Server
Built on Django Rest Framework, the server needs **Python 3.8 and above** installed on your system to contribute and work on the server-side instances. If you do not have Python installed, you can install it from [here](https://www.python.org/downloads/).

Move into the `src` folder
```bash
cd src
```

Install the various dependencies to run the server
```bash
# Create a virtual environment 
python3 -m venv <name-of-virtual-environment>
source <name-of-virtual-environment>/bin/activate

# Install the dependencies
pip3 install -r requirements.txt
```

Activate the virtual environment
```bash
source <name-of-virtual-environment>/bin/activate
```

Move into the `api` folder and start the server
```bash
cd api
python3 manage.py runserver
```

<br>

### Client Website
Built on NextJS, the client webapp requires **NodeJS 12 and above** installed on your system to contribute and work on the client-side instances. If you do not have NodeJS installed, you can install it from [here](https://nodejs.org/en/download/).

Move into the `src/client` folder
```bash
cd src/client
```

Install the various dependencies to run the server
```bash
npm install
```

Start the client
```bash
npm run dev
```