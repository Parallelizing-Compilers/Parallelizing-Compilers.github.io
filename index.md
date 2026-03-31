---
layout: page
# Index page
---

# CS6245: Parallelizing Compilers
CRN-34760

All computers today are parallel computers.  Are you curious about how to generate or write code for parallel processors (vector, multicore, GPU, clusters) in modern computing systems, and how to better use memory hierarchies (scratchpads, aches, TLBs)?  What program properties enable or prevent an application from exploiting the parallelism and locality on modern hardware?  These questions have taken on new importance as parallelism is now ubiquitous in hardware with the end of Dennard Scaling and Moore's Law, and has also become critical for newer application domains including machine learning and data analytics.  To address these questions, this course will cover the foundations of compilation techniques for parallel computer systems, including the analysis of data and control dependences and program transformations to enhance fine-grained parallelism, register/cache locality, and coarse-grained parallelism.  By the end of this course, students will be knowledgeable about the strengths and limitations of state-of-the-art compilers, both from the viewpoint of the application developers as well as of the compiler developer. The techniques taught in the course should be relevant to anyone interested in enabling software to execute efficiently on current and future parallel processors, whether the parallelism is created manually or through the use of compilers.

## Learning Objectives

Upon successful completion of this course, you should be able to:

- Optimize the performance of compiler-generated code and HPC programs.
- Understand the capabilities and limitations of loop transformations for locality and parallelism (distribution, fusion, interchange, skewing, tiling, polyhedral)
- Design compiler extensions to perform automatic parallelization, and related high level code optimizations
- Through your project, learn about the state of the art in current research on a topic of your choice related to optimizing compilers. Your project report should include: (1) an abstract problem statement that can be stated formally, (2) an overview of your solution approach, (3) demonstration of the practicality of your approach through a prototype implementation in a compiler framework or through performance studies of hand-coded examples, and (4) a comparison with related work.

## Policies
See the [Course Policies](/policies) for more information on grading, assignments, and other course policies.

## Course Information

- **Course Code:** CS6245 
- **CRN:** 34760  
- **Credits:** 3  
- **Instructor:** Willow Ahrens ([ahrens@gatech.edu](mailto:ahrens@gatech.edu))  
- **Office Hours:** 12:00 PM - 1:00 PM on Tuesdays in Klaus Advanced Computing Building, Room 3144
- **TA**: Ruchika R Shirsath ([rshirsath3@gatech.edu](mailto:rshirsath3@gatech.edu)) and Joel Mathew Cherian ([jcherian32@gatech.edu](mailto:jcherian32@gatech.edu))
- **TA Office Hours:** 11:00 AM - 12:00 PM on Thursdays in Klaus Advanced Computing Building, Room 2108
- **Class Room:**  College of Computing Room 101
- **Class Time:** Monday & Wednesday, 5:00–6:15 PM

## Course Materials

- **Textbook:** Randy Allen and Ken Kennedy, Optimizing Compilers for Modern Architectures, Morgan-Kaufmann, Second Printing, 2005.

- **Optional Textbook:** Alfred V. Aho, Jeffrey D. Ullman, Ravi Sethi, Monica S. Lam, Compilers: Principles, Techniques, and Tools, 2nd edition, 2011.

