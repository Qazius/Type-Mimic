# Type-Mimic

## about

mimics human-realistic typing with balanced delays or intervals between unique characters and supports complex text like code

for example, with the following text from [Hacker Typer](https://hackertyper.com/):

```python
text="""   }
   return group_info;

out_undo_partial_alloc:
   while (--a >= 0) {
      free_page((unsigned long)group_info->blocks[a]);
   }
   kfree(group_info);
   return NULL;
}
"""
```

you get:\
![demo](assets/demo.gif)

### functions

- if there are a defined number of consecutive spaces, they will group into a `tab`
- if consecutive special characters `!@#$%^&*()-,.`etc that are the same, they will be grouped and typed faster
- all letters and spaces will be grouped into sentences

### configuration

`tabSize` changes how many spaces in a tab\
`typeInterval` changes sentence type speed\
`specialInterval` changes type speed of consecutive similar special characters
