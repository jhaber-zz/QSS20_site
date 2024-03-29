#!/usr/bin/env python
# coding: utf-8

# (software_setup)=
# 
# # Overview of tools
# 
# We will be using the following tools in the course:
# 
# - **Piazza for communication, i.e. Q&A and announcements**. You can join the class Piazza by [clicking this signup link](https://piazza.com/dartmouth/fall2022/qss20). See [here](https://piazza.com/help/formatting.html) for formatting help (e.g., you can add code or even format a post in LaTeX!), and feel free to give the developers feedback by emailing team@piazza.com. For project-related teamwork, you can make private posts visible to select people to communicate directly with your project group. 
# 
# **Please use Piazza instead of emailing the instructor or TA(s)**, as other students will likely share your questions and may be able to answer them too (or edit the question to make it clearer or more complete). While I will be answering questions within a window of 24 hours, I encourage you to help each other and answer each other's questions. 
# 
# There are folders in Piazza for each major part of the course, including each problem set, project milestone, and final project component (the final presentation and report share the `final_project` folder). The other folders and their respective topics for discussion are:
# 
#     - `enrollment/logistics`: enrolling in the course and other logistics, like the schedule and due dates.
#     - `pythonhelp_general`: python in general, not specific to problem sets or final project components.
#     - `datacamp`: DataCamp, esp. about making sure your account is set up.
#     - `git/github`: creating git repositories, the online GitHub interface, making commits and pull requests, etc.
#     - `latex/overleaf`: LaTeX syntax, working with templates on Overleaf, etc.
#     - `miscellaneous`: random stuff, i.e. anything that doesn't fit a problem set, final project component, or the above folders.
#     
# - **Jhub as a remote computing environment**. [Jonathan Crossett in Dartmouth’s Information, Technology, and Computing](https://itc.dartmouth.edu/people/jonathan-crossett) has set up a dedicated course server on Dartmouth's Jupyter Hub (Jhub for short). This allows you to open up any browser and complete Python tutorials without needing to download data or files locally / deal with package installation issues. More details on the server are below.
# 
# - **Locally-installed Python**. Eventually, you'll leave the course and Dartmouth and need to know how to use Python locally. So in addition to getting used to Jhub, please install Python and the associated packages to run things locally. 
# 
# - **Terminal/terminal emulator**. This is mainly for interfacing with Git/GitHub. See instructions below for installation.
# 
# - **Git/GitHub for version control**. One of the course goals is to get you more familiar with using Git/GitHub for version control. You can interact with GitHub both from the Jhub remote environment and from your local machine. There are instructions below for each, and we'll have an in-class activity where you create your own repository and add me as a collaborator. 
# 
# - **LaTeX/Overleaf for dynamic typesetting**. We'll be using the LaTeX typesetting software to integrate writing and formulae and more cleanly integrate figures into writeups. We'll be interacting with LaTeX through an online interface called Overleaf, so please [create a free account here](https://www.overleaf.com/register). If you want to work with LaTeX offline/locally, try googling "how to install LaTeX"; some popular editors include TeXworks and LaTeXiT.
# 
# 
# ## How to access Jhub
# 
# 1. Navigate to: [jhub.dartmouth.edu](https://jhub.dartmouth.edu/) while logged in with your Dartmouth netid. If you're off-campus, you may need to connect to Dartmouth VPN ([instructions here](https://services.dartmouth.edu/TDClient/1806/Portal/KB/ArticleDet?ID=66806); feel free and email Dartmouth IT about issues). You should see an option on Jhub for our course. Click on it and the server will start up in a minute or two.
# 
# ```{image} ../images/jhub1.png
# :alt: jhub 1
# :class: bg-primary mb-1
# :width: 500px
# :align: center
# ```
# 
# 2. Navigate to your home directory by clicking the folder icon at the top left. You can create whatever directory structure and files you want there without it interfering the the common class content (which you can't change and lives in `/shared/QSS20`):
# 
# ```{image} ../images/jhub2.png
# :alt: jhub 2
# :class: bg-primary mb-1
# :width: 500px
# :align: center
# ```
# 
# 3. To start a new python3 notebook/kernel from scratch, click the `Python 3` icon in the top left of the launcher window (right portion of the screen). Make sure to give it a name (or you'll get crowded by mysterious files called "Untitled.pynb"!):
# 
# ```{image} ../images/jhub3.png
# :alt: jhub 3
# :class: bg-primary mb-1
# :width: 300px
# :align: center
# ```
# 
# 4. If interfacing with GitHub from Jhub, open a terminal by clicking the `Terminal` icon in that same launcher menu to make a terminal that works with syntax similar to your local one: 
# 
# ```{image} ../images/terminal.png
# :alt: jhub terminal menu
# :class: bg-primary mb-1
# :width: 300px
# :align: center
# ```
# 
# We're going to focus on interfacing with GitHub from your local computer, so don't worry too much about the remote terminal for now.
# 
# 
# ### [QSS20 repository](https://github.com/jhaber-zz/QSS20_public) content on Jhub
# 
# Course content like slides or activities should automatically populate this directory on Jhub: `shared/QSS20/`. However, to get the latest content added to course repo (anything added/changed since the last user started a new server), you might need to restart your server as follows:
# 
# - Click the "File" button from the top menu bar
# - Click "Hub Control Panel"
# - Click "Stop My Server"
# - Then click "Start My Server"
# 
# 
# ## Local Python
# 
# Please download Python 3.8+ via [the Anaconda distribution system](https://www.anaconda.com/what-is-anaconda/) ([download it here](https://www.anaconda.com/products/distribution)). 3.8+ is strongly preferred due to compatibility between `.pkl` files.
# 
# 
# ## Terminal/terminal emulator
# 
# We’ll be reviewing basic "command line" syntax, which is important for:
# 
# - *Interacting with Git*: while there are ways to interact with Git through the online user interface (GitHub), Git's full functionality depends on being able to interact with repositories (basically, folders that store code) through the command line.
# 
# -  *Executing .py or .R scripts that take a long time to finish executing*: ideally, you should write code that is efficient (runs quickly). But sometimes, regardless of how efficient the code is, things take a long time to run given the limited resources of your laptop or local environment. Executing code on the command line requires telling your computer to run a script and sometimes feeding that script arguments to parse. This is easier to leave in the background and less prone to error than is running time-consuming/at-scale code from a Jupyter notebook. 
# 
# 
# ### Macs/OSX
# 
# Macs have a built-in terminal (to access, go to: 1. Search -> 2. Terminal). Below's an example of what one looks like, with commands to move to a folder called `Dropbox/optimizingschools_publicviews` and then view folder contents:
# 
# ```{image} ../images/local_terminal.png
# :alt: local terminal example
# :class: bg-primary mb-1
# :width: 500px
# :align: center
# ```
# 
# I recommend also using a terminal manager to start long-running processes, detach from them while they are running, and re-attach when they’re done. A good one for Macs is called [screen](http://www.kinnetica.com/2011/05/29/using-screen-on-mac-os-x/), but [tmux](https://www.howtogeek.com/671422/how-to-use-tmux-on-linux-and-why-its-better-than-screen/) also works well (I prefer [byobu](https://www.byobu.org/), which is built on tmux). 
# 
# 
# ### Windows
# 
# Windows users have the option of running a native Linux distribution inside traditional windows to access a UNIX-style command line. This is called the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about) and is the option I suggest. It lets you interact with files and programs through a UNIX command line rather than the usual method of clicking through folders. Feel free to also check out "terminal emulators" such as [cygwin](https://www.cygwin.com/).
# 
# 
# ## Git/GitHub
# 
# We'll go over more Git/GitHub instructions during class. Before then:
# 
# 1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) if you haven't already
# 
# 2. [Create a free GitHub account](https://docs.github.com/en/github/getting-started-with-github/signing-up-for-a-new-github-account) if you don't have one already
# 
# 
# ## Text editor
# 
# Using a text editor tailored to programming is really helpful when writing code that takes longer to run, as it is visually appealing and highlights parts of the syntax (e.g., the start of a function) to more easily catch mistakes. An overall workflow for this might be:
# 
# 1. Write and test the code on a small sample of data in an IDE (e.g., a Jupyter notebook for `.ipynb` or RStudio for `.Rmd`)
# 2. Translate the code into a `.py` or `.R` script that can be run all at once (without having to execute each cell) 
# 
# For step two, the code can be opened in any basic text editor that comes standard on your machine (e.g., text editor on Macs), but a more visually appealing text editor makes the process smoother and more enjoyable.
# 
# Options (definitely non-exhaustive!):
# 
# - [Sublime Text](https://www.sublimetext.com/3)
# - [Atom](https://atom.io/)
# - [Nano](https://www.nano-editor.org/download.php)
# - [AquaMacs](http://aquamacs.org/)
# 
# Text editors are also good for working with `.yaml` files, which can be used to store things like passwords/credentials to access APIs. Here's an example of Sublime Text and a `.yaml` file that has the table of contents for this QSS20 course website:
# 
# ```{image} ../images/sublime_example.png
# :alt: sublime example
# :class: bg-primary mb-1
# :width: 300px
# :align: center
# ```
