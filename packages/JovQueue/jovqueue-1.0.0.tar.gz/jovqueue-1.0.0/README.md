# JovQueue
JovQueue is a python module created to add queue functionality to any function, allowing the user to also specify the amount of workers they want.
### Features
##### JovQueue Class
- init: 
  - Inputs:
    - thread_count (0-99): the amount of daemons the user wants to act as workers for their function
    - target_func (any function): the function for which the user wants to add a queue functionality
  - Actions:
    - This constructor initializes all of the daemons (specified by thread_count), and augments the target_func code to enable it to work with the queue (this queue is local to the instance of the JovQueue class)
- run:
  - Inputs: 
    - args: the arguments for the target_func call
  - Actions:
    - This function will put the args value into a queue which will then be ran by the next free daemon
### Installation
JovQueue can be installed via pip: 'pip install JovQueue'
### Example
A (very simple) example of using JovQueue can be found in the Examples directory of the JovQueue repo
