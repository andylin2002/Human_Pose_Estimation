## Dependencies

*   Anaconda
*   Python == 3.8.20
*   Libraries listed in `requirements.txt`

## Algorithm

This implementation likely involves a deep learning-based approach, possibly utilizing **Convolutional Neural Networks (CNNs)**, given their effectiveness in computer vision tasks. Two common approaches for multi-person pose estimation are:

*   **Top-down:** Localize humans, estimate parts, then calculate the pose.
*   **Bottom-up:** Estimate body parts, then calculate the pose.

A bottom-up approach called **OpenPose** is mentioned as an efficient method for multi-person pose estimation that uses **Part Affinity Fields (PAFs)** to encode the location and orientation of limbs. The network iteratively predicts PAFs and detection confidence maps.
