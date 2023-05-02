findings = []
while symbol in target:
    findings.append(target.rfind(symbol))
    target = target[:target.rfind(symbol)] + target[target.rfind(symbol) + 1::]
findings.reverse()
return findings