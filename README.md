# ComfyUI-Unload-Model

For unloading a model or all models, using the memory management that is already present in ComfyUI. Copied from https://github.com/willblaschko/ComfyUI-Unload-Models but without the unnecessary extra stuff.

Includes two nodes: Unload Model and Unload All Models. These are used as passthrough nodes, so that you can unload one or all models at a specific step in your workflow.

The main use of this is to unload the CLIP model after getting the embedding for the prompt, because it's just a waste of VRAM to keep it loaded while sampling, and VRAM is at a premium with Flux. For example, if you use the Q4_K_S version of Flux dev, with unloading the CLIP model, only about 10 GB of VRAM is used when generating at 1024 x 1024, which means that users with 12 or 16 GB GPUs might be able to run the model without going into shared memory, which could be a huge speedup. Please let me know if you test it and see this benefit. This could also be useful if you want to free up VRAM so you can keep a local LLM loaded for prompt generation.

## Installation

1. Clone this repo into the `custom_nodes` folder:
```
git clone https://github.com/SeanScripts/ComfyUI-Unload-Model.git
```
2. Restart the ComfyUI server.

## Usage

Add the Unload Model or Unload All Models node in the middle of a workflow to unload a model at that step. Use any value for the `value` field and the model you want to unload for the `model` field, then route the output of the node to wherever you would have routed the input `value`.

For example, if you want to unload the CLIP models to save VRAM while using Flux, add this node after the `ClipTextEncode` or `ClipTextEncodeFlux` node, using the conditioning for the `value` field, and using the CLIP model for the `model` field, then route the output to wherever you would send the conditioning, e.g. `FluxGuidance` or `BasicGuider`.
