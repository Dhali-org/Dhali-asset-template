from fastapi import FastAPI, File, HTTPException

# <ADD DEPENDENCIES>

app = FastAPI()

# <To improve efficiency, ensure that only what is required is
#  in the /run/ method. E.g., consider loading models here.>

@app.put("/run/")
async def infer(input: bytes = File()):

    try:
        # You must extract the input to the model from `input`.
        #
        # If `input` is a text string:
        #   text=input.decode("utf-8")
        #
        # If `input` is a json object:
        #   import json
        #   json_input = json.loads(input.decode("utf-8"))
        #
        # If `input` is an image:
        #   from PIL import Image
        #   image = Image.open(io.BytesIO(input))
        #
        # If `input` is an image base64 embedded into a json:
        #   import json
        #   import base64
        #   json_input = json.loads(input.decode("utf-8"))
        #   img_data = json_input["image"].encode()
        #   content = base64.b64decode(img_data)
        #
        # <PARSE `input`>
        # <PROCESS `input`>
        # <RETURN RESULT OF `input` PROCESS>
        #
        # The format of the result can be anything returnable from a FastAPI
        # endpoint. E.g.:

        return {"results": "CALCULATED RESULT"}
    
    except Exception as e:
        raise HTTPException(422, f"Your input could not be parsed: {e}")
