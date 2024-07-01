# Find specific files recursively and operate on them
===================================================

## Just find'em (and list them):
```
find . -name "*.bak" -type f
```


## Delete them:
```
find . -name "*.bak" -type f -delete
```
Or, delete only lines in them files starting with '#endif':
```
find . -name "*.c" -exec sed -i "/^#endif/d" {} \;
```


## Rename (parts of) them:
```
rename "s/.old_suffix/.new_suffix/" ./*/*.old_suffix
```
To change suffix of all files ending in '*.old_suffix'.


## Substitute string(s) in them:
```
find . -name "*.py" -exec sed -i 's/foo/bar/g' {} \;
```
But if single quote(s) are present in any of the strings, 
then use double quotes to not confuse 'sed':
```
find . -name "*.py" -type f -exec sed -i "s/'''not < /# /g" {} \;
```
And of course, $, \, and / must *always* be escaped w. '\'.


## Insert strings in them:
TODO ...



