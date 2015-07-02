# Karnaugh Map Solver
Karnaugh Map Solver solves Karnaugh Maps, duh! Input values to the K-Map table and get equivalent minimized boolean function as output. This application supports K-Maps for boolean functions of up to **4** variables. `Don't care` conditions are also supported.


## Requirements
+ [Python](http://python.org) (2.7.x)
+ [wxPython](http://wxpython.org) (3.0)

## Usage
1. Simply executing the `main.py` file will start the app.

		$ python KMapSolver/main.py
	
2. Select the number of variables.
3. Click on the buttons to change their value. Click twice to get `don't care` condition, denoted by an `X`.

## Caveats
+ In some very rare cases, the returned function might not be in its most minimized form. So take the result with a grain of salt.
+ In OS X, the buttons look kind of distorted and misplaced. Apparently, there's no easy fix for that.

## Acknowledgement
This application was developed by me as an academic project for the course **CSE 2100 Software Development Project 1**, under the supervision of my respected instructor, *Jakaria Rabbi (Lecturer), Department of Computer Science and Engineering, Khulna University of Engineering and Technology, Khulna.*

## License
This software is released under the [GNU General Public License, version 2](http://opensource.org/licenses/gpl-2.0.php).