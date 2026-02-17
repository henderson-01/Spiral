# Python Turtle Spiral

Welcome to the **Python Turtle Spiral** project! This script demonstrates how to create a vibrant geometric pattern using Python's built-in `turtle` graphics library. It’s a perfect "Hello World" style project for visual learners.

## Description

The program opens a graphics window with a black background and draws an intricate spiral. To demonstrate logic flow, the drawing starts in **green** and dynamically switches to **red** as it expands, eventually stopping itself once it reaches a set size.

## Prerequisites

This guide is tailored for **Ubuntu Desktop** users.

### 1. Install System Dependencies

Python's `turtle` library relies on a toolkit called Tkinter. On Ubuntu, this isn't always installed by default. Run the following command to ensure your system is ready:

```bash
sudo apt update && sudo apt install python3-tk python3-venv -y

```

### 2. Set Up a Virtual Environment

It is best practice to run Python projects in a virtual environment to keep your system clean.

1. **Clone or enter your project folder:**
```bash
cd Spiral

```


2. **Create the environment:**
```bash
python3 -m venv venv

```


3. **Activate it:**
```bash
source venv/bin/activate

```



## How to Run

Once your virtual environment is active (you should see `(venv)` in your terminal prompt), run the script:

```bash
python spiral_image.py

```

> **Note:** A window will appear showing the animation. Once the drawing is complete, click anywhere inside the turtle window to close it.

## Code Concepts Used

This script bridges the gap between code and art by using:

* **Libraries**: Importing `turtle` to handle the heavy lifting of window management and drawing.
* **Variables**: Tracking `distance` and `angle` to determine where the "pen" moves next.
* **Loops**: Using a `while` loop to repeat drawing actions without writing hundreds of lines of code.
* **Conditionals**: Using `if` statements to change the color based on the spiral's size and to `break` (stop) the loop when the drawing is finished.

## License

This project is open-source and intended for educational use. Happy coding!

---

## Disclaimer

This project is provided "as-is" without any warranty of any kind. I am not responsible for any issues, data loss, or "explosions" (code-related or otherwise) that may occur from using this software. **Use it at your own risk.**

