#!/usr/bin/python
#coding:utf-8
from django.template import Context, Template
from django.conf import settings

settings.configure(DEBUG=False, TEMPLATE_DEBUG=False)

def as_dict(in_lines):
    d = {}
    for line in in_lines:
        name, value = line.split("=")
        name = name.strip()
        value = value.strip()
        d[name] = value
    return d

def fill_conf(template_file, context_file):
    output_file = ".".join(template_file.split('/')[-1].split('.')[:2])
    template_f = open(template_file, 'r')
    context_f = open(context_file, 'r')
    output_f = open(output_file, 'w')
    template = Template(template_f.read())
    context = Context(as_dict(context_f.readlines()))
    output_f.write(template.render(context))
    template_f.close()
    context_f.close()
    output_f.close()

if __name__ == '__main__':
    fill_conf('settings.py.template', 'settings.py.context')
    
    
    
