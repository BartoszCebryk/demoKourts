# demoKourts
Repo for task given in pdf file

The idea behind the solution was to make it as simple as possible - just to show solution.
For more information see "Possible extensions" section

Language used: Python
Tool: selenium webdriver

How to:
Please be sure to have "pip" installed on you machine.
I was doing everything under PyCharm Community Edition.

after cloning this repository make sure you have python 2.7 as interpreter.
Then right click on runner.sh and select "Run runner.sh"

If everything is ok chromedriver, selenium and pytest check will be done and test will be started.
Other method:
open terminal, navigate to runner.sh file and execute script as root to enable neccessary installations.

After the script is executed you should be able to see 2 more files generated:
extra_one.png
and
extra_two.png

these are screenshots taken during test execution. Task was not required but I wanted to prove myself.

Possible extensions:
To make code easier to look, use and read using page object pattern is suggested.
This enables us adding more layers of abstraction and separating test code
from locators and selectors.

Test were runned from Virtual Ubuntu Machine under Windows 10.

To make things easier in the future and not bother other team members with setting up environment
simple export of my machine is possible.

And that is all.
The whole task took me 2hours 45 minutes including virtual machine preparation and getting some selectors to work.

