# Local Fantasy Sports Lineup Optimizer

A locally run fantasy sports lineup optimizer built with **Python**, **Django**, and the `pydfs-lineup-optimizer` library.

This project allows users to generate optimized DFS lineups without relying on third-party subscription services. Everything runs locally, giving full control over projections, constraints, and strategy while keeping data private.

---

## Features

- Generate optimized fantasy lineups using custom projections
- Supports DraftKings, FanDuel, and Yahoo Fantasy
- Enforces salary caps and roster rules
- Runs entirely on your local machine
- Simple web interface built with Django
- No external APIs or cloud services required

---

## Demo

A short walkthrough of the optimizer and interface:

<iframe width="560" height="315" src="https://www.youtube.com/embed/1UK4ewB5ItY" title="Lineup Optimizer Demo" frameborder="0" allowfullscreen></iframe>

---

## Requirements

- Python 3.9 or higher
- pip
- Virtual environment (recommended)

---

## Setup

Clone the repository:

```bash
git clone https://github.com/djbrown227/lineup_optimizer_basic.git
cd lineup_optimizer_basic

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py runserver

http://localhost:8000
