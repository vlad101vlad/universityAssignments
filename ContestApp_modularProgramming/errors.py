def problem_score_out_of_range(problem1_score, problem2_score, problem3_score):

    if problem1_score < 0 or problem1_score > 10:
        raise IndexError("Problem score out of range: must be in [0, 10]")
    if problem2_score < 0 or problem2_score > 10:
        raise IndexError("Problem score out of range: must be in [0, 10]")
    if problem3_score < 0 or problem3_score > 10:
        raise IndexError("Problem score out of range: must be in [0, 10]")
    return 1

