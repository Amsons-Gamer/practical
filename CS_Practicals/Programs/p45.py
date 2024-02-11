n = list(eval(input("Enter list of no seperated by ,")))
fn = [0, 1]
for i in range(2, max(n)):
    nn = fn[i-1] + fn[i-2]
    if nn > max(n):
        break
    fn.append(nn)
result = []
for number in n:
    if number in fn:
        result.append(number)
print(result)
