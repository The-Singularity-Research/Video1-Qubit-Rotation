# Video 1: Qubit Rotation Tutorial
Video 1: Qubit Rotation Tutorial in PennyLane

In this repository, we will go through the [PennyLane tutorial on qubit rotations](https://pennylane.ai/qml/tutorial/tutorial_qubit_rotation.html). 

## Prerequisites

### Programming Experience
You will not need any programing experience. The vast majority of the coding that you will need to do will be explained in the tutorials. You will be able to get more comfortable with coding in Python as we go. So don't worry if you are not a professional programmer, it is not really needed. If you are really into coding and you're already familiar with Python, then you are a step ahead! All you need to do now is learn linear algebra, tensor products, quantum computing, and machine learning!

### Anaconda and Jupyter
To run the tutorial, we will need Jupyter Notebooks. You can get Jupyter by downloading the latest version of [Anaconda](https://www.anaconda.com/distribution/). You can also run Jupyter Lab right in your browser without having to downlaod anything. Most of our tutorials will run in [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/). If you prefer to run Python scripts rather than the interactive environments provided by Jupyter Lab, we will provide Python Scripts as well. We will use terminal some, but not much, but feel free to convert everything over to those environments if you prefer. 


### Math

We have included a [PDF document](https://github.com/The-Singularity-Research/Video1-Qubit-Rotation/blob/master/video1_qubit_rotation_latex.pdf) showing how to convert quantum circuit diagrams to linear algebra. 

For example, in the PennyLane tutorial, the following circuit diagram:

![circuit_diagram_pltutorial](circuit_diagram_pltutorial.png)

can be interpreted as matrix operators, the first operator being:

![matrix_operator_pltutorial](matrix_operator_pltutorial.png)

The PDF document includes the Pauli operators (also called the Pauli gates), the Hadamard gate, and the CNOT gate. There are three circuits. The first two only involve a single qubit and should be very easy for people who already know the basics of linear algebra. If you are not familiar with linear algebra, it is a prerequisite, so it is highly recommended that you go to Khan Academy and go through their [linear algebra course](https://www.khanacademy.org/math/linear-algebra). This should be enough linear algebra to get you through the tutorials. 

The third circuit involves a CNOT gate on two qubits which means you will need to use a tensor product. If you are unfamiliar with tensor products, we will be using them often so you can get used to them as you go along, treat them as a black-box that the code takes care of, or you can go learn about tensor products in the context of quantum computing in this video:

[![Alt text](video1_video_thumbnail.png)](https://www.youtube.com/watch?v=F_Riqjdh2oM)


## Gate Operations

Quantum gates are just unitary matrix operators that operate on one or several qubits. For example, the Hadamard gate puts a qubit into a superposition of the 0 and 1 state:

![superposition](https://cyberdefensereview.army.mil/Portals/6/Images/morris_quantum/morris_quantum_1.png?ver=2017-03-30-192830-177)

Operating on the qubit with other unitary operators (gates) can move it to some position on the Bloch sphere:

![Bloch sphere state](https://www.researchgate.net/publication/333130675/figure/fig3/AS:759029836034048@1557978223308/The-Bloch-sphere-representation-of-a-single-quantum-bit.jpg)

More complicated operators may operate on several qubits at a time, each of which might be in a superposition. In this tutorial we focus on a single qubit to keep things simple, but more complicated operations on tensor producst will be needed soon, so be sure to think about the third circuit diagram given in the [Circuit Diagrams to Linear Algebra Document](https://github.com/The-Singularity-Research/Video1-Qubit-Rotation/blob/master/video1_qubit_rotation_latex.pdf).
