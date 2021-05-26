import questions

def distance(movement):
    #6 400 steps per rev at 1/32
    #3 200 steps per rev at 1/16
    #5mm pitch threaded rod

    steps = float(movement) / 5 * 6400
    return steps

def duration(duration, step_count):
    #requires steps

    interval = float(duration) * 60 / float(step_count)
    return interval, step_count
    
    

    

