# maap_che_sidebar_visibility_jupyter_extension

## Overview

A Jupyter extension that provides users the ability to hide the Eclipse Che sidebar in the MAAP ADE.

<br>
<img title="Extension Menu" alt="Help Menu" src="./docs/img/extension-ui.png" width="300">
<br>
<br>

If the command pallete button is not visible in the left toolbar, toggling the "Modal Command Pallete" setting is needed. 

Menu -> Settings -> Advanced Settings -> Command Pallete - > Uncheck "Modal Command Pallete"

<br>
<img title="Advanced Settings - Command Pallete" alt="Help Menu" src="./docs/img/command-pallete.png" width="600">
<br>
<br>

## Requirements

* JupyterLab >= 3.4

## Install

### To install the extension if it isn't already pre-installed in a MAAP workspace, execute the following command<sup>1,2</sup>:


```bash
pip install git+https://github.com/MAAP-Project/che-sidebar-visibility-jupyter-extension.git@develop#egg-info=che-sidebar-visibility-jupyter-extension
```

### To install the extension during the image building process of the workspace, refer to the [maap-workspaces jupyterlab dockerfile](https://github.com/MAAP-Project/maap-workspaces/blob/main/jupyterlab3/docker/Dockerfile) where jupyterlab extensions are installed.

The typical command to install this extension in Jupyter would be:

```
pip install maap_che_sidebar_visibility_jupyter_extension
```

Notes:

1. Extension is not currently published to PyPi.
2. If installing in an already built and running MAAP workspace, a browser refresh is needed for the extension to be displayed in the Command Pallete. Restarting the workspace will require a reinstallation of the extension.


## Uninstall

To remove the extension, execute:

```bash
pip uninstall maap_che_sidebar_visibility_jupyter_extension
```

## Contributing

### Development install

Note: You will need NodeJS to build the extension package.

The `jlpm` command is JupyterLab's pinned version of
[yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use
`yarn` or `npm` in lieu of `jlpm` below.

```bash
# Clone the repo to your local environment
# Change directory to the che_sidebar_visibility_jupyter_extension directory
# Install package in development mode
pip install -e "."
# Link your development version of the extension with JupyterLab
jupyter labextension develop . --overwrite
# Rebuild extension Typescript source after making changes
jlpm build
```

You can watch the source directory and run JupyterLab at the same time in different terminals to watch for changes in the extension's source and automatically rebuild the extension.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
jlpm watch
# Run JupyterLab in another terminal
jupyter lab
```

With the watch command running, every saved change will immediately be built locally and available in your running JupyterLab. Refresh JupyterLab to load the change in your browser (you may need to wait several seconds for the extension to be rebuilt).

By default, the `jlpm build` command generates the source maps for this extension to make it easier to debug using the browser dev tools. To also generate source maps for the JupyterLab core extensions, you can run the following command:

```bash
jupyter lab build --minimize=False
```

### Development uninstall

```bash
pip uninstall maap_che_sidebar_visibility_jupyter_extension
```

In development mode, you will also need to remove the symlink created by `jupyter labextension develop`
command. To find its location, you can run `jupyter labextension list` to figure out where the `labextensions`
folder is located. Then you can remove the symlink named `che-sidebar-visibility-jupyter-extension` within that folder.

## Questions?
Refer to the [Q&A discussion board](https://github.com/MAAP-Project/che-sidebar-visibility-jupyter-extension/discussions/categories/q-a)

### Packaging the extension

See [RELEASE](RELEASE.md)
