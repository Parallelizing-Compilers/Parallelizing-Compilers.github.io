# Assignment 1: Optimizing Matrix Multiplication

**Due Date:** Tuesday, February 11th at 11:59 PM EST

*Content referenced from [CS267 Spring 2025: Optimizing Matrix Multiplication](https://sites.google.com/lbl.gov/cs267-spr2025/hw-1?authuser=0#h.p_wUx8PSDWAdpd)*

## Table of Contents
* [Problem statement](#problem-statement)
* [Instructions](#instructions)
    * [Teams](#teams)
    * [Getting Started with PACE](#getting-started-with-pace)
    * [Getting Set Up](#getting-set-up)
    * [Building our Code](#building-our-code)
    * [Running our Code](#running-our-code)
    * [Running the benchmark](#running-the-benchmark)
    * [Editing the Code](#editing-the-code)
    * [Our Harness](#our-harness)
    * [PACE's Processors](#paces-processors)
* [Grading](#grading)
    * [Submission Details](#submission-details)
    * [Write-up Details](#write-up-details)
* [Notes](#notes)
* [Optional Parts](#optional-parts)
* [Documentation](#documentation)
* [References](#references)

---

## Problem statement

Your task in this assignment is to write an optimized [matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication) function for the PACE ICE Cluster. We will give you a generic matrix multiplication code (also called matmul or dgemm), and it will be your job to tune our code to run efficiently on the Intel Xeon Gold 6226 processors. We are asking you to write an optimized matrix multiply kernel which can be multi-threaded and run on multiple cores.

We consider a special case of matmul:

_C := C + A*B_

where A, B, and C are n x n matrices. This can be performed using 2n^3 floating point operations (n^3 adds, n^3 multiplies), as in the following pseudocode:

```
for i = 1 to n
  for j = 1 to n
    for k = 1 to n
      C(i,j) = C(i,j) + A(i,k) * B(k,j)
    end
  end
end
```

---

# Instructions

Note that this is an individual assignment, no teams are required for this assignment.
## Getting Started with PACE

If you are new to the PACE cluster, please ensure you are connected to the GT VPN. You will be logging into the ICE cluster environment.

## Getting Set Up

To get started, log in to the PACE login node and clone the assignment.
```
student@local:~> ssh <username>@login-ice.pace.gatech.edu
student@login04:~> cd scratch
student@login04:~> git clone <link-to-the-repository>
student@login04:~> cd Homework1
student@login04:~/HW1> ls
benchmark.cpp		dgemm-naive.c		json.hpp		npy.hpp			Readme.md
benchmark.py		dgemm-optimized.c	Makefile		pyproject.toml		requirements.txt
```

There are ten files in the base repository. Their purposes are as follows:
* **benchmark.cpp**

This file benchmarks the matrix multiplication and saves the result and timings.

* **dgemm-naive.c** 

For illustrative purposes, a naive implementation of matrix multiply using three nested loops.

* **README.md**

README file explaining the build system in more detail.

* **benchmark.py** 

This executes your pre-compiled binaries to measure performance, verify correctness, and generate scaling plots.

* **dgemm-optimized.c**  - - -  **You may only modify this file.** 

This is where you will write your optimized code optimizing the `square_dgemm()` function in this file.

* **Makefile**

The build script that manages compiling your code with the correct PACE-specific flags




> Please **do not** modify any of the files besides _dgemm-optimized.c_

## Building our Code

We use a Makefile to simplify compilation.

1. Clean previous builds if any and then compile
```
make clean
make
```
This will generate two executables: dgemm-naive and dgemm-optimized.

## Running our Code
Command to request an interactive session: [We will be making use of Intel Xeon Gold 6226 processor]
```
salloc -N 1 -n 1 -c <no. of cores> -t <session-time> -C gold6226
```

ex:
salloc -N 1 -n 1 -c 2 -t 01:00:00 -C gold6226


Once the command is granted, your terminal prompt will change (e.g., to [gt_username@login-ice-1]$). You are now on a compute node.

## Running the Benchmark
Once you are on a compute node (inside salloc):

1. Load modules
```
module load gcc
module load anaconda3
```

2. Run the Python Driver
```
python3 benchmark.py
```
Running this script will verify your implementation's correctness, reporting per-size performance metrics (GFLOPS & Speedup) to the terminal, and saves the final scaling graph to the plot/ directory.

## Editing the Code

We suggest you to clone this repository and use code editor like VS-Code and make changes to only the suggest file and test its performance.

## Our Harness
The benchmark.cpp file (driven by benchmark.py) generates matrices of different sizes and benchmarks the performance. It outputs performance in [FLOPS](https://en.wikipedia.org/wiki/FLOPS) and as a percentage of the theoretical peak. Your job is to get your matrix-multiply performance as close to the theoretical peak as possible.

Since you are running on PACE-ICE, the theoretical peak is different from other systems. You may need to ensure your benchmark.py or build system uses the correct MAX_SPEED for the Intel Xeon Gold 6226.

On PACE (Intel Gold 6226), this value is computed as: 2.7 GHz * 8 (vector width) * 2 (FMA units) * 2 (ops/FMA) = 86.4 GFLOPS/core.

## PACE's Processors

### PACE-ICE (Intel Cascade Lake)
In this assignment, we will be using the **PACE-ICE Cluster**. Be sure to request the correct node type using the flag _-C gold6226_ on any interactive jobs you run.

### Theoretical Peak

Our benchmark reports numbers as a percentage of theoretical peak. Here is how we calculate the peak for the Intel Xeon Gold 6226 processors on PACE.

### Single Core Peak

- Frequency: ~2.7 GHz
- Vector Width: 512-bit (AVX-512) = 8 doubles per vector
- FMA Units: 2 units per core
- Ops per FMA: 2 (Multiply + Add)
- Calculation : $2.7 \times 8 \times 2 \times 2 = \mathbf{86.4 \text{ GFLOPS/core}}$

### Multi Core Peak 

You can use multiple cores in this assignment and for that the calculation will be as below :
- If you use 4 cores: $86.4 \times 4 = \mathbf{345.6 \text{ GFLOPS}}$


## Optimizing

Now, it's time to optimize!  A few optimizations you might consider adding:
1. Blocking (Tiling): Break the matrix into smaller sub-matrices that fit into L1/L2 cache.
2. Vectorization: Use AVX-512 intrinsics (e.g., _mm512_fmadd_pd) to utilize the full width of the vector unit
3. Multithreading: Use OpenMP to utilize all cores on the node.
4. Add manual prefetching

You may, of course, proceed however you wish.  We recommend you look through the lecture notes as reference material to guide your optimization process, as well as the references at the bottom of this write-up.

### Available Compilers

The development environment on PACE relies on the GNU C Compiler (GCC). You must load the correct module to ensure you have a modern version of GCC that supports AVX-512.
```
student@login04:~> module load gcc
```
We recommend sticking to GCC for this assignment. Still, you might want to try your code with different compilers to see if one outperforms the other. If the difference is significant, consider using the [Compiler Explorer](https://gcc.godbolt.org/z/v2fTDJ) to figure out why GCC isn't optimizing your code as well. 

---

# Grading

We will grade your assignment by reviewing your write-up, analyzing the optimizations you attempted in _dgemm-optimized.c_, and benchmarking your code's performance on the PACE cluster. Note that code that returns incorrect results will receive significant penalties.

## Submission Details


1.  Ensure that your write-up is located in your source directory, next to **dgemm-optimized.c**. It should be named **cs6245_<gt_username>_hw1.pdf**.
2.  Clean your build directory 
    ```
    make clean
    ```
    This second command will fail if the PDF is not present.
3.  Create a compressed archive of your work:
    ```
    tar -czvf cs6245_<gt_username>_hw1_submission.tar.gz dgemm-optimized.c cs6245_<gt_username>_hw1.pdf Makefile
    ```
4.  Submit the .tar.gz file through Canvas

## Write-up Details

* Your write-up should contain:
    * The optimizations used or attempted,
    * the results of those optimizations(Speedup graphs)
    * the reason for any odd behavior (e.g., dips) in performance

* Your write-up should be a maximum of 3-4 pages in length, including all text, figures, tables, and references.

---

# Notes [ Confirm with Willow]

* **Your grade will mostly depend on three factors:**
    * Whether or not it is correct (ie. finishes running without exiting early)
    * Performance sustained on the Intel Xeon Gold 6226.
    * Explanations of the performance features you observed (including what didn't work)
    
* There are other formulations of matmul (e.g., [Strassen](http://en.wikipedia.org/wiki/Strassen_algorithm)) that are mathematically equivalent, but perform asymptotically fewer computations - we will not grade submissions that do fewer computations than the 2n^3 algorithm. This is actually an optional part of HW1.
* You must use the GNU C Compiler for this assignment. If your code does not compile and run with GCC, it will not be graded.
* Besides compiler intrinsic functions and built-ins, your code (`dgemm-optimized.c`) must only call into the C standard library.
* GNU C provides [many](http://gcc.gnu.org/onlinedocs/gcc/C-Extensions.html) extensions, which include intrinsics for vector (SIMD) instructions and data alignment. (Other compilers may have different interfaces.)
    * To manually vectorize, you should prefer to add compiler intrinsics to your code; avoid using inline assembly, at least at first.
    * The [Compiler Explorer](https://gcc.godbolt.org/z/v2fTDJ) project will be useful for exploring the relationship between your C code and its corresponding assembly. Release mode builds compile with `-O3`.
* You may assume that A and B do not alias C; however, A and B may alias each other. It is semantically correct to qualify C (the last argument to square_dgemm) with the C99 `restrict` keyword. There is a lot online about restrict and pointer-aliasing - [this](http://cellperformance.beyond3d.com/articles/2006/05/demystifying-the-restrict-keyword.html) is a good article to start with, along with the [Wikipedia article](https://en.wikipedia.org/wiki/Restrict) on the restrict keyword.
* The matrices are all stored in **row-major order**, i.e. `A[row * n + col]`, unlike the Column-Major layout typically found in BLAS or Fortran resources.
* We will check correctness by the following component-wise error bound: |square_dgemm(n,A,B,0) - A*B| < eps*n*|A|*|B|.
    * where eps := 2^-52 = 2.2 * 10^-16 is the [machine epsilon](http://en.wikipedia.org/wiki/Machine_epsilon).

---

# Optional Parts

These parts are not graded. You should be satisfied with your square_dgemm results and write-up before beginning an optional part.

* Implement Strassen matmul. Consider switching over to the three-nested-loops algorithm when the recursive subproblems are small enough.
* Support the dgemm interface (ie, rectangular matrices, transposing, scalar multiples).
* Try float (single-precision).
* Try complex numbers (single- and double-precision) - note that complex numbers are part of C99 and [supported in gcc](http://gcc.gnu.org/onlinedocs/gcc/Complex.html). [This forum thread](http://stackoverflow.com/questions/3211346/complex-mul-and-div-using-sse-instructions) gives advice on vectorizing complex multiplication with the conventional approach - but note that there are [other algorithms](http://en.wikipedia.org/wiki/Multiplication_algorithm#Gauss.27s_complex_multiplication_algorithm) for this operation.
* Optimize your matmul for the case when the inputs are symmetric. Consider [conventional](http://www.netlib.org/lapack/lug/node122.html) and [packed](http://www.netlib.org/lapack/lug/node123.html) symmetric storage.

If you wish to submit optional parts, send them to us via email.

---

# Documentation

* [PACE-ICE User Guide](https://docs.pace.gatech.edu/ice_cluster/ice/) Official documentation for the cluster you are using.
* [GCC](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/) documentation - PACE-ICE's default version currently is GCC 12.3.0.
* [Intel's intrinsics guide](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#techs=AVX2,FMA) - a complete overview of all available vector intrinsics.
* [GCC's vector extensions](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/Vector-Extensions.html#Vector-Extensions) - special types that make programming with vectors easier
* [GCC's built-ins](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/Other-Builtins.html#Other-Builtins) - special commands that give optimization hints to the compiler. See assume_aligned, unreachable, and expect. [Some are specific to x86.](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/x86-Built-in-Functions.html#x86-Built-in-Functions)
* [GCC's variable attributes](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/Common-Variable-Attributes.html#Common-Variable-Attributes) - useful for optimizing the memory layout of your program
* [GCC's function attributes](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/Common-Function-Attributes.html#Common-Function-Attributes) - useful for controlling the optimization of particular functions. Some are [specific to x86.](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/x86-Function-Attributes.html#x86-Function-Attributes)

You are also welcome to learn from the source code of state-of-art BLAS implementations such as [ATLAS](http://math-atlas.sourceforge.net/). However, you should not reuse those codes in your submission.

* We emphasize these are example scripts because for these as well as all other assignment scripts we provide, you may need to adjust the number of requested nodes and cores and amount of time according to your needs (your allocation and the total class allocation is limited). To understand how you are charged, [READ THIS](https://pace.gatech.edu/new-cost-model/) alongside the given scripts. [Confirm with Willow]


## Important Policy Note
Please remember that PACE is a shared resource
1. Never run benchmarks on the login node. It will be slow and you may get your account suspended.
2. Request accurate resources. If you only need 4 cores, do not request 24.
3. Walltime: The example salloc commands use 1 hour (-t 01:00:00). If your code hangs, this ensures the job eventually dies so you don't waste allocation.
---

# References

* Goto, K., and van de Geijn, R. A. 2008. Anatomy of High-Performance Matrix Multiplication, ACM Transactions on Mathematical Software 34, 3, Article 12.
    * (Note: explains the design decisions for the GotoBLAS dgemm implementation, which also apply to your code.)
* Chellappa, S., Franchetti, F., and Puschel, M. 2008. [How To Write Fast Numerical Code: A Small Introduction](https://users.ece.cmu.edu/~franzf/papers/gttse07.pdf), Lecture Notes in Computer Science 5235, 196-259.
    * (Note: how to write C code for modern compilers and memory hierarchies, so that it runs fast. Recommended reading, especially for newcomers to code optimization.)
* Bilmes, et al. [The PHiPAC (Portable High Performance ANSI C) Page for BLAS3 Compatible Fast Matrix Matrix Multiply](https://people.eecs.berkeley.edu/~krste/papers/phipac_ics97.pdf).
    * Also see [ATLAS](http://math-atlas.sourceforge.net/)
* Lam, M. S., Rothberg, E. E, and Wolf, M. E. 1991. The Cache Performance and Optimization of Blocked Algorithms, ASPLOS'91, 63-74.
    * (Note: clearly explains cache blocking, supported by with performance models.)