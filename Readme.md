## 1kb

just a [small website](https://hi.veryunited.net), so i can join the [1k club](https://1kb.club/).

### build

0. use something like pyenv to have the recommended `.python-version` installed
1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. upon calling `build.py`, every `.html` file in `src` will be minified and put into `build`
