from fasthtml.common import *
from icecream import ic
from dotenv import load_dotenv
import os

load_dotenv()

app = FastHTML()
setup_toasts(app)


@app.get("/")
def home():
    return Title("Mushroom 🍄 Map"), Main(
        H1("Mushroom 🍄 Map"),
        P("The map displays your mushroom observations."),
        A("Click to add new observation", href="/new-observation"),
    )


@app.get("/new-observation")
def new_observation():
    # return a Title and page for new observation that includes an image upload
    return Title("New Observation"), Main(
        H1("Add a New Observation"),
        P(
            "Please select the mushroom image for the observation. The photo should come with the GPS location where it has been taken in the metadata."
        ),
        Form(
            Input(id="photo", type="file", name="photo"),
            Button("Submit", type="submit"),
            action="/new-observation",
            method="POST",
            enctype="multipart/form-data",
            accept="image/*",
        ),
    )


@app.post("/new-observation")
async def new_observation_post(session, photo: str):
    add_toast(session, "Photo upload successful", "success")
    photo_content = await photo.read()
    with open("./static/photo-output.jpg", "wb") as output:
        output.write(photo_content)
    ic(type(photo))
    return Title("Successful Submission "), Main(
        H1("Information about Uploaded Photo"), Img(src="/photo-output.jpg")
    )


serve()
