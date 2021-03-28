# dc-mst-hssga

This repository is a third-party implementation of [A hybrid genetic algorithm for the degree-constrained minimum spanning tree problem](https://doi.org/10.1007/S00500-019-04051-X).

# Requirements

- python 3.8.3

# Getting Started

Open dc_mst_ga.py and run the example code.

Given an adjacency matrix

<img src="http://www.sciweavers.org/tex2img.php?eq=A%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bccccccccc%7D%0A0%20%26%20224%20%26%20224%20%26%20361%20%26%20671%20%26%20300%20%26%20539%20%26%20800%20%26%20943%20%5C%5C%0A224%20%26%200%20%26%20200%20%26%20200%20%26%20447%20%26%20283%20%26%20400%20%26%20728%20%26%20762%20%5C%5C%0A224%20%26%20200%20%26%200%20%26%20400%20%26%20566%20%26%20447%20%26%20600%20%26%20922%20%26%20949%20%5C%5C%0A361%20%26%20200%20%26%20400%20%26%200%20%26%20400%20%26%20200%20%26%20200%20%26%20539%20%26%20583%20%5C%5C%0A671%20%26%20447%20%26%20566%20%26%20400%20%26%200%20%26%20600%20%26%20447%20%26%20781%20%26%20510%20%5C%5C%0A300%20%26%20283%20%26%20447%20%26%20200%20%26%20600%20%26%200%20%26%20283%20%26%20500%20%26%20707%20%5C%5C%0A539%20%26%20400%20%26%20600%20%26%20200%20%26%20447%20%26%20283%20%26%200%20%26%20361%20%26%20424%20%5C%5C%0A800%20%26%20728%20%26%20922%20%26%20539%20%26%20781%20%26%20500%20%26%20361%20%26%200%20%26%20500%20%5C%5C%0A943%20%26%20762%20%26%20949%20%26%20583%20%26%20510%20%26%20707%20%26%20424%20%26%20500%20%26%200%0A%5Cend%7Barray%7D%5Cright%5D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="A=\left[\begin{array}{ccccccccc}0 & 224 & 224 & 361 & 671 & 300 & 539 & 800 & 943 \\224 & 0 & 200 & 200 & 447 & 283 & 400 & 728 & 762 \\224 & 200 & 0 & 400 & 566 & 447 & 600 & 922 & 949 \\361 & 200 & 400 & 0 & 400 & 200 & 200 & 539 & 583 \\671 & 447 & 566 & 400 & 0 & 600 & 447 & 781 & 510 \\300 & 283 & 447 & 200 & 600 & 0 & 283 & 500 & 707 \\539 & 400 & 600 & 200 & 447 & 283 & 0 & 361 & 424 \\800 & 728 & 922 & 539 & 781 & 500 & 361 & 0 & 500 \\943 & 762 & 949 & 583 & 510 & 707 & 424 & 500 & 0\end{array}\right]" width="482" height="182" />

and a degree constraint <img src="http://www.sciweavers.org/tex2img.php?eq=d%5Cle3&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="d\le3" width="47" height="17" />.

We can find the exact solution shown below.

![example](example.png)

# License

MIT

# Acknowledgments

- UCAS course: Intelligent Optimization Methods [070105M05002H](http://jwxk.ucas.ac.cn/course/courseplan/184399)