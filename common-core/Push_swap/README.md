*This project has been created as part of the 42 curriculum by ouel-ons.*

# push_swap

## Description

**push_swap** is an algorithmic project from the 42 curriculum.

The goal is to sort a list of integers using two stacks (`a` and `b`) and a restricted set of operations, while producing the smallest possible number of instructions.

This project focuses on:
- Algorithm design and optimization
- Time and space complexity
- Stack-based data structures
- Rigorous error handling
- Writing clean, norm-compliant C code

The program outputs a sequence of instructions that, when executed, sorts stack `a` in ascending order.

---

## Instructions

### Compilation

To compile the project, run:

    make

This will generate the `push_swap` executable.

Available Makefile rules:
- make or make all
- make clean
- make fclean
- make re

---

### Execution

    ./push_swap <list_of_integers>

Example:

    ./push_swap 2 1 3 6 5 8

Output:

    sa
    pb
    pb
    pb
    sa
    pa
    pa
    pa

Each instruction is printed on its own line.

---

### Error Management

The program prints `Error` followed by a newline on **standard error** if:
- An argument is not a valid integer
- A number exceeds INT_MIN or INT_MAX
- Duplicate values are provided
- The input format is invalid

Example:

    ./push_swap 0 one 2 3
    Error

If no arguments are given, the program outputs nothing.

---

## Allowed Operations

- sa / sb / ss — swap the first two elements
- pa / pb — push the top element between stacks
- ra / rb / rr — rotate stack upwards
- rra / rrb / rrr — rotate stack downwards

---

## Algorithm

The sorting strategy adapts to the number of elements.

### Small Input (≤ 5 numbers)

- Direct optimal sorting logic
- Minimal number of operations

### Large Input (100 / 500 numbers)

- Value indexing (normalization)
- Chunk-based pushing to stack b
- Optimal rotations to rebuild stack a

This approach respects the required benchmarks:
- 100 numbers sorted in fewer than 700 operations
- 500 numbers sorted in fewer than 5500 operations

---

## Bonus — Checker

The bonus part implements a `checker` program that validates the correctness of the instructions produced by `push_swap`.

Usage:

    ./push_swap <args> | ./checker <args>

Results:
- OK → stack a is sorted and stack b is empty
- KO → sorting failed
- Error → invalid input or instruction

---

## Resources

- Stack data structure  
  https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

- Sorting algorithms and complexity  
  https://en.wikipedia.org/wiki/Sorting_algorithm  
  https://en.wikipedia.org/wiki/Analysis_of_algorithms

- 42 push_swap subject (intranet)

### AI Usage

AI tools were used only to:
- Clarify algorithmic concepts
- Review edge cases
- Improve documentation quality

All code was written, reviewed, and fully understood by the author.

---

## Author

- ouel-ons — 42 Student

---

## License

This project is part of the 42 curriculum and is intended for educational purposes only.
