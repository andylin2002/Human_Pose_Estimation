## Overview

This project implements a human pose estimation algorithm, as part of EAI Lab 3. **Human Pose Estimation (HPE) captures coordinates for joints (arms, head, torso, etc.)**, known as keypoints, to describe a person's pose [1]. The connections between these keypoints are called pairs [1]. This lab explores deep learning-based approaches to 2D HPE [2].

## Algorithm

This implementation likely involves a deep learning-based approach, possibly utilizing **Convolutional Neural Networks (CNNs)**, given their effectiveness in computer vision tasks [2]. Two common approaches for multi-person pose estimation are:

*   **Top-down:** Localize humans, estimate parts, then calculate the pose [3].
*   **Bottom-up:** Estimate body parts, then calculate the pose [3].

A bottom-up approach called **OpenPose** is mentioned as an efficient method for multi-person pose estimation that uses **Part Affinity Fields (PAFs)** to encode the location and orientation of limbs [4]. The network iteratively predicts PAFs and detection confidence maps [4].

The core of the algorithm likely involves:

1.  **Finding Gaussian peaks coordinates** in heatmaps [5].
2.  **Assigning Identity numbers** to these peaks [5].
3.  **Finding and validating connection candidates** [5].
4.  **Converting connections to human subsets** [5].
5.  **Grouping** to form final pose estimations [5].
6.  **Design your own grouping algorithm** [6].

## Implementation

The implementation is based on Python and utilizes libraries specified in `requirements.txt` [7].

### Dependencies

*   Anaconda
*   Python 3.8
*   Libraries listed in `requirements.txt`

### Setup

1.  **Install Anaconda** [6].
2.  **Create a conda environment:** `conda create --name poseLab python=3.8` (or your preferred environment name) [7].
3.  **Activate the environment:** `conda activate poseLab` [7].
4.  **Install Git:** `conda install git` [7].
5.  **Navigate to the project directory** in the Anaconda Prompt [7].
6.  **Install dependencies:** `pip install -r requirements.txt` [7].

### Running the Demo

1.  **Modify `demo_image.py`** to set the correct paths for the input image (`input_image`) and the output image (`output_image`) [8].
2.  **Open Anaconda Prompt**, activate the environment, and navigate to the project directory [8].
3.  **Run the demo:** `python demo_image.py` [8].

## Lab Task

The primary task is to complete the `EAI_Lab3/estimation/merge.py` file [7]. The `merge.py` file is for grouping [5].

*   **Input:**  `subset = [[-1. 1. 2. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. 1.9540779 2.], [-1. 1. -1. -1. -1. 5. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. 1.76488239 2.]]` [9]
*   **Output:** `subset = [[ 0. 1. 2. 3. -1. 5. -1. -1. -1. -1. -1. -1. -1. -1. 6. 7. 8. 9. 16.18416846 9.]]` [8]

## Code Structure

*   `demo_image.py`: Main script to run the pose estimation demo [5].
*   `coordinates.py`: Finds Gaussian peak coordinates in heatmaps and assigns identity numbers [5].
*   `connections.py`: Finds and returns valid connection candidates [5].
*   `estimators.py`: Converts connections to human subsets [5].
*   `merge.py`:  Grouping [5].

## Report

The lab report should include the following [10]:

1.  **Algorithm Description:** A detailed explanation of the implemented algorithm [10].
2.  **Output Subsets:** The results of the output subset [10].
3.  **Test Pictures:** Results on test pictures [10].
4.  **Challenges and Solutions:** Discuss any challenges faced and the solutions implemented [10].
