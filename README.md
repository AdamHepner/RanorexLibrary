# RanorexLibrary
The RanorexLibrary offers an integration of the [Ranorex API](https://www.ranorex.com) into the [Robot Test Automation Framework](http://robotframework.org). This means, you can write Robot tests like you are used to, and use Ranorex functionality to automate GUIs independent of the underlying technology.

You can find a full documentation about the RanorexLibrary and how to use it in the [Wiki](https://github.com/Thomas-Gruber-90/RanorexLibrary/wiki).

**Please note:** You will still need valid Ranorex licenses to run the tests.

# Build the documentation

You need to install [IronPython](https://ironpython.net/), ensure that the `ipy32.exe` is in your `%PATH%`, install PIP and required packages (run the following as user who can modify IronPython's directory):

```cmd
ipy32 -m ensurepip
ipy32 -m pip install -r requirements.txt
```

run 

```cmd
makedocs.bat
```

The last one does no need to be elevated. Keywords documentation will be placed in `docs/index.html` folder. 
