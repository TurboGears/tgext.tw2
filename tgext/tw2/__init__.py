def plugme(app_config, options=None):
    from .component import ToscaWidgets2ConfigurationComponent
    app_config.register(ToscaWidgets2ConfigurationComponent)
    return dict(appid='tgext.tw2')

