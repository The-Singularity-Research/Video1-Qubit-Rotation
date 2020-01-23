# Video1-Qubit-Rotation
Video 1: Qubit Rotation Tutorial in PennyLane

In this repository, we will go through the [PennyLane tutorial on qubit rotations](https://pennylane.ai/qml/tutorial/tutorial_qubit_rotation.html). 

## Prerequisites

We have included a [PDF document](https://github.com/The-Singularity-Research/Video1-Qubit-Rotation/blob/master/video1_qubit_rotation_latex.pdf) showing how to convert quantum circuit diagrams to linear algebra. 

For example, in the PennyLane tutorial, the following circuit diagram:

![circuit_diagram_pltutorial](circuit_diagram_pltutorial.png)

can be interpreted as matrix operators, the first operator being:

![matrix_operator_pltutorial](matrix_operator_pltutorial.png)

The PDF document includes the Pauli operators (also called the Pauli gates), the Hadamard gate, and the CNOT gate. There are three circuits. The first two only involve a single qubit and should be very easy for people who already know the basics of linear algebra. If you are not familiar with linear algebra, it is a prerequisite, so it is highly recommended that you go to Khan Academy and go through their [linear algebra course](https://www.khanacademy.org/math/linear-algebra). This should be enough linear algebra to get you through the tutorials. 

The third circuit involves a CNOT gate on two qubits which means you will need to use a tensor product. If you are unfamiliar with tensor products, we will be using them often so you can get used to them as you go along, treat them as a black-box that the code takes care of, or you can go learn about tensor products in the context of quantum computing in this video:

[![Alt text](video1_video_thumbnail.png)](https://www.youtube.com/watch?v=F_Riqjdh2oM)

