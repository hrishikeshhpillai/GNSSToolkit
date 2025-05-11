# GNSSToolkit
---

## Table of Contents

1. [Setup Instructions](#setup)
   - [Create a Virtual Environment](#venv)
   - [Activate the Virtual Environment](#activate-venv)
   - [Install Dependencies](#install-dependencies)
2. [Running the programs](#running-programs)
   - [Running `rotation.py`](#rotation)
   - [Running `lla2xyz.py`](#lla2xyz)

---

<a name="setup"></a>

## Setup Instructions

<a name="venv"></a>

### Create a Virtual Environment

To maintain isolated dependencies, create a Python virtual environment:

```bash
python3 -m venv venv
```

<a name="activate-venv"></a>

### Activate the Virtual Environment

- For macOS/ Linux

```bash
source venv/bin/activate
```

- For Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```


<a name="running-programs"></a>

## Running Programs


<a name="rotation"></a>

### Rotation

To run rotation.py, navigate to the directory

```bash
cd rotation
```

Run the program

```bash
python3 rotation.py
```

To run the testcase

```bash
python3 test_rotation.py
```

<a name="lla2xyz"></a>

### LLA2XYZ

To run lla2xyz.py, navigate to the directory

```bash
cd lla2xyz
```

Run the program

```bash
python3 lla2xyz.py
```

To run the testcase

```bash
python3 test_lla2xyz.py
```


