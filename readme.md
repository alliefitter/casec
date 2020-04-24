# `casec`

A case converter utility

## Usage

```bash
$ cat camel_case
fooBarBaz
__fooBarBaz
fooBARBaz
fooIDs
barID
bazIds
$ casec camel-case -s -f camel_case
foo_bar_baz
__foo_bar_baz
foo_bar_baz
foo_ids
bar_id
baz_ids
$ casec camel-case -p -f camel_case -a BAR
FooBARBaz
__FooBARBaz
FooBARBaz
FooIds
BARId
BazIds
$ cat camel_case | casec camel-case -o
FOO_BAR_BAZ
__FOO_BAR_BAZ
FOO_BAR_BAZ
FOO_IDS
BAR_ID
BAZ_IDS
```