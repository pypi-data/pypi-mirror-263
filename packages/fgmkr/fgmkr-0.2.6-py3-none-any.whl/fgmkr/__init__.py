from matplotlib import pyplot as plt

# Single Input
def fgmk(n,x,y,xlabel,ylabel, titlestr, figtext = None, glabel = None, grid = None,dim=None):
    # Figure Setup
    if dim is not None:
        plt.figure(n, figsize=dim)
    else:
        plt.figure(n)

    # Data Visualization
    plt.plot(x,y, label = glabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titlestr)
    plt.text(0.5, -0.18, r'$\bf{Figure\ }$' + str(n) + r': '+ str(figtext), transform=plt.gca().transAxes,
            horizontalalignment='center', verticalalignment='center', fontsize=10)

    # Figure Cleanup
    if grid:
        plt.grid(which='both')
    if glabel is not None:
        plt.legend()

# Double Input
def fgmk2(n, x0, y0, xlabel, ylabel, t,
          l=None, lst='-', c='tab:blue',
          x=None, y=None, l1=None, lst1='-', c1='tab:orange',
          fig=None, grid=1, dim=None):
    # Figure Setup
    if dim is not None:
        plt.figure(n, figsize=dim)
    else:
        plt.figure(n)
    plt.title(t)
    if fig is not None:
        plt.text(0.5, -0.18, r'$\bf{Figure\ }$' + str(n) + r': ' + str(fig), transform=plt.gca().transAxes,
                 horizontalalignment='center', verticalalignment='center', fontsize=10)

    # Data Visualization
    plt.plot(x0, y0, label=l, linestyle=lst, color=c)  # Set 0
    if x is not None and y is not None:  # Set 1
        plt.plot(x, y, label=l1, linestyle=lst1, color=c1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Figure Cleanup
    if grid:
        plt.grid(which='both')
    if l is not None or l1 is not None:
        plt.legend()

# Help
def fgmk_help():
    print('Mandatory: \nFigure Number\nx0\ny0\nx0 Label\ny0 Label\nTitle\n')
    print('Optional Graph Features: \nfig, Figure Text\ngrid, enabled by default\ndim, 1x2 Tuple\n')
    print('Data Set 0: \nl, Label\nlst, \'-\' by default\nc \'tab:blue\' by default\n')
    print('Data Set 1: \nx\ny\nl1, Label\nlst1, \'-\' by default\nc1 \'tab:orange\' by default\n')