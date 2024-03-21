<p align="center">
Better aliases['..'] = 'cd ..'
</p>


## Installation

To install use pip:

```xsh
xpip install xontrib-dotdot
# or: xpip install -U git+https://github.com/yggdr/xontrib-dotdot
```

## Usage

This xontrib will get loaded automatically for interactive sessions.
To stop this, set

```xsh
$XONTRIBS_AUTOLOAD_DISABLED = {"dotdot", }
```

Now going up in directories can be simply done by chaining dots:

```xsh
% pwd
/some/deep/nested/directory/structure/I/want/to/leave
$ .....
$ pwd
/some/deep/nested/directory/structure/
```

The first two dots takes you to the parent, any further dot will go up one more.

Dots and commas can be freely mixed, the above example could've also been
achieved by typing `..,,.`. This behaviour can be changed by setting the
`$XONTRIB_DOTDOT_COMMA` environment variable to False

## Credits

This package was created with [xontrib template](https://github.com/xonsh/xontrib-template).
