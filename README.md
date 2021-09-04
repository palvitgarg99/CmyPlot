# Discord-bot














Notes: (will be removed eventually!)

- we can use different branches to avoid code-conflicts and will can assign pull-request-maintainers ( on rolling basis - so that everybody can wear different hats) whose reponsibility is to merge pull-request into main.!(Thoughts!)

- creating a [virtualenv(venv in python3)](https://docs.python.org/3/library/venv.html) to have package dependency of our python codebase.(created one and folks can add update it.)
for ease can use put it in project directory, but will not push to remote-repo/branch.

  - create venv       : `python3 -m venv project1_env`
  - source it         : `source project1_env/bin/activate`
    now you can check which python interpretor you're using by 
    `which python`  
     Eg. `~/Downloads/project1/project1_env/bin/python`
    install whichever package you want `pip install []`
    for start I installed only 2 packages `requests` & `pytest`
  - freeze it to file : `pip3 freeze > requirements.txt`
  - load from file    : `pip install -r requirements.txt`