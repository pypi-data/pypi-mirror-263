# import pkgutil
# from plyer import notification
# from playsound import playsound

# def notify_execution(scenario="success", custom_message=None):
#     try:
#         # Dictionary to map default scenarios to notification messages
#         scenario_messages = {
#             "success": "Command executed successfully!",
#             "failure": "Command terminated with an error!",
#             "user_input_required": "Command is waiting for user input!",
#             "crash": "Command crashed!",
#             "unknown": "Unknown scenario!"
#         }

#         # Use custom message if specified
#         if scenario == "custom" and custom_message:
#             notification_message = custom_message
#         else:
#             notification_message = scenario_messages.get(scenario, scenario_messages["unknown"])

#         # Display notification with a default timeout of 5 seconds
#         notification.notify(
#             title="Command Execution",
#             message=notification_message,
#             timeout=5
#         )
        
#         # Get the sound file data using pkgutil
#         sound_data = pkgutil.get_data(__name__, "sound.mp3")
#         # Write the sound data to a temporary file
#         with open("sound.mp3", "wb") as f:
#             f.write(sound_data)
#         # Play the temporary sound file
#         playsound("sound.mp3")

#     except Exception as e:
#         print(f"Error: {e}")

# with glocal exception
import sys
import traceback
import pkgutil
from plyer import notification
from playsound import playsound

def notify_execution(scenario="success", custom_message=None):
    try:
        # Dictionary to map default scenarios to notification messages
        scenario_messages = {
            "success": "Command executed successfully!",
            "failure": "Command terminated with an error!",
            "user_input_required": "Command is waiting for user input!",
            "crash": "Command crashed!",
            "unknown": "Unknown scenario!"
        }

        # Use custom message if specified
        if scenario == "custom" and custom_message:
            notification_message = custom_message
        else:
            notification_message = scenario_messages.get(scenario, scenario_messages["unknown"])

        # Display notification with a default timeout of 5 seconds
        notification.notify(
            title="Command Execution",
            message=notification_message,
            timeout=5
        )
        
        # Get the sound file data using pkgutil
        sound_data = pkgutil.get_data(__name__, "sound.mp3")
        # Write the sound data to a temporary file
        with open("sound.mp3", "wb") as f:
            f.write(sound_data)
        # Play the temporary sound file
        playsound("sound.mp3")

    except Exception as e:
        print(f"Error: {e}")

# Define a global exception handler function
def global_exception_handler(exctype, value, tb):
    notify_execution(scenario="crash")
    # Print the exception traceback
    traceback.print_exception(exctype, value, tb)

# Set the global exception handler
sys.excepthook = global_exception_handler
