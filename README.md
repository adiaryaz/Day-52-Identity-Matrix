# Day-52-Identity-Matrix

Day 52/100 - Python Program to Print an Identity Matrix

# Print an Identity Matrix

A program to generate and display a mathematical identity matrix of a user-defined size using nested loops and conditional logic.

## 📝 Description

This program creates an **Identity Matrix** (often denoted by $I$), which is a fundamental concept in linear algebra. An identity matrix is always a square matrix ($n \times n$) where all the elements on the main diagonal (from the top-left to the bottom-right) are $1$, and all other elements are $0$.

The script achieves this by utilizing two nested `for` loops to iterate through the rows and columns. The outer loop tracks the current row index (`i`), and the inner loop tracks the column index (`j`). It uses a simple mathematical condition: if the row index exactly equals the column index (`i == j`), it prints a `1`; otherwise, it prints a `0`. Furthermore, the program is wrapped in a `try-except` block to gracefully handle non-integer inputs without crashing.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A single positive integer representing the size ($n$) of the square matrix.



### Output:

* If valid: A visual grid of numbers representing the $n \times n$ identity matrix, printed row by row.


* If invalid (zero or negative): "Please enter a positive integer for the size of the matrix."


* If invalid (non-numeric): "Invalid input! Please enter a valid integer."



### Rules:

1. The program must accept input from the user and attempt to cast it to an integer.


2. The program must use a `try-except ValueError` block to catch any non-numerical inputs.


3. The program must evaluate if the inputted integer is less than or equal to 0; if so, it must prompt the user for a positive integer and terminate.


4. The program must use nested loops to iterate through an $n \times n$ grid.


5. The program must print `1` if the current row index equals the column index, and `0` otherwise, utilizing `end=" "` to keep them on the same line.



---

## 💡 Examples

### Example 1 (Standard 3x3 Matrix)

**Input:**

```
3

```

**Output:**

```
1 0 0 
0 1 0 
0 0 1 

```

**Explanation:** The program generates a $3 \times 3$ grid. The `1`s are placed at coordinates (0,0), (1,1), and (2,2) where the row index matches the column index.

### Example 2 (Larger Matrix)

**Input:**

```
5

```

**Output:**

```
1 0 0 0 0 
0 1 0 0 0 
0 0 1 0 0 
0 0 0 1 0 
0 0 0 0 1 

```

**Explanation:** The same logic scales perfectly to a $5 \times 5$ square matrix, maintaining the perfect diagonal line of $1$s.

### Example 3 (Negative Value Handling)

**Input:**

```
-4

```

**Output:**

```
Please enter a positive integer for the size of the matrix.

```

**Explanation:** An identity matrix cannot have a negative size. The initial `if n <= 0:` check intercepts this and halts the execution, printing a safe error message.

### Example 4 (String Error Handling)

**Input:**

```
four

```

**Output:**

```
Invalid input! Please enter a valid integer.

```

**Explanation:** The string "four" cannot be cast to an integer. The `ValueError` exception is caught, and the program avoids a runtime crash.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script)

```bash
git clone https://github.com/adiaryaz/Day-52-Identity-Matrix.git
cd identity-matrix

```

2. **Run the program**:

```bash
python main.py

```

Enter a positive integer when prompted to see the corresponding identity matrix generated in the terminal.
