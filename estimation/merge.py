import numpy as np


def merge(subset, min_num_body_parts=4, min_score=0.4):
    """
    Estimates the skeletons.
    :param connections: valid connections
    :param min_num_body_parts: minimum number of body parts for a skeleton
    :param min_score: minimum score value for the skeleton
    :return: list of skeletons. Each skeleton has a list of identifiers of body parts:
        [
            [id1, id2,...,idN, score, parts_num],
            [id1, id2,...,idN, score, parts_num]
            ...
        ]

    position meaning:
        [   [nose       , neck           , right_shoulder , right_elbow      , right_wrist  , left_shoulder
             left_elbow , left_wrist     , right_hip      , right_knee       , right_ankle  , left_hip
             left_knee  , left_ankle     , right_eye      , left_eye         , right_ear    , left_ear
             score, parts_num],
        ]
    """

    # 2 step :
    #---merge----
    # Merge the limbs in the subset
    # score : score
    # parts_num : How many limbs are in the subset 
    ###############################

    for i in range(len(subset) - 1):
        for j in range(i + 1, len(subset)):
            # Check if the two subsets share body parts
            shared_parts = np.logical_and(subset[i][:-2] > 0, subset[j][:-2] > 0)
            
            if np.sum(shared_parts) > 0:  # If there are shared body parts
                # Merge subset[j] into subset[i]
                for k in range(len(subset[i]) - 2):  # Ignore score and parts_num columns
                    if subset[i][k] == -1 and subset[j][k] != -1:
                        subset[i][k] = subset[j][k]

                subset[i][-2] += subset[j][-2]    # Combine scores
                subset[i][-1] = subset[i][-1] + subset[j][-1] - shared_parts   # Combine parts count
                
                # Mark subset[j] for deletion (set score and part_num to 0)
                subset[j][-2] = 0
                subset[j][-1] = 0
    
    
    # after merge
    #---delete---
    # Delete the non-compliant subset
    # 1. parts_num < 4
    # 2. Average score(score / parts_num) < 0.4 
    ############################################
    
    delete_idx = []
    for i in range(len(subset)): 
        parts_num = subset[i][-1]
        avg_score = subset[i][-2] / parts_num if parts_num > 0 else 0
        if parts_num < min_num_body_parts or avg_score < min_score:  # revise here
            delete_idx.append(i)
    subset = np.delete(subset, delete_idx, axis=0)

    return subset   