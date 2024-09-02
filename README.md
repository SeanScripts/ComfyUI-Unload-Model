# ComfyUI-Unload-Model

For unloading a model or all models, using the memory management that is already present in ComfyUI. Copied from https://github.com/willblaschko/ComfyUI-Unload-Models but without the unnecessary extra stuff.

How to install: Clone this repo into the `custom_nodes` folder, then restart ComfyUI.

How to use: Add in the middle of a workflow to unload a model at that step. Use any value for the `value` field and the model you want to unload for the `model` field, then route the output of the node to wherever you would have routed the input `value`.

For example, if you want to unload the CLIP models to save VRAM while using Flux, add this node after the `ClipTextEncode` or `ClipTextEncodeFlux` node, using the conditioning for the `value` field, and using the CLIP model for the `model` field, then route the output to wherever you would send the conditioning, e.g. `FluxGuidance` or `BasicGuider`.
