import comfy.model_management as model_management
import gc
import torch
import time

# Note: This doesn't work with reroute for some reason?
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any = AnyType("*")

class UnloadModelNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"value": (any, )}, # For passthrough
            "optional": {"model": (any, )},
        }
    
    @classmethod
    def VALIDATE_INPUTS(s, **kwargs):
        return True
    
    RETURN_TYPES = (any, )
    FUNCTION = "route"
    CATEGORY = "Unload Model"
    
    def route(self, **kwargs):
        print("Unload Model:")
        loaded_models = model_management.loaded_models()
        if kwargs.get("model") in loaded_models:
            print(" - Model found in memory, unloading...")
            loaded_models.remove(kwargs.get("model"))
        model_management.free_memory(1e30, model_management.get_torch_device(), loaded_models)
        model_management.soft_empty_cache(True)
        try:
            print(" - Clearing Cache...")
            gc.collect()
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
        except:
            print("   - Unable to clear cache")
        #time.sleep(2) # why?
        return (list(kwargs.values()))

class UnloadAllModelsNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"value": (any, )},
        }
    
    @classmethod
    def VALIDATE_INPUTS(s, **kwargs):
        return True
    
    RETURN_TYPES = (any, )
    FUNCTION = "route"
    CATEGORY = "Unload Model"
    
    def route(self, **kwargs):
        print("Unload Model:")
        print(" - Unloading all models...")
        model_management.unload_all_models()
        model_management.soft_empty_cache(True)
        try:
            print(" - Clearing Cache...")
            gc.collect()
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
        except:
            print("   - Unable to clear cache")
        #time.sleep(2) # why?
        return (list(kwargs.values()))


NODE_CLASS_MAPPINGS = {
    "UnloadModel": UnloadModelNode,
    "UnloadAllModels": UnloadAllModelsNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UnloadModel": "Unload Model",
    "UnloadAllModels": "Unload All Models",
}
