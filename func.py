def cdown(n):
    if n <= 0:
        print("Blastoff!!")
        return 
    print(n)
    countdown(n-1)

def dict_depth(d, max_depth_so_far):
    if not isinstance (d, dict) or not d: 
        return max_depth_so_far
    cur_val = max_depth_so_far
    for v in d.values: 
        depth_of subdict = dict_depth(v, max_depth_so_far)
    

cdown(5)