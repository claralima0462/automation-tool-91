# automation-tool-91

A high-performance Python-based autoclicker designed for precision and efficiency. This tool provides a customizable interface to automate repetitive mouse tasks with low system overhead and configurable click intervals.

## Features

*   **Configurable Click Rate:** Define exact intervals in milliseconds to suit specific application requirements.
*   **Dynamic Hotkey Control:** Start and stop automation instantly using global keyboard shortcuts.
*   **Randomized Delay Mode:** Prevent anti-bot detection by adding human-like jitter to click timings.
*   **Multi-Button Support:** Select between left, right, or middle mouse button triggers.

## Installation

Ensure you have [Python 3.8+](https://www.python.org/) installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/automation-tool-91.git
cd automation-tool-91
pip install -r requirements.txt
```

## Usage

You can launch the tool directly from your terminal. Use the flags to define your click behavior:

```bash
# Basic usage: Click every 500ms
python main.py --interval 0.5

# Advanced usage: Randomized delays with Right-click
python main.py --interval 0.2 --randomize --button right
```

Once running, press **F6** to toggle the clicker on or off, and **ESC** to terminate the process.

## Requirements

*   **Operating System:** Windows 10/11 (due to low-level input hook requirements).
*   **Dependencies:** `pynput`, `pyautogui`.

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.