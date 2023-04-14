def prettyprintdict(value, htchar='\t', lfchar='\n', indent=0):
    nlch = lfchar + htchar * (indent + 1)
    if type(value) is dict:
        items = [
            nlch + repr(key) + ': ' + prettyprintdict(value[key], htchar, lfchar, indent + 1)
            for key in value
        ]
        items = sorted(items)
        return '{%s}' % (','.join(items) + lfchar + htchar * indent).replace("'","\"")
    elif type(value) is list:
        items = [
            nlch + prettyprintdict(item, htchar, lfchar, indent + 1)
            for item in value
        ]
        items = sorted(items)
        return '[%s]' % (','.join(items) + lfchar + htchar * indent).replace("'","\"")
    elif type(value) is tuple:
        items = [
            nlch + prettyprintdict(item, htchar, lfchar, indent + 1)
            for item in value
        ]
        items = sorted(items)
        return '(%s)' % (','.join(items) + lfchar + htchar * indent).replace("'","\"")
    else:
        return repr(value).replace("'","\"")