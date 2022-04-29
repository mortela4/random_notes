API recommendations
====================

1) A function (or method) should not exceed 1x A4-page (preferrably < 50 lines w. fontsize=11pt)

2) preferrably < 5 function args

3) direction convention for transfer/copy/compare/transform functions:  
```C
funcname(<source>, <destination>, <size>, ...)  
```
in that order!

4) use varargs for complex functions with a few, base arguments! (assumes C++)

5) standardize library usage!
Examples:
- logging = liblog
- config/INI-file parsing = libconfig/libini/simplejson/tinyxml
No-opt:
- POSIX functionality = libc/libm/pthreads

6) structure
a. preferrably < 7 levels of call stack
b. use function pointers instead of multiple calls to separate functions w. identical signature!
Example:
```C
switch(type)
{
	case(TYPE_1): funptr = func1; break;
	case(TYPE_2): funptr = func2; break;
	case(TYPE_3): funptr = func3; break;
		.
		.
		.
	case(TYPE_N): funptr = funcN; break;
	default: funptr = NULL; break;
}
if (NULL != funptr)
{
	funptr(&args);
}
```

