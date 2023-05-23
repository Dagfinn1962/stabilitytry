import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
os.environ['STABILITY_KEY'] = 'sk-Vf1g2hV9pvGAJYm5n16EYB7D7veCInOd13RXBit99qRFlFDd'
stability_api = client.StabilityInference(key=os.environ['STABILITY_KEY'],
verbose=True,
engine="stable-diffusion-xl-beta-v2-2-2",
)


answers = stability_api.generate (
prompt="expansive landscape ",
seed=992446758,
steps=30,
cfg_scale=8.0,
width=512,
height=512, 
samples=1, 
sampler=generation.SAMPLER_K_DPMPP_2M )

