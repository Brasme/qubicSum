# Qubic Sum

Python app that find best qubic sum of integers

Note - it is far from optimal, but do the job. Feel free to optimize it or use it as you wish.  For example - it stores all alternatives - which is nice for debug, but .. no point to get alternatives first and then find the best one if only the local minimum is needed

## About qubic sum

All normal numbers can be expressed as sum of qubic values

For example "brute force" (highest qubic root first):

    1234567 = 107^3 + 21^3 + 6^3 + 3^3 + 2 * 2^3 + 4 * 1^3

But "best match" is:

    1234567 = 102^3 + 55^3 + 19^3 + 5^3


## Run app

Search for best alternatives - fast
```
%> python qubic.py 123456789
Brute force: 123456789 : [497, 88, 22, 10, 5, 4, 1, 1, 1, 1, 1, 1, 1]
Best match: 123456789 : [491, 161, 97, 4]
```

Gathers list of all alternatives and checks for best:
```
%> python qubic_all_combinations.py 1234567
1234567 : [107, 21, 6, 3, 2, 2, 1, 1, 1, 1] : [1225043, 9261, 216, 27, 8, 8, 1, 1, 1, 1]
Evaluated 25783 alternatives
Best = 164(4) = [102, 55, 19, 5]
1234567 : [102, 55, 19, 5] : [1061208, 166375, 6859, 125]
```


Scans all alternatives and checks for best (takes some seconds):
```
%> python qubic_slow.py 1234567 
Brute force: 1234567 : [107, 21, 6, 3, 2, 2, 1, 1, 1, 1] : [1225043, 9261, 216, 27, 8, 8, 1, 1, 1, 1]
Scan best: 1234567 : [102, 55, 19, 5] : [1061208, 166375, 6859, 125]
```

And to really do some CPU crunching for this O(2^N) solution (takes forever - probably and hour..):
```
%> python qubic_slow.py 123456789
Brute force: 123456789 : [497, 88, 22, 10, 5, 4, 1, 1, 1, 1, 1, 1, 1] : [122763473, 681472, 10648, 1000, 125, 64, 1, 1, 1, 1, 1, 1, 1]
Scan best: 123456789 : [494, 129, 91, 14, 1] : [120553784, 2146689, 753571, 2744, 1]
```