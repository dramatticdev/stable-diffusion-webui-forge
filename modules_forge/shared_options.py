
def register(options_templates, options_section, OptionInfo):
    options_templates.update(options_section((None, "Forge Hidden options"), {
        "forge_unet_storage_dtype": OptionInfo('None'),
        "forge_inference_memory": OptionInfo(1024),
        "forge_async_loading": OptionInfo(False),
    }))
