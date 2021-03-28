# dc-mst-hssga

This repository is a third-party implementation of [A hybrid genetic algorithm for the degree-constrained minimum spanning tree problem](https://doi.org/10.1007/S00500-019-04051-X).

# Requirements

- python 3.8.3

# Getting Started

Open dc_mst_ga.py and run the example code.\

Given an adjacency matrix
$$
A=\left[\begin{array}{ccccccccc}
0 & 224 & 224 & 361 & 671 & 300 & 539 & 800 & 943 \\
224 & 0 & 200 & 200 & 447 & 283 & 400 & 728 & 762 \\
224 & 200 & 0 & 400 & 566 & 447 & 600 & 922 & 949 \\
361 & 200 & 400 & 0 & 400 & 200 & 200 & 539 & 583 \\
671 & 447 & 566 & 400 & 0 & 600 & 447 & 781 & 510 \\
300 & 283 & 447 & 200 & 600 & 0 & 283 & 500 & 707 \\
539 & 400 & 600 & 200 & 447 & 283 & 0 & 361 & 424 \\
800 & 728 & 922 & 539 & 781 & 500 & 361 & 0 & 500 \\
943 & 762 & 949 & 583 & 510 & 707 & 424 & 500 & 0
\end{array}\right]
$$
and a degree constraint $d\le3$.

We can find the exact solution shown below.

![example](D:\mine\Github\_mine_github\dc-mst-hssga\example.png)

# License

MIT

# Acknowledgments

- UCAS course: Intelligent Optimization Methods [070105M05002H](http://jwxk.ucas.ac.cn/course/courseplan/184399)