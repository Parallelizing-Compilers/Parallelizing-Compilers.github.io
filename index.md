---
layout: page
# Index page
---

# CS6245: Parallelizing Compilers
CRN-34760

All computers today are parallel computers.  Are you curious about how to generate or write code for parallel processors (vector, multicore, GPU, clusters) in modern computing systems, and how to better use memory hierarchies (scratchpads, aches, TLBs)?  What program properties enable or prevent an application from exploiting the parallelism and locality on modern hardware?  These questions have taken on new importance as parallelism is now ubiquitous in hardware with the end of Dennard Scaling and Moore's Law, and has also become critical for newer application domains including machine learning and data analytics.  To address these questions, this course will cover the foundations of compilation techniques for parallel computer systems, including the analysis of data and control dependences and program transformations to enhance fine-grained parallelism, register/cache locality, and coarse-grained parallelism.  By the end of this course, students will be knowledgeable about the strengths and limitations of state-of-the-art compilers, both from the viewpoint of the application developers as well as of the compiler developer. The techniques taught in the course should be relevant to anyone interested in enabling software to execute efficiently on current and future parallel processors, whether the parallelism is created manually or through the use of compilers.

## Learning Objectives

Upon successful completion of this course, you should be able to:

- Understand the capabilities and limitations of different array dependence analysis techniques
- Understand the capabilities and limitations of different loop transformations for locality and parallelism (distribution, fusion, interchange, skewing, tiling, polyhedral)
- Design compiler extensions to perform automatic parallelization, and related high-level code optimizations
- Through your project, learn about the state of the art in current research on a topic of your choice related to parallelizing compilers. Your project report should include: (1) an abstract problem statement that can be stated formally, (2) an overview of your solution approach, (3) demonstration of the practicality of your approach through a prototype implementation in a compiler framework or through performance studies of hand-coded examples, and (4) a comparison with related work.


## Policies
See the [Course Policies](/policies) for more information on grading, assignments, and other course policies.

## Course Information

- **Course Code:** CS6245 
- **CRN:** 34760  
- **Credits:** 3  
- **Instructor:** Willow Ahrens ([ahrens@gatech.edu](mailto:ahrens@gatech.edu))  
- **Office Hours:** `TBD`
- **TA**: Ruchika R Shirsath ([rshirsath3@gatech.edu](mailto:rshirsath3@gatech.edu)) and Joel Mathew Cherian ([jcherian32@gatech.edu](mailto:jcherian32@gatech.edu))
- **TA Office Hours:** `TBD`
- **Meeting Room:**  College of Computing Room 101
- **Meeting Time:** Monday & Wednesday, 5:00–6:15 PM

## Course Materials

- **Textbook:** R. Allen and K. Kennedy, Optimizing Compilers for Modern Architectures, Morgan-Kaufmann, Second Printing, 2005.
- **Additional Readings:** Additional readings will be recommended throughout the course. You will need to authenticate to the [Georgia Tech Library Proxy](https://library.gatech.edu/research-help-support/accessing-eresources) to access the official versions of these readings. For convenience, try adding the papers you read to a citation manager, such as [Zotero](https://www.zotero.org/) or [Mendeley](https://www.mendeley.com/).

## Assignments

- There will be 4 homework assignments, a midterm exam, a final exam, and a final project.
- Additionally, there will be in-class worksheets to help you practice concepts.
- Please see the [Course Policies](/policies) for more information on grading.

## Schedule

| Date | Topic | Assignments |
| --- | --- | --- |
| Mon, Jan 12 | Class: Course Overview, Motivation, Preview |
| Wed, Jan 14 | Class: Performance Engineering and Measurement | [Homework 1](https://sites.google.com/lbl.gov/cs267-spr2025/hw-1) Assigned |
| Mon, Jan 19 | NO CLASS - SCHOOL HOLIDAY |
| Wed, Jan 21 | Performance Modeling |
| Mon, Jan 26 | Optimization by Hand |
| Wed, Jan 28 | Dependence Analysis |
| Mon, Feb 2 | Dependence Theory | Homework 2 Assigned |
| Wed, Feb 4 | Dependence Theory |
| Fri, Feb 6 |  | Homework 1 Due |
| Mon, Feb 9 | Vectorization |
| Wed, Feb 11 | Vectorization Continued |
| Mon, Feb 16 | Dependence Testing |
| Wed, Feb 18 | Polyhedral Compilation Intro |
| Mon, Feb 23 | Polyhedral Compilation |
| Wed, Feb 25 | Enhancing Fine-Grained Parallelism |
| Fri, Feb 27 |  | Homework 2 Due |
| Mon, Mar 2 | Unimodular Transformations |
| Wed, Mar 4 | Midterm Review |
| TBD | Midterm |
| Mon, Mar 9 | Cache Management | Homework 3 Assigned |
| Wed, Mar 11 | Cache Management |
| Mon, Mar 16 | Compiler Improvement of Register Usage |
| Wed, Mar 18 | Control Flow |
| Fri, Mar 20 |  | Homework 3 Due |
| Mon, Mar 23 | NO CLASS - SPRING BREAK |
| Wed, Mar 25 |
| Mon, Mar 30 | If Conversion | Homework 4 assigned |
| Wed, Apr 1 | Creating Course-Grained Parallelism |
| Mon, Apr 6 | Loop Fusion |
| Wed, Apr 8 | Compiling Array Assignments |
| Mon, Apr 13 | Domain-Specific Languages |
| Wed, Apr 15 | DSLs for Distributed Memory |
| Fri, Apr 17 |  | Homework 4 due |
| Mon, Apr 20 | DSLs for Sparse Arrays |
| Wed, Apr 22 | Course Review |
| Mon, Apr 27 | Final project presentations |
| TBD | Final Exam |