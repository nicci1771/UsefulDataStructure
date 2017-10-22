def getnext(p):
	i = 0
	j = -1
	nxt = [0] * (len(p)+1)
	nxt[0] = -1
	while i < len(p):
		if j == -1 or p[i] == p[j]:
			i += 1
			j += 1
			nxt[i] = j
		else:
			j = nxt[j]
	return nxt

def match(s, p):
	slen = len(s)
	plen = len(p)
	if plen == 0:
		return 0
	if slen == 0:
		return -1
	nxt = getnext(p)
	start = 0
	matched = 0
	stop = slen - plen + 1
	res = []
	while True:
		while matched == plen or s[start+matched] != p[matched]:
			if matched == plen:
				res.append(start)
			start += matched - nxt[matched]
			matched = max(0, nxt[matched])
			if not start < stop:
				return res
		else:
			matched += 1

if __name__ == '__main__':
	s = "ecdabcdabcd"
	p = "qecdabcd"
	print match(s, p)


