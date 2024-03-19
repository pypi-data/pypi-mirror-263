"""Experimental module for loading Julia files as Python modules.

Being experimental, it does not form part of the JuliaCall API. It may be changed or removed
in any release.

Basic usage is:
    import juliacall.importer
    juliacall.importer.install()

And now you can import any Julia file as Python module. That is, if 'foo.jl' is in your
Python path, then 'import foo' will work.

By default, all objects at the top level of the file whose name does not start with '_' are
exposed. Alternatively, you may explicitly 'export' objects.

The importer is intended for development use. To release a package, use 'gen_file' on each
Julia module file to generate a corresponding Python file and only include the Python files
in the release.
"""

import io
import os
import sys

from . import newmodule, Base
from importlib.machinery import ModuleSpec, SourceFileLoader

class Finder:
    def __init__(self, jlext='.jl', pyext='.py'):
        self.jlext = jlext
        self.pyext = pyext

    def find_spec(self, fullname, path, target=None):
        if path is None:
            path = sys.path
            if '.' in fullname:
                return
            name = fullname
        else:
            name = fullname.split('.')[-1]
        for root in path:
            jlfile = os.path.join(root, name + self.jlext)
            if os.path.isfile(jlfile):
                jlfile = os.path.realpath(jlfile)
                pyfile = os.path.join(root, name + self.pyext)
                gen_file(jlfile, pyfile)
                return ModuleSpec(fullname, SourceFileLoader(fullname, pyfile), origin=jlfile)

def install(**kw):
    """Install the Julia importer.

    After calling this, files ending '.jl' in your Python path may be imported as Python
    modules.

    The return value may be passed to 'uninstall'.
    """
    finder = Finder(**kw)
    sys.meta_path.insert(0, finder)
    return finder

def uninstall(finder):
    """Uninstall the Julia importer."""
    sys.meta_path.remove(finder)

def gen_code(jl):
    buf = io.StringIO()
    pr = lambda x: print(x, file=buf)
    jl2 = jl.replace('\\', '\\\\').replace("'", "\\'")
    pr('# This file was automatically generated by juliacall.importer')
    pr('import juliacall.importer')
    pr('juliacall.importer.exec_module(__name__,')
    pr("'''"+jl2+"''')")
    return buf.getvalue()

def gen_file(jl, py):
    """Convert a Julia module file to a Python module file."""
    with open(jl, encoding='utf-8') as fp:
        jlcode = fp.read()
    pycode = gen_code(jlcode)
    with open(py, 'w', encoding='utf-8') as fp:
        fp.write(pycode)

def exec_module(name, code):
    pymod = sys.modules[name]
    jlmod = newmodule(name)
    jlmod.seval('begin\n' + code + '\nend')
    delattr(pymod, 'juliacall')
    setattr(pymod, '__jl_code__', code)
    setattr(pymod, '__jl_module__', jlmod)
    ks = [str(k) for k in Base.names(jlmod)]
    ks = [k for k in ks if k != name]
    if not ks:
        ks = [str(k) for k in Base.names(jlmod, all=True)]
        ks = [k for k in ks if not (k == name or k == 'include' or k == 'eval' or k.startswith('_') or '#' in k)]
    setattr(pymod, '__all__', ks)
    setattr(pymod, '__doc__', str(Base.Docs.doc(jlmod)))
    for k in ks:
        setattr(pymod, k, getattr(jlmod, k))
