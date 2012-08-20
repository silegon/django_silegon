#!/usr/bin/python
#coding:utf-8
import re

def gc(template_file):
    """
    Generate the empty context file
    """

    if not template_file.endswith('template'):
        raise "Template name error"
    else:
        file_name = template_file.split('.')[0]
    context_file_name = file_name + '.c' 
    context_file = open(context_file_name, 'w')
    template_file = open(template_file, 'r')
    template = template_file.read()
    for item in re.findall('{{(.*?)}}', template):
        item = item.strip()
        context_file.write(item + ' =  \n')

    context_file.close()
    template_file.close()

if __name__ == '__main__':
    template_file = 'settings.py.template'
    print 'Done'
    gc(template_file)

