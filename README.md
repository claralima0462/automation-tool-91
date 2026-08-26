# automation-tool-91

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

A lightweight, high-performance desktop automation utility built in Python. Designed for repetitive clicking tasks, it provides precise interval control and coordinate mapping with minimal resource overhead.

---

### Features

* **High-Precision Timing:** Executes mouse clicks at exact millisecond intervals using optimized system-level thread sleeping.
* **Smart Coordinate Locking:** Capture and lock onto specific screen (X, Y) coordinates to prevent drift during long execution runs.
* **Emergency Safety Killswitch:** Instantly halt all automated actions by simply slamming your mouse cursor into any corner of the screen.
* **Configurable Profiles:** Save and load custom click sequences, delays, and repeat counts for different workflows.

---

### Installation

Ensure you have Python 3.8 or higher installed on your system. 

1. Clone the repository:
   ```bash
   git clone https://github.com/Developer/automation-tool-91.git
   cd automation-tool-91
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### Usage

Run the tool from your terminal to launch the interactive CLI configuration:

```bash
python main.py
```

#### Quick Script Example

You can also import the core engine into your own Python scripts for advanced automation workflows:

```python
from engine import AutoClicker

# Initialize clicker with a 50ms delay and right-click action
bot = AutoClicker(delay=0.05, button="right")

# Target specific screen coordinates and run for 500 iterations
bot.set_position(x=500, y=300)
bot.start(clicks=500)
```

---

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.