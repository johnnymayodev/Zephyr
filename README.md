# Zephyr

/zĕf′ər/ - a gentle breeze

## Description

Zephyr is a lightweight and easy to use component-based front-end framework. It is built with Python and leverages Svelte for its files and syntax.

## Installation

```bash
git clone https://www.github.com/johnnymayodev/Zephyr
```

```bash
cd Zephyr
```

## Usage

#### Via Scripts

Setup

```bash
chmod u+x setup.sh && . ./setup.sh
```

Run

```bash
chmod u+x run.sh && ./run.sh
```

#### Command Line Arguments

--debug

- Compiles the page on every request

#### Manually

Commands are written for macOS systems. Please adjust accordingly for your system.

1. Create a virtual environment

```bash
python3 -m venv venv
```

2. Activate the virtual environment

```bash
source venv/bin/activate
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python zephyr.py
```
