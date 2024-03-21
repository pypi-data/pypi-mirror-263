# Terminal Notifier

Terminal Notifier is a Python package designed to provide simple notifications about command execution in the terminal environment. It offers the capability to display notifications and play sounds upon completion of commands, enhancing user experience and workflow.

## Installation

You can install Terminal Notifier via pip:

```bash
pip install terminal-notifier
```

## Usage
```
from terminal_notifier import notify_execution

notify_execution(scenario="success")
notify_execution(scenario="failure")
notify_execution(scenario="user_input_required")
notify_execution(scenario="crash")
notify_execution(scenario="unknown")




```

## Custom Messages
```
notify_execution(scenario="failure", custom_message="Command failed to execute!")
notify_execution(scenario="custom", custom_message="Custom message here")
```





