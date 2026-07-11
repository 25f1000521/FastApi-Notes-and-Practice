# Date - 11 july 2026

# Lecture Overview 
 [FastApi-Tutorial-1](https://youtu.be/7AMjmCTumuo?si=MRmdvE9aXUw6mu8o) This is the first leacture of this fastapi playlist .
 

# Things I learn 
* uv - It is a python package & project manager which is very fast written in rust by by astral.
     - It is faster than pip . 
     - Just like pip it can 
           - create virtual environments .
           - Run Python programs 
           -It can even manage python versions
* why uv :-
  - Before UV, python developers oftern used several tools together Like - 
       - pip :- To install packages 
       - venv :-To create virtual environments
       - pip tools :- lock dependencies
       - pyenv :- manage python versions
       - poetry :- Project management 
  - **UV**  combine many of these features into a single tool .

* Frequently used commands & their purposes
| Command | Purpose |
|---------|---------|
| uv init project-name | create new project |
| uv add venv | create virtual environment |
| uv add package-name | Install package |
| uv remove package-name | remove / uninstall package|
| uv sync | Install all project dependencies |
| uv pip list| list install packages |
| uv python list | show available python versions |
| uv add "uvicorn [standard]" | install uvicorn and optional features |
| uv run uvicorn main:app --reload | run a fastapi app |


# Code Example

# Important Command Used

# Notes / Tips

# Common errors & solutions 
