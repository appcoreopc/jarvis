#!/usr/bin/env python3
import jarvis

ex = jarvis.Experiment('plate_demo')

ex.groundClient('git')

ones = ex.literal([1, 2, 3], "ones")
ones.forEach()

tens = ex.literal([10, 100], "tens")
tens.forEach()

@jarvis.func
def multiply(x, y):
    z = x*y
    print(z)
    return z

doMultiply = ex.action(multiply, [ones, tens])
product = ex.artifact('product.txt', doMultiply)

product.pull()
product.plot()
# product_df = product.parallelPull(manifest=True)
# jarvis.Util.pickleTo(product_df, 'product.pkl')