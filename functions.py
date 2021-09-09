import math

def expectedValue(data:list):
    counter = {}
    for num in data:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    output = 0
    total = len(data)
    for key in counter:
        output += key*counter[key]/total
    return output

def variance(data:list):
    miu = expectedValue(data)
    output = 0
    for x in data:
        output += (x-miu)*(x-miu)
    return output/len(data)

def standard_deviation(data:list):
    return math.sqrt(variance(data))

def covariance(data:dict):
    x = data['x']
    y = data['y']
    miux = expectedValue(x)
    miuy = expectedValue(y)
    output = 0
    for i in range(len(x)):
        output += (x[i]-miux)*(y[i]-miuy)
    return output/len(x)

def correlation(data:dict):
    x = data['x']
    y = data['y']
    return covariance(data)/(variance(x)*variance(y))

if __name__ == '__main__':
    lis = [1,1,1,1,1,1,1,2]
    dic = {
        "x":[1,2,3,4,5,6,7,1],
        "y":[5,6,1,2,3,5,6,9]
    }
    print(correlation(dic))