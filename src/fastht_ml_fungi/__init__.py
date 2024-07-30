from fasthtml.common import *
from icecream import ic
from dotenv import load_dotenv

load_dotenv()

from fasthtml.common import *
from icecream import ic
from dotenv import load_dotenv

load_dotenv()

app = FastHTML()

count = 0


@app.get("/")
def home():
    return Title(f"Count Demo - running on {os.getenv('name')}"), Main(
        H1("Count Demo"),
        P(f"Using super secret {os.getenv('name')} secret: {os.getenv('secret')}"),
        P(f"Count is set to {count}", id="count"),
        Button(
            "Increment", hx_post="/increment", hx_target="#count", hx_swap="innerHTML"
        ),
        Button(
            "Decrement", hx_post="/decrement", hx_target="#count", hx_swap="innerHTML"
        ),
        Button("Reset", hx_post="/reset", hx_target="#count", hx_swap="innerHTML"),
    )


@app.post("/increment")
def increment():
    global count
    ic(count)
    count += 1
    return f"Count is set to {count}"


@app.post("/decrement")
def decrement():
    global count
    ic(count)
    count -= 1
    return f"Count is set to {count}"


@app.post("/reset")
def reset():
    global count
    ic(count)
    count = 0
    return f"Count is set to {count}"


serve()
