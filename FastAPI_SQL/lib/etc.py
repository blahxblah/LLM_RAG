def get_config_values(sets:list):
    import os
    from configparser import ConfigParser
    
    # create config
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../config/config.ini")
    config = ConfigParser()
    config.read(config_path)
    
    # read values
    returned = [config.get(category, key) for (category, key) in sets]
    
    return returned