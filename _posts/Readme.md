# Assignment 1: Optimizing Matrix Multiplication

**Due Date:** Tuesday, February 11th at 11:59 PM PST

*Content referenced from [CS267 Spring 2025: Optimizing Matrix Multiplication](https://sites.google.com/lbl.gov/cs267-spr2025/hw-1?authuser=0#h.p_wUx8PSDWAdpd)*

## Table of Contents
* [Problem statement](#problem-statement)
* [Instructions](#instructions)
    * [Teams](#teams)
    * [Getting Started with Perlmutter](#getting-started-with-perlmutter)
    * [Getting Set Up](#getting-set-up)
    * [Building our Code](#building-our-code)
    * [Running our Code](#running-our-code)
    * [Interactive Session](#interactive-session)
    * [Editing the Code](#editing-the-code)
    * [Our Harness](#our-harness)
    * [Perlmutter's Processors](#perlmutters-processors)
* [Grading](#grading)
    * [Submission Details](#submission-details)
    * [Write-up Details](#write-up-details)
* [Notes](#notes)
* [Optional Parts](#optional-parts)
* [Documentation](#documentation)
* [References](#references)

---

## Problem statement

Your task in this assignment is to write an optimized [matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication) function for NERSC's Perlmutter supercomputer. We will give you a generic matrix multiplication code (also called matmul or dgemm), and it will be your job to tune our code to run efficiently on Perlmutter's processors. We are asking you to write an optimized single-threaded matrix multiply kernel. This will run on only one core.

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

## Teams

Note that you will work in assigned teams for this assignment. See bCourses for your group assignments.

## Getting Started with Perlmutter

Please read through the Perlmutter tutorial, available here: [https://github.com/Berkeley-CS267/perlmutter-tutorial/blob/master/perlmutter-tutorial.md](https://github.com/Berkeley-CS267/perlmutter-tutorial/blob/master/perlmutter-tutorial.md)

## Getting Set Up

The starter code is available on GitHub at [https://github.com/Berkeley-CS267/HW1](https://github.com/Berkeley-CS267/HW1) and should work out of the box. To get started, we recommend you log in to Perlmutter and download the first part of the assignment. This will look something like the following:

```
student@local:~> ssh <username>@perlmutter.nersc.gov 
student@login04:~> git clone [https://github.com/Berkeley-CS267/HW1.git](https://github.com/Berkeley-CS267/HW1.git)
student@login04:~> cd HW1
student@login04:~/HW1> ls
CMakeLists.txt  README.md  benchmark.c  dgemm-blas.c  dgemm-blocked.c  dgemm-naive.c  job.in
```

There are seven files in the base repository. Their purposes are as follows:

* **CMakeLists.txt**


The build system that manages compiling your code.
* **README.md**


README file explaining the build system in more detail.
* **benchmark.c**

A driver program that runs your code.
* **dgemm-blas.c**

A wrapper which calls the vendor's optimized BLAS implementation of matrix multiply.
* **dgemm-blocked.c**  - - -  **You may only modify this file.** 

A simple blocked implementation of matrix multiply. It is your job to optimize the `square_dgemm()` function in this file.
* **dgemm-naive.c** 

For illustrative purposes, a naive implementation of matrix multiply using three nested loops.
* **job.in**

Template job script that is filled in by the build system for each of **blas, blocked, and naive**.


> Please **do not** modify any of the files besides _dgemm-blocked.c_

## Building our Code

First, we need to make sure that the CMake module is loaded and that the GNU compiler is selected.

```
student@login04:~/HW1> module load cmake
```

You should put these commands in your `~/.bash_profile` file to avoid typing them every time you log in.

Next, let's build the code. CMake prefers out of tree builds, so we start by creating a build directory.

```
student@login04:~/HW1> mkdir build
student@login04:~/HW1> cd build
student@login04:~/HW1/build>
```

Next, we have to **configure our build**. We can either build our code in **Debug** mode or Release mode. In debug mode, optimizations are disabled and debug symbols are embedded in the binary for easier debugging with GDB. In release mode, optimizations are enabled, and debug symbols are omitted. For example:

```
student@login04:~/HW1/build> cmake -DCMAKE_BUILD_TYPE=Release ..
-- The C compiler identification is GNU 12.3.0
...
-- Configuring done
-- Generating done
-- Build files have been written to: /global/homes/s/student/HW1/build
```

Once our build is configured, we may actually **execute** the build:

```
student@login04:~/HW1/build> make
Scanning dependencies of target benchmark
[ 14%] Building C object CMakeFiles/benchmark.dir/benchmark.c.o
[ 14%] Built target benchmark
...
[ 85%] Building C object CMakeFiles/benchmark-naive.dir/dgemm-naive.c.o
[100%] Linking C executable benchmark-naive
[100%] Built target benchmark-naive

student@login04:~/HW1/build> ls
benchmark-blas     benchmark-naive  CMakeFiles           job-blas     job-naive
benchmark-blocked  CMakeCache.txt   cmake_install.cmake  job-blocked  Makefile
```

We now have three **binaries** (`benchmark-blas`, `benchmark-blocked`, and `benchmark-naive`) and three corresponding **job scripts** (`job-blas`, `job-blocked`, and `job-naive`). Feel free to create your own job scripts by copying one of these to the above source directory.

### Other build considerations

You might find that your code works in Debug mode, but not Release mode. To add debug symbols to a release build, run:

```
student@login04:~/HW1/build> cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_FLAGS="-g3" ..
```

You can add arbitrary extra compiler flags in this way, just remember to re-run **make** after you do this.

## Running our Code

The easiest way to run the code is to submit a batch job. We've already provided batch files which will launch jobs for each matrix multiply version.

```
student@login04:~/HW1/build> sbatch job-blas
Submitted batch job 27505251
student@login04:~/HW1/build> sbatch job-blocked
Submitted batch job 27505253
student@login04:~/HW1/build> sbatch job-naive
Submitted batch job 27505255
```

Our jobs are now submitted to Perlmutter's job queue. We can now check on the status of our submitted jobs using a few different commands.

```
student@login04:~/HW1/build> squeue -u student
             JOBID PARTITION     NAME     USER ST      TIME  NODES NODELIST(REASON)
           4613712 regular_m job-naiv    yuedai PD       0:00      1 (QOSMaxJobsPerUserLimit)
           4613708 regular_m job-bloc    yuedai  R       0:07      1 nid004961
           4613705 regular_m job-blas    yuedai  R       0:16      1 nid005254

student@login04:~/HW1/build> sqs
JOBID           ST USER      NAME          NODES TIME_LIMIT       TIME  SUBMIT_TIME          QOS             START_TIME          FEATURES       NODELIST(REASON
4613760          PD yuedai    job-naive      1           2:00       0:00  2023-01-11T21:38:08  debug           2023-01-11T21:38:35  cpu            (QOSMaxJobsPerU
4613758          R  yuedai    job-blocked    1           2:00       0:02  2023-01-11T21:38:04  debug           2023-01-11T21:38:33  cpu            nid004649      
4613754          R  yuedai    job-blas       1           2:00       0:07  2023-01-11T21:37:58  debug           2023-01-11T21:38:28  cpu            nid006483
```

When our job is finished, we'll find new files in our directory containing the output of our program. For example, we'll find the files `job-blas.o4613754` and `job-blas.e4613754`. The first file contains the [standard output](https://en.wikipedia.org/wiki/Standard_streams) of our program, and the second file contains the [standard error](https://en.wikipedia.org/wiki/Standard_streams).

## Interactive Session

You may find it useful to launch an [interactive session](https://docs.nersc.gov/jobs/interactive/#cori) when developing your code. This lets you compile and run code interactively on a compute node that you've reserved. In addition, running interactively lets you use the special interactive queue, which means you'll receive your allocation quicker. To launch an interactive Milan node for 1 hour and run a benchmark (after you've built your code), try this:

```
student@login04:~/HW1> salloc -N 1 -C cpu -q interactive -t 01:00:00
salloc: Pending job allocation 4613849
salloc: job 4613849 queued and waiting for resources
salloc: job 4613849 has been allocated resources
salloc: Granted job allocation 4613849
salloc: Waiting for resource configuration
salloc: Nodes nid005179 are ready for job

student@nid005179:~/HW1> cd build
student@nid005179:~/HW1/build> ./benchmark-blocked
```

Interactive nodes may not always be available, depending on system demand. Be aware that compiling your code is much slower on an interactive node compared to a login node.

## Editing the Code

One of the easiest ways to implement your homework is to directly change the code on the server. For this you need to use a command line editor like `nano` or `vim`.

For beginners we recommend taking your first steps with `nano`. You can use it on Perlmutter like this:

```
student@login04:~/HW1> module load nano
student@login04:~/HW1> nano dgemm-blocked.c
```
Use `Ctrl+X` to exit.

For a more complete code editor try _vim_ which is loaded by default:
```
student@login04:~/HW1> vim dgemm-blocked.c
```
Use `Esc` and `:q` to exit. (`:q!` if you want to discard changes). Try out the [interactive vim tutorial](https://www.openvim.com/) to learn more.

If you're more familiar with a graphical environment, many popular IDEs can use the provided `CMakeLists.txt` as a project definition. Refer to the documentation of your particular IDE for help setting this up. Using hosted version control like GitHub makes uploading your changes much easier. If you're in a Windows environment, consider using the Windows Subsystem for Linux (WSL) for development.

## Our Harness

The `benchmark.c` file generates matrices of a number of different sizes and benchmarks the performance. It outputs the performance in [FLOPS](https://en.wikipedia.org/wiki/FLOPS) and in a percentage of theoretical peak attained. Your job is to get your matrix-multiply's performance as close to the theoretical peak as possible.

When you run your code on a different computer, you will likely need to adjust the **MAX_SPEED** variable. This can be done like so:

```
student@login04:~/HW1/build> cmake -DCMAKE_BUILD_TYPE=Debug -DMAX_SPEED=56 ..
student@login04:~/HW1/build> make
```

On **Perlmutter**, this value is computed as 3.5 GHz * 4 vector width * 2 vector pipelines * 2 flops for FMA = **56 GF/s**.

## Perlmutter's Processors

### Perlmutter

In this assignment, we will only be using **Perlmutter AMD Milan**. Be sure you use the flag `-C cpu` on any jobs that you run. The job files included with the starter code do this automatically.

### Theoretical Peak

Our benchmark harness reports numbers as a percentage of theoretical peak. Here, we show you how we calculate the theoretical peak of Perlmutter's AMD Milan processors. If you'd like to run the assignment on your own processor, you should follow this process to arrive at the theoretical peak of your own machine, and then replace the **MAX_SPEED** constant in `benchmark.c` with the theoretical peak of your machine. Be sure to change it back if you run your code on Perlmutter again.

### One Core

One core has a normal clock rate of 2.45 GHz, and boost mode clock rate 3.5GHz, so it can issue 3.5 billion instructions per second at maximum. Perlmutter's processors also have a 256-bit _vector width_, meaning each instruction can operate on 4 64-bit data elements at a time. Furthermore, the Milan microarchitecture includes a _fused multiply-add_ (FMA) instruction, which means 2 floating point operations can be performed in a single instruction.

So, the theoretical peak of Perlmutter's Milan nodes is:
- 3.5 GHz * 4-element (256-bit) vector * 2 vector pipelines * 2 ops in an FMA = 56 GFlops/s

### Optimizing

Now, it's time to optimize!  A few optimizations you might consider adding:
1. Perform blocking. The dgemm-blocked.c already gets you started with this, although you'll need to tune block sizes.
2. Write a register-blocked kernel, either by writing an inner-level fixed-size matrix multiply and hoping (and [maybe checking](https://godbolt.org/)) that the compiler inlines it, writing [AVX intrinsics](https://software.intel.com/sites/landingpage/IntrinsicsGuide/), or even writing inline assembly instructions.
3. Add manual prefetching.

You may, of course, proceed however you wish.  We recommend you look through the lecture notes as reference material to guide your optimization process, as well as the references at the bottom of this write-up.

### Available Compilers

The development environment on Perlmutter supplies several different compilers, including GNU, Cray, and AOCC. However, we want you to use the GNU C compiler for this assignment. GNU compiler will be used as default, but you can make sure you are using GNU by running:
```
student@login04:~> module load PrgEnv-gnu
```

Still, you might want to try your code with different compilers to see if one outperforms the other. If the difference is significant, consider using the [Compiler Explorer](https://gcc.godbolt.org/z/v2fTDJ) to figure out why GCC isn't optimizing your code as well. For more information on compilers available on Perlmutter, see the [NERSC docs](http://www.nersc.gov/users/computational-systems/cori/programming/compiling-codes-on-cori/).

---

# Grading

We will grade your assignment by reviewing your assignment write-up, looking at the optimization methods you attempted, and benchmarking your code's performance. To benchmark your code, we will compile it with the exact process detailed above, with the GNU compiler. Note that code that does not return correct results will receive significant penalties.

## Submission Details

Supposing you are **Group #04**, follow these steps to create an appropriate submission archive:

1.  Ensure that your write-up is located in your source directory, next to **dgemm-blocked.c**. It should be named **cs267Group04_hw1.pdf**.
2.  From your **build** directory, run:
    ```
    student@login04:~/HW1/build> cmake -DGROUP_NO=04 ..
    student@login04:~/HW1/build> make package
    ```
    This second command will fail if the PDF is not present.
3.  Confirm that it worked using the following command. You should see output like:
    ```
    student@login04:~/HW1/build> tar tfz cs267Group04_hw1.tar.gz 
    cs267Group04_hw1/cs267Group04_hw1.pdf
    cs267Group04_hw1/dgemm-blocked.c
    ```
4.  Submit your .tar.gz through bCourses.

## Write-up Details

* Your write-up should contain:
    * the names of the people in your group (and each member's contribution),
    * the optimizations used or attempted,
    * the results of those optimizations,
    * the reason for any odd behavior (e.g., dips) in performance
* Please carefully read the notes for implementation details. Stay tuned to Ed discussion for updates and clarifications, as well as discussion.
* If you are new to optimizing numerical codes, we recommend reading the papers in the references section.
* Your write-up should be a maximum of 8 pages in length, including all text, figures, tables, and references.

---

# Notes

* **Your grade will mostly depend on three factors:**
    * whether or not it is correct (ie. finishes running without exiting early)
    * performance sustained by your codes on the Perlmutter supercomputer,
    * explanations of the performance features you observed (including what didn't work)
* There are other formulations of matmul (e.g., [Strassen](http://en.wikipedia.org/wiki/Strassen_algorithm)) that are mathematically equivalent, but perform asymptotically fewer computations - we will not grade submissions that do fewer computations than the 2n^3 algorithm. This is actually an optional part of HW1.
* You must use the GNU C Compiler 12.3 for this assignment. If your code does not compile and run with GCC 12.3, it will not be graded.
* Besides compiler intrinsic functions and built-ins, your code (`dgemm-blocked.c`) must only call into the C standard library.
* GNU C provides [many](http://gcc.gnu.org/onlinedocs/gcc/C-Extensions.html) extensions, which include intrinsics for vector (SIMD) instructions and data alignment. (Other compilers may have different interfaces.)
    * To manually vectorize, you should prefer to add compiler intrinsics to your code; avoid using inline assembly, at least at first.
    * The [Compiler Explorer](https://gcc.godbolt.org/z/v2fTDJ) project will be useful for exploring the relationship between your C code and its corresponding assembly. Release mode builds compile with `-O3`.
* You may assume that A and B do not alias C; however, A and B may alias each other. It is semantically correct to qualify C (the last argument to square_dgemm) with the C99 `restrict` keyword. There is a lot online about restrict and pointer-aliasing - [this](http://cellperformance.beyond3d.com/articles/2006/05/demystifying-the-restrict-keyword.html) is a good article to start with, along with the [Wikipedia article](https://en.wikipedia.org/wiki/Restrict) on the restrict keyword.
* The matrices are all stored in [column-major order](http://en.wikipedia.org/wiki/Row-major_order), i.e. `C[i,j] == C(i,j) == C[(i-1)+(j-1)*n]`, for `i=1:n`, where `n` is the number of rows in C. Note that we use 1-based indexing when using mathematical symbols and MATLAB index notation (parentheses), and 0-based indexing when using C index notation (square brackets).
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

If you wish to submit optional parts, send them to us via email, rather than through the bCourses system.

---

# Documentation

* [Perlmutter's programming environment](https://docs.nersc.gov/systems/perlmutter/) documentation
* [GCC](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/) documentation - Perlmutter's default version currently is GCC 12.3.0.
* [Intel's intrinsics guide](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#techs=AVX2,FMA) - a complete overview of all available vector intrinsics.
* [GCC's vector extensions](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/Vector-Extensions.html#Vector-Extensions) - special types that make programming with vectors easier
* [GCC's built-ins](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/Other-Builtins.html#Other-Builtins) - special commands that give optimization hints to the compiler. See assume_aligned, unreachable, and expect. [Some are specific to x86.](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/x86-Built-in-Functions.html#x86-Built-in-Functions)
* [GCC's variable attributes](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/Common-Variable-Attributes.html#Common-Variable-Attributes) - useful for optimizing the memory layout of your program
* [GCC's function attributes](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/Common-Function-Attributes.html#Common-Function-Attributes) - useful for controlling the optimization of particular functions. Some are [specific to x86.](https://gcc.gnu.org/onlinedocs/gcc-11.2.0/gcc/x86-Function-Attributes.html#x86-Function-Attributes)

You are also welcome to learn from the source code of state-of-art BLAS implementations such as [ATLAS](http://math-atlas.sourceforge.net/). However, you should not reuse those codes in your submission.

* We emphasize these are example scripts because for these as well as all other assignment scripts we provide, you may need to adjust the number of requested nodes and cores and amount of time according to your needs (your allocation and the total class allocation is limited).  To understand how you are charged, [READ THIS](http://www.nersc.gov/users/accounts/user-accounts/how-usage-is-charged/) alongside the given scripts.  For testing (1) try running and debugging on your laptop first, (2) try running with the minimum resources you need for testing and debugging, (3) once your code is fully debugged, use the amount of resources you need to collect the final results for the assignment.  This will become more important for later assignments, but it is good to get in the habit now.
---

# References

* Goto, K., and van de Geijn, R. A. 2008. Anatomy of High-Performance Matrix Multiplication, ACM Transactions on Mathematical Software 34, 3, Article 12.
    * (Note: explains the design decisions for the GotoBLAS dgemm implementation, which also apply to your code.)
* Chellappa, S., Franchetti, F., and Puschel, M. 2008. [How To Write Fast Numerical Code: A Small Introduction](https://users.ece.cmu.edu/~franzf/papers/gttse07.pdf), Lecture Notes in Computer Science 5235, 196-259.
    * (Note: how to write C code for modern compilers and memory hierarchies, so that it runs fast. Recommended reading, especially for newcomers to code optimization.)
* Bilmes, et al. [The PHiPAC (Portable High Performance ANSI C) Page for BLAS3 Compatible Fast Matrix Matrix Multiply](https://people.eecs.berkeley.edu/~krste/papers/phipac_ics97.pdf).
    * (Note: PHiPAC is a code-generating autotuner for matmul that started as a submission for this HW in a previous semester of CS267. Also see [ATLAS](http://math-atlas.sourceforge.net/); both are good examples if you are considering code generation strategies.)
* Lam, M. S., Rothberg, E. E, and Wolf, M. E. 1991. The Cache Performance and Optimization of Blocked Algorithms, ASPLOS'91, 63-74.
    * (Note: clearly explains cache blocking, supported by with performance models.)