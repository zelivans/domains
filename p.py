# I don't expect anyone to read this but if you are i'm sorry it's late and i'm tired so it's bad
# find a cool domain
import json

def get_domains():
     # instructions source is https://github.com/asmjit/asmdb/blob/master/x86data.js (split to json and comments removed)
    # tlds are from http://jecas.cz/tld-list/ (from google)
    with open("x86data.js", 'r') as f:
        insts = json.load(f)
    with open("tlds.js", 'r') as f:
        tlds = json.load(f)
    res = []
    for t in tlds: # sorted by tlds
        for i in insts["instructions"]:
            for i_s in i[0].split("/"):
                t_l, i_l = t.lower(), i_s.lower()
                if len(t_l) != len(i_l) and i_l[-len(t_l):] == t_l:
                    domain = i_l[:-len(t_l)] + "." + i_l[-len(t_l):]
                    if not domain in res: res.append(domain) 
    return res

def main():
    domains = get_domains()
    with open("result.txt", 'w') as f:
            f.write("\n".join(domains))

if "__main__" == __name__:
    main()