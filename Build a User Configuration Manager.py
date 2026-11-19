# 5. Create a dictionary named test_settings to store user preferences
test_settings = {
    'theme': 'light',
    'language': 'english',
    'notifications': 'enabled'
}

# 1 & 2. Define add_setting function
def add_setting(settings_dict, setting_tuple):
    key, value = setting_tuple
    key = key.lower()
    value = str(value).lower()
    
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

# 3 & 4. Define update_setting function
def update_setting(settings_dict, setting_tuple):
    key, value = setting_tuple
    key = key.lower()
    value = str(value).lower()
    
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

# 5 & 6. Define delete_setting function
def delete_setting(settings_dict, key):
    key = key.lower()
    
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"

# 7 & 8. Define view_settings function
def view_settings(settings_dict):
    if not settings_dict:
        return "No settings available."
    
    result = "Current User Settings:\n"
    for key, value in settings_dict.items():
        result += f"{key.capitalize()}: {value}\n"
    
    return result
