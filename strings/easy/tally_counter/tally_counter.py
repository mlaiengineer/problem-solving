def get_tally_count(s):
    pipe = s.count('|')
    forward_slash = s.count('/')
    return pipe + forward_slash
