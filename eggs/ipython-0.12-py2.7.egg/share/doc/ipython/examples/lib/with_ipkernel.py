#!/usr/bin/env python
"""Example integrating an IPython kernel into a GUI App.

This trivial GUI application internally starts an IPython kernel, to which Qt
consoles can be connected either by the user at the command line or started
from the GUI itself, via a button.  The GUI can also manipulate one variable in
the kernel's namespace, and print the namespace to the console.

Play with it by running the script and then opening one or more consoles, and
pushing the 'Counter++' and 'Namespace' buttons.

Upon exit, it should automatically close all consoles opened from the GUI.

Consoles attached separately from a terminal will not be terminated, though
they will notice that their kernel died.
"""
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

import subprocess
import sys

from IPython.lib.kernel import connect_qtconsole
from IPython.zmq.ipkernel import IPKernelApp

#-----------------------------------------------------------------------------
# Functions and classes
#-----------------------------------------------------------------------------
def pylab_kernel(gui):
    """Launch and return an IPython kernel with pylab support for the desired gui
    """
    kernel = IPKernelApp.instance()
    kernel.initialize(['python', '--pylab=%s' % gui,
                       '--log-level=10'
                       ])
    return kernel


class InternalIPKernel(object):

    def init_ipkernel(self, backend='qt', namespace=None):
        # Start IPython kernel with GUI event loop and pylab support
        self.ipkernel = pylab_kernel(backend)
        # To create and track active qt consoles
        self.consoles = []

        if namespace is not None:
            namespace.update(self.ipkernel.shell.user_ns)
            self.ipkernel.shell.user_ns = namespace
        

    def new_qt_console(self):
        """start a new qtconsole connected to our kernel"""
        return connect_qtconsole(self.ipkernel.connection_file, 
                                 profile=self.ipkernel.profile)

    def cleanup_consoles(self, evt=None):
        for c in self.consoles:
            c.kill()

#-----------------------------------------------------------------------------
# Main script
#-----------------------------------------------------------------------------

if __name__ == "__main__":
    print 'Running long simulation'
    import numpy
    zz = numpy.random.rand(100)

    kernel = InternalIPKernel()
    kernel.init_ipkernel(namespace = globals())
    con  = kernel.new_qt_console()
    kernel.ipkernel.start()
    
