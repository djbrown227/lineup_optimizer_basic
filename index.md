# 🏈 Local Fantasy Sports Lineup Optimizer

Welcome to **Lineup Optimizer Basic** — a simple, locally run fantasy sports lineup optimizer built with Django and the `pydfs-lineup-optimizer` library.

## 🎥 Demo Video

Want to see it in action? Here's a short walkthrough:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/1UK4ewB5ItY" title="Lineup Optimizer Demo" frameborder="0" allowfullscreen></iframe>

## 🎯 Why I Built This

Most lineup optimizers for fantasy sports platforms like **DraftKings**, **FanDuel**, and **Yahoo Fantasy** are locked behind expensive monthly subscriptions. I built this — along with other versions — for people who wanted a **free**, **private**, and **fully controllable** tool they could run on their own machine.

Whether you're a casual DFS player or a data-savvy fantasy sports strategist, this tool gives you everything you need to generate optimized lineups — no paywalls, no limits.


## 💡 What This Tool Does

This lineup optimizer:

- Generates optimal fantasy lineups based on your custom projections
- Supports major platforms: DraftKings, FanDuel, Yahoo
- Lets you control salary caps, roster rules, and stacking logic
- Runs 100% locally using Django and Python — your data stays private

## ⚙️ How to Use It

1. **Clone the repo**
   ```bash
   git clone https://github.com/djbrown227/lineup_optimizer_basic.git
   cd lineup_optimizer_basic
````

2. **Set up your environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the server**

   ```bash
   python manage.py runserver
   ```

4. **Open your browser**
   Visit `http://localhost:8000` to use the optimizer through a simple web interface.

## 🔐 Why Local Matters

* **No subscriptions** – completely free to use
* **Full privacy** – your player data and strategy stay on your machine
* **Customizable** – adjust projections, constraints, and rules as you like

## 🚧 Notes

This is a basic version.

## 📌 Interested in More?

Feel free to explore other tools I’ve built or reach out if you're looking to build something custom around fantasy sports optimization.

---