- **Additional Readings:** Additional readings will be recommended throughout the course. You will need to authenticate to the [Georgia Tech Library Proxy](https://library.gatech.edu/research-help-support/accessing-eresources) to access the official versions of these readings. For convenience, try adding the papers you read to a citation manager, such as [Zotero](https://www.zotero.org/) or [Mendeley](https://www.mendeley.com/).

## Assignments

- There will be 4 homework assignments, a midterm exam, a final exam, and a final project.
- Additionally, there will be in-class worksheets to help you practice concepts.
- Please see the [Course Policies](/policies) for more information on grading.

## Schedule

| Date | Topic | Assignments | Reading |
| --- | --- | --- | --- |
| Mon, Jan 12 | Class: Course Overview, Motivation, Preview |  | [A New Golden Age for Computer Architecture](https://cacm.acm.org/research/a-new-golden-age-for-computer-architecture/)<br/>[How to Read a Paper](https://web.stanford.edu/class/cs245/readings/how-to-read-a-paper.pdf) <br/>[How to Write a Good Systems Paper](https://ben.edu/wp-content/uploads/2022/06/How-and-How-Not-to-Write-a-Good-Systems-Paper.pdf)|
| Wed, Jan 14 | Class: Timing and Measurement | [Homework 1](https://sites.google.com/lbl.gov/cs267-spr2025/hw-1) Assigned | [Sigplan Guidelines for Empirical Measurement](https://www.sigplan.org/Resources/EmpiricalEvaluation/)<br/>[Scientific benchmarking of parallel computing systems: twelve ways to tell the masses when reporting performance results](https://doi.org/10.1145/2807591.2807644)<br/>[Producing wrong data without doing anything obviously wrong!](https://doi.org/10.1145/1508284.1508275) |
| Mon, Jan 19 | NO CLASS - SCHOOL HOLIDAY |
| Wed, Jan 21 | Performance Modeling and Optimization |  | Chapter 1 of Allen and Kennedy<br/>[Roofline: an insightful visual performance model for multicore architectures](https://doi.org/10.1145/1498765.1498785) |
| Mon, Jan 26 | NO CLASS - SNOW DAY |
| Wed, Jan 28 | Data Dependence |  | Chapter 2.1-2.3 of Allen and Kennedy |
| Mon, Feb 2 | Dependence and Parallelism |  | Chapter 2.4 of Allen and Kennedy |
| Wed, Feb 4 | Dependence Testing |  | Chapter 3 of Allen and Kennedy |
| Fri, Feb 6 |  | Homework 1 Due |
| Mon, Feb 9 | Term Rewriting |  | [Achieving high-performance the functional way: a functional pearl on expressing high-performance optimizations as rewrite strategies](https://doi.org/10.1145/3580371)<br/>[Software Design for Flexibility, Chapter 4](https://mitpress.mit.edu/9780262045490/software-design-for-flexibility/) |
| Wed, Feb 11 | Syntax and Semantics |  | "Types and Programming Languages" by Benjamin A. Pierce<br/>[Heartbeat Scheduling: Provable Efficiency for Nested Parallelism](https://doi.org/10.1145/3192366.3192391) |
| Mon, Feb 16 | Dataflow and Preliminary Transformations | Homework 2 Assigned | Chapter 4 of Allen and Kennedy<br/>[Compilers: Principles, Techniques, and Tools, Second Edition, Chapter 9](https://dl.acm.org/doi/10.5555/1177220)<br/>[Lecture 4, Dataflow Analysis, Cornell CS 6120](https://www.cs.cornell.edu/courses/cs6120/2025sp/lesson/4/) |
| Wed, Feb 18 | Domain-Specific Languages |  | [Programming Pearls: Little Languages](https://doi.org/10.1145/6424.315691) <br/> [Halide: decoupling algorithms from schedules for high-performance image processing](https://doi.org/10.1145/3150211) <br/> [DSL4HPC](https://dsls-for-hpc.github.io) |
| Fri, Feb 20 |  | Final Project Proposals Due |
| Mon, Feb 23 | Enhancing Fine-Grained Parallelism |  | Chapter 5 of Allen and Kennedy |
| Wed, Feb 25 | Enhancing Course-Grained Parallelism |  | Chapter 6 of Allen and Kennedy |
| Fri, Feb 27 |  | Homework 2 Due |
| Mon, Mar 2 | Unimodular Transformations |  | [Presburger Formulas and Polyhedral Compilation](https://joelburget.com/polycomp-tutorial-v0.02.pdf)<br>[Compilers: Principles, Techniques, and Tools, Chapter 10.4, 11](https://dl.acm.org/doi/10.5555/1177220) |
| Wed, Mar 4 | Midterm |
| Mon, Mar 9 | Compiler Management of Registers |  | Chapter 8 of Allen and Kennedy |
| Wed, Mar 11 | Compiler Management of Cache | Homework 3 Assigned | Chapter 9 of Allen and Kennedy |
| Mon, Mar 16 | Scheduling Languages |
| Wed, Mar 18 | Polyhedral Compilation |  | [Presburger Formulas and Polyhedral Compilation](https://joelburget.com/polycomp-tutorial-v0.02.pdf)<br>[Compilers: Principles, Techniques, and Tools, Chapter 10.4, 11](https://dl.acm.org/doi/10.5555/1177220) |
| Fri, Mar 20 |  | Homework 3 Due |
| Mon, Mar 23 | NO CLASS - SPRING BREAK |
| Wed, Mar 25 |
| Mon, Mar 30 | Autoscheduling |  | [OpenTuner: An Extensible Framework for Program Autotuning](https://doi.org/10.1145/2628071.2628092)<br/> [Autotuning in High-Performance Computing Applications](https://doi.org/10.1109/JPROC.2018.2841200) |
| Wed, Apr 1 | Scalarization | Homework 4 Assigned | Chapter 13 of Allen and Kennedy |
| Mon, Apr 6 | Dependence and Control Flow |  | Chapter 7 of Allen and Kennedy<br/>[All you need is superword-level parallelism: systematic control-flow vectorization with SLP](https://dl.acm.org/doi/10.1145/3519939.3523701) |
| Wed, Apr 8 | Compilers for Irregular Data |  | [The tensor algebra compiler](https://doi.org/10.1145/3133901)<br/>[Looplets: A Language for Structured Coiteration](https://doi.org/10.1145/3579990.3580020) |
| Mon, Apr 13 | Compilers for Accelerators |  | [Task-Based Tensor Computations on Modern GPUs](https://doi.org/10.1145/3729262) |
| Wed, Apr 15 | Compilers for Distributed Memory |  | [Legion: Expressing Locality and Independence with Logical Regions](https://doi.org/10.1109/SC.2012.71)<br/>[DISTAL: The Distributed Tensor Algebra Compiler](https://doi.org/10.1145/3519939.3523437) |
| Fri, Apr 17 |  | Homework 4 due |
| Mon, Apr 20 | Final project presentations (5 min each + 4 min questions) |
| Wed, Apr 22 | Final project presentations (5 min each + 4 min questions) |
| Mon, Apr 27 | Final project presentations (5 min each + 4 min questions) |
| Fri, May 1 | Final Exam (6:00pm - 8:50pm) |

## Inspired by
- [GA Tech CS 8803-DSL: Domain Specific Languages for High Performance Computing](https://dsls-for-hpc.github.io), Willow Ahrens.
- [Stanford CS343D: Domain-Specific Programming Models and Compilers](https://cs343d.github.io/course_info.html), Fredrik Kjolstad.
- [MIT 6.172: Performance Engineering of Software Systems](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/),
- [Cornell CS 6120: Advanced Compilers](https://www.cs.cornell.edu/courses/cs6120/2025sp/syllabus/)
- [UC Berkeley CS267: Applications of Parallel Computers](https://sites.google.com/lbl.gov/cs267-spr2022), Aydin Buluc, Kathy Yelick, James Demmel.
- [UC Berkeley CS294: Building User-Centered Programming Tools](https://schasins.com/cs294-usable-programming-2025/)
- [Stanford CS448h: Domain-specific Languages for Graphics, Imaging, and Beyond](https://cs448h.stanford.edu/)
- [6.S894: Accelerated Computing](https://accelerated-computing-class.github.io/fall24/)

