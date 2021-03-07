# A CLI tool for plotting polynomial functions based on [argparse](https://docs.python.org/3.8/howto/argparse.html) and [matplotlib](https://matplotlib.org/)

1. Conditional Arguments: "coeff" - a list of polynomial coefficients

2. Optional Arguments (flags):
	..* --roots "Plot the root points"
	..* --min-max "Plot the min-max points"
	..* --inflection "Plot the inflection points"
	..* --graph "Polynomial function graph with the given coefficients"
	..* --first-derivative "First derivative polynomial with the given coefficients"
	..* --second-derivative "Second derivative polynomial with the given coefficients"


### Here's a command example

```
python3 main.py 1 -2 3 5 --graph
````

### Or

```
python3 main.py 1 -2 3 5 --roots
```

### With the respective output





## Future Work

* Consider edge cases
* Add statistics related plotting functions (sample distribution, box-plot, etc.)