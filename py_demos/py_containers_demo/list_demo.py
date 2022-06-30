liston = [123, str("123"), 12.7, bytes('\x12', 'ascii'), None, bytearray("12.7", encoding='ascii'), bytearray("123", encoding='ascii')]

var1, var2, var3, var4 = liston[:4]         # Auto (=implicit) --> OBS: no of variables MUST match list-slice length!

print(f"var1 = {var1}")
print(f"var2 = {var2}")
print(f"var3 = {var3}")
print(f"var4 = {var4}")
print()

int_var = None
str_var = None
float_var = None
byte_var = None

for var in liston:                      # Explicit (NOTE: my_var = "akkar" is AMBIGUOUS - it is a BYTEARRAY unless *encoding* is specified!)           
    if isinstance(var, int):
        int_var = var
    elif isinstance(var, str):
        str_var = var
    elif isinstance(var, float):
        float_var = var
    elif isinstance(var, bytes):
        byte_var = var
    else:
        print("ERROR: unknown type - cannot process!")

print(f"int_var = {int_var}")
print(f"str_var = {str_var}")
print(f"float_var = {float_var}")
print(f"byte_var = {byte_var}")
print()

# Ternary assignment-operations:
last_element = str(liston[-1], encoding='ascii')
int_var = int(last_element) if last_element.isdigit() else 0             # Should assign 123 to 'int_var' ...
print(f"int_var = {int_var}")
#
next_last_element= str(liston[-2], encoding='ascii')
int_var = int(next_last_element) if next_last_element.isdigit() else 0    # Should assign 0 to 'int_var' ...
print(f"int_var = {int_var}")
#
float_var = float(next_last_element) if next_last_element.isnumeric() else 0    # Fails - must (unfortunately) use try-except for FLOATs as they are locale-dependent(decimal point) and take multiple formats(scientific notation etc.)
print(f"float_var = {float_var}")                                               # Prints 0 ...
#
float_var = float(next_last_element) if next_last_element.replace('.', '').isdigit() else 0    # May work - but NOT for scientific notation!! (e.g. fstr = "1.2345E-6")
print(f"float_var = {float_var}")     # prints '12.7' ...
#
test_sci_notation = "1.2345E-6"
float_var = float(test_sci_notation) if test_sci_notation.replace('.', '').replace('-', '').replace('E', '').replace('e', '').isdigit() else 0    # MAY WORK - but lacks proper validation! (e.g. "--123.567-E6" will run 'float()' then trigger 'ValueError')
print(f"float_var = {float_var}")      # Prints '1.2345e-06' --> both 'e' and 'E' are valid exponent-symbol in scientific notation! (which adds to the format problems ...)

def is_float(val: str) -> bool:
    try:
        float(val)
        return True
    except ValueError:
        return False

print()
float_var = float(next_last_element) if is_float(next_last_element) else 0 
print(f"float_var = {float_var}")                                               # Prints 12,7 ...

print()
print(is_float("123,567"))     # False - my LOCALE language-input setting is "English(US)" ...
print(is_float("123.567"))     # True
print(is_float("1.23567E2"))   # True
print(is_float("1,3567E2"))    # False

# Slicing examples:
print()
s = "sunshine"
print(s[1:5:2])
print(s[1:5:1])
print(s[0:5:1])
print(s[0:5:1])

