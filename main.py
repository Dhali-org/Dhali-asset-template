from fastapi import FastAPI, File, HTTPException

# <ADD DEPENDENCIES>

app = FastAPI()

@app.put("/run/")
async def infer(input: bytes = File()):

    try:
        # You must extract the input to the model from `input`.
        #
        # If `input` is a text string:
        #   text=input.decode("utf-8")
        #
        # If `input` is a json object:
        #   json_input = json.loads(input.decode("utf-8"))
        #
        # If `input` is an image:
        #   image = Image.open(io.BytesIO(input))
        #
        # If `input` is an image base64 embedded into a json:
        #   json_input = json.loads(input.decode("utf-8"))
        #   img_data = json_input["image"].encode()
        #   content = base64.b64decode(img_data)


        # <PARSE `input`>
        # <PROCESS `input`>
        # <RETURN RESULT OF `input` PROCESS>


        return {"results": "CALCULATED RESULT"}
    except:
        raise HTTPException(422, "Your input could not be processed")
