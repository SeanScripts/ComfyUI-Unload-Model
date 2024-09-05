# ComfyUI-Unload-Model

For unloading a model or all models, using the memory management that is already present in ComfyUI. Copied from https://github.com/willblaschko/ComfyUI-Unload-Models but without the unnecessary extra stuff.

Includes two nodes: Unload Model and Unload All Models. These are used as passthrough nodes, so that you can unload one or all models at a specific step in your workflow.

These nodes are used for manual memory management, and ComfyUI's built-in memory management will be sufficient for most users. If you notice your generation speeds slowing down after the first batch, then this node might help with that.

The main use of this is to unload the CLIP model after getting the embedding for the prompt, in order to save VRAM while sampling, and this is especially relevant when using Flux. This could be useful if you have enough VRAM to load both the Flux diffusion model and the T5XXL text encoder at the same time (at some quantization level for each), but don't want to keep them both persistently loaded. I find this useful for having spare VRAM to keep a local LLM loaded. Unloading models could also be useful at the end of a workflow, or when switching between different models, if you want to manage your memory manually.

These nodes are experimental and may not always work correctly. In particular, there have been some recent changes in the GGUF loader nodes that could cause the unload command to not actually unload the GGUF models (though this might be fixed already).

## Installation

1. Clone this repo into the `custom_nodes` folder:
```
git clone https://github.com/SeanScripts/ComfyUI-Unload-Model.git
```
2. Restart the ComfyUI server.

## Usage

Add the Unload Model or Unload All Models node in the middle of a workflow to unload a model at that step. Use any value for the `value` field and the model you want to unload for the `model` field, then route the output of the node to wherever you would have routed the input `value`.

For example, if you want to unload the CLIP models to save VRAM while using Flux, add this node after the `ClipTextEncode` or `ClipTextEncodeFlux` node, using the conditioning for the `value` field, and using the CLIP model for the `model` field, then route the output to wherever you would send the conditioning, e.g. `FluxGuidance` or `BasicGuider`.
