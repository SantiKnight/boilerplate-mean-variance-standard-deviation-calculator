import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        lista = np.array(lista).reshape(3,3)
        mean1 = np.mean(lista, axis = 0)
        mean2 = np.mean(lista, axis = 1)
        mean3 = np.mean(lista)
        means = [list(mean1), list(mean2), float(mean3)]
        variance1 = np.var(lista, axis = 0)
        variance2 = np.var(lista, axis = 1)
        variance3 = np.var(lista)
        variances = [list(variance1), list(variance2), float(variance3)]
        std1 = np.std(lista, axis = 0)
        std2 = np.std(lista, axis = 1)
        std3 = np.std(lista)
        stds = [list(std1), list(std2), float(std3)]
        max1 = np.max(lista, axis = 0)
        max2 = np.max(lista, axis = 1)
        max3 = np.max(lista)
        maxs = [list(max1), list(max2), float(max3)]
        min1 = np.min(lista, axis = 0)
        min2 = np.min(lista, axis = 1)
        min3 = np.min(lista)
        mins = [list(min1), list(min2), float(min3)]
        sum1 = np.sum(lista, axis = 0)
        sum2 = np.sum(lista, axis = 1)
        sum3 = np.sum(lista)
        sums = [list(sum1), list(sum2), float(sum3)]
        calculations = {
            'mean': means,
            'variance': variances,
            'standard deviation': stds,
            'max': maxs,
            'min': mins,
            'sum': sums
        }
    return calculations