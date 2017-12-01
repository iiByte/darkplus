# darkplus

### **About**

darkplus is a small program I made that runs through terminal (or any other terminal emulator) to toggle macOS's dark mode based on the perceived brightness of the wallpaper. It assumes you have the following installed:

1. Python >3.6.x (It may work on lower versions)
	- Pillow (this is the image processing module used.)
```
	pip3 install Pillow
```
2. Homebrew [(brew.sh)](brew.sh)
	- wallpaper
		- > brew install wallpaper

	- dark-mode
		- > brew install dark-mode

### **Installation**

To get this working you need to know where you saved darkplus.py and you need to know what shell you are using.

First, open your terminal emulator. I'm using Hyper.

Next, open your shell's config file. I'm using zsh, so I would type
```
nano .zshrc
```
to open my config in nano. If you're using bash, you'd type
```
nano .bash_profile
```


Add the following lines to your shell's config file:
```
wp() {
	wallpaper $1
	python3 /path/to/darkplus.py
}
```

Now press control+o to save, then hit enter, and control+x to exit. Close your current terminal window and open a new one to make sure the function saved in your config.

**You can now run wp!**

Test it in your terminal by typing wp /path/to/random/image.extension

### **Credits**

Credit goes to any creators of modules and libraries used! Thanks guys